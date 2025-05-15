import os
import shutil
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

# Configuration des chemins
PROJECT_ROOT = Path(r"D:\00-Conception_AI\__Automations_n8n\n8n-docker-https-setup")
COURSE_DIR = Path(r"D:\00-Conception_AI\__Automations_n8n\udemy-course-creator\course")
MODULES_DIR = COURSE_DIR / "modules"
RESOURCES_DIR = COURSE_DIR / "resources"
SCRIPTS_DIR = COURSE_DIR / "scripts"
SLIDES_DIR = COURSE_DIR / "slides"
EXERCISES_DIR = COURSE_DIR / "exercises"
RECORDINGS_DIR = COURSE_DIR / "recordings"

# Métadonnées du cours
COURSE_METADATA = {
    "title": "n8n Docker HTTPS Setup: Automatisation de workflows avec IA",
    "subtitle": "Maîtrisez la configuration de n8n dans Docker avec HTTPS via ngrok et fonctionnalités d'IA",
    "description": """
Ce cours complet vous apprendra à configurer et utiliser n8n, une puissante plateforme d'automatisation de workflows, dans un environnement Docker sécurisé avec accès HTTPS via ngrok et fonctionnalités d'IA intégrées.

### Ce que vous apprendrez:
- Configurer n8n dans un environnement Docker
- Mettre en place un accès HTTPS sécurisé via ngrok
- Activer et utiliser les fonctionnalités d'IA dans n8n
- Créer des workflows automatisés avec scraping web via IA
- Documenter et partager votre configuration avec Streamlit

### Prérequis:
- Connaissances de base en ligne de commande
- Familiarité avec Docker (pas d'expertise requise)
- Ordinateur Windows, Mac ou Linux

### Public cible:
- Développeurs et ingénieurs DevOps
- Experts en automatisation et intégration
- Professionnels de l'IA cherchant à automatiser des workflows
- Toute personne souhaitant créer des automatisations sans code
    """,
    "language": "French",
    "level": "Intermediate",
    "category": "IT & Software",
    "subcategory": "DevOps",
    "price_tier": "Tier 2", # $49.99
    "duration_hours": 5.5,
    "author": "Stéphane CELTON"
}

