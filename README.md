# Projet de Lecture de QR Codes et PDF

Ce projet permet de lire des QR codes à partir d'images (formats PNG, JPG, JPEG) et d'extraire du texte à partir de fichiers PDF. Les résultats sont affichés dans une interface graphique, avec la possibilité d'ouvrir les liens trouvés.

## Fonctionnalités

- Lecture de QR codes à partir d'images.
- Extraction de texte à partir de fichiers PDF.
- Interface graphique simple avec Tkinter.
- Boutons pour ouvrir les liens trouvés.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé Python et `pip` sur votre machine.

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/Luis06000/qr-reader.git
    ```

2. Accédez au répertoire du projet dans votre terminal :
    ```bash
    cd qr-reader
    ```

3. Installez les dépendances requises en exécutant :

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Placez votre fichier image (PNG, JPG, JPEG) ou PDF dans le même répertoire que `main.py`.
2. Modifiez la variable `file` dans `main.py` pour correspondre au nom de votre fichier.
3. Exécutez le script :

   ```bash
   python main.py
   ```

4. Une fenêtre s'ouvrira affichant les résultats. Cliquez sur le bouton "Ouvrir" à côté de chaque lien pour l'ouvrir dans votre navigateur.

## Auteurs

- [Luis FERNANDES](https://github.com/Luis06000)
