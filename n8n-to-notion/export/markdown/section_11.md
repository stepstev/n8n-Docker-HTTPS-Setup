
    ## Pourquoi ngrok ?
    
    ngrok est utilisé dans ce projet pour :
    1. Exposer votre instance n8n locale à Internet avec un tunnel sécurisé
    2. Fournir un accès HTTPS sans nécessiter la configuration de certificats SSL
    3. Permettre l'accès à votre instance n8n depuis n'importe où
    4. Faciliter les tests de webhooks depuis des services externes
    
    ## Configuration de ngrok
    
    Le projet inclut un gestionnaire de configuration ngrok dans `0-start_n8n_menu.py` qui vérifie et configure automatiquement ngrok.
    
    ### Processus de configuration
    
    1. **Création d'un compte** : Vous devez avoir un compte sur [ngrok.com](https://ngrok.com)
    2. **Obtention du token** : Récupérez votre authtoken depuis le [dashboard ngrok](https://dashboard.ngrok.com/get-started/your-authtoken)
    3. **Configuration du token** : Le script vérifie et vous demande de configurer votre token si nécessaire
    
    ### Configuration manuelle du token ngrok
    
    Si vous préférez configurer manuellement le token :
    ```bash
    ngrok authtoken YOUR_TOKEN
    ```
    
    ## Lancement du tunnel ngrok
    
    Le script `0-start_n8n_menu.py` (option 2) lance automatiquement le tunnel ngrok après avoir démarré n8n.
    
    Vous pouvez également lancer ngrok manuellement :
    ```bash
    ngrok http 5678
    ```
    
    ## Limitations de la version gratuite de ngrok
    
    La version gratuite de ngrok présente quelques limitations :
    - URL aléatoire qui change à chaque redémarrage
    - Limite de 40 connexions par minute
    - Une seule session active à la fois
    - Pas de sous-domaines personnalisés
    
    Pour des fonctionnalités avancées, vous pouvez envisager [l'abonnement Pro](https://ngrok.com/pricing).
    