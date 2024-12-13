import os
import tkinter as tk
from tkinter import messagebox
import webbrowser

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
        import cv2
        from pyzbar.pyzbar import decode
        
        image_cv = cv2.imread(file)
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

file = 'image.png'
lire_fichier(file)
