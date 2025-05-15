# Module 6: Projets et cas d'usage
## Leçon 1: Projet: Moniteur de sites web avec alerte

*Durée estimée: 30 minutes*

### Objectifs d'apprentissage
- Créer un workflow complet de monitoring de sites web
- Configurer différents types d'alertes (disponibilité et contenu)
- Mettre en place un système de notification multicanal
- Comprendre les bonnes pratiques de monitoring

### Script

```
Bienvenue dans cette leçon pratique où nous allons créer un moniteur de sites web avec système d'alerte en utilisant n8n.

Je vais vous montrer comment construire un workflow complet qui surveille automatiquement la disponibilité de sites web et vous alerte en cas de problème.

Commençons par l'architecture globale de notre projet. Nous utiliserons n8n pour:
1. Vérifier périodiquement la disponibilité de sites web
2. Détecter des changements de contenu
3. Envoyer des alertes via différents canaux
4. Stocker l'historique des vérifications

Pour notre premier workflow, nous allons créer une surveillance de base qui vérifie si un site est en ligne.

Ouvrons l'interface n8n et créons un nouveau workflow nommé "Web Monitor".

D'abord, nous avons besoin d'un déclencheur. Nous utiliserons le node Scheduler pour exécuter notre vérification périodiquement.

Configurons-le pour s'exécuter toutes les 5 minutes, ce qui est une fréquence raisonnable pour un monitoring de base.

Maintenant, ajoutons un node "Set" pour définir les sites à surveiller. Cela permettra de facilement ajouter de nouveaux sites plus tard.

Dans ce node, nous allons créer un tableau de sites avec leurs URLs et noms.

Ajoutons maintenant un node "Split In Batches" pour traiter chaque site séparément.

L'étape cruciale est l'ajout d'un node "HTTP Request" qui vérifiera la disponibilité du site.

Configurons-le pour effectuer une requête GET vers l'URL du site et vérifier le code de statut.

Après la requête HTTP, nous ajoutons un node "IF" pour prendre différentes actions selon que le site est disponible ou non.

Si le site est indisponible (code autre que 200-299), nous voulons déclencher une alerte.

Configurons deux canaux d'alerte : Telegram et Email.

Pour Telegram, nous utilisons le node correspondant, configuré avec un bot que nous avons préalablement créé.

Pour l'email, nous utilisons le node "Send Email" avec nos paramètres SMTP.

N'oublions pas d'ajouter un node pour stocker l'historique des vérifications.

Testons maintenant notre workflow en simulant un site indisponible.

Voilà! Notre moniteur de sites web basique est fonctionnel.

Nous pouvons maintenant l'améliorer en ajoutant la détection de changements de contenu et d'autres fonctionnalités avancées, que nous verrons dans les exercices pratiques.
```

### Points clés à couvrir
- Configuration correcte du node HTTP Request pour détecter différents types d'erreurs
- Gestion des délais d'attente et des tentatives multiples
- Configuration sécurisée des notifications (tokens Telegram, SMTP)
- Personnalisation des messages d'alerte
- Techniques pour éviter les faux positifs

### Démonstrations
- Création complète du workflow de monitoring
- Simulation d'un site web indisponible pour tester les alertes
- Vérification du changement de contenu d'une page
- Configuration d'un tableau de bord simple pour visualiser l'état

### Ressources à montrer
- Workflow complet dans n8n
- Configuration du bot Telegram
- Exemples de messages d'alerte
- Système de stockage des vérifications historiques

### Notes pour l'enregistrement
- Préparer plusieurs sites de test, dont certains instables pour la démonstration
- Avoir déjà configuré les credentials pour Telegram et Email
- Montrer des exemples réels d'alertes reçues
- Expliquer l'importance du monitoring pour les projets critiques
