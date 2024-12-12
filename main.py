import os

def lire_fichier(file):
    _, extension = os.path.splitext(file)

    if extension in ['.png', '.jpg', '.jpeg']:
        import cv2
        from pyzbar.pyzbar import decode
        
        image_cv = cv2.imread(file)
        decoded_objects = decode(image_cv)
        for obj in decoded_objects:
            print("QR Code trouvé : ", obj.data.decode('utf-8'))
    elif extension == '.pdf':
        import PyPDF2
        with open(file, 'rb') as fichier:
            lecteur = PyPDF2.PdfReader(fichier)
            for page in lecteur.pages:
                print(page.extract_text())
    else:
        print("Type de fichier non pris en charge.")

file = 'image.png'
lire_fichier(file)
