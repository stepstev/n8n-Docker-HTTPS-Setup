---
marp: true
theme: default
paginate: true
---

# Module 6: Projets et cas d'usage
## Leçon 1: Projet: Moniteur de sites web avec alerte

---

# Objectifs

- Créer un workflow de monitoring de sites web avec n8n
- Configurer des alertes en cas d'indisponibilité ou de changement
- Développer un système de notification par email et Telegram
- Implémenter une surveillance périodique automatisée

---

# Architecture du projet

![width:800px](https://i.imgur.com/DfXm1vG.png)

---

# Outils et nodes n8n nécessaires

- **HTTP Request**: Pour tester la disponibilité des sites
- **IF**: Pour la logique conditionnelle
- **Set**: Pour manipuler les données
- **Telegram**: Pour envoyer des alertes via Telegram
- **Send Email**: Pour les notifications par email
- **Scheduler**: Pour exécuter le workflow périodiquement

---

# Étape 1: Vérification de disponibilité

```javascript
// Configuration du node HTTP Request
{
  "url": "{{$node["Set URL"].json["url"]}}",
  "responseFormat": "json",
  "options": {
    "timeout": 10000,
    "redirect": "follow"
  }
}
```

- Tester le code de statut HTTP
- Mesurer le temps de réponse
- Vérifier que le contenu est correct

---

# Étape 2: Vérification du contenu

```javascript
// Code pour vérifier si le contenu a changé
function compareContent(newContent, oldContent) {
  // Supprimer les éléments dynamiques (dates, etc.)
  const cleanNew = newContent.replace(/date|time|timestamp/gi, '');
  const cleanOld = oldContent.replace(/date|time|timestamp/gi, '');
  
  // Comparer les empreintes
  return cleanNew !== cleanOld;
}
```

---

# Étape 3: Configuration des alertes

## Telegram
```javascript
{
  "chatId": "{{$node["Credentials"].json["telegramChatId"]}}",
  "text": "⚠️ ALERTE: Le site {{$node["Set URL"].json["siteName"]}} est INDISPONIBLE!\nStatut: {{$node["HTTP Request"].json["status"]}}\nHeure: {{$timestamp}}",
  "additionalFields": {}
}
```

## Email
```javascript
{
  "to": "{{$node["Credentials"].json["alertEmail"]}}",
  "subject": "⚠️ ALERTE: Site {{$node["Set URL"].json["siteName"]}} indisponible",
  "text": "Le monitoring a détecté que le site est inaccessible.\n\nDétails:\nURL: {{$node["Set URL"].json["url"]}}\nCode: {{$node["HTTP Request"].json["status"]}}\nHeure: {{$timestamp}}"
}
```

---

# Étape 4: Planification des vérifications

- Configuration du node **Scheduler**:
  - Toutes les 5 minutes pour les sites critiques
  - Toutes les 15-30 minutes pour les sites normaux
  - Chaque heure pour les sites à faible priorité

- Utiliser des webhooks pour des vérifications à la demande

---

# Étape 5: Stockage des données historiques

- Stocker les résultats des vérifications dans:
  - Une base de données (PostgreSQL/MySQL)
  - Un fichier JSON local
  - Un service cloud (Airtable, Google Sheets)

```javascript
// Exemple de données à stocker
{
  "url": "https://example.com",
  "timestamp": "2023-06-15T14:30:22Z",
  "status": 200,
  "responseTime": 345,
  "isUp": true,
  "contentChanged": false
}
```

---

# Gestion des faux positifs

- Vérifications multiples avant de déclencher une alerte
- Délai entre les notifications (éviter le spam)
- Filtrage intelligent des changements de contenu
- Période de grâce après une maintenance planifiée

---

# Bonnes pratiques

- Ne pas surcharger les sites (respecter robots.txt)
- Utiliser des User-Agents appropriés
- Configurer des délais d'attente raisonnables
- Documenter les configurations
- Mettre en place un système de rotation des logs

---

# Démo

![width:900px](https://i.imgur.com/XB6AYbF.png)

---

# Projet complet: Tableau de bord

- Visualisation en temps réel de l'état des sites
- Historique de disponibilité 
- Statistiques de performance
- Journal des incidents
- Configuration des seuils d'alerte

---

# Résumé

- Le monitoring de sites web est un cas d'usage parfait pour n8n
- Combinaison puissante de HTTP Request et alertes
- Automatisation complète du processus de surveillance
- Extensible avec d'autres services et fonctionnalités
- Peut être adapté pour surveiller des API ou services

---

# Questions?

Merci de votre attention!
