
    ## Agent IA pour le Scraping Web
    
    Le projet inclut un workflow d'exemple qui utilise l'agent IA pour le scraping web.
    
    ### Fonctionnalités
    
    - Interface de chat pour communiquer avec l'agent
    - Utilisation de l'API OpenAI pour comprendre les demandes
    - Outils de scraping web via MCP Client
    - Mémoire contextuelle pour les conversations
    
    ### Composants du workflow
    
    1. **Chat Trigger** : Déclenche le workflow quand un message est reçu
    2. **AI Agent** : Agent qui comprend les demandes et utilise les outils appropriés
    3. **OpenAI Chat Model** : Modèle de langage pour l'agent (GPT-3.5 Turbo)
    4. **Simple Memory** : Stocke l'historique de la conversation
    5. **MCP Client List** : Liste les outils de scraping disponibles
    6. **MCP Client Execute** : Exécute l'outil de scraping sélectionné
    
    ### Utilisation du workflow
    
    1. Activez le workflow dans n8n
    2. Accédez à l'interface de chat (via le lien webhook généré)
    3. Demandez à l'agent de scraper un site web spécifique
    4. L'agent utilisera les outils disponibles pour extraire les informations
    
    ### Exemple de demande
    
    ```
    Peux-tu scraper les titres des articles sur https://example.com ?
    ```
    
    ### Personnalisation
    
    Vous pouvez personnaliser :
    - Le message système de l'agent dans les paramètres du nœud AI Agent
    - Le modèle de langage utilisé (par défaut GPT-3.5 Turbo)
    - Les paramètres de scraping (sélecteurs CSS, type d'extraction, etc.)
    