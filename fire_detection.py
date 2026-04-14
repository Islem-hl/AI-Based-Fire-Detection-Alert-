import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import os 
import time

model= YOLO("C:/Users/islem/miniconda3/myenv/best_fire.pt")
cap= cv2.VideoCapture("C:/Users/islem/OneDrive/Images/ressources/fire.mp4")

now = datetime.now() 
date = now.strftime("%d/%m/%Y")
Time= now.strftime("%H:%M:%S")

seuil_time= 2 
last_time= 0
timing=0
# Adresse expediteur
email_sender = "sender@gmail.com"
app_password = "vovi ensr xhds qddu"

# Adresse recepteur
email_receiver = "receiver@gmail.com"

# Objet + message
subject = "Fire Alerte"
body = f"Fire detected!🔥 Please take necessary actions.⚠️📢\n Date: {date} \n Time : {Time} "

# Construction message
msg = MIMEMultipart()
msg["From"] = email_sender
msg["To"] = email_receiver
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# Envoi via SMTP
#a=int(input("a= "))
email_sent = False
fire_started_time = None
saved_images = []    # liste des photos à envoyer
MAX_IMAGES = 5 
while True:
    ret, frame= cap.read()
    
#cap = cv2.VideoCapture(0)
#img= cv2.imread("C:\\Users\\islem\\OneDrive\\Images\\ressources\\,,.jpeg")
    print ("fire system activated 🔥")
    height, width, _ = frame.shape

    # Resize the frame
    scale_percent = 50
    new_width = int(width * scale_percent / 100)
    new_height = int(height * scale_percent / 100)
    dim = (new_width, new_height)
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    
    result= model (frame ,conf= 0.55,save = True  )
   
    
    annotated = result[0].plot()  # Récupérer le chemin de l'image sauvegardée
    

    # Affichage des résultats
    class_names = result[0].names                # ex: {0: 'fire'}
    detected_ids = result[0].boxes.cls.tolist()  # ex: [0, 0, 0]
    detected_classes = [class_names[int(i)] for i in detected_ids]
    #print("Detected:", detected_classes)
    
    
    # Vérification
    if "fire" in detected_classes and not email_sent :
        print("🔥 FEU DÉTECTÉ ! Envoi email...")
        save_path = "fire_detected.jpg"
        cv2.imwrite(save_path, annotated)
        print("Image sauvegardée :", save_path)
        
        try:
            with open(save_path, 'rb') as f:
                img_data = f.read()
             # sauvegarder l'image annotée
        
            image_part = MIMEImage(img_data, _subtype="jpg")
            image_part.add_header('Content-Disposition', 'attachment', filename=f"fire_detected.jpg")
            msg.attach(image_part)
    
        except Exception as e:
            print("Erreur lors de la lecture de l'image:", e)
             
        try:
            #current_time = time.time()
            
            # if current_time - last_time >= 1:  # 1 second has passed
            #     timing += 1  # Increment the timing
            #     last_time = current_time  # Update the last time
            # if timing >= seuil_time:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(email_sender, app_password)
            server.sendmail(email_sender, email_receiver, msg.as_string())
            server.quit()
            print("📧 Email envoyé !")
            email_sent = True
            
          
        except Exception as e:
            print("Erreur email:", e)
    
    cv2.imshow("fire detection",result[0].plot())
    if cv2.waitKey(10) & 0xFF == ord ('q'):
        break
    
cv2.destroyAllWindows()


