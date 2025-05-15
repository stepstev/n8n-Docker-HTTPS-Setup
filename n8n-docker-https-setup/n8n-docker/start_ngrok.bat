@echo off
echo ============================================
echo Démarrage du tunnel ngrok pour n8n
echo ============================================
echo.
echo Ce script va démarrer un tunnel ngrok vers n8n
echo qui tourne sur le port 5678.
echo.
echo Informations importantes à connaître:
echo - L'URL générée sera accessible depuis Internet
echo - Utilisez l'URL https://xxx.ngrok-free.app affichée 
echo   dans la section "Forwarding"
echo - L'interface ngrok est disponible sur http://127.0.0.1:4040
echo - Pour arrêter le tunnel, appuyez sur Ctrl+C
echo.
echo ============================================

REM Vérifier si n8n fonctionne
curl -s http://localhost:5678 > nul
if %ERRORLEVEL% NEQ 0 (
    echo ERREUR: n8n ne semble pas fonctionner sur localhost:5678
    echo Veuillez démarrer n8n avant de lancer ce script.
    echo Utilisez le script 0-start_n8n_menu.py option 1.
    pause
    exit /b 1
)

echo n8n est en cours d'exécution sur localhost:5678.
echo Démarrage du tunnel ngrok...
echo.

ngrok http 5678

echo.
echo Le tunnel ngrok a été fermé.
echo Si n8n est toujours en cours d'exécution, vous pouvez
echo relancer ce script pour créer un nouveau tunnel.
echo.
pause
