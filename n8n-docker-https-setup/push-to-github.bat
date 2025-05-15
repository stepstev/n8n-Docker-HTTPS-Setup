@echo off
echo =====================================================
echo  Script pour envoyer le projet sur GitHub
echo =====================================================
echo.

REM Vérifier si Git est installé
where git >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Git n'est pas installé ou n'est pas dans le PATH.
    echo Installez Git depuis https://git-scm.com/downloads
    pause
    exit /b 1
)

echo Veuillez saisir les informations suivantes pour configurer le dépôt GitHub:
echo.
set /p GH_USERNAME="Nom d'utilisateur GitHub: "
set /p GH_REPO="Nom du dépôt GitHub (ex: n8n-docker-https-setup): "
set /p GH_EMAIL="Email GitHub: "
set /p GH_NAME="Nom complet (pour les commits): "

echo.
echo Configuration de Git avec vos informations...
git config --local user.email "%GH_EMAIL%"
git config --local user.name "%GH_NAME%"

REM Vérifier si le répertoire est déjà un dépôt Git
if exist ".git" (
    echo Le répertoire est déjà un dépôt Git.
) else (
    echo Initialisation du dépôt Git...
    git init
)

REM Création du .gitignore
echo Création du fichier .gitignore...
echo node_modules/ > .gitignore
echo .env >> .gitignore
echo *.log >> .gitignore
echo .DS_Store >> .gitignore
echo dist/ >> .gitignore
echo .vscode/ >> .gitignore

REM Afficher le status des fichiers
echo.
echo Fichiers détectés dans le projet:
git status

echo.
echo Ajout des fichiers au suivi Git...
git add .

echo.
echo Les fichiers suivants seront inclus dans le commit:
git status

echo.
set /p COMMIT_MSG="Message du premier commit: "
if "%COMMIT_MSG%"=="" set COMMIT_MSG="Premier commit - Configuration n8n avec Docker et ngrok"

echo.
echo Création du commit...
git commit -m "%COMMIT_MSG%"

echo.
echo Création de la branche principale (main)...
git branch -M main

echo.
echo Configuration du dépôt distant...
git remote add origin https://github.com/%GH_USERNAME%/%GH_REPO%.git

echo.
echo Envoi du code sur GitHub...
echo (Vous devrez peut-être saisir vos identifiants GitHub)
git push -u origin main

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ====================================================
    echo IMPORTANT: Si vous recevez une erreur d'authentification
    echo ----------------------------------------------------
    echo 1. Assurez-vous que le dépôt %GH_REPO% existe sur votre compte GitHub
    echo 2. GitHub n'accepte plus l'authentification par mot de passe simple
    echo 3. Utilisez un token d'accès personnel:
    echo    - Allez sur https://github.com/settings/tokens
    echo    - Générez un nouveau token avec les autorisations "repo"
    echo    - Utilisez ce token comme mot de passe
    echo ====================================================
) else (
    echo.
    echo ====================================================
    echo Succès! Votre code est maintenant sur GitHub:
    echo https://github.com/%GH_USERNAME%/%GH_REPO%
    echo ====================================================
)

echo.
echo Pour les modifications futures, utilisez ces commandes:
echo git add .
echo git commit -m "Description des modifications"
echo git push
echo.

pause
