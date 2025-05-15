@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

echo =====================================================
echo    Correction des erreurs Git
echo =====================================================
echo.

echo Cette opération va:
echo 1. Supprimer les dépôts Git imbriqués qui causent des erreurs
echo 2. Créer une liste d'exclusions pour git add
echo.
set /p CONTINUE="Continuer? (o/n): "
if /i not "%CONTINUE%"=="o" exit /b

echo.
echo Recherche des dépôts Git imbriqués problématiques...

REM Traiter spécifiquement le dépôt problématique mentionné dans l'erreur
if exist "n8n-docker-https-setup\n8n-docker\.git" (
    echo Suppression de n8n-docker-https-setup\n8n-docker\.git
    rmdir /s /q "n8n-docker-https-setup\n8n-docker\.git"
)

REM Traiter le dépôt imbriqué mentionné dans l'avertissement
if exist "n8n-docker-https-setup\streamlit_docs\.git" (
    echo Suppression de n8n-docker-https-setup\streamlit_docs\.git
    rmdir /s /q "n8n-docker-https-setup\streamlit_docs\.git"
)

echo.
echo Création d'un fichier .gitignore global...

REM Ajouter les dossiers typiquement ignorés s'ils n'existent pas déjà dans .gitignore
if not exist .gitignore (
    echo # Fichiers et dossiers ignorés par Git > .gitignore
) else (
    echo. >> .gitignore
    echo # Ajouts de correctifs pour les dépôts imbriqués >> .gitignore
)

REM Ajouter les dossiers temporaires et de configuration
echo node_modules/ >> .gitignore
echo __pycache__/ >> .gitignore
echo .venv/ >> .gitignore
echo .env >> .gitignore
echo *.log >> .gitignore
echo .DS_Store >> .gitignore
echo .vscode/ >> .gitignore
echo .idea/ >> .gitignore

echo.
echo Vérification des autres dépôts Git imbriqués...
set GITREPO_COUNT=0

REM Créer un fichier temporaire pour les chemins à ignorer
set TEMP_IGNORE=%TEMP%\git_ignore_paths.txt
if exist "%TEMP_IGNORE%" del "%TEMP_IGNORE%"

for /f "delims=" %%a in ('dir /a:d /b /s ".git" ^| findstr /v "\\\.git\\"') do (
    if not "%%a"==".\.git" (
        set /a GITREPO_COUNT+=1
        echo Dépôt Git trouvé: %%a
        
        REM Extraire le chemin relatif pour l'ajouter au .gitignore
        set "REPO_PATH=%%a"
        set "REPO_PATH=!REPO_PATH:%CD%\=!"
        set "REPO_PATH=!REPO_PATH:\.git=!"
        
        echo !REPO_PATH! >> "%TEMP_IGNORE%"
    )
)

if %GITREPO_COUNT% GTR 0 (
    echo.
    echo %GITREPO_COUNT% dépôts Git imbriqués trouvés.
    echo Que souhaitez-vous faire?
    echo 1. Supprimer tous les dépôts Git imbriqués
    echo 2. Les ajouter au fichier .gitignore
    echo 3. Ignorer (non recommandé)
    set /p GIT_ACTION="Choix (1/2/3): "
    
    if "%GIT_ACTION%"=="1" (
        for /f "delims=" %%a in ('dir /a:d /b /s ".git" ^| findstr /v "\\\.git\\"') do (
            if not "%%a"==".\.git" (
                echo Suppression de %%a
                rmdir /s /q "%%a"
            )
        )
    ) else if "%GIT_ACTION%"=="2" (
        for /f "delims=" %%a in ('type "%TEMP_IGNORE%"') do (
            echo # Dépôt Git imbriqué >> .gitignore
            echo %%a >> .gitignore
        )
    )
)

del "%TEMP_IGNORE%" 2>nul

echo.
echo Création d'un script pour ajouter les fichiers sans erreur...

echo @echo off > git-add-safe.bat
echo setlocal enabledelayedexpansion >> git-add-safe.bat
echo echo Ajout sécurisé des fichiers au dépôt Git... >> git-add-safe.bat
echo. >> git-add-safe.bat
echo REM Ajouter les fichiers à la racine >> git-add-safe.bat
echo git add *.* README.md >> git-add-safe.bat
echo. >> git-add-safe.bat
echo REM Ajouter chaque répertoire individuellement, en excluant ceux problématiques >> git-add-safe.bat
echo for /d %%%%D in (*) do ( >> git-add-safe.bat
echo     if not "%%%%D"==".git" ( >> git-add-safe.bat
echo         if not exist "%%%%D\.git" ( >> git-add-safe.bat
echo             echo Ajout de %%%%D... >> git-add-safe.bat
echo             git add "%%%%D" >> git-add-safe.bat
echo         ) else ( >> git-add-safe.bat
echo             echo Répertoire %%%%D ignoré (contient un dépôt Git) >> git-add-safe.bat
echo         ) >> git-add-safe.bat
echo     ) >> git-add-safe.bat
echo ) >> git-add-safe.bat
echo. >> git-add-safe.bat
echo git status >> git-add-safe.bat
echo echo. >> git-add-safe.bat
echo echo Pour créer un commit: git commit -m "Votre message" >> git-add-safe.bat
echo echo Pour pousser vers GitHub: git push origin main >> git-add-safe.bat
echo. >> git-add-safe.bat
echo pause >> git-add-safe.bat

echo.
echo =====================================================
echo Corrections terminées!
echo =====================================================
echo.
echo Exécutez git-add-safe.bat pour ajouter les fichiers sans erreur
echo.
pause
