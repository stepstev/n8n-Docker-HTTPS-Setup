import os
import sys
import json
import time
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

# Configuration du projet
PROJECT_DIR = r"D:\00-Conception_AI\__Automations_n8n\n8n-docker-https-setup"
OUTPUT_DIR = Path(__file__).parent / "output"
SCREENSHOTS_DIR = OUTPUT_DIR / "screenshots"
SCRIPT_FILE = OUTPUT_DIR / "script.md"
STORYBOARD_FILE = OUTPUT_DIR / "storyboard.json"
VIDEO_SEGMENTS_DIR = OUTPUT_DIR / "segments"

# Structure du script et du storyboard
YOUTUBE_SCRIPT = {
    "title": "Configuration complète de n8n avec Docker, HTTPS et IA en 15 minutes",
    "description": "Guide pas à pas pour configurer n8n avec Docker, ngrok pour HTTPS, et activation des fonctionnalités d'IA.",
    "tags": ["n8n", "automation", "docker", "ngrok", "workflow", "tutorial", "ai", "self-hosted"],
    "sections": [
        {
            "title": "Introduction",
            "duration": 60,  # secondes
            "script": """
Bonjour et bienvenue dans ce tutoriel complet sur la configuration de n8n avec Docker, HTTPS via ngrok, et les fonctionnalités d'IA.

n8n est un outil puissant d'automatisation de workflow qui vous permet de connecter différentes applications et services sans coder.

Dans cette vidéo, je vais vous montrer comment:
1. Installer n8n dans un conteneur Docker
2. Configurer un accès HTTPS sécurisé avec ngrok
3. Activer et utiliser les fonctionnalités d'IA dans n8n
4. Créer un workflow de démonstration avec scraping web via IA

Cette configuration vous donnera une instance n8n complète, accessible de partout, et avec de puissantes capacités d'IA.
Commençons!
            """,
            "capture": "intro_screen_with_logos",
        },
        {
            "title": "Prérequis",
            "duration": 90,
            "script": """
Avant de commencer, assurons-nous que vous avez tous les prérequis nécessaires.

Vous aurez besoin de:
- Docker et Docker Compose installés sur votre ordinateur
- ngrok installé et un compte gratuit créé
- Python 3.8 ou supérieur pour nos scripts d'automatisation

Notre projet fournit un script pratique qui vérifie tous ces prérequis automatiquement.

Exécutons check_prerequisites.py pour nous assurer que tout est bien configuré...

Comme vous pouvez le voir, le script vérifie:
- Si Docker est installé et fonctionne correctement
- Si Docker Compose est disponible
- Si ngrok est installé
- Et si un token d'authentification ngrok est configuré

Si quelque chose manque, le script vous guidera pour l'installation.
            """,
            "capture": "prerequisites_check",
        },
        {
            "title": "Structure du projet",
            "duration": 60,
            "script": """
Examinons rapidement la structure de notre projet:

Le répertoire principal contient:
- Le fichier docker-compose.yml qui définit notre configuration n8n
- Le script check_prerequisites.py que nous venons d'exécuter
- Le script 0-start_n8n_menu.py qui facilite le démarrage
- Un dossier Scénarios avec des exemples de workflows
- Une documentation interactive avec Streamlit

Cette organisation rend le projet facile à utiliser et à maintenir.
            """,
            "capture": "project_structure",
        },
        {
            "title": "Configuration Docker",
            "duration": 120,
            "script": """
La configuration Docker est au cœur de notre projet. Examinons le fichier docker-compose.yml.

Les éléments clés de cette configuration sont:
1. L'image officielle n8n est utilisée
2. Le port 5678 est exposé pour accéder à l'interface web
3. L'authentification de base est activée avec un nom d'utilisateur et un mot de passe
4. Les fonctionnalités expérimentales d'IA sont activées avec N8N_EXPERIMENTAL_MCP
5. Un volume est configuré pour persister les données entre les redémarrages

Cette configuration vous donne un environnement n8n stable et sécurisé.

Pour les fonctionnalités d'IA, nous pointons vers Ollama qui est un serveur local d'IA. 
C'est facultatif, mais recommandé pour avoir des fonctionnalités d'IA locales.
            """,
            "capture": "docker_compose_config",
        },
        {
            "title": "Démarrage de n8n",
            "duration": 120,
            "script": """
Maintenant, démarrons n8n avec notre script de menu.

Exécutons 0-start_n8n_menu.py et sélectionnons l'option 1 pour démarrer en mode localhost.

Le script:
1. Vérifie que tous les prérequis sont installés
2. Démarre les conteneurs Docker avec la configuration spécifiée
3. Nous informe quand n8n est prêt à être utilisé

Maintenant, n8n est accessible à l'adresse http://localhost:5678.

Ouvrons cette URL dans le navigateur...

Voilà! Nous avons maintenant n8n qui fonctionne localement avec Docker.
            """,
            "capture": "starting_n8n",
        },
        {
            "title": "Configuration HTTPS avec ngrok",
            "duration": 150,
            "script": """
Maintenant, rendons notre instance n8n accessible depuis Internet avec HTTPS.

Pour cela, nous utilisons ngrok qui crée un tunnel sécurisé vers notre serveur local.

Revenons au menu principal et sélectionnons l'option 2 pour démarrer n8n avec ngrok.

Le script:
1. Vérifie que le token ngrok est configuré
2. Démarre n8n s'il n'est pas déjà en cours d'exécution
3. Lance le tunnel ngrok vers le port 5678

Vous pouvez voir que ngrok nous fournit une URL HTTPS unique, quelque chose comme:
https://abcd1234.ngrok-free.app

C'est votre instance n8n accessible publiquement avec HTTPS!

Cette URL change à chaque redémarrage de ngrok dans la version gratuite, mais elle est parfaite pour des tests ou un usage personnel.
            """,
            "capture": "ngrok_https_setup",
        },
        {
            "title": "Activer et configurer l'IA",
            "duration": 180,
            "script": """
Une des fonctionnalités les plus intéressantes de notre configuration est la prise en charge de l'IA dans n8n.

Nous avons déjà activé cela dans le fichier docker-compose.yml avec:
- N8N_EXPERIMENTAL_MCP=true
- N8N_MCP_BACKEND_URL pointant vers Ollama

Pour utiliser pleinement ces fonctionnalités, il vous faudra:
1. Installer Ollama depuis ollama.ai si vous voulez des modèles locaux
2. Ou configurer une clé API pour OpenAI ou d'autres services d'IA

Dans l'interface n8n, allons dans Credentials et ajoutons une nouvelle clé API OpenAI.

Une fois configurée, vous verrez de nouveaux nodes disponibles:
- AI Agents
- Chat Models
- Vector Stores
- Et d'autres outils d'IA puissants

Ces fonctionnalités vous permettent de créer des workflows intelligents qui peuvent:
- Comprendre et générer du texte
- Analyser des documents
- Extraire des informations de sites web
- Et bien plus encore
            """,
            "capture": "ai_configuration",
        },
        {
            "title": "Démonstration d'un workflow d'IA",
            "duration": 240,
            "script": """
Explorons maintenant un exemple de workflow qui utilise ces fonctionnalités d'IA.

Importons le workflow "N8n_Agent_IA_MCP.json" depuis le dossier Scénarios.

Ce workflow crée un agent IA spécialisé dans le scraping web. Il combine:
1. Un déclencheur de chat pour interagir avec l'agent
2. Un modèle de langage OpenAI pour comprendre les demandes
3. Des outils MCP pour le scraping web
4. Une mémoire pour maintenir le contexte de la conversation

Testons ce workflow en lui demandant de scraper un site web.

[Démonstration: Demander à l'agent de scraper les titres d'un site]

Comme vous pouvez voir, l'agent:
1. Comprend notre demande
2. Sélectionne l'outil approprié (scrape)
3. Exécute le scraping avec les bons paramètres
4. Nous retourne les résultats formatés

C'est un exemple simple, mais vous pouvez créer des workflows beaucoup plus complexes qui combinent IA et automatisation.
            """,
            "capture": "ai_workflow_demo",
        },
        {
            "title": "Documentation et support",
            "duration": 60,
            "script": """
Notre projet inclut une documentation complète créée avec Streamlit.

Lançons-la avec:
```bash
cd streamlit_docs
streamlit run app.py
```

Cette documentation interactive couvre:
- L'installation et la configuration
- Les détails de la configuration Docker
- Comment utiliser ngrok pour HTTPS
- La configuration de l'IA
- Et des exemples de workflows

Vous pouvez également déployer cette documentation sur Streamlit Cloud pour un accès facile.
            """,
            "capture": "streamlit_docs",
        },
        {
            "title": "Conclusion",
            "duration": 90,
            "script": """
Et voilà! Vous avez maintenant:

1. Une instance n8n fonctionnelle dans Docker
2. Un accès HTTPS sécurisé via ngrok
3. Les fonctionnalités d'IA activées et configurées
4. Un exemple de workflow IA pour le scraping web
5. Une documentation complète pour référence future

Cette configuration vous offre une plateforme d'automatisation puissante que vous pouvez utiliser pour:
- Automatiser des tâches répétitives
- Connecter différentes applications et services
- Créer des assistants IA personnalisés
- Extraire et traiter des données du web

N'hésitez pas à explorer les possibilités infinies en créant vos propres workflows.

Si cette vidéo vous a été utile, n'oubliez pas de liker et de vous abonner pour plus de tutoriels sur l'automatisation.

Merci d'avoir regardé, et à bientôt!
            """,
            "capture": "conclusion",
        }
    ]
}