# Structure du cours
COURSE_STRUCTURE = [
    {
        "module_id": 1,
        "title": "Introduction et vue d'ensemble",
        "description": "Découvrez n8n et les objectifs du projet",
        "lectures": [
            {
                "lecture_id": 1,
                "title": "Présentation du cours et objectifs",
                "type": "video",
                "duration_minutes": 8,
                "script_outline": """
- Bienvenue au cours n8n Docker HTTPS Setup
- Qui suis-je et mon expérience avec n8n et l'automatisation
- Ce que vous allez apprendre dans ce cours
- Structure du cours et comment en tirer le meilleur parti
- Prérequis techniques
- Comment obtenir de l'aide pendant le cours
                """
            },
            {
                "lecture_id": 2,
                "title": "Qu'est-ce que n8n?",
                "type": "video",
                "duration_minutes": 12,
                "script_outline": """
- Présentation de n8n et ses cas d'utilisation
- Comparaison avec d'autres outils (Zapier, Integromat, etc.)
- Avantages de n8n: open-source, auto-hébergé, extensible
- Interface visuelle et concept de workflows
- Écosystème et communauté
                """
            },
            {
                "lecture_id": 3,
                "title": "Architecture du projet",
                "type": "video",
                "duration_minutes": 15,
                "script_outline": """
- Vue d'ensemble de l'architecture
- Docker et conteneurisation
- HTTPS via ngrok
- Stockage persistant
- Intégration IA via MCP
- Documentation avec Streamlit
                """
            }
        ]
    },
    {
        "module_id": 2,
        "title": "Installation et configuration",
        "description": "Mettez en place l'environnement n8n avec Docker",
        "lectures": [
            {
                "lecture_id": 1,
                "title": "Installation des prérequis",
                "type": "video",
                "duration_minutes": 20,
                "script_outline": """
- Installation de Docker Desktop
- Installation de Docker Compose
- Installation de ngrok
- Installation de Python pour les scripts utilitaires
- Vérification des installations avec check_prerequisites.py
                """
            },
            {
                "lecture_id": 2,
                "title": "Configuration de Docker pour n8n",
                "type": "video",
                "duration_minutes": 25,
                "script_outline": """
- Explication du fichier docker-compose.yml
- Configuration des variables d'environnement
- Configuration de l'authentification
- Configuration des volumes persistants
- Options avancées de configuration
                """
            },
            {
                "lecture_id": 3,
                "title": "Premier démarrage de n8n",
                "type": "video",
                "duration_minutes": 15,
                "script_outline": """
- Utilisation du script de menu pour démarrer n8n
- Vérification du fonctionnement
- Premier accès à l'interface web
- Exploration de l'interface utilisateur
- Exercice pratique: Premier workflow simple
                """
            }
        ]
    },
    {
        "module_id": 3,
        "title": "Configuration HTTPS avec ngrok",
        "description": "Sécurisez l'accès à n8n avec HTTPS via ngrok",
        "lectures": [
            {
                "lecture_id": 1,
                "title": "Configuration de ngrok",
                "type": "video",
                "duration_minutes": 15,
                "script_outline": """
- Création d'un compte ngrok
- Obtention et configuration du token d'authentification
- Configuration du tunnel vers n8n
- Options de configuration avancées
                """
            },
            {
                "lecture_id": 2,
                "title": "Démarrage de n8n avec HTTPS",
                "type": "video",
                "duration_minutes": 18,
                "script_outline": """
- Utilisation du script de menu pour démarrer avec ngrok
- Analyse des informations de connexion
- Accès à l'interface via HTTPS
- Configuration des webhooks avec l'URL publique
- Gestion des limitations de la version gratuite de ngrok
                """
            },
            {
                "lecture_id": 3,
                "title": "Sécurité et bonnes pratiques",
                "type": "video",
                "duration_minutes": 20,
                "script_outline": """
- Importance de l'authentification
- Gestion des identifiants et mots de passe
- Limites de sécurité de ngrok
- Bonnes pratiques pour un environnement de production
- Alternatives à ngrok pour un déploiement permanent
                """
            }
        ]
    },
    {
        "module_id": 4,
        "title": "Fonctionnalités IA dans n8n",
        "description": "Exploitez les capacités d'IA dans n8n",
        "lectures": [
            {
                "lecture_id": 1,
                "title": "Activation des fonctionnalités IA",
                "type": "video",
                "duration_minutes": 15,
                "script_outline": """
- Configuration des variables d'environnement pour l'IA
- Installation d'Ollama (facultatif)
- Configuration de MCP (Model Control Protocol)
- Vérification de l'activation des nodes d'IA
                """
            },
            {
                "lecture_id": 2,
                "title": "Utilisation des nodes LangChain",
                "type": "video",
                "duration_minutes": 25,
                "script_outline": """
- Introduction à LangChain dans n8n
- Configuration des modèles de langage
- Création d'agents IA
- Utilisation de la mémoire
- Exercice pratique: Création d'un assistant simple
                """
            },
            {
                "lecture_id": 3,
                "title": "Workflow avancé: Agent IA pour le scraping web",
                "type": "video",
                "duration_minutes": 35,
                "script_outline": """
- Introduction au workflow N8n_Agent_IA_MCP.json
- Explication des différents composants
- Configuration des nodes MCP Client
- Test du workflow avec différentes requêtes
- Personnalisation du comportement de l'agent
- Exercice pratique: Adaptation du workflow pour un autre cas d'usage
                """
            }
        ]
    },
    {
        "module_id": 5,
        "title": "Documentation et partage",
        "description": "Documentez et partagez votre configuration",
        "lectures": [
            {
                "lecture_id": 1,
                "title": "Documentation Streamlit",
                "type": "video",
                "duration_minutes": 20,
                "script_outline": """
- Introduction à la documentation Streamlit
- Structure et contenu
- Démarrage de la documentation
- Options de déploiement
                """
            },
            {
                "lecture_id": 2,
                "title": "Déploiement de la documentation",
                "type": "video",
                "duration_minutes": 25,
                "script_outline": """
- Options de déploiement local
- Déploiement sur le réseau
- Déploiement avec ngrok
- Déploiement sur Streamlit Cloud
                """
            },
            {
                "lecture_id": 3,
                "title": "Exportation de la documentation",
                "type": "video",
                "duration_minutes": 15,
                "script_outline": """
- Exportation vers HTML
- Exportation vers Notion
- Création de présentations PowerPoint
- Partage des configurations
                """
            }
        ]
    },
    {
        "module_id": 6,
        "title": "Projets et cas d'usage",
        "description": "Appliquez vos connaissances à des projets concrets",
        "lectures": [
            {
                "lecture_id": 1,
                "title": "Projet: Moniteur de sites web avec alerte",
                "type": "video",
                "duration_minutes": 30,
                "script_outline": """
- Objectif du projet
- Configuration du workflow
- Intégration avec le service de notification
- Test et débogage
- Déploiement et monitoring
                """
            },
            {
                "lecture_id": 2,
                "title": "Projet: Automatisation des réseaux sociaux avec IA",
                "type": "video",
                "duration_minutes": 35,
                "script_outline": """
- Objectif du projet
- Configuration de l'authentification OAuth
- Création du workflow avec génération de contenu IA
- Planification des publications
- Test et ajustements
                """
            },
            {
                "lecture_id": 3,
                "title": "Conclusion et prochaines étapes",
                "type": "video",
                "duration_minutes": 12,
                "script_outline": """
- Récapitulatif de ce que nous avons appris
- Ressources supplémentaires
- Communauté n8n
- Mises à jour futures
- Comment continuer à apprendre
- Merci et au revoir!
                """
            }
        ]
    }
]

