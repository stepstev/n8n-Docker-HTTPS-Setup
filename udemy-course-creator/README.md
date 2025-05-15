# Générateur de cours Udemy - n8n Docker HTTPS Setup

Ce projet génère automatiquement une structure complète pour créer un cours Udemy basé sur le projet n8n Docker HTTPS Setup.

## Fonctionnalités

- Génération de la structure complète du cours (modules et leçons)
- Création de scripts détaillés pour chaque leçon
- Modèles de diapositives pour chaque segment
- Exercices pratiques pour chaque module
- Guide d'enregistrement vidéo
- Planificateur de cours interactif
- Guide d'upload sur Udemy

## Utilisation

1. Exécutez le script principal pour générer tous les fichiers nécessaires :
```bash
python create_udemy_course.py
```

2. Le script va créer la structure suivante :
```
course/
├── modules/            # Structure des modules du cours
│   ├── module_01/      # Premier module
│   │   ├── lecture_01/ # Première leçon
│   │   │   ├── script/ # Script de la leçon
│   │   │   ├── slides/ # Diapositives
│   │   │   └── resources/ # Ressources spécifiques
│   │   └── ...
│   └── ...
├── resources/         # Ressources globales du cours
├── scripts/           # Scripts généraux
├── slides/            # Diapositives communes
├── exercises/         # Exercices pratiques
├── recordings/        # Guide d'enregistrement
├── course_metadata.json  # Métadonnées du cours
├── course_structure.json # Structure détaillée
├── course_planner.html   # Planificateur interactif
└── udemy_upload_guide.md # Guide d'upload
```

3. Personnalisez les fichiers générés selon vos besoins.

4. Utilisez le planificateur de cours (`course_planner.html`) pour suivre votre progression.

## Structure du cours

Le cours est organisé en 6 modules :

1. **Introduction et vue d'ensemble**
2. **Installation et configuration**
3. **Configuration HTTPS avec ngrok**
4. **Fonctionnalités IA dans n8n**
5. **Documentation et partage**
6. **Projets et cas d'usage**

Chaque module contient 3 leçons, pour un total d'environ 5,5 heures de contenu.

## Personnalisation

Vous pouvez personnaliser la structure du cours en modifiant les constantes au début du fichier `create_udemy_course.py` :

- `COURSE_METADATA` : Informations générales sur le cours
- `COURSE_STRUCTURE` : Structure détaillée des modules et leçons

## Prérequis

- Python 3.6 ou supérieur
- Accès aux fichiers du projet n8n Docker HTTPS Setup

## Note

Ce générateur est conçu pour accélérer le processus de création d'un cours Udemy en fournissant une structure complète. Il vous restera à créer le contenu réel (enregistrements vidéo, finalisation des scripts, etc.).
