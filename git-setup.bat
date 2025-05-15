@echo off
chcp 65001 > nul
echo =====================================================
echo    Configuration Git pour Automations_n8n
echo =====================================================
echo.

REM Vérifier si Git est installé
where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Git n'est pas installe ou n'est pas dans le PATH.
    echo Installez Git depuis https://git-scm.com/downloads
    pause
    exit /b 1
)

REM Vérifier si le dépôt existe déjà
if not exist ".git" (
    echo Initialisation du depot Git...
    git init
) else (
    echo Depot Git deja initialise.
)

REM Vérifier la configuration de Git
echo Verification de la configuration Git...
git config --get user.name > nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    set /p GIT_NAME="Entrez votre nom pour Git: "
    git config --local user.name "%GIT_NAME%"
)

git config --get user.email > nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    set /p GIT_EMAIL="Entrez votre email pour Git: "
    git config --local user.email "%GIT_EMAIL%"
)

REM Recherche des sous-répertoires contenant des dépôts Git - Version simplifiée
echo Verification des sous-repertoires Git...
echo Cette operation peut prendre quelques instants...

REM Créer un fichier temporaire pour stocker les chemins des dépôts Git imbriqués
set TEMP_FILE=%TEMP%\git_repos.txt
if exist "%TEMP_FILE%" del "%TEMP_FILE%"

echo Recherche des depots Git imbriques...
for /f "delims=" %%a in ('dir /b /s /ad ".git" ^| findstr /v "\\\.git\\"') do (
    if not "%%a"==".\.git" (
        echo %%a >> "%TEMP_FILE%"
        set FOUND_NESTED_GIT=1
    )
)

set FOUND_NESTED_GIT=0
if exist "%TEMP_FILE%" (
    for /f %%a in ('type "%TEMP_FILE%" ^| find /c /v ""') do set GIT_COUNT=%%a
    if !GIT_COUNT! GTR 0 set FOUND_NESTED_GIT=1
)

if %FOUND_NESTED_GIT%==1 (
    echo.
    echo Depots Git imbriques trouves: %GIT_COUNT%
    echo Verifiez le fichier %TEMP_FILE% pour la liste complete.
    echo.
    echo Options:
    echo 1. Supprimer les depots .git imbriques (recommande)
    echo 2. Ignorer ces repertoires avec .gitignore 
    echo 3. Continuer malgre tout (risque)
    set /p GIT_NESTED_CHOICE="Choisissez une option (1/2/3): "
    
    if "%GIT_NESTED_CHOICE%"=="1" (
        echo Suppression des depots Git imbriques...
        for /f "delims=" %%a in ('type "%TEMP_FILE%"') do (
            echo Suppression de %%a
            rmdir /s /q "%%a"
        )
    ) else if "%GIT_NESTED_CHOICE%"=="2" (
        echo Ajout des repertoires problematiques a .gitignore...
        echo. >> .gitignore
        echo # Repertoires avec Git imbriques >> .gitignore
        for /f "delims=" %%a in ('type "%TEMP_FILE%"') do (
            for %%b in ("%%a\..") do (
                set "REL_PATH=%%~dpnxb"
                setlocal enabledelayedexpansion
                set "REL_PATH=!REL_PATH:%CD%\=!"
                echo !REL_PATH! >> .gitignore
                endlocal
            )
        )
    )
)

del "%TEMP_FILE%"

REM Ajouter les fichiers au suivi Git - un par un pour éviter les erreurs
echo.
echo Ajout des fichiers au suivi Git (un par un)...

REM Fichiers à la racine
git add *.* 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Erreur lors de l'ajout des fichiers a la racine, ignore.
)

REM Lister les répertoires principaux
echo.
echo Repertoires disponibles:
dir /ad /b

REM Ajouter chaque répertoire séparément
echo.
echo Ajout des repertoires un par un...
for /d %%D in (*) do (
    if not "%%D"==".git" (
        echo Ajout de %%D...
        git add "%%D" 2>nul
        if %ERRORLEVEL% NEQ 0 (
            echo Erreur lors de l'ajout de %%D, ignore.
        )
    )
)

REM Vérifier s'il y a des fichiers à committer
echo.
echo Statut Git:
git status

git diff --cached --quiet
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Des fichiers sont prêts à être commités.
    set /p COMMIT_MSG="Message du commit initial: "
    if "%COMMIT_MSG%"=="" set COMMIT_MSG="Initial commit - Automations_n8n"
    
    git commit -m "%COMMIT_MSG%"
    echo Commit créé avec succès.
) else (
    echo.
    echo Aucun fichier n'a été stagé pour le commit.
    echo Options:
    echo 1. Continuer avec setup (créer un commit vide)
    echo 2. Ajouter manuellement des fichiers et réessayer
    echo 3. Quitter le script
    set /p NO_FILES_CHOICE="Choisissez une option (1/2/3): "
    
    if "%NO_FILES_CHOICE%"=="1" (
        echo Création d'un commit initial vide...
        git commit --allow-empty -m "Initial empty commit"
    ) else if "%NO_FILES_CHOICE%"=="2" (
        echo.
        echo Instructions:
        echo 1. Utilisez 'git add [fichier/dossier]' pour ajouter des fichiers spécifiques
        echo 2. Utilisez 'git commit -m "Message"' pour créer le commit
        echo 3. Relancez ce script ensuite
        pause
        exit /b 0
    ) else (
        echo Sortie du script.
        pause
        exit /b 0
    )
)

REM Vérifier quelle est la branche actuelle
for /f "tokens=*" %%a in ('git branch --show-current') do set CURRENT_BRANCH=%%a
echo Branche actuelle: %CURRENT_BRANCH%

REM Renommer la branche en main si nécessaire
if not "%CURRENT_BRANCH%"=="main" (
    echo Renommage de la branche en "main"...
    git branch -M main
    echo Branche renommée en "main".
)

REM Configurer le dépôt distant si ce n'est pas déjà fait
git remote -v | findstr "origin" > nul
if %ERRORLEVEL% NEQ 0 (
    echo Configuration du dépôt distant...
    set /p REMOTE_URL="URL du dépôt GitHub (ex: https://github.com/stepstev/Automations_n8n.git): "
    git remote add origin %REMOTE_URL%
) else (
    echo Dépôt distant déjà configuré.
)

REM Pousser vers le dépôt distant
echo Envoi du code vers GitHub...
git push -u origin main

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo =====================================================
    echo ERREUR: Impossible de pousser vers le dépôt distant.
    echo =====================================================
    echo 1. Vérifiez que le dépôt existe sur GitHub
    echo 2. Vérifiez vos identifiants GitHub
    echo 3. Si vous utilisez un token, assurez-vous qu'il a les permissions suffisantes
    echo.
    echo Pour les dépôts existants avec du contenu, essayez d'abord:
    echo git pull --rebase origin main
    echo Puis réessayez:
    echo git push -u origin main
) else (
    echo.
    echo =====================================================
    echo Succès! Votre code est maintenant sur GitHub
    echo =====================================================
)

echo.
pause