def create_directory_structure():
    """Crée la structure de répertoires pour le cours."""
    directories = [
        COURSE_DIR, MODULES_DIR, RESOURCES_DIR, SCRIPTS_DIR, 
        SLIDES_DIR, EXERCISES_DIR, RECORDINGS_DIR
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"Répertoire créé: {directory}")
    
    # Créer les sous-répertoires pour chaque module
    for module in COURSE_STRUCTURE:
        module_dir = MODULES_DIR / f"module_{module['module_id']:02d}"
        module_dir.mkdir(exist_ok=True)
        
        # Créer les sous-répertoires pour chaque leçon
        for lecture in module["lectures"]:
            lecture_dir = module_dir / f"lecture_{lecture['lecture_id']:02d}"
            lecture_dir.mkdir(exist_ok=True)
            
            # Créer des sous-répertoires spécifiques pour chaque type de contenu
            (lecture_dir / "script").mkdir(exist_ok=True)
            (lecture_dir / "slides").mkdir(exist_ok=True)
            (lecture_dir / "resources").mkdir(exist_ok=True)
            
    print("Structure de répertoires créée avec succès!")

def generate_course_metadata():
    """Génère le fichier de métadonnées du cours."""
    metadata_file = COURSE_DIR / "course_metadata.json"
    
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(COURSE_METADATA, f, ensure_ascii=False, indent=4)
    
    print(f"Métadonnées du cours générées: {metadata_file}")

def generate_course_structure():
    """Génère le fichier de structure du cours."""
    structure_file = COURSE_DIR / "course_structure.json"
    
    with open(structure_file, 'w', encoding='utf-8') as f:
        json.dump(COURSE_STRUCTURE, f, ensure_ascii=False, indent=4)
    
    print(f"Structure du cours générée: {structure_file}")

def generate_lecture_scripts():
    """Génère les scripts pour chaque leçon."""
    for module in COURSE_STRUCTURE:
        module_id = module["module_id"]
        module_title = module["title"]
        
        for lecture in module["lectures"]:
            lecture_id = lecture["lecture_id"]
            lecture_title = lecture["title"]
            script_outline = lecture["script_outline"].strip()
            
            # Chemin du script pour cette leçon
            script_dir = MODULES_DIR / f"module_{module_id:02d}" / f"lecture_{lecture_id:02d}" / "script"
            script_file = script_dir / f"script.md"
            
            # Générer le contenu du script
            script_content = f"""# Module {module_id}: {module_title}
## Leçon {lecture_id}: {lecture_title}

*Durée estimée: {lecture['duration_minutes']} minutes*

### Objectifs d'apprentissage
- [Listez ici les objectifs d'apprentissage spécifiques]

### Script

```
{script_outline}
```

### Points clés à couvrir
- [Point clé 1]
- [Point clé 2]
- [Point clé 3]

### Démonstrations
- [Description de la démonstration 1]
- [Description de la démonstration 2]

### Ressources à montrer
- [Ressource 1]
- [Ressource 2]

### Notes pour l'enregistrement
- [Note 1]
- [Note 2]
"""
            
            with open(script_file, 'w', encoding='utf-8') as f:
                f.write(script_content)
            
            print(f"Script généré: {script_file}")

def generate_slide_templates():
    """Génère des modèles de diapositives pour chaque leçon."""
    for module in COURSE_STRUCTURE:
        module_id = module["module_id"]
        module_title = module["title"]
        
        for lecture in module["lectures"]:
            lecture_id = lecture["lecture_id"]
            lecture_title = lecture["title"]
            
            # Chemin pour les diapositives de cette leçon
            slides_dir = MODULES_DIR / f"module_{module_id:02d}" / f"lecture_{lecture_id:02d}" / "slides"
            slides_md_file = slides_dir / f"slides.md"
            
            # Générer le contenu du fichier Markdown pour les diapositives
            slides_content = f"""---
marp: true
theme: default
paginate: true
---

# Module {module_id}: {module_title}
## Leçon {lecture_id}: {lecture_title}

---

# Objectifs

- Objectif 1
- Objectif 2
- Objectif 3

---

# Contenu

1. Section 1
2. Section 2
3. Section 3

---

<!-- Ajoutez d'autres diapositives ici -->

---

# Résumé

- Point clé 1
- Point clé 2
- Point clé 3

---

# Questions?

Merci de votre attention!
"""
            
            with open(slides_md_file, 'w', encoding='utf-8') as f:
                f.write(slides_content)
            
            print(f"Modèle de diapositives généré: {slides_md_file}")

