import os
import tkinter as tk
from tkinter import messagebox
import webbrowser
from tkinter import filedialog
from pyzbar.pyzbar import decode
import cv2

def afficher_resultat(resultats):
    fenetre = tk.Tk()
    fenetre.title("Résultats")
    fenetre.configure(bg="#f0f0f0")

    for resultat, lien in resultats:
        label = tk.Label(fenetre, text=resultat, bg="#f0f0f0", font=("Arial", 12), wraplength=400)
        label.pack(pady=5)

        def ouvrir_lien(lien=lien):
            webbrowser.open(lien)

        bouton = tk.Button(fenetre, text="Ouvrir", command=ouvrir_lien, bg="#4CAF50", fg="white", font=("Arial", 12))
        bouton.pack(pady=5)

    fenetre.mainloop()

def lire_fichier(file):
    _, extension = os.path.splitext(file)
    resultats = []

    if extension in ['.png', '.jpg', '.jpeg']:
        image_cv = cv2.imread(file)
        if image_cv is None:
            print("Erreur : Impossible de lire l'image. Vérifiez le chemin du fichier.")
            return
        decoded_objects = decode(image_cv)
        for obj in decoded_objects:
            lien = obj.data.decode('utf-8')
            resultats.append((f"QR Code trouvé : {lien}", lien))
    elif extension == '.pdf':
        import PyPDF2
        with open(file, 'rb') as fichier:
            lecteur = PyPDF2.PdfReader(fichier)
            for page in lecteur.pages:
                texte = page.extract_text()
                if texte:
                    resultats.append((texte, ""))
    else:
        resultats.append(("Type de fichier non pris en charge.", ""))

    afficher_resultat(resultats)

def choisir_fichier():
    chemin_fichier = filedialog.askopenfilename(title="Sélectionnez un fichier", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if chemin_fichier:
        lire_fichier(chemin_fichier)

root = tk.Tk()
root.withdraw()
choisir_fichier()
