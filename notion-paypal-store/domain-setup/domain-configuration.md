# Configuration du domaine formation.oceanphenix.fr

Ce guide vous explique comment configurer le sous-domaine formation.oceanphenix.fr pour votre site de formation basé sur Notion.

## 1. Options de configuration

Vous avez plusieurs options pour configurer votre domaine personnalisé:

1. **Notion + Service tiers** (Super.so, Potion, Fruition)
2. **Notion + Redirection DNS** (méthode simple)
3. **Notion + Serveur proxy personnalisé** (méthode avancée)

Ce guide couvre les trois méthodes, choisissez celle qui vous convient le mieux.

## 2. Méthode 1: Utilisation d'un service tiers (Recommandé)

### Option A: Super.so

1. Créez un compte sur [Super.so](https://super.so)
2. Connectez votre compte Notion
3. Importez votre page Notion de formation
4. Dans Super.so, allez dans "Domains"
5. Ajoutez "formation.oceanphenix.fr" comme domaine personnalisé
6. Suivez les instructions pour configurer les enregistrements DNS:
   - Type: CNAME
   - Nom: formation
   - Valeur: proxy.super.so
7. Attendez la propagation DNS (généralement 24-48h)

### Option B: Potion.so

Suivez des étapes similaires avec [Potion.so](https://potion.so) si vous préférez ce service.

## 3. Méthode 2: Redirection DNS simple

Si vous préférez ne pas utiliser de service tiers:

1. Accédez à votre gestionnaire DNS (où oceanphenix.fr est enregistré)
2. Créez un enregistrement CNAME:
   - Type: CNAME
   - Nom: formation
   - Valeur: notion.so
3. Configurez une redirection URL:
   - De: formation.oceanphenix.fr
   - Vers: votre-page-notion-publique.notion.site
4. Cette méthode est simple mais a des limitations (pas de personnalisation avancée)

## 4. Méthode 3: Serveur proxy personnalisé

Pour un contrôle total (méthode avancée):

1. Configurez un serveur VPS (DigitalOcean, AWS, etc.)
2. Installez Nginx comme proxy inverse
3. Utilisez le fichier de configuration Nginx fourni (`nginx-notion-proxy.conf`)
4. Configurez un certificat SSL avec Let's Encrypt
5. Pointez l'enregistrement DNS A vers l'IP de votre serveur:
   - Type: A
   - Nom: formation
   - Valeur: [IP de votre serveur]

## 5. Configuration des redirections

Pour une meilleure UX, configurez ces redirections:

- `formation.oceanphenix.fr` → Page d'accueil de la formation
- `formation.oceanphenix.fr/programme` → Page détaillée du programme
- `formation.oceanphenix.fr/tarifs` → Page d'inscription et paiement
- `formation.oceanphenix.fr/merci` → Page de remerciement après achat

## 6. Vérification et tests

Après configuration:

1. Vérifiez que le domaine est accessible
2. Testez la fonctionnalité HTTPS (certificat valide)
3. Vérifiez que les liens internes fonctionnent
4. Testez sur différents appareils (desktop, mobile)
5. Vérifiez le processus d'achat complet

## 7. Maintenance DNS

- Conservez une copie de vos configurations DNS
- Notez les dates d'expiration des domaines/certificats
- Configurez des alertes pour les renouvellements

## Ressources annexes

- `nginx-notion-proxy.conf`: Configuration Nginx pour le proxy
- `dns-records.txt`: Exemples d'enregistrements DNS
- `ssl-setup.sh`: Script pour configurer Let's Encrypt