def generate_exercises():
    """Génère des exercices pratiques pour chaque module."""
    for module in COURSE_STRUCTURE:
        module_id = module["module_id"]
        module_title = module["title"]
        
        # Fichier d'exercices pour ce module
        exercise_file = EXERCISES_DIR / f"module_{module_id:02d}_exercises.md"
        
        # Générer le contenu des exercices
        exercise_content = f"""# Exercices pratiques - Module {module_id}: {module_title}

## Exercice 1: [Titre de l'exercice]

### Objectif
[Description de l'objectif de l'exercice]

### Instructions
1. [Étape 1]
2. [Étape 2]
3. [Étape 3]

### Critères de réussite
- [Critère 1]
- [Critère 2]

### Solution
<details>
  <summary>Cliquez pour voir la solution</summary>
  
  ```python
  # Code ou étapes de la solution
  ```
</details>

## Exercice 2: [Titre de l'exercice]

### Objectif
[Description de l'objectif de l'exercice]

### Instructions
1. [Étape 1]
2. [Étape 2]
3. [Étape 3]

### Critères de réussite
- [Critère 1]
- [Critère 2]

### Solution
<details>
  <summary>Cliquez pour voir la solution</summary>
  
  ```python
  # Code ou étapes de la solution
  ```
</details>

## Projet pratique

### Objectif
[Description du projet pratique pour ce module]

### Instructions
1. [Étape 1]
2. [Étape 2]
3. [Étape 3]

### Livrables
- [Livrable 1]
- [Livrable 2]

### Critères d'évaluation
- [Critère 1]
- [Critère 2]
"""
        
        with open(exercise_file, 'w', encoding='utf-8') as f:
            f.write(exercise_content)
        
        print(f"Exercices générés: {exercise_file}")

def generate_resources():
    """Copie et génère des ressources pour le cours."""
    # Créer un fichier README pour les ressources
    readme_file = RESOURCES_DIR / "README.md"
    
    readme_content = """# Ressources du cours

Ce répertoire contient toutes les ressources nécessaires pour suivre le cours "n8n Docker HTTPS Setup".

## Fichiers de configuration

- `docker-compose.yml` - Fichier de configuration Docker pour n8n
- `ngrok_config.yml` - Configuration exemple pour ngrok

## Scripts

- `check_prerequisites.py` - Script de vérification des prérequis
- `start_n8n_menu.py` - Script de menu pour démarrer n8n

## Workflows d'exemple

- `N8n_Agent_IA_MCP.json` - Workflow d'agent IA pour le scraping
- `web_monitor.json` - Workflow de monitoring de sites web
- `social_media_automation.json` - Workflow d'automatisation des réseaux sociaux

## Documentation

- Liens vers la documentation officielle
- Ressources supplémentaires
- Communauté et support

## Comment utiliser ces ressources

1. Téléchargez les fichiers nécessaires pour chaque section du cours
2. Suivez les instructions dans les vidéos
3. Utilisez les fichiers comme référence pour vos propres projets
"""
    
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"README des ressources généré: {readme_file}")
    
    # Copier les fichiers du projet source
    try:
        # Copier le fichier docker-compose.yml
        docker_compose_src = PROJECT_ROOT / "n8n-docker" / "docker-compose.yml"
        docker_compose_dst = RESOURCES_DIR / "docker-compose.yml"
        
        if docker_compose_src.exists():
            shutil.copy2(docker_compose_src, docker_compose_dst)
            print(f"Fichier copié: {docker_compose_dst}")
        else:
            print(f"Attention: Fichier source introuvable - {docker_compose_src}")
        
        # Copier le script de vérification des prérequis
        prereq_script_src = PROJECT_ROOT / "n8n-docker" / "check_prerequisites.py"
        prereq_script_dst = RESOURCES_DIR / "check_prerequisites.py"
        
        if prereq_script_src.exists():
            shutil.copy2(prereq_script_src, prereq_script_dst)
            print(f"Fichier copié: {prereq_script_dst}")
        else:
            print(f"Attention: Fichier source introuvable - {prereq_script_src}")
        
        # Copier le workflow d'exemple
        workflow_src = PROJECT_ROOT / "n8n-docker" / "Scénarios" / "N8n_Agent_IA_MCP.json"
        workflow_dst = RESOURCES_DIR / "N8n_Agent_IA_MCP.json"
        
        if workflow_src.exists():
            shutil.copy2(workflow_src, workflow_dst)
            print(f"Fichier copié: {workflow_dst}")
        else:
            print(f"Attention: Fichier source introuvable - {workflow_src}")
            
    except Exception as e:
        print(f"Erreur lors de la copie des fichiers: {e}")

