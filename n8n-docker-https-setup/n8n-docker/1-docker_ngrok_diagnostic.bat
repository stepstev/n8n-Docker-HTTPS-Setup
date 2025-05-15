@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion
title Docker et ngrok - Diagnostic et Resolution d'Erreurs

:menu
cls
echo ===================================================
echo   OUTIL DE DIAGNOSTIC DOCKER ET NGROK
echo ===================================================
echo.
echo  1. Verifier les prerequis (Docker, Docker Compose, ngrok)
echo  2. Verifier l'etat des conteneurs Docker
echo  3. Verifier si le port 5678 est deja utilise
echo  4. Configurer le token d'authentification ngrok
echo  5. Redemarrer les services Docker
echo  6. Demarrer un tunnel ngrok sur le port 5678
echo  7. Aide et depannage
echo  0. Quitter
echo.
echo ===================================================

set /p choix="Entrez votre choix (0-7): "

if "%choix%"=="0" goto fin
if "%choix%"=="1" goto verif_prerequis
if "%choix%"=="2" goto verif_conteneurs
if "%choix%"=="3" goto verif_port
if "%choix%"=="4" goto config_ngrok
if "%choix%"=="5" goto redemarrer_docker
if "%choix%"=="6" goto tunnel_ngrok
if "%choix%"=="7" goto aide
echo Choix invalide. Veuillez reessayer.
timeout /t 2 >nul
goto menu

:verif_prerequis
cls
echo Verification des prerequis...
echo.
echo === Verification de Docker ===
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] Docker n'est pas installe ou n'est pas accessible.
    echo Solution: Installez Docker depuis https://docs.docker.com/get-docker/
) else (
    echo [OK] Docker est installe.
    docker info | findstr "running" >nul 2>&1
    if %errorlevel% neq 0 (
        echo [AVERTISSEMENT] Docker ne semble pas fonctionner correctement.
        echo Solution: Redemarrez le service Docker.
    ) else (
        echo [OK] Docker fonctionne correctement.
    )
)

echo.
echo === Verification de Docker Compose ===
docker-compose --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] Docker Compose n'est pas installe ou n'est pas accessible.
    echo Solution: Installez Docker Compose depuis https://docs.docker.com/compose/install/
) else (
    echo [OK] Docker Compose est installe.
)

echo.
echo === Verification de ngrok ===
ngrok --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERREUR] ngrok n'est pas installe ou n'est pas accessible dans le PATH.
    echo Solution: Telechargez ngrok depuis https://ngrok.com/download
    echo           et ajoutez son repertoire au PATH systeme.
) else (
    echo [OK] ngrok est installe.
)

pause
goto menu

:verif_conteneurs
cls
echo Verification de l'etat des conteneurs Docker...
echo.
docker ps -a
echo.
echo Pour demarrer les conteneurs arretes, utilisez:
echo docker-compose up -d
echo.
echo Pour arreter les conteneurs en cours d'execution, utilisez:
echo docker-compose down
echo.
pause
goto menu

:verif_port
cls
echo Verification si le port 5678 est deja utilise...
echo.
netstat -ano | findstr ":5678"
if %errorlevel% neq 0 (
    echo [INFO] Le port 5678 semble libre.
) else (
    echo [AVERTISSEMENT] Le port 5678 est deja utilise.
    echo.
    echo Solution 1: Arretez le processus qui utilise ce port.
    echo Solution 2: Modifiez le port dans docker-compose.yml:
    echo   ports:
    echo     - "5679:5678"  ^<-- Changez 5679 par un port disponible
)
echo.
pause
goto menu

:config_ngrok
cls
echo Configuration du token d'authentification ngrok
echo.
set /p token="Entrez votre token d'authentification ngrok: "
ngrok authtoken %token%
echo.
echo Token configure. Vous pouvez maintenant utiliser ngrok avec votre compte.
pause
goto menu

:redemarrer_docker
cls
echo Redemarrage des services Docker...
echo.
echo 1. Arret des conteneurs
docker-compose down
echo.
echo 2. Demarrage des conteneurs
docker-compose up -d
echo.
echo Operation terminee.
pause
goto menu

:tunnel_ngrok
cls
echo Demarrage d'un tunnel ngrok sur le port 5678...
echo.
echo IMPORTANT: Cette commande va bloquer cette fenetre.
echo Pour revenir au menu, fermez la fenetre avec Ctrl+C.
echo.
pause
cls
echo Demarrage du tunnel ngrok...
echo Appuyez sur Ctrl+C pour arreter.
echo.
start cmd /k "ngrok http 5678"
timeout /t 5
goto menu

:aide
cls
echo === AIDE ET DEPANNAGE ===
echo.
echo === Erreur: docker-compose ne demarre pas ===
echo Causes possibles:
echo - Docker ou Docker Compose n'est pas installe
echo - Le service Docker n'est pas en cours d'execution
echo Solution: Utilisez l'option 1 du menu pour verifier les prerequis
echo.
echo === Erreur: ngrok ne demarre pas ===
echo Causes possibles:
echo - ngrok n'est pas installe ou n'est pas dans le PATH
echo - Token d'authentification non configure
echo Solution: Utilisez l'option 1 pour verifier l'installation et l'option 4 pour configurer le token
echo.
echo === Erreur: Port 5678 deja utilise ===
echo Causes possibles:
echo - Un autre processus utilise ce port
echo - Une instance precedente de n8n est toujours en cours d'execution
echo Solution: Utilisez l'option 3 pour verifier le port et suivez les recommandations
echo.
echo === Erreur: URL ngrok non generee ===
echo Causes possibles:
echo - Probleme de connexion Internet
echo - Le port 5678 n'est pas accessible
echo - Token ngrok non configure ou invalide
echo Solution: Verifiez votre connexion Internet et utilisez l'option 4 pour reconfigurer votre token
echo.
pause
goto menu

:fin
cls
echo Fermeture du programme...
endlocal
exit /b 0