def clear_screen():
    """Nettoie l'écran de la console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_directories():
    """Crée les répertoires nécessaires s'ils n'existent pas."""
    directories = [OUTPUT_DIR, SCREENSHOTS_DIR, VIDEO_SEGMENTS_DIR]
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"Répertoire créé/vérifié: {directory}")

def save_script_and_storyboard():
    """Sauvegarde le script et le storyboard dans des fichiers."""
    # Enregistrer le storyboard au format JSON
    with open(STORYBOARD_FILE, 'w', encoding='utf-8') as f:
        json.dump(YOUTUBE_SCRIPT, f, ensure_ascii=False, indent=2)
    print(f"Storyboard enregistré dans: {STORYBOARD_FILE}")
    
    # Enregistrer le script au format Markdown
    with open(SCRIPT_FILE, 'w', encoding='utf-8') as f:
        f.write(f"# {YOUTUBE_SCRIPT['title']}\n\n")
        f.write(f"## Description\n{YOUTUBE_SCRIPT['description']}\n\n")
        f.write(f"## Tags\n{', '.join(YOUTUBE_SCRIPT['tags'])}\n\n")
        
        for i, section in enumerate(YOUTUBE_SCRIPT['sections'], 1):
            f.write(f"## {i}. {section['title']} ({section['duration']} secondes)\n\n")
            f.write(f"{section['script'].strip()}\n\n")
            f.write(f"[Capture: {section['capture']}]\n\n")
            f.write("---\n\n")
    
    print(f"Script détaillé enregistré dans: {SCRIPT_FILE}")

def generate_screenshot_instructions():
    """Génère des instructions pour les captures d'écran nécessaires."""
    instructions_file = OUTPUT_DIR / "instructions_captures.md"
    
    with open(instructions_file, 'w', encoding='utf-8') as f:
        f.write("# Instructions pour les captures d'écran\n\n")
        f.write("Voici la liste des captures d'écran à réaliser pour la vidéo YouTube:\n\n")
        
        for i, section in enumerate(YOUTUBE_SCRIPT['sections'], 1):
            f.write(f"## {i}. {section['capture']}\n\n")
            f.write(f"**Section:** {section['title']}\n")
            f.write(f"**Durée:** {section['duration']} secondes\n\n")
            
            # Générer des instructions spécifiques selon le type de capture
            if section['capture'] == "intro_screen_with_logos":
                f.write("- Créer une image de titre avec les logos de n8n, Docker et ngrok\n")
                f.write("- Inclure le titre de la vidéo\n")
            elif section['capture'] == "prerequisites_check":
                f.write("- Exécuter le script check_prerequisites.py en plein écran\n")
                f.write("- Montrer les résultats de la vérification des prérequis\n")
            elif section['capture'] == "project_structure":
                f.write("- Ouvrir l'explorateur de fichiers montrant la structure du projet\n")
                f.write("- Mettre en évidence les fichiers clés mentionnés\n")
            elif section['capture'] == "docker_compose_config":
                f.write("- Ouvrir le fichier docker-compose.yml dans un éditeur de code\n")
                f.write("- Mettre en évidence les sections importantes\n")
            elif section['capture'] == "starting_n8n":
                f.write("- Démarrer le script 0-start_n8n_menu.py et choisir l'option 1\n")
                f.write("- Montrer le processus de démarrage et l'accès à l'interface n8n\n")
            elif section['capture'] == "ngrok_https_setup":
                f.write("- Exécuter l'option 2 du script de menu pour démarrer avec ngrok\n")
                f.write("- Montrer l'URL HTTPS générée par ngrok\n")
                f.write("- Accéder à n8n via cette URL\n")
            elif section['capture'] == "ai_configuration":
                f.write("- Naviguer dans l'interface n8n vers Credentials\n")
                f.write("- Montrer la configuration d'une clé API OpenAI\n")
                f.write("- Naviguer vers les nodes AI et MCP disponibles\n")
            elif section['capture'] == "ai_workflow_demo":
                f.write("- Importer le workflow N8n_Agent_IA_MCP.json\n")
                f.write("- Montrer la structure du workflow\n")
                f.write("- Faire une démonstration en demandant de scraper un site\n")
                f.write("- Montrer les résultats obtenus\n")
            elif section['capture'] == "streamlit_docs":
                f.write("- Démarrer la documentation Streamlit\n")
                f.write("- Naviguer dans les différentes sections\n")
            elif section['capture'] == "conclusion":
                f.write("- Créer une diapositive récapitulative avec les 5 points clés\n")
                f.write("- Inclure un écran final avec un appel à l'action\n")
            
            f.write("\n---\n\n")
    
    print(f"Instructions pour les captures d'écran enregistrées dans: {instructions_file}")