def generate_recording_guide():
    """Génère un guide pour l'enregistrement des vidéos."""
    recording_guide_file = RECORDINGS_DIR / "recording_guide.md"
    
    recording_guide_content = """# Guide d'enregistrement des vidéos du cours

## Configuration technique recommandée

- **Résolution d'écran:** 1920x1080 (Full HD)
- **Format d'enregistrement:** MP4, 30fps
- **Microphone:** Microphone externe de qualité (USB ou XLR avec interface audio)
- **Logiciel d'enregistrement:** OBS Studio, Camtasia, ou ScreenFlow
- **Éclairage:** Éclairage suffisant pour éviter les ombres sur le visage

## Structure des vidéos

Chaque vidéo doit suivre cette structure:

1. **Introduction (15-30 secondes)**
   - Accueil et présentation du sujet
   - Ce que l'étudiant va apprendre dans cette leçon

2. **Contenu principal**
   - Explication pas à pas des concepts
   - Démonstrations pratiques
   - Points clés à souligner

3. **Conclusion (15-30 secondes)**
   - Récapitulatif de ce qui a été appris
   - Transition vers la prochaine leçon ou exercice pratique

## Conseils pour l'enregistrement

- **Discours:** Parlez clairement et à un rythme modéré
- **Langage corporel:** Soyez énergique et engageant
- **Écran:** Augmentez la taille des polices et du curseur pour une meilleure visibilité
- **Démos:** Pratiquez les démos plusieurs fois avant l'enregistrement
- **Erreurs:** Si vous faites une erreur, expliquez-la et montrez comment la corriger
- **Silence:** Évitez les longues périodes de silence
- **Édition:** Marquez les points où l'édition sera nécessaire

## Processus d'enregistrement

1. **Préparation**
   - Relisez le script de la leçon
   - Préparez l'environnement technique
   - Testez l'audio et la vidéo

2. **Enregistrement**
   - Suivez le script mais restez naturel
   - Parlez à la caméra comme si vous parliez à un étudiant
   - Prenez des pauses si nécessaire

3. **Post-production**
   - Éditez la vidéo pour supprimer les erreurs et les pauses
   - Ajoutez des annotations et des zooms si nécessaire
   - Ajoutez une intro et un outro standard
   - Assurez-vous que l'audio est clair et à un niveau cohérent

## Nomenclature des fichiers

Format: `module_XX_lecture_YY_[description].mp4`

Exemple: `module_01_lecture_02_what_is_n8n.mp4`

## Checklist avant publication

- [ ] Vidéo en résolution 1920x1080
- [ ] Audio clair sans bruits de fond
- [ ] Introduction et conclusion présentes
- [ ] Contenu conforme au script
- [ ] Annotations et zooms ajoutés
- [ ] Qualité globale vérifiée
- [ ] Fichier correctement nommé
"""
    
    with open(recording_guide_file, 'w', encoding='utf-8') as f:
        f.write(recording_guide_content)
    
    print(f"Guide d'enregistrement généré: {recording_guide_file}")

def generate_udemy_upload_guide():
    """Génère un guide pour l'upload du cours sur Udemy."""
    upload_guide_file = COURSE_DIR / "udemy_upload_guide.md"
    
    upload_guide_content = """# Guide d'upload du cours sur Udemy

## Préparer votre compte instructeur

1. Créez un compte instructeur sur Udemy: [https://www.udemy.com/teaching/?ref=teach_header](https://www.udemy.com/teaching/?ref=teach_header)
2. Complétez votre profil instructeur avec une photo, une biographie et vos qualifications

## Préparer les éléments marketing

Avant de commencer l'upload, assurez-vous d'avoir:

- **Image de couverture:** 750x422 pixels, au format JPG ou PNG
- **Vidéo promotionnelle:** 1-3 minutes présentant le cours
- **Description du cours:** Titre, sous-titre et description complète
- **Public cible:** À qui s'adresse ce cours
- **Prérequis:** Ce que les étudiants doivent savoir avant de commencer
- **Objectifs d'apprentissage:** Ce que les étudiants vont apprendre

## Processus d'upload

1. **Créer un nouveau cours**
   - Allez à "Instructor Dashboard" > "Create Your Course"
   - Remplissez les informations de base du cours

2. **Organiser le curriculum**
   - Créez les sections correspondant aux modules du cours
   - Créez les leçons dans chaque section
   - Téléchargez les vidéos pour chaque leçon
   - Ajoutez les ressources supplémentaires à chaque leçon
   - Créez des quiz pour chaque module

3. **Configurer le prix**
   - Sélectionnez le niveau de prix approprié
   - Envisagez d'offrir un coupon de lancement

4. **Soumettre pour approbation**
   - Vérifiez que tous les éléments obligatoires sont complétés
   - Soumettez votre cours pour révision par Udemy

## Exigences techniques de Udemy

- **Vidéos:** MP4, résolution minimale 720p (1280x720), idéalement 1080p (1920x1080)
- **Audio:** Qualité claire sans bruits de fond, 44.1 kHz, 128 kbps+
- **Durée du cours:** Minimum 30 minutes de contenu vidéo
- **Durée des leçons:** Idéalement entre 3-15 minutes chacune

## Stratégie de lancement

1. **Pré-lancement**
   - Créez une page de pré-inscription
   - Annoncez le cours sur les réseaux sociaux et via email
   - Offrez des codes promo de pré-lancement

2. **Lancement**
   - Publiez sur vos réseaux sociaux
   - Envoyez un email à votre liste
   - Demandez des avis à des étudiants beta

3. **Post-lancement**
   - Répondez aux questions des étudiants
   - Demandez des avis aux premiers étudiants
   - Mettez à jour le cours en fonction des retours

## Conseils pour le succès sur Udemy

- Répondez rapidement aux questions des étudiants
- Mettez à jour régulièrement votre cours
- Encouragez les étudiants à laisser des avis
- Créez une communauté autour de votre cours
- Utilisez les analyses Udemy pour améliorer votre cours
"""
    
    with open(upload_guide_file, 'w', encoding='utf-8') as f:
        f.write(upload_guide_content)
    
    print(f"Guide d'upload Udemy généré: {upload_guide_file}")

