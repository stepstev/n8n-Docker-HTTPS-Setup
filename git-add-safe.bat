@echo off 
setlocal enabledelayedexpansion 
echo Ajout sécurisé des fichiers au dépôt Git... 
 
REM Ajouter les fichiers à la racine 
git add *.* README.md 
 
REM Ajouter chaque répertoire individuellement, en excluant ceux problématiques 
for /d %%D in (*) do ( 
    if not "%%D"==".git" ( 
        if not exist "%%D\.git" ( 
            echo Ajout de %%D... 
            git add "%%D" 
        ) else ( 
            echo Répertoire %%D ignoré (contient un dépôt Git) 
        ) 
    ) 
) 
 
git status 
echo. 
echo Pour créer un commit: git commit -m "Votre message" 
echo Pour pousser vers GitHub: git push origin main 
 
pause 
