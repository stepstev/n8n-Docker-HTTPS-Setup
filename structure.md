# Structure du projet Automations n8n

Ce document explique la structure simplifiée du projet pour faciliter la gestion Git.

## Organisation des dossiers

```
__Automations_n8n/
│
├── docs/                      # Documentation globale
│   ├── installation.md        # Guide d'installation
│   └── usage.md               # Guide d'utilisation
│
├── examples/                  # Exemples de workflows
│   ├── ai-integration/        # Workflows d'intégration IA
│   └── marketing/             # Workflows marketing
│
├── marketing/                 # Ressources marketing
│   └── linkedin/              # Contenu LinkedIn
│
├── training/                  # Matériel de formation
│   └── slides/                # Présentations
│
├── .gitignore                 # Configuration Git
├── README.md                  # Documentation principale
└── structure.md               # Ce document
```

## Notes importantes

- Le répertoire `n8n-docker-https-setup/n8n-docker/` est exclu du versionnement Git pour éviter les conflits
- Pour accéder aux fonctionnalités complètes, référez-vous à la documentation originale dans le dossier `docs/`
- Les workflows d'exemple dans `examples/` sont indépendants et peuvent être importés individuellement

## Conseils d'utilisation avec Git

1. Utilisez toujours le fichier `.gitignore` fourni
2. Pour ajouter des fichiers: `git add -A`
3. Pour vérifier ce qui sera commité: `git status`
4. Pour commiter: `git commit -m "Description des changements"`
5. Pour pousser: `git push origin main`

## Restauration des dossiers exclus

Si vous avez besoin d'accéder aux dossiers exclus, vous pouvez:

1. Cloner le dépôt complet sans Git: `mkdir n8n-docker && curl -L url-du-zip > temp.zip && unzip temp.zip -d n8n-docker && rm temp.zip`
2. Utiliser le script de téléchargement: `python download_excluded_dirs.py`

Ces méthodes restaureront les dossiers sans les problèmes Git associés.