def create_course_planner():
    """Crée un fichier HTML pour planifier le cours."""
    planner_file = COURSE_DIR / "course_planner.html"
    
    planner_content = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Planificateur de cours Udemy</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        
        h1, h2, h3 {
            color: #2a7ab0;
        }
        
        .course-header {
            background-color: #2a7ab0;
            color: white;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        
        .course-header h1 {
            color: white;
            margin: 0;
        }
        
        .course-header p {
            margin: 10px 0 0 0;
            font-size: 1.2rem;
        }
        
        .module {
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            padding: 15px;
        }
        
        .module-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 15px;
        }
        
        .module-title {
            margin: 0;
            cursor: pointer;
        }
        
        .module-title:hover {
            color: #1c567d;
        }
        
        .lecture {
            background-color: #f9f9f9;
            border-radius: 5px;
            padding: 10px 15px;
            margin-bottom: 10px;
        }
        
        .lecture-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            cursor: pointer;
        }
        
        .lecture-title {
            margin: 0;
            font-size: 1.1rem;
        }
        
        .lecture-details {
            display: none;
            padding: 10px 0;
            border-top: 1px solid #eee;
            margin-top: 10px;
        }
        
        .lecture-details.show {
            display: block;
        }
        
        .status {
            padding: 3px 8px;
            border-radius: 3px;
            font-size: 0.8rem;
            font-weight: bold;
        }
        
        .status-not-started {
            background-color: #e0e0e0;
            color: #555;
        }
        
        .status-in-progress {
            background-color: #ffd8a8;
            color: #805b36;
        }
        
        .status-completed {
            background-color: #a8e6cf;
            color: #2d6a4f;
        }
        
        .progress-bar-container {
            width: 100%;
            background-color: #e0e0e0;
            border-radius: 3px;
            margin-top: 20px;
        }
        
        .progress-bar {
            height: 10px;
            background-color: #2a7ab0;
            border-radius: 3px;
            width: 0%;
        }
        
        .course-stats {
            display: flex;
            justify-content: space-between;
            margin-top: 10px;
            font-size: 0.9rem;
        }
        
        button {
            background-color: #2a7ab0;
            color: white;
            border: none;
            padding: 5px 10px;
            border-radius: 3px;
            cursor: pointer;
            font-size: 0.9rem;
        }
        
        button:hover {
            background-color: #1c567d;
        }
        
        .filters {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }
        
        .filter-btn {
            background-color: white;
            color: #333;
            border: 1px solid #ddd;
            padding: 5px 15px;
            border-radius: 20px;
            cursor: pointer;
        }
        
        .filter-btn.active {
            background-color: #2a7ab0;
            color: white;
            border-color: #2a7ab0;
        }
    </style>
