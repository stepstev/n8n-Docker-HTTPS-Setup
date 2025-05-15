# Générateur de contenu vidéo YouTube pour n8n Docker HTTPS Setup

Ce projet contient les outils nécessaires pour créer une vidéo YouTube complète présentant la configuration de n8n avec Docker, HTTPS via ngrok et les fonctionnalités d'IA.

## Contenu du projet

- `create_youtube_video.py` : Script principal qui génère tous les fichiers nécessaires pour la création de la vidéo
- `output/` : Répertoire contenant les fichiers générés
  - `script.md` : Script détaillé pour chaque section de la vidéo
  - `storyboard.json` : Structure du storyboard au format JSON
  - `instructions_captures.md` : Instructions pour réaliser les captures d'écran
  - `guide_enregistrement.md` : Guide pour l'enregistrement et la post-production
  - `screenshots/` : Dossier pour stocker les captures d'écran
  - `segments/` : Dossier pour stocker les segments vidéo

## Utilisation

1. Exécutez le script principal :
   ```bash
   python create_youtube_video.py
   ```

2. Suivez les instructions générées dans les fichiers de sortie pour :
   - Réaliser les captures d'écran
   - Enregistrer les segments vidéo
   - Effectuer la post-production

## Structure de la vidéo

La vidéo est structurée en 10 sections :

1. Introduction
2. Prérequis
3. Structure du projet
4. Configuration Docker
5. Démarrage de n8n
6. Configuration HTTPS avec ngrok
7. Activer et configurer l'IA
8. Démonstration d'un workflow d'IA
9. Documentation et support
10. Conclusion

Durée totale estimée : environ 15 minutes.

## Personnalisation

Vous pouvez personnaliser le contenu de la vidéo en modifiant la structure `YOUTUBE_SCRIPT` dans le fichier `create_youtube_video.py`.
