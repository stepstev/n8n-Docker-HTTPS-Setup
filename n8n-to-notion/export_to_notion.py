import os
import sys
import json
import shutil
import subprocess
import markdown
import re
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import streamlit as st
import base64
from PIL import Image, ImageGrab
import io

# Chemins des répertoires
STREAMLIT_DOCS_DIR = Path(r"D:\00-Conception_AI\__Automations_n8n\n8n-docker-https-setup\streamlit_docs")
NOTION_EXPORT_DIR = Path(r"D:\00-Conception_AI\__Automations_n8n\n8n-to-notion\export")
NOTION_IMAGES_DIR = NOTION_EXPORT_DIR / "images"
NOTION_MARKDOWN_DIR = NOTION_EXPORT_DIR / "markdown"

# Assurez-vous que les répertoires existent
for directory in [NOTION_EXPORT_DIR, NOTION_IMAGES_DIR, NOTION_MARKDOWN_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

def clear_screen():
    """Nettoie l'écran de la console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def capture_streamlit_content():
    """Capture le contenu de l'application Streamlit à partir du code source."""
    app_py_path = STREAMLIT_DOCS_DIR / "app.py"
    
    if not app_py_path.exists():
        print(f"Erreur: Fichier app.py introuvable à l'emplacement {app_py_path}")
        sys.exit(1)
    
    with open(app_py_path, 'r', encoding='utf-8') as f:
        app_content = f.read()
    
    # Extraire les sections Markdown de l'application Streamlit
    markdown_sections = []
    
    # Recherche des blocs st.markdown(""" ... """)
    pattern = r'st\.markdown\((?:r?)"""(.*?)"""\)'
    matches = re.findall(pattern, app_content, re.DOTALL)
    
    for i, match in enumerate(matches):
        section_path = NOTION_MARKDOWN_DIR / f"section_{i+1}.md"
        with open(section_path, 'w', encoding='utf-8') as f:
            f.write(match)
        markdown_sections.append((section_path, match))
    
    # Recherche des titres avec st.title(" ... ")
    title_pattern = r'st\.title\("(.*?)"\)'
    title_matches = re.findall(title_pattern, app_content, re.DOTALL)
    
    for i, match in enumerate(title_matches):
        section_path = NOTION_MARKDOWN_DIR / f"title_{i+1}.md"
        with open(section_path, 'w', encoding='utf-8') as f:
            f.write(f"# {match}")
        markdown_sections.append((section_path, f"# {match}"))
    
    print(f"{len(markdown_sections)} sections Markdown extraites.")
    return markdown_sections

def convert_markdown_to_html(markdown_sections):
    """Convertit les sections Markdown en HTML pour une meilleure compatibilité avec Notion."""
    html_sections = []
    
    for path, content in markdown_sections:
        html_content = markdown.markdown(content, extensions=['tables', 'fenced_code', 'codehilite'])
        html_path = NOTION_MARKDOWN_DIR / f"{path.stem}.html"
        
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        html_sections.append((html_path, html_content))
    
    print(f"{len(html_sections)} sections HTML générées.")
    return html_sections

def generate_notion_page():
    """Génère un fichier HTML complet pour l'import dans Notion."""
    notion_html_path = NOTION_EXPORT_DIR / "n8n_documentation.html"
    
    # Début du document HTML
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Documentation n8n Docker HTTPS Setup</title>
        <meta charset="UTF-8">
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 20px; }
            h1, h2, h3 { margin-top: 28px; margin-bottom: 14px; }
            code { font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace; background-color: #f6f8fa; padding: 2px 5px; border-radius: 3px; font-size: 0.9em; }
            pre { background-color: #f6f8fa; padding: 16px; overflow: auto; border-radius: 3px; line-height: 1.45; }
            pre code { background-color: transparent; padding: 0; }
            table { border-collapse: collapse; width: 100%; margin-bottom: 16px; }
            th, td { border: 1px solid #ddd; padding: 8px 12px; text-align: left; }
            th { background-color: #f6f8fa; }
            img { max-width: 100%; }
            blockquote { margin: 0; padding-left: 16px; border-left: 4px solid #ddd; color: #555; }
        </style>
    </head>
    <body>
        <h1>Documentation n8n Docker HTTPS Setup</h1>
        <p><em>Documentation complète pour configurer n8n avec Docker, HTTPS via ngrok et les fonctionnalités d'IA.</em></p>
        <p><strong>Date de génération:</strong> """ + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + """</p>
        <hr>
    """
    
    # Capture des sections HTML
    markdown_sections = capture_streamlit_content()
    html_sections = convert_markdown_to_html(markdown_sections)
    
    # Ajouter les sections au document
    for _, content in html_sections:
        # Nettoyer le HTML pour Notion
        soup = BeautifulSoup(content, 'html.parser')
        
        # Assurez-vous que les images pointent vers des URL absolues
        for img in soup.find_all('img'):
            if img.get('src') and not img['src'].startswith(('http://', 'https://')):
                img['src'] = f"images/{os.path.basename(img['src'])}"
        
        # Ajouter au document principal
        html_content += str(soup) + "\n\n"
    
    # Fin du document HTML
    html_content += """
        <hr>
        <p><em>Cette documentation a été générée automatiquement à partir de l'application Streamlit.</em></p>
    </body>
    </html>
    """
    
    with open(notion_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Documentation HTML pour Notion générée: {notion_html_path}")
    return notion_html_path

def create_notion_integration_guide():
    """Crée un guide d'intégration pour Notion."""
    guide_path = NOTION_EXPORT_DIR / "guide_import_notion.md"
    
    guide_content = """# Guide d'importation dans Notion

## Méthode 1: Importation directe du HTML

1. Ouvrez Notion et créez une nouvelle page
2. Cliquez sur les trois points `...` en haut à droite
3. Sélectionnez `Import` dans le menu
4. Choisissez le fichier HTML généré (`n8n_documentation.html`)
5. Notion importera le contenu et tentera de préserver la mise en forme

## Méthode 2: Import via Markdown

1. Ouvrez Notion et créez une nouvelle page
2. Pour chaque fichier Markdown dans le dossier `markdown`:
   - Copiez le contenu du fichier
   - Dans Notion, collez-le dans une nouvelle page ou section
   - Notion convertira automatiquement le Markdown

## Méthode 3: Copier-coller depuis le navigateur

1. Ouvrez le fichier HTML généré dans un navigateur
2. Sélectionnez tout le contenu (Ctrl+A)
3. Copiez (Ctrl+C)
4. Dans Notion, collez (Ctrl+V) dans une nouvelle page
5. Notion préservera la plupart de la mise en forme

## Conseils pour Notion

- Les tableaux complexes peuvent nécessiter un reformatage manuel
- Utilisez `/code` dans Notion pour créer des blocs de code pour les snippets
- Pour les images, vous pouvez les télécharger manuellement et les insérer avec `/image`
- Créez une table des matières avec `/table of contents`

## Structure recommandée

Organisez votre documentation dans Notion avec cette structure:

```
📄 n8n Docker HTTPS Setup (page principale)
 ├── 📝 Introduction
 ├── 📝 Installation et prérequis
 ├── 📝 Configuration Docker
 ├── 📝 Configuration HTTPS avec ngrok
 ├── 📝 Fonctionnalités IA
 ├── 📝 Workflows d'exemple
 └── 📝 Dépannage
```

Vous pouvez utiliser la fonctionnalité "Synced blocks" de Notion pour réutiliser des éléments communs.
"""
    
    with open(guide_path, 'w', encoding='utf-8') as f:
        f.write(guide_content)
    
    print(f"Guide d'importation Notion créé: {guide_path}")
    return guide_path

def capture_screenshots():
    """Capture des captures d'écran de l'application Streamlit si elle est en cours d'exécution."""
    try:
        # Vérifier si l'application Streamlit est en cours d'exécution
        response = requests.get("http://localhost:8501")
        
        if response.status_code == 200:
            print("Application Streamlit détectée. Capture d'écran en cours...")
            
            # Attendre que l'utilisateur positionne la fenêtre
            input("Positionnez la fenêtre de l'application Streamlit et appuyez sur Entrée pour capturer...")
            
            # Capturer l'écran
            screenshot = ImageGrab.grab()
            screenshot_path = NOTION_IMAGES_DIR / "streamlit_app_screenshot.png"
            screenshot.save(screenshot_path)
            
            print(f"Capture d'écran enregistrée: {screenshot_path}")
        else:
            print("L'application Streamlit ne semble pas fonctionner sur le port 8501.")
            print("Aucune capture d'écran n'a été réalisée.")
    
    except Exception as e:
        print(f"Erreur lors de la capture d'écran: {e}")
        print("Assurez-vous que l'application Streamlit est en cours d'exécution.")

def main():
    clear_screen()
    print("=" * 70)
    print(" Exportation de la documentation Streamlit vers Notion ")
    print("=" * 70)
    print("\nCe script va générer les fichiers nécessaires pour importer la documentation")
    print("dans Notion à partir de l'application Streamlit.\n")
    
    # Vérifier le répertoire Streamlit
    if not STREAMLIT_DOCS_DIR.exists():
        print(f"Erreur: Le répertoire {STREAMLIT_DOCS_DIR} n'existe pas.")
        sys.exit(1)
    
    # Créer l'exportation
    notion_html_path = generate_notion_page()
    guide_path = create_notion_integration_guide()
    
    # Capturer des captures d'écran si demandé
    capture_screenshots_option = input("\nVoulez-vous capturer des captures d'écran de l'application Streamlit? (o/n): ")
    if capture_screenshots_option.lower() == 'o':
        capture_screenshots()
    
    print("\n" + "=" * 70)
    print(" Exportation terminée! ")
    print("=" * 70)
    print(f"\nFichiers générés dans: {NOTION_EXPORT_DIR}\n")
    print(f"Documentation HTML: {notion_html_path}")
    print(f"Guide d'importation: {guide_path}")
    print("\nSuivez les instructions du guide pour importer la documentation dans Notion.")

if __name__ == "__main__":
    main()