</head>
<body>
    <div class="course-header">
        <h1>n8n Docker HTTPS Setup - Planificateur de cours</h1>
        <p>Automatisation de workflows avec Docker, ngrok et IA</p>
    </div>
    
    <div class="filters">
        <button class="filter-btn active" data-filter="all">Tout</button>
        <button class="filter-btn" data-filter="not-started">Non commencé</button>
        <button class="filter-btn" data-filter="in-progress">En cours</button>
        <button class="filter-btn" data-filter="completed">Terminé</button>
    </div>
    
    <div class="progress-bar-container">
        <div class="progress-bar" id="overall-progress"></div>
    </div>
    
    <div class="course-stats">
        <span id="completion-rate">Taux de complétion: 0%</span>
        <span id="total-duration">Durée totale: 0/0 minutes</span>
    </div>
    
    <div id="modules-container">
        <!-- Modules générés dynamiquement ici -->
    </div>
    
    <script>
        // Données du cours (générées par le script)
        const courseStructure = COURSE_STRUCTURE_JSON;
        
        // État du cours (à sauvegarder localement)
        let courseState = JSON.parse(localStorage.getItem('courseState')) || {};
        
        // Initialisation
        function initializeCourseState() {
            let initialized = false;
            
            courseStructure.forEach(module => {
                if (!courseState[`module_${module.module_id}`]) {
                    courseState[`module_${module.module_id}`] = { status: 'not-started' };
                    initialized = true;
                }
                
                module.lectures.forEach(lecture => {
                    const lectureKey = `module_${module.module_id}_lecture_${lecture.lecture_id}`;
                    if (!courseState[lectureKey]) {
                        courseState[lectureKey] = { 
                            status: 'not-started',
                            notes: '',
                            completedDate: null
                        };
                        initialized = true;
                    }
                });
            });
            
            if (initialized) {
                saveCourseState();
            }
        }
        
        // Rendu des modules
        function renderModules() {
            const modulesContainer = document.getElementById('modules-container');
            modulesContainer.innerHTML = '';
            
            courseStructure.forEach(module => {
                const moduleElement = document.createElement('div');
                moduleElement.className = `module module-status-${courseState[`module_${module.module_id}`].status}`;
                moduleElement.dataset.status = courseState[`module_${module.module_id}`].status;
                
                moduleElement.innerHTML = `
                    <div class="module-header">
                        <h2 class="module-title" onclick="toggleModule(this)">
                            Module ${module.module_id}: ${module.title}
                        </h2>
                        <span class="status status-${courseState[`module_${module.module_id}`].status}">
                            ${getStatusText(courseState[`module_${module.module_id}`].status)}
                        </span>
                    </div>
                    <p>${module.description}</p>
                    <div class="lectures">
                        ${renderLectures(module)}
                    </div>
                    <div class="module-controls">
                        <button onclick="updateModuleStatus('module_${module.module_id}', 'not-started')">Non commencé</button>
                        <button onclick="updateModuleStatus('module_${module.module_id}', 'in-progress')">En cours</button>
                        <button onclick="updateModuleStatus('module_${module.module_id}', 'completed')">Terminé</button>
                    </div>
                `;
                
                modulesContainer.appendChild(moduleElement);
            });
            
            updateStats();
        }
        
        // Rendu des leçons
        function renderLectures(module) {
            return module.lectures.map(lecture => {
                const lectureKey = `module_${module.module_id}_lecture_${lecture.lecture_id}`;
                const lectureState = courseState[lectureKey];
                
                return `
                    <div class="lecture lecture-status-${lectureState.status}" data-status="${lectureState.status}">
                        <div class="lecture-header" onclick="toggleLecture(this)">
                            <h3 class="lecture-title">
                                Leçon ${lecture.lecture_id}: ${lecture.title}
                            </h3>
                            <span class="status status-${lectureState.status}">
                                ${getStatusText(lectureState.status)}
                            </span>
                        </div>
                        <div class="lecture-details">
                            <p><strong>Type:</strong> ${lecture.type}</p>
                            <p><strong>Durée estimée:</strong> ${lecture.duration_minutes} minutes</p>
                            <div>
                                <p><strong>Notes:</strong></p>
                                <textarea 
                                    id="${lectureKey}-notes" 
                                    rows="3" 
                                    style="width: 100%;"
                                    onchange="updateLectureNotes('${lectureKey}')"
                                >${lectureState.notes}</textarea>
                            </div>
                            <div class="lecture-controls">
                                <button onclick="updateLectureStatus('${lectureKey}', 'not-started')">Non commencé</button>
                                <button onclick="updateLectureStatus('${lectureKey}', 'in-progress')">En cours</button>
                                <button onclick="updateLectureStatus('${lectureKey}', 'completed')">Terminé</button>
                            </div>
                        </div>
                    </div>
                `;
            }).join('');
        }
        
        // Mise à jour du statut d'une leçon
        function updateLectureStatus(lectureKey, status) {
            courseState[lectureKey].status = status;
            
            if (status === 'completed' && !courseState[lectureKey].completedDate) {
                courseState[lectureKey].completedDate = new Date().toISOString();
            } else if (status !== 'completed') {
                courseState[lectureKey].completedDate = null;
            }
            
            updateModuleStatusBasedOnLectures(lectureKey);
            saveCourseState();
            renderModules();
        }
        
        // Mise à jour des notes d'une leçon
        function updateLectureNotes(lectureKey) {
            const notesElement = document.getElementById(`${lectureKey}-notes`);
            courseState[lectureKey].notes = notesElement.value;
            saveCourseState();
        }
        
        // Mise à jour du statut d'un module
        function updateModuleStatus(moduleKey, status) {
            courseState[moduleKey].status = status;
            saveCourseState();
            renderModules();
        }
        
        // Mise à jour du statut d'un module en fonction des leçons
        function updateModuleStatusBasedOnLectures(lectureKey) {
            // Extraire l'ID du module du lectureKey (ex: "module_1_lecture_2" -> "module_1")
            const moduleKey = lectureKey.substring(0, lectureKey.indexOf('_lecture_'));
            
            // Trouver le module dans la structure du cours
            const moduleId = parseInt(moduleKey.split('_')[1]);
            const module = courseStructure.find(m => m.module_id === moduleId);
            
            if (!module) return;
            
            // Vérifier le statut de toutes les leçons
            const lectureStatuses = module.lectures.map(lecture => {
                const key = `${moduleKey}_lecture_${lecture.lecture_id}`;
                return courseState[key].status;
            });
            
            if (lectureStatuses.every(status => status === 'completed')) {
                courseState[moduleKey].status = 'completed';
            } else if (lectureStatuses.some(status => status === 'completed' || status === 'in-progress')) {
                courseState[moduleKey].status = 'in-progress';
            } else {
                courseState[moduleKey].status = 'not-started';
            }
        }
        
        // Sauvegarde de l'état du cours
        function saveCourseState() {
            localStorage.setItem('courseState', JSON.stringify(courseState));
        }
        
        // Texte du statut
        function getStatusText(status) {
            switch (status) {
                case 'not-started': return 'Non commencé';
                case 'in-progress': return 'En cours';
                case 'completed': return 'Terminé';
                default: return status;
            }
        }
        
        // Afficher/masquer les détails d'une leçon
        function toggleLecture(element) {
            const details = element.nextElementSibling;
            details.classList.toggle('show');
        }
        
        // Afficher/masquer les leçons d'un module
        function toggleModule(element) {
            const lectures = element.closest('.module').querySelector('.lectures');
            lectures.style.display = lectures.style.display === 'none' ? 'block' : 'none';
        }
        
        // Filtrage
        document.querySelectorAll('.filter-btn').forEach(button => {
            button.addEventListener('click', () => {
                // Mise à jour des boutons de filtre
                document.querySelectorAll('.filter-btn').forEach(btn => {
                    btn.classList.remove('active');
                });
                button.classList.add('active');
                
                // Filtrage des modules et leçons
                const filter = button.dataset.filter;
                
                document.querySelectorAll('.module').forEach(module => {
                    if (filter === 'all' || module.dataset.status === filter) {
                        module.style.display = 'block';
                    } else {
                        module.style.display = 'none';
                    }
                });
                
                document.querySelectorAll('.lecture').forEach(lecture => {
                    if (filter === 'all' || lecture.dataset.status === filter) {
                        lecture.style.display = 'block';
                    } else {
                        lecture.style.display = 'none';
                    }
                });
            });
        });
        
        // Mise à jour des statistiques
        function updateStats() {
            let totalLectures = 0;
            let completedLectures = 0;
            let totalDuration = 0;
            let completedDuration = 0;
            
            courseStructure.forEach(module => {
                module.lectures.forEach(lecture => {
                    const lectureKey = `module_${module.module_id}_lecture_${lecture.lecture_id}`;
                    totalLectures++;
                    totalDuration += lecture.duration_minutes;
                    
                    if (courseState[lectureKey].status === 'completed') {
                        completedLectures++;
                        completedDuration += lecture.duration_minutes;
                    }
                });
            });
            
            const completionRate = totalLectures > 0 ? Math.round((completedLectures / totalLectures) * 100) : 0;
            
            document.getElementById('completion-rate').textContent = `Taux de complétion: ${completionRate}%`;
            document.getElementById('total-duration').textContent = `Durée: ${completedDuration}/${totalDuration} minutes`;
            document.getElementById('overall-progress').style.width = `${completionRate}%`;
        }
        
        // Initialisation
        initializeCourseState();
        renderModules();
    </script>
    
    <script>
        // Remplacer par les données réelles du cours
        document.querySelector('script').textContent = document.querySelector('script').textContent.replace('COURSE_STRUCTURE_JSON', JSON.stringify(COURSE_STRUCTURE));
    </script>
