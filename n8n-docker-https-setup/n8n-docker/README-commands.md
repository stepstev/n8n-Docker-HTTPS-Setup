# Récapitulatif des commandes utiles

## Docker

### Vérifier la version de Docker
```bash
docker --version
```

### Vérifier la version de Docker Compose
```bash
docker-compose --version
```

### Lancer les conteneurs en arrière-plan
```bash
docker-compose up -d
```

### Arrêter les conteneurs
```bash
docker-compose down
```

### Voir les logs des conteneurs
```bash
docker-compose logs -f
```

### Lister les conteneurs en cours d'exécution
```bash
docker ps
```

### Identifier un processus utilisant un port spécifique
```bash
lsof -i :5678
```

---

## ngrok

### Vérifier la version de ngrok
```bash
ngrok --version
```

### Ajouter un token d'authentification
```bash
ngrok config add-authtoken VOTRE_TOKEN_AUTH
```

### Démarrer un tunnel HTTP
```bash
ngrok http 5678
```

---

## n8n

### Lancer n8n en mode Docker
```bash
docker-compose up -d
```

### Accéder à l'interface n8n
- URL locale : `http://localhost:5678`
- URL ngrok : Générée après exécution de `ngrok http 5678`

### Redémarrer n8n
```bash
docker-compose restart
```

---
