import subprocess
import sys
import os
import platform
import time

# Correction du chemin vers le fichier docker-compose.yml
DOCKER_COMPOSE_FILE = "D:\\00-Conception_AI\\__Automations_n8n\\n8n-docker-https-setup\\n8n-docker\\docker-compose.yml"
N8N_PORT = "5678"

def check_and_install_prerequisite(command, install_instructions):
    """Vérifie si une commande est disponible, sinon affiche les instructions d'installation."""
    try:
        subprocess.run([command, "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except FileNotFoundError:
        print(f"{command} n'est pas installé. Veuillez suivre les instructions suivantes pour l'installer :")
        print(install_instructions)
        sys.exit(1)

def check_prerequisites():
    """Vérifie si Docker, Docker Compose et ngrok sont installés."""
    print("Vérification des prérequis...")
    check_and_install_prerequisite("docker", "Téléchargez et installez Docker Desktop depuis https://www.docker.com/products/docker-desktop.")
    check_and_install_prerequisite("docker-compose", "Téléchargez et installez Docker Compose depuis https://docs.docker.com/compose/install/")
    check_and_install_prerequisite("ngrok", "Téléchargez et installez ngrok depuis https://ngrok.com/download.")
    print("Tous les prérequis sont satisfaits.")

def check_docker_running():
    """Vérifie si Docker est en cours d'exécution et essaie de le démarrer si nécessaire."""
    print("Vérification de l'état de Docker...")
    
    try:
        # Essayer d'exécuter une commande Docker simple pour vérifier si le daemon est accessible
        result = subprocess.run(["docker", "info"], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True, check=False)
        
        if result.returncode != 0:
            if "Cannot connect to the Docker daemon" in result.stderr or "error during connect" in result.stderr:
                print("Docker n'est pas en cours d'exécution ou n'est pas accessible. ❌")
                
                if platform.system() == "Windows":
                    print("\nActions recommandées:")
                    print("1. Assurez-vous que Docker Desktop est installé")
                    print("2. Lancez Docker Desktop depuis le menu Démarrer")
                    print("3. Attendez que l'icône Docker dans la barre des tâches indique 'Docker Desktop is running'")
                    
                    # Essayer de démarrer Docker Desktop automatiquement
                    try:
                        print("\nTentative de démarrage automatique de Docker Desktop...")
                        # Chemin typique de Docker Desktop sur Windows
                        docker_path = "C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe"
                        
                        if os.path.exists(docker_path):
                            subprocess.Popen([docker_path])
                            print("Docker Desktop est en cours de démarrage. Veuillez patienter...")
                            
                            # Attendre que Docker soit disponible (max 60 secondes)
                            for i in range(12):  # 12 x 5 = 60 secondes
                                time.sleep(5)
                                print(".", end="", flush=True)
                                check_result = subprocess.run(["docker", "info"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
                                if check_result.returncode == 0:
                                    print("\nDocker Desktop est maintenant en cours d'exécution! ✅")
                                    return True
                            
                            print("\nDocker Desktop ne semble pas répondre après 60 secondes.")
                        else:
                            print(f"Docker Desktop n'a pas été trouvé à l'emplacement standard: {docker_path}")
                    except Exception as e:
                        print(f"Erreur lors de la tentative de démarrage automatique: {e}")
                
                print("\nVeuillez démarrer Docker manuellement et réessayer.")
                return False
            else:
                print(f"Erreur Docker: {result.stderr}")
                return False
        
        print("Docker est en cours d'exécution. ✅")
        return True
        
    except Exception as e:
        print(f"Erreur lors de la vérification de Docker: {e}")
        return False

def start_docker_compose():
    """Démarre les conteneurs Docker via docker-compose."""
    print("Démarrage de n8n avec Docker Compose...")
    print(f"Utilisation du fichier de configuration: {DOCKER_COMPOSE_FILE}")
    
    # Vérifier si le fichier docker-compose.yml existe
    if not os.path.exists(DOCKER_COMPOSE_FILE):
        print(f"ERREUR: Le fichier docker-compose.yml n'existe pas à l'emplacement: {DOCKER_COMPOSE_FILE}")
        print("Veuillez vérifier le chemin du fichier et réessayer.")
        sys.exit(1)
    
    # Vérifier si Docker est en cours d'exécution
    if not check_docker_running():
        print("Docker n'est pas disponible. Impossible de démarrer les conteneurs.")
        print("Veuillez vous assurer que Docker Desktop est en cours d'exécution et réessayez.")
        sys.exit(1)
    
    # Exécuter docker-compose avec le chemin explicite du fichier
    try:
        result = subprocess.run(["docker-compose", "-f", DOCKER_COMPOSE_FILE, "up", "-d"], stderr=subprocess.PIPE, text=True, check=False)
        if result.returncode != 0:
            print(f"Erreur lors du démarrage des conteneurs Docker:")
            print(f"{result.stderr}")
            
            if "error during connect" in result.stderr or "Cannot connect to the Docker daemon" in result.stderr:
                print("\nIl semble y avoir un problème de connexion au daemon Docker.")
                print("Assurez-vous que Docker Desktop est correctement démarré et qu'il n'y a pas de problème de pare-feu.")
            elif "pull access denied" in result.stderr or "denied: requested access to the resource is denied" in result.stderr:
                print("\nAccès refusé lors de la récupération de l'image. Vérifiez votre connexion Internet et vos identifiants Docker Hub.")
            
            sys.exit(1)
        print("n8n est maintenant en cours d'exécution sur http://localhost:5678.")
    except Exception as e:
        print(f"Erreur lors du démarrage des conteneurs Docker: {e}")
        sys.exit(1)
    
    # Créer le fichier d'infos sur ngrok
    ngrok_info_file = os.path.join(os.path.dirname(DOCKER_COMPOSE_FILE), "ngrok_infos.txt")
    with open(ngrok_info_file, "w", encoding="utf-8") as f:
        f.write("""# Guide des informations ngrok

Lorsque vous démarrez ngrok, vous verrez des informations comme celles-ci:

```
Session Status                online                                                                                             
Account                       Stéphane CELTON (Plan: Free)                                                                        
Version                       3.22.1                                                                                             
Region                        Europe (eu)                                                                                        
Latency                       13ms                                                                                              
Web Interface                 http://127.0.0.1:4040                                                                            
Forwarding                    https://bf56-2a01-cb04-94b-e700-18b4-a002-ad6b-cfb6.ngrok-free.app -> http://localhost:5678        
                                                                                                                                
Connections                   ttl     opn     rt1     rt5     p50     p90                                                        
                              8       0       0.10    0.03    0.36    8.88 
```

## Explication des informations affichées:

- **Session Status**: État de la connexion (online = connecté)
- **Account**: Votre compte ngrok et le plan utilisé
- **Version**: Version de ngrok utilisée
- **Region**: Région du serveur ngrok utilisé
- **Latency**: Temps de latence entre votre machine et le serveur ngrok
- **Web Interface**: URL de l'interface web de ngrok pour surveiller les connexions
- **Forwarding**: L'URL HTTPS publique qui redirige vers votre n8n local
  - C'est cette URL que vous devez utiliser pour accéder à n8n depuis l'extérieur
  - Exemple: https://bf56-2a01-cb04-94b-e700-18b4-a002-ad6b-cfb6.ngrok-free.app

- **Connections**: Statistiques des connexions
  - ttl: Nombre total de connexions
  - opn: Connexions ouvertes
  - rt1/rt5: Temps de réponse moyen sur 1 et 5 minutes
  - p50/p90: Percentiles des temps de réponse

## Utilisation de l'URL ngrok:

1. Copiez l'URL dans la section "Forwarding" (ex: https://bf56-...ngrok-free.app)
2. Utilisez cette URL pour accéder à n8n depuis n'importe où sur internet
3. Les identifiants de connexion sont les mêmes que pour l'accès local

## Interface Web ngrok:

Ouvrez http://127.0.0.1:4040 dans votre navigateur pour:
- Surveiller le trafic en temps réel
- Voir les détails des requêtes HTTP
- Rejouer des requêtes pour le débogage

Note: L'URL de redirection change à chaque redémarrage de ngrok (dans la version gratuite).
""")
    print(f"Un guide d'explication des informations ngrok a été créé: {ngrok_info_file}")

def start_localhost():
    """Démarre n8n en mode localhost."""
    print("Démarrage de n8n en localhost...")
    start_docker_compose()
    print("Accédez à n8n via http://localhost:5678.")

def configure_ngrok_token():
    """Vérifie et configure le token d'authentification ngrok."""
    print("Vérification du token d'authentification ngrok...")
    
    # Déterminer le chemin du fichier de configuration ngrok en fonction du système d'exploitation
    if platform.system() == "Windows":
        config_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "ngrok")
    else:
        config_path = os.path.join(os.path.expanduser("~"), ".ngrok2")
    
    print(f"Chemin probable du fichier de configuration ngrok : {config_path}")
    
    # Vérification de la configuration ngrok
    print("Vérification de l'authentification ngrok...")
    
    token_configured = False
    
    try:
        # Utiliser seulement ngrok config check - ne PAS exécuter "ngrok authtoken check"
        result = subprocess.run(["ngrok", "config", "check"], capture_output=True, text=True)
        
        # Vérifier si un token est déjà configuré
        if result.returncode == 0 and "authtoken" in result.stdout and "not set" not in result.stdout:
            token_configured = True
    except Exception as e:
        print(f"Info: Exception lors de la vérification du token: {e}")
        # Fallback pour les versions plus récentes de ngrok
        try:
            # Exécuter simplement ngrok pour voir s'il y a un message sur l'authtoken manquant
            result = subprocess.run(["ngrok", "--version"], capture_output=True, text=True)
        except Exception as e2:
            print(f"Erreur lors de l'exécution de ngrok: {e2}")
    
    if not token_configured:
        print("Le token ngrok n'est pas configuré ou il y a un problème avec la configuration. ❌")
        print("Vous devez entrer un token d'authentification valide pour utiliser ngrok.")
        print("Vous pouvez obtenir votre token sur https://dashboard.ngrok.com/get-started/your-authtoken")
        token = input("Veuillez entrer votre token ngrok: ")
        
        if token:
            if len(token) < 15 or not token.startswith("2"):
                print("AVERTISSEMENT: Ce token ne semble pas être un token ngrok valide.")
                confirm = input("Voulez-vous quand même utiliser ce token? (o/n): ")
                if confirm.lower() != 'o':
                    print("Configuration annulée.")
                    sys.exit(1)
            
            print(f"Configuration du token ngrok: {token[:5]}...{token[-5:] if len(token) > 10 else '***'}")
            
            try:
                # Nous utilisons ngrok authtoken AVEC un vrai token, pas "check"
                token_result = subprocess.run(["ngrok", "authtoken", token])
                if token_result.returncode != 0:
                    print("Erreur lors de la configuration du token ngrok. Veuillez réessayer.")
                    sys.exit(1)
                print("Le token ngrok a été configuré avec succès. ✅")
            except Exception as e:
                print(f"Erreur pendant la configuration du token: {e}")
                sys.exit(1)
        else:
            print("Aucun token fourni. Impossible de continuer.")
            sys.exit(1)
    else:
        print("Le token ngrok est configuré avec succès. ✅")

def start_ngrok():
    """Démarre n8n avec un tunnel HTTPS via ngrok."""
    print("Démarrage de n8n avec ngrok...")
    configure_ngrok_token()
    start_docker_compose()
    print("Lancement de ngrok...")
    result = subprocess.run(["ngrok", "http", N8N_PORT])
    if result.returncode != 0:
        print("Une erreur s'est produite lors du démarrage de ngrok.")
        sys.exit(1)
    print("n8n est maintenant exposé via ngrok en HTTPS.")

def main():
    """Affiche un menu principal en boucle pour interagir avec l'utilisateur."""
    print("\n🐋 Vérification de l'état de Docker")
    if not check_docker_running():
        print("⚠️ Docker n'est pas disponible. Certaines fonctionnalités pourraient ne pas fonctionner correctement.")
        input("Appuyez sur Entrée pour continuer tout de même...")
    
    while True:
        print("===========================================")
        print("Menu de lancement de n8n :")
        print("===========================================")
        print("0. Vérifier les prérequis")
        print("1. Démarrer n8n en localhost (http://localhost:5678)")
        print("2. Démarrer n8n avec ngrok (HTTPS)")
        print("3. Quitter")
        print("===========================================")
        choice = input("Entrez votre choix (0/1/2/3) : ")

        if choice == "0":
            check_prerequisites()  # Vérifie les prérequis nécessaires
        elif choice == "1":
            start_localhost()  # Démarre n8n en mode localhost
        elif choice == "2":
            start_ngrok()  # Démarre n8n avec un tunnel HTTPS via ngrok
        elif choice == "3":
            print("Au revoir !")  # Quitte le programme
            sys.exit(0)
        else:
            print("Choix invalide. Veuillez réessayer.")  # Gère les choix invalides

if __name__ == "__main__":
    main()
