
    ## Personnalisation
    
    Vous pouvez personnaliser cette configuration en modifiant les valeurs dans le fichier `docker-compose.yml` :
    
    - **Changer le port** : Modifiez la ligne `"5678:5678"` (format "port-externe:port-interne")
    - **Changer les identifiants** : Modifiez les variables `N8N_BASIC_AUTH_USER` et `N8N_BASIC_AUTH_PASSWORD`
    - **Désactiver l'authentification** : Changez `N8N_BASIC_AUTH_ACTIVE` à `false`
    - **Changer le fuseau horaire** : Modifiez `GENERIC_TIMEZONE` selon vos besoins
    
    ## Gestion des conteneurs Docker
    
    Le script `0-start_n8n_menu.py` vous aide à gérer les conteneurs Docker, mais vous pouvez également utiliser ces commandes directement :
    
    - **Démarrer les conteneurs** : `docker-compose up -d`
    - **Arrêter les conteneurs** : `docker-compose down`
    - **Voir les logs** : `docker-compose logs -f`
    - **Redémarrer les conteneurs** : `docker-compose restart`
    