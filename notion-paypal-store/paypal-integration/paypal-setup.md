# Intégration de PayPal pour vendre votre formation

Ce guide vous explique comment configurer PayPal pour vendre votre formation directement depuis votre page Notion.

## 1. Création du compte PayPal Business

Si vous n'avez pas encore de compte PayPal Business:

1. Visitez [PayPal Business](https://www.paypal.com/fr/business)
2. Cliquez sur "S'inscrire" et suivez les étapes
3. Complétez votre profil d'entreprise
4. Vérifiez votre compte selon les instructions

## 2. Configuration du produit dans PayPal

1. Connectez-vous à votre compte PayPal
2. Accédez à "Produits et services" > "Gérer les produits"
3. Cliquez sur "Créer un nouveau produit"
4. Configurez votre formation:
   - **Nom**: "Formation n8n Docker HTTPS Setup"
   - **Description**: "Formation complète pour configurer n8n avec Docker, HTTPS et IA"
   - **Prix**: 149,00 EUR (prix promotionnel)
   - **Type**: Produit numérique
   - **Photo**: Ajoutez une image de la formation
   - **Catégorie**: Formation/Éducation

## 3. Création du bouton de paiement

### Option 1: Bouton PayPal standard

1. Dans PayPal, allez dans "Outils de vente" > "Boutons PayPal"
2. Sélectionnez "Créer un bouton"
3. Type de bouton: "Acheter maintenant"
4. Configurez les détails:
   - Sélectionnez le produit créé précédemment
   - URL de retour: `https://formation.oceanphenix.fr/merci`
   - URL d'annulation: `https://formation.oceanphenix.fr/tarifs`
5. Personnalisez l'apparence du bouton si nécessaire
6. Copiez le code HTML généré

### Option 2: Bouton PayPal Smart

Pour une expérience plus moderne:

1. Accédez à l'onglet "PayPal Checkout" dans les outils de vente
2. Suivez les étapes pour créer un bouton Smart
3. Personnalisez les options et les styles
4. Copiez le code JavaScript généré

## 4. Intégration dans Notion

### Méthode 1: Embed HTML (via Super.so ou autre outil)

Si vous utilisez Super.so ou un outil similaire pour personnaliser Notion:

1. Collez le code HTML/JavaScript du bouton PayPal dans un bloc "Embed"
2. Publiez les modifications

### Méthode 2: iFrame dans Notion

Si vous ne pouvez pas utiliser l'intégration directe:

1. Créez une page HTML simple contenant uniquement le bouton PayPal (voir `payment_button.html`)
2. Hébergez cette page sur GitHub Pages, Netlify ou similaire
3. Dans Notion, utilisez un bloc "Embed" pour intégrer cette page

### Méthode 3: Lien externe

Si les méthodes ci-dessus ne fonctionnent pas:

1. Créez une page de paiement hébergée par PayPal
2. Dans Notion, ajoutez un bouton avec un lien vers cette page

## 5. Configuration des webhooks PayPal

Pour automatiser les actions après paiement:

1. Dans PayPal, accédez à "Paramètres du compte" > "Notifications"
2. Configurez un webhook vers votre instance n8n:
   - URL: `https://votre-instance-n8n.com/webhook/paypal`
   - Événements: `PAYMENT.SALE.COMPLETED`
3. Notez l'ID du webhook et le token secret
4. Utilisez ces informations dans le workflow n8n (voir dossier `automation`)

## 6. Tests de paiement

Avant de mettre en production:

1. Activez le mode Sandbox dans PayPal
2. Créez des comptes de test acheteur/vendeur
3. Effectuez des achats de test
4. Vérifiez que les webhooks fonctionnent correctement
5. Testez le processus complet de A à Z

## 7. Considérations légales

Assurez-vous d'inclure sur votre page Notion:

- Conditions générales de vente (CGV)
- Politique de remboursement
- Mentions légales complètes
- Informations sur la TVA si applicable

## Ressources annexes

- `payment_button.html`: Template HTML pour le bouton de paiement
- `paypal_ipn_handler.js`: Script pour gérer les notifications instantanées de paiement
- `paypal_webhook_config.json`: Configuration des webhooks pour n8n
