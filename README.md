🔥 YOLO-Based Real-Time Fire Detection & Email Alert

Un système intelligent de détection d’incendie en temps réel basé sur YOLO, capable d’identifier les flammes dans une vidéo ou un flux caméra et d’envoyer automatiquement une alerte par email avec photo.

📌 Description

Ce projet utilise un modèle YOLOv11n entraîné pour détecter les incendies dans des images ou des vidéos.
Lorsqu’un feu est détecté, le système :

capture automatiquement une image annotée,
envoie une alerte email contenant l'heure de détection, la date,
joint la photo du feu détecté,
assure un fonctionnement en temps réel sans interruption du flux vidéo.

Ce projet peut être utilisé pour :

surveillance vidéo,
sécurité industrielle,
systèmes IoT,
détection d’incendie,
automatisation bâtiment.
🚀 Fonctionnalités
Détection de feu en temps réel via YOLO (Ultralytics)
Support vidéo + webcam
Envoi automatique d’email via la bibliothèque Gmail "SMTP"
Image capturée et annotée jointe à l’email

🧠 Technologie utilisée
YOLOv11n (Ultralytics)
Python (OpenCV, smtplib, email.mime)
Modèle entraîné sur un dataset personnalisé Roboflow
SMTP Gmail pour les alertes email
