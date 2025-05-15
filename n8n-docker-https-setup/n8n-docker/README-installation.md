# Installation et démarrage de n8n avec ngrok

Ce guide explique comment configurer et démarrer `n8n` en utilisant Docker Compose et `ngrok` pour un accès HTTPS.

---

## Prérequis

1. **Docker et Docker Compose** :
   - Installez Docker Desktop depuis [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop).

2. **ngrok** :
   - Téléchargez et installez ngrok depuis [https://ngrok.com/download](https://ngrok.com/download).

---

## Configuration Docker

Le fichier `docker-compose.yml` suivant est utilisé pour configurer et démarrer `n8n` :

```yaml
services:
  n8n:
    image: n8nio/n8n
    restart: always
    ports:
      - "5678:5678" # Port pour accéder à l'interface n8n
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true # Active l'authentification de base
      - N8N_BASIC_AUTH_USER=admin@example.com # Utilisateur (doit être une adresse e-mail valide)
      - N8N_BASIC_AUTH_PASSWORD=VotrePass  # Mot de passe
      - N8N_HOST=localhost # Hôte pour n8n
      - N8N_PORT=5678 # Port pour n8n
      - WEBHOOK_URL=http://localhost:5678/ # URL pour les webhooks
      - N8N_PROTOCOL=http # Protocole utilisé
      - GENERIC_TIMEZONE=Europe/Paris # Fuseau horaire
    volumes:
      - n8n_data:/home/node/.n8n # Volume pour persister les données

volumes:
  n8n_data:
```

### Étapes pour démarrer les conteneurs Docker :
1. Placez le fichier `docker-compose.yml` dans le répertoire de votre choix.
2. Démarrez les conteneurs Docker avec la commande suivante :
   ```bash
   docker-compose up -d
   ```
3. Accédez à `n8n` via `http://localhost:5678` dans votre navigateur.
4. Connectez-vous avec les identifiants suivants :
   - **Utilisateur** : `admin@example.com`
   - **Mot de passe** : `N8nDockrNgrok`.

---

## Configuration avec ngrok pour HTTPS

`ngrok` est un outil qui permet d'exposer un serveur local à Internet via un tunnel sécurisé. Vous pouvez l'utiliser pour fournir un accès HTTPS à votre instance `n8n`.

### Étapes
1. **Configurer et lancer ngrok** :
   - Téléchargez ngrok et placez l'exécutable dans un dossier accessible (par exemple : `C:\ngrok`).
   - Connectez ngrok à votre compte en exécutant la commande suivante dans un terminal :
     ```bash
     ngrok config add-authtoken 2wuH8OryD4yZ3rjGhwKFNkBsY11_3gx2SnEuDV6gjhniKjfwB
     ```
   - Lancez ngrok pour exposer le port `5678` :
     ```bash
     ngrok http 5678
     ```
   - Vous verrez une sortie similaire à ceci :
     ```
     Forwarding                    https://random-subdomain.ngrok.io -> http://localhost:5678
     ```
   - Notez l'URL HTTPS générée (par exemple : `https://random-subdomain.ngrok.io`).

2. **Configurer `WEBHOOK_URL` pour n8n** :
   - Modifiez votre fichier `docker-compose.yml` pour inclure l'URL générée par ngrok dans la variable `WEBHOOK_URL` :
     ```yaml
     environment:
       - WEBHOOK_URL=https://random-subdomain.ngrok.io/
     ```
   - Redémarrez les conteneurs Docker pour appliquer les modifications :
     ```bash
     docker-compose down
     docker-compose up -d
     ```

3. **Tester l'accès** :
   - Accédez à l'URL HTTPS générée par ngrok (par exemple : `https://random-subdomain.ngrok.io`) dans votre navigateur.
   - Connectez-vous avec les identifiants configurés dans le fichier `docker-compose.yml`.

---

## Remarques importantes

- **URL temporaire** : L'URL générée par ngrok change à chaque redémarrage. Si vous avez besoin d'une URL persistante, vous pouvez souscrire à un plan payant sur ngrok.
- **Limites de ngrok gratuit** : Le plan gratuit de ngrok impose des limitations, comme une durée maximale pour les tunnels actifs et un débit limité.
- **Token d'authentification** : Le token fourni (`2wuH8OryD4yZ3rjGhwKFNkBsY11_3gx2SnEuDV6gjhniKjfwB`) est lié à un compte ngrok spécifique. Si vous avez votre propre compte ngrok, utilisez votre propre token.

---

## Support

- Documentation officielle : [https://docs.n8n.io](https://docs.n8n.io)
- Forum communautaire : [https://community.n8n.io](https://community.n8n.io)
