import subprocess
import sys
import os

def check_command(command, install_instructions):
    """Vérifie si une commande est disponible, sinon affiche les instructions d'installation."""
    try:
        subprocess.run([command, "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        print(f"{command} est installé. ✅")
    except FileNotFoundError:
        print(f"{command} n'est pas installé. ❌")
        print(f"Veuillez suivre les instructions suivantes pour l'installer : {install_instructions}")
        sys.exit(1)
    except Exception as e:
        print(f"Erreur inattendue lors de la vérification de {command} : {e}")
        sys.exit(1)

def check_ngrok_token():
    """Vérifie si un token ngrok est configuré en utilisant les fichiers de configuration possibles."""
    try:
        # Vérification de la configuration via la commande ngrok
        result = subprocess.run(["ngrok", "config", "check"], capture_output=True, text=True, check=False)
        
        # Vérification du fichier de configuration legacy
        legacy_config_path = os.path.expanduser("~/.ngrok2/ngrok.yml")
        new_config_path = os.path.expanduser("~/.config/ngrok/ngrok.yml")
        
        if "No authtoken" in result.stdout:
            if os.path.exists(legacy_config_path):
                with open(legacy_config_path, 'r') as f:
                    if 'authtoken' in f.read():
                        print(f"Le token ngrok est configuré via le fichier legacy {legacy_config_path}. ✅")
                        return
            elif os.path.exists(new_config_path):
                with open(new_config_path, 'r') as f:
                    if 'authtoken' in f.read():
                        print(f"Le token ngrok est configuré via le fichier {new_config_path}. ✅")
                        return
                
            print("Le token ngrok n'est pas configuré. ❌")
            print("Veuillez configurer un token ngrok avec la commande : ngrok config add-authtoken <VOTRE_TOKEN>")
            sys.exit(1)
        else:
            print("Le token ngrok est configuré via le fichier de configuration. ✅")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la vérification du token ngrok : {e.stderr.strip()}")
        sys.exit(1)
    except Exception as e:
        print(f"Erreur inattendue lors de la vérification du token ngrok : {e}")
        sys.exit(1)

def check_docker_compose_file():
    """Vérifie si le fichier docker-compose.yml est présent et correctement formaté."""
    # Utiliser le chemin absolu exact plutôt que le répertoire courant
    docker_compose_path = r"D:\00-Conception_AI\__Automations_n8n\n8n-docker-https-setup\n8n-docker\docker-compose.yml"
    
    try:
        if not os.path.isfile(docker_compose_path):
            print(f"Le fichier docker-compose.yml est manquant à l'emplacement {docker_compose_path}. ❌")
            print("Veuillez créer ou restaurer le fichier docker-compose.yml à l'emplacement spécifié.")
            sys.exit(1)
            
        with open(docker_compose_path, "r") as file:
            content = file.read()
            if not content.strip():
                print("Le fichier docker-compose.yml est vide. ❌")
                print("Veuillez vérifier le contenu du fichier docker-compose.yml.")
                sys.exit(1)
                
        # Vérifier si le fichier est correctement formaté en le validant
        validate_result = subprocess.run(
            ["docker-compose", "-f", docker_compose_path, "config", "--quiet"],
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        
        if validate_result.returncode != 0:
            print(f"Le fichier docker-compose.yml contient des erreurs : {validate_result.stderr}")
            sys.exit(1)
            
        print(f"Le fichier docker-compose.yml est présent et valide à l'emplacement {docker_compose_path}. ✅")
    except Exception as e:
        print(f"Erreur inattendue lors de la vérification du fichier docker-compose.yml : {e}")
        sys.exit(1)

def main():
    """Vérifie tous les prérequis nécessaires."""
    print("Vérification des prérequis pour n8n et ngrok...")
    print("===============================================")
    check_command("docker", "Téléchargez et installez Docker Desktop depuis https://www.docker.com/products/docker-desktop.")
    check_command("docker-compose", "Téléchargez et installez Docker Compose depuis https://docs.docker.com/compose/install/")
    check_command("ngrok", "Téléchargez et installez ngrok depuis https://ngrok.com/download.")
    check_ngrok_token()
    check_docker_compose_file()
    print("Tous les prérequis sont satisfaits. ✅")

if __name__ == "__main__":
    main()
