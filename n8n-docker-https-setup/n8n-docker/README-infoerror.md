## Erreurs courantes et solutions

### 1. Erreur : `docker-compose` ne démarre pas
**Message d'erreur :**
```
Une erreur s'est produite lors du démarrage des conteneurs Docker.
```

**Cause possible :**
- Docker ou Docker Compose n'est pas installé ou configuré correctement.

**Solution :**
1. Vérifiez que Docker est installé et en cours d'exécution.
2. Assurez-vous que Docker Compose est installé en exécutant :
   ```bash
   docker-compose --version
   ```
3. Si Docker Compose n'est pas installé, suivez les instructions ici : [https://docs.docker.com/compose/install/](https://docs.docker.com/compose/install/).

---

### 2. Erreur : `ngrok` ne démarre pas
**Message d'erreur :**
```
Une erreur s'est produite lors du démarrage de ngrok.
```

**Cause possible :**
- `ngrok` n'est pas installé ou n'est pas accessible dans le PATH.

**Solution :**
1. Vérifiez que `ngrok` est installé en exécutant :
   ```bash
   ngrok --version
   ```
2. Si `ngrok` n'est pas installé, téléchargez-le depuis [https://ngrok.com/download](https://ngrok.com/download) et ajoutez son exécutable au PATH.
3. Si vous utilisez un compte `ngrok`, assurez-vous d'avoir configuré votre token d'authentification :
   ```bash
   ngrok config add-authtoken YOUR_AUTH_TOKEN
   ```

---

### 3. Erreur : Choix invalide dans le menu
**Message d'erreur :**
```
Choix invalide. Veuillez relancer le script.
```

**Cause possible :**
- Une option non valide a été saisie dans le menu principal.

**Solution :**
- Relancez le script et saisissez une option valide (0, 1 ou 2).

---

### 4. Erreur : Port 5678 déjà utilisé
**Message d'erreur :**
```
Bind for 0.0.0.0:5678 failed: port is already allocated.
```

**Cause possible :**
- Un autre processus utilise déjà le port 5678.

**Solution :**
1. Identifiez le processus utilisant le port 5678 :
   ```bash
   lsof -i :5678
   ```
2. Arrêtez le processus ou modifiez le port dans le fichier `docker-compose.yml` :
   ```yaml
   ports:
     - "5679:5678" # Changez 5679 par un port disponible
   ```
3. Redémarrez les conteneurs Docker :
   ```bash
   docker-compose down
   docker-compose up -d
   ```

---

### 5. Erreur : URL ngrok non générée
**Message d'erreur :**
```
ngrok http 5678
```
**Cause possible :**
- `ngrok` n'a pas pu établir un tunnel.

**Solution :**
1. Vérifiez votre connexion Internet.
2. Assurez-vous que le port 5678 est accessible.
3. Si le problème persiste, redémarrez `ngrok` :
   ```bash
   ngrok http 5678
   ```

---