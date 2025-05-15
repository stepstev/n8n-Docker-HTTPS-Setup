@echo off
echo =======================================================
echo   Génération de la présentation n8n Docker HTTPS Setup
echo =======================================================
echo.

REM Vérifier si le modèle PowerPoint existe
set "TEMPLATE_FILE=d:\00-Conception_AI\__Automations_n8n\n8n-presentation\ThinkinG_modele.pptx"
if not exist "%TEMPLATE_FILE%" (
    echo ERREUR: Le fichier modèle PowerPoint n'existe pas:
    echo %TEMPLATE_FILE%
    echo.
    echo Veuillez vérifier que le fichier existe avant de continuer.
    pause
    exit /b 1
)
echo Modèle PowerPoint trouvé: %TEMPLATE_FILE%

REM Vérifier si Python est installé
where python >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python n'est pas installé ou n'est pas dans le PATH.
    echo Veuillez installer Python depuis https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Vérifier si pip est disponible
python -m pip --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo pip n'est pas disponible.
    echo Veuillez réinstaller Python en cochant l'option "Add pip to PATH".
    pause
    exit /b 1
)

REM Installer les dépendances
echo Installation des dépendances...
pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo Erreur lors de l'installation des dépendances.
    pause
    exit /b 1
)

REM Créer le dossier images s'il n'existe pas
if not exist "images" mkdir images
echo Dossier images créé. Placez-y vos captures d'écran pour personnaliser la présentation.

REM Créer la présentation
echo.
echo Génération de la présentation PowerPoint...
python create_presentation.py
if %ERRORLEVEL% NEQ 0 (
    echo Une erreur s'est produite lors de la génération de la présentation.
    pause
    exit /b 1
)

echo.
echo =======================================================
echo   Présentation générée avec succès!
echo =======================================================
echo.
echo Vous pouvez maintenant:
echo 1. Ouvrir la présentation avec PowerPoint
echo 2. Ajouter des images depuis le dossier "images"
echo 3. Personnaliser la mise en forme et les animations
echo.
echo Fichier: n8n_Docker_HTTPS_Setup.pptx
echo.

pause