def generate_recording_guide():
    """Génère un guide pour l'enregistrement de la vidéo."""
    recording_guide = OUTPUT_DIR / "guide_enregistrement.md"
    
    with open(recording_guide, 'w', encoding='utf-8') as f:
        f.write("# Guide d'enregistrement vidéo\n\n")
        f.write("## Configuration technique recommandée\n\n")
        f.write("- **Résolution d'écran:** 1920x1080 (Full HD)\n")
        f.write("- **Logiciel de capture:** OBS Studio ou Camtasia\n")
        f.write("- **Microphone:** Un microphone externe de qualité est recommandé\n")
        f.write("- **Police de caractères:** Augmenter la taille pour une meilleure lisibilité\n\n")
        
        f.write("## Avant l'enregistrement\n\n")
        f.write("1. Fermez les applications inutiles et les notifications\n")
        f.write("2. Préparez tous les fichiers et sites à montrer\n")
        f.write("3. Testez l'audio et la vidéo\n")
        f.write("4. Pratiquez chaque section au moins une fois\n\n")
        
        f.write("## Structure d'enregistrement\n\n")
        f.write("Il est recommandé d'enregistrer la vidéo par segments selon le storyboard:\n\n")
        
        total_duration = sum(section['duration'] for section in YOUTUBE_SCRIPT['sections'])
        minutes = total_duration // 60
        seconds = total_duration % 60
        
        f.write(f"- **Durée totale estimée:** {minutes} minutes et {seconds} secondes\n")
        f.write("- **Nombre de segments:** {}\n\n".format(len(YOUTUBE_SCRIPT['sections'])))
        
        f.write("### Segments à enregistrer\n\n")
        for i, section in enumerate(YOUTUBE_SCRIPT['sections'], 1):
            f.write(f"{i}. **{section['title']}** - {section['duration']} sec\n")
        
        f.write("\n## Conseils de narration\n\n")
        f.write("- Parlez clairement et à un rythme modéré\n")
        f.write("- Faites une pause de 2-3 secondes entre les sections\n")
        f.write("- Mentionnez les étapes précisément pendant que vous les réalisez\n")
        f.write("- Expliquez brièvement pourquoi vous faites chaque action\n\n")
        
        f.write("## Post-production\n\n")
        f.write("- Ajoutez une introduction avec musique et logo\n")
        f.write("- Insérez des transitions entre les segments\n")
        f.write("- Ajoutez des sous-titres pour l'accessibilité\n")
        f.write("- Incluez des textes explicatifs pour les concepts complexes\n")
        f.write("- Terminez avec un écran d'outro invitant à s'abonner\n")
    
    print(f"Guide d'enregistrement créé dans: {recording_guide}")

def main():
    """Fonction principale du script."""
    print("=" * 60)
    print("Générateur de contenu pour vidéo YouTube sur n8n Docker HTTPS Setup")
    print("=" * 60)
    print("\nCe script va générer tous les fichiers nécessaires pour créer une vidéo YouTube")
    print("présentant la configuration de n8n avec Docker, HTTPS via ngrok et IA.\n")
    
    # Créer les répertoires nécessaires
    create_directories()
    
    # Enregistrer le script et le storyboard
    save_script_and_storyboard()
    
    # Générer les instructions pour les captures d'écran
    generate_screenshot_instructions()
    
    # Générer le guide d'enregistrement
    generate_recording_guide()
    
    print("\n" + "=" * 60)
    print("Génération terminée!")
    print("=" * 60)
    print(f"\nTous les fichiers ont été créés dans le répertoire: {OUTPUT_DIR}")
    print("\nPour commencer à créer votre vidéo YouTube:")
    print("1. Suivez les instructions de capture d'écran")
    print("2. Enregistrez votre narration en suivant le script")
    print("3. Utilisez le guide d'enregistrement pour la post-production")
    print("\nBonne création!")

if __name__ == "__main__":
    main()