</body>
</html>
"""
    
    # Remplacer le placeholder par les données réelles du cours
    planner_content = planner_content.replace('COURSE_STRUCTURE', json.dumps(COURSE_STRUCTURE, ensure_ascii=False))
    
    with open(planner_file, 'w', encoding='utf-8') as f:
        f.write(planner_content)
    
    print(f"Planificateur de cours généré: {planner_file}")

def main():
    """Fonction principale."""
    print("=" * 70)
    print("Générateur de cours Udemy - n8n Docker HTTPS Setup")
    print("=" * 70)
    print("\nCe script va générer une structure complète pour créer un cours Udemy")
    print("basé sur le projet n8n Docker HTTPS Setup.\n")
    
    # Créer la structure de répertoires
    create_directory_structure()
    
    # Générer les fichiers principaux
    generate_course_metadata()
    generate_course_structure()
    
    # Générer les scripts et ressources
    generate_lecture_scripts()
    generate_slide_templates()
    generate_exercises()
    generate_resources()
    
    # Générer les guides
    generate_recording_guide()
    generate_udemy_upload_guide()
    
    # Créer le planificateur de cours
    create_course_planner()
    
    print("\n" + "=" * 70)
    print("Génération terminée!")
    print("=" * 70)
    print(f"\nTous les fichiers ont été créés dans le répertoire: {COURSE_DIR}")
    print("\nPour commencer à créer votre cours Udemy:")
    print("1. Explorez la structure des modules et leçons")
    print("2. Personnalisez les scripts générés")
    print("3. Préparez les diapositives basées sur les modèles")
    print("4. Suivez le guide d'enregistrement pour créer vos vidéos")
    print("5. Utilisez le planificateur pour suivre votre progression")
    
    # Ouvrir le dossier du cours
    try:
        if os.name == 'nt':  # Windows
            os.startfile(COURSE_DIR)
        elif os.name == 'posix':  # macOS ou Linux
            subprocess.call(['open' if sys.platform == 'darwin' else 'xdg-open', COURSE_DIR])
    except Exception as e:
        print(f"\nErreur lors de l'ouverture du dossier: {e}")

if __name__ == "__main__":
    main()
