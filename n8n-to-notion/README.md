# Exportation de la documentation n8n vers Notion

Cet outil permet d'exporter la documentation Streamlit du projet n8n Docker HTTPS Setup vers Notion.

## Fonctionnalités

- Extraction du contenu Markdown depuis l'application Streamlit
- Génération de fichiers HTML et Markdown prêts pour l'importation dans Notion
- Capture d'écrans optionnelle de l'application Streamlit en cours d'exécution
- Guide détaillé pour l'importation dans Notion

## Prérequis

1. Python 3.8 ou supérieur
2. Les dépendances listées dans `requirements.txt`
3. Application Streamlit déjà configurée

## Installation

```bash
# Installer les dépendances
pip install -r requirements.txt
```

## Utilisation

1. Assurez-vous que l'application Streamlit est bien configurée dans le répertoire spécifié
2. Exécutez le script d'exportation :

```bash
python export_to_notion.py
```

3. Suivez les instructions à l'écran
4. Les fichiers exportés seront générés dans le dossier `export/`

## Structure des fichiers générés

- `export/n8n_documentation.html` : Documentation complète au format HTML
- `export/guide_import_notion.md` : Guide d'importation dans Notion
- `export/markdown/` : Sections individuelles au format Markdown
- `export/images/` : Captures d'écran et images

## Importation dans Notion

Consultez le fichier `export/guide_import_notion.md` pour des instructions détaillées sur l'importation de la documentation dans Notion.
