import cv2
import requests
import time
import os

# Obtenir l'URL de l'API depuis les variables d'environnement
API_URL = os.getenv('API_URL', 'http://localhost:5000/upload')

def capture_image():
    # Ouvrir la caméra USB (0 pour la première caméra, 1 pour la deuxième, etc.)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erreur: Impossible d'ouvrir la caméra.")
        return None

    # Capturer une image
    ret, frame = cap.read()

    # Libérer la caméra
    cap.release()

    if ret:
        # Enregistrer l'image capturée dans un fichier temporaire
        image_path = 'captured_image.jpg'
        cv2.imwrite(image_path, frame)
        return image_path
    else:
        print("Erreur: Impossible de capturer l'image.")
        return None

def upload_image(image_path):
    # Ouvrir le fichier image
    with open(image_path, 'rb') as img:
        # Envoyer la requête POST avec l'image
        files = {'image': img}
        response = requests.post(API_URL, files=files)

    # Afficher la réponse du serveur
    print(response)

if __name__ == '__main__':

    while(True):
        # Capturer l'image
        image_path = capture_image()

        if image_path:
            # Envoyer l'image à l'API
            upload_image(image_path)
        
        time.sleep(1)