# Configuration complète de n8n avec Docker, HTTPS et IA en 15 minutes

## Description
Guide pas à pas pour configurer n8n avec Docker, ngrok pour HTTPS, et activation des fonctionnalités d'IA.

## Tags
n8n, automation, docker, ngrok, workflow, tutorial, ai, self-hosted

## 1. Introduction (60 secondes)

Bonjour et bienvenue dans ce tutoriel complet sur la configuration de n8n avec Docker, HTTPS via ngrok, et les fonctionnalités d'IA.

n8n est un outil puissant d'automatisation de workflow qui vous permet de connecter différentes applications et services sans coder.

Dans cette vidéo, je vais vous montrer comment:
1. Installer n8n dans un conteneur Docker
2. Configurer un accès HTTPS sécurisé avec ngrok
3. Activer et utiliser les fonctionnalités d'IA dans n8n
4. Créer un workflow de démonstration avec scraping web via IA

Cette configuration vous donnera une instance n8n complète, accessible de partout, et avec de puissantes capacités d'IA.
Commençons!

[Capture: intro_screen_with_logos]

---

## 2. Prérequis (90 secondes)

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

[Capture: prerequisites_check]

---

## 3. Structure du projet (60 secondes)

Examinons rapidement la structure de notre projet:

Le répertoire principal contient:
- Le fichier docker-compose.yml qui définit notre configuration n8n
- Le script check_prerequisites.py que nous venons d'exécuter
- Le script 0-start_n8n_menu.py qui facilite le démarrage
- Un dossier Scénarios avec des exemples de workflows
- Une documentation interactive avec Streamlit

Cette organisation rend le projet facile à utiliser et à maintenir.

[Capture: project_structure]

---

## 4. Configuration Docker (120 secondes)

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

[Capture: docker_compose_config]

---

## 5. Démarrage de n8n (120 secondes)

Maintenant, démarrons n8n avec notre script de menu.

Exécutons 0-start_n8n_menu.py et sélectionnons l'option 1 pour démarrer en mode localhost.

Le script:
1. Vérifie que tous les prérequis sont installés
2. Démarre les conteneurs Docker avec la configuration spécifiée
3. Nous informe quand n8n est prêt à être utilisé

Maintenant, n8n est accessible à l'adresse http://localhost:5678.

Ouvrons cette URL dans le navigateur...

Voilà! Nous avons maintenant n8n qui fonctionne localement avec Docker.

[Capture: starting_n8n]

---

## 6. Configuration HTTPS avec ngrok (150 secondes)

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

[Capture: ngrok_https_setup]

---

## 7. Activer et configurer l'IA (180 secondes)

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

[Capture: ai_configuration]

---

## 8. Démonstration d'un workflow d'IA (240 secondes)

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

[Capture: ai_workflow_demo]

---

## 9. Documentation et support (60 secondes)

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

[Capture: streamlit_docs]

---

## 10. Conclusion (90 secondes)

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

[Capture: conclusion]

---

