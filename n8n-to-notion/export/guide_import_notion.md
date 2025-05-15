# Guide d'importation dans Notion

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
