# Exercices pratiques - Module 6: Projets et cas d'usage

## Exercice 1: Moniteur de site web basique

### Objectif
Créer un workflow n8n qui vérifie la disponibilité d'un site web et envoie une notification en cas de problème.

### Instructions
1. Créez un nouveau workflow dans n8n nommé "Basic Web Monitor"
2. Ajoutez un node Scheduler configuré pour s'exécuter toutes les 15 minutes
3. Ajoutez un node Set pour définir l'URL à surveiller (utilisez https://example.com ou votre propre site)
4. Ajoutez un node HTTP Request pour effectuer une requête GET vers l'URL
5. Ajoutez un node IF pour vérifier si le code de statut est dans la plage 200-299
6. Si le site est indisponible, configurez un node Telegram ou Email pour envoyer une alerte
7. Testez votre workflow en modifiant temporairement l'URL vers une adresse inexistante

### Critères de réussite
- Le workflow s'exécute automatiquement selon la planification
- Les sites disponibles sont correctement identifiés
- Une alerte est envoyée uniquement lorsqu'un site est indisponible
- L'alerte contient des informations pertinentes (URL, heure, code d'erreur)

### Solution
<details>
  <summary>Cliquez pour voir la solution</summary>
  
  ```json
  {
    "nodes": [
      {
        "parameters": {
          "rule": {
            "interval": [
              {
                "field": "minutes",
                "minuteInterval": 15
              }
            ]
          }
        },
        "name": "Scheduler",
        "type": "n8n-nodes-base.scheduleTrigger",
        "position": [
          250,
          300
        ]
      },
      {
        "parameters": {
          "values": {
            "string": [
              {
                "name": "url",
                "value": "https://example.com"
              },
              {
                "name": "siteName",
                "value": "Example Site"
              }
            ]
          },
          "options": {}
        },
        "name": "Set Site Data",
        "type": "n8n-nodes-base.set",
        "position": [
          450,
          300
        ]
      },
      {
        "parameters": {
          "url": "={{ $node[\"Set Site Data\"].json[\"url\"] }}",
          "options": {
            "timeout": 10000
          }
        },
        "name": "HTTP Request",
        "type": "n8n-nodes-base.httpRequest",
        "position": [
          650,
          300
        ]
      },
      {
        "parameters": {
          "conditions": {
            "string": [
              {
                "value1": "={{ $node[\"HTTP Request\"].json[\"statusCode\"] }}",
                "operation": "regex",
                "value2": "^(2)[0-9]{2}$"
              }
            ]
          }
        },
        "name": "IF",
        "type": "n8n-nodes-base.if",
        "position": [
          850,
          300
        ]
      },
      {
        "parameters": {
          "chatId": "YOUR_CHAT_ID",
          "text": "⚠️ ALERTE: Le site {{ $node[\"Set Site Data\"].json[\"siteName\"] }} est INDISPONIBLE!\nURL: {{ $node[\"Set Site Data\"].json[\"url\"] }}\nStatut: {{ $node[\"HTTP Request\"].json[\"statusCode\"] }}\nHeure: {{ $now.format(\"YYYY-MM-DD HH:mm:ss\") }}",
          "additionalFields": {}
        },
        "name": "Telegram",
        "type": "n8n-nodes-base.telegram",
        "position": [
          1050,
          400
        ]
      }
    ],
    "connections": {
      "Scheduler": {
        "main": [
          [
            {
              "node": "Set Site Data",
              "type": "main",
              "index": 0
            }
          ]
        ]
      },
      "Set Site Data": {
        "main": [
          [
            {
              "node": "HTTP Request",
              "type": "main",
              "index": 0
            }
          ]
        ]
      },
      "HTTP Request": {
        "main": [
          [
            {
              "node": "IF",
              "type": "main",
              "index": 0
            }
          ]
        ]
      },
      "IF": {
        "main": [
          [],
          [
            {
              "node": "Telegram",
              "type": "main",
              "index": 0
            }
          ]
        ]
      }
    }
  }
  ```
</details>

## Exercice 2: Détection de changement de contenu

### Objectif
Améliorer votre moniteur de site web pour détecter les changements dans le contenu d'une page web.

### Instructions
1. Utilisez comme base le workflow créé dans l'Exercice 1
2. Ajoutez un node Function qui extrait et nettoie le contenu HTML de la page
3. Configurez un node n8n (Workflow Storage) pour stocker la version précédente du contenu
4. Utilisez un node IF pour comparer l'ancienne et la nouvelle version du contenu
5. Si le contenu a changé, envoyez une notification différente 
6. Stockez la nouvelle version du contenu pour la prochaine vérification

### Critères de réussite
- Le workflow détecte correctement les changements de contenu
- Les faux positifs sont minimisés (ignorer les changements mineurs comme les dates)
- La notification indique clairement qu'il s'agit d'un changement de contenu (pas d'une panne)
- Le contenu actuel est correctement stocké pour les futures comparaisons

### Solution
<details>
  <summary>Cliquez pour voir la solution</summary>
  
  ```javascript
  // Code du node Function pour nettoyer le contenu HTML
  const $ = require('cheerio').load($input.item.json.data);
  
  // Supprimer les éléments dynamiques qui changent souvent
  $('time, [data-timestamp], [data-datetime], script').remove();
  
  // Extraire seulement le contenu principal (adapter selon le site)
  const mainContent = $('main, #content, .content, article').html() || $('body').html();
  
  // Nettoyer davantage
  const cleanContent = mainContent
    .replace(/\s+/g, ' ')        // Normaliser les espaces
    .replace(/<!--.*?-->/g, '')  // Supprimer les commentaires HTML
    .trim();
  
  return {
    cleanContent,
    timestamp: new Date().toISOString()
  };
  ```
</details>

## Projet pratique: Tableau de bord de monitoring complet

### Objectif
Créer un système de monitoring complet avec un tableau de bord pour visualiser l'état de plusieurs sites web.

### Instructions
1. Créez un workflow principal qui coordonne la surveillance de plusieurs sites web
2. Stockez les résultats des vérifications dans une base de données (SQLite, PostgreSQL ou MySQL)
3. Créez un webhook qui permet de récupérer l'état actuel de tous les sites
4. Développez une page HTML simple qui affiche un tableau de bord des statuts
5. Ajoutez des fonctionnalités avancées comme:
   - Calcul du temps de disponibilité (uptime)
   - Graphiques de temps de réponse
   - Historique des incidents
   - Configuration des seuils d'alerte personnalisés

### Livrables
- Workflow n8n complet pour le monitoring
- Script de création de la base de données
- Code HTML/JS pour le tableau de bord
- Documentation explicative du système

### Critères d'évaluation
- Fonctionnalité complète du système de monitoring
- Organisation et lisibilité du workflow
- Design et ergonomie du tableau de bord
- Performance et fiabilité du système
- Documentation claire et exhaustive
