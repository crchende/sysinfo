Aplicatia poate fi instalata intr-un container docker.

Pentru aceasta, este nevoie de fisierul: Dockerfile.
Acesta contine informatiile de care are nevoie aplicatia docker pentru a crea
containerul.

TBD - explicare continut Dockerfile.

Cerinte
=================
docker sa fie disponibil pe calculator.

Creere container
=================
Dupa creerea Dockerfile, in acelasi director cu acest fisier - pentru acest caz
site_disribuitor, trebuie executata comanda:

    sudo docker build -t sysinfo:v01 .

Aceasta creeaza o imagine de container care poate fi vizualizata cu comanda:
    
    sudo docker images
    
    ex:
    REPOSITORY                  TAG             IMAGE ID       CREATED       SIZE
    sysinfo                     v01             beadef0060e0   2 hours ago   110MB
    python                      3.8-alpine      0ccdcbe88eaa   5 days ago    47.5MB
    
    Avem doua imagini:
    - imaginea de baza, python:3.8-alpine, folosita pentru a
      crea imaginea site_distribuitor
    - imaginea sysinfo, creata pe baza imaginii python, in care se
      creaza venv-ul, se instaleaza pachetele necesare aplicatiei, se copiaza
      codul aplicatiei - conform Dockerfile

Executie container
===================
Pentru a genera un container din fisierul imagine trebuie executata comanda run:

    sudo docker run --name sysinfo -p 8020:5011 sysinfo:v01 
    
    Aceasta va crea containerul si va si porni executia acestuia.
    
    Portul pe calculator unde va raspunde serverul din docker este  - 8020
    Portul in interiorul containerului este                         - 5011.

    Rezultatul executie containerului va fi vizibil in terminalul de unde s-a dat
    comanda.
    In consola apar mesajele generate de aplicatia din container.
    
    -d - optiune care trebuie adaugata pentru a rula containerul in background
         altfel, consola din care ruleaza containerul este blocata pe timpul
         rularii acestuia
         
    NOTA:
    --nume <nume>  este de folosit aceasta optiune.
                   altfel docker va crea un string aleator si-l va aloca ca nume
                   container-ului pornit
         
Vizualizare containere
=======================

    - vizualizare continere care ruleaza


    sudo docker ps

    CONTAINER ID   IMAGE                            COMMAND              CREATED          STATUS          PORTS                                       NAMES
    0e9388ac0d7d   sysinfo:v01                      "./dockerstart.sh"   2 hours ago      Up 22 minutes   0.0.0.0:8020->5011/tcp, :::8020->5011/tcp   sysinfo

    - vizualizarea tuturor containerelor (inclusiv cele oprite)

    
    sudo docker ps -a

    CONTAINER ID   IMAGE                            COMMAND              CREATED          STATUS                     PORTS                                       NAMES
    0e9388ac0d7d   sysinfo:v01                      "./dockerstart.sh"   2 hours ago      Exited (0) 6 seconds ago                                               site



Oprire / pornire container - cu aplicatia din container
=======================================================
sudo docker stop site
sudo docker start site



Inspectare container - conectare la container-ul care ruleaza cu shell
=======================================================

sudo docker exec -it cchende_sysinfo sh

    - vizualizare procese pe container (pot fi date si alte comenzi LINUX)
    
~/app $ ps
PID   USER     TIME  COMMAND
    1 site      0:02 {flask} /home/sysinfo/sysinfo.venv/bin/python /home/sysinfo/sysinfo/.venv/bin/flask run -h 0.0.0.0 -p 5011 --reload
    8 site      0:30 /home/sysinfo/sysinfo/.venv/bin/python /home/sysinfo/sysinfo/.venv/bin/flask run -h 0.0.0.0 -p 5011 --reload
   11 site      0:00 sh
   17 site      0:00 ps
   
(inchiderea terminalului pe container se face cu 'exit')



Curatenie - stergere containere / imagini
=========================================================

sudo docker rm  <container (id, nume)r>
sudo docker rmi <imagine (id, nume:tag ...)>


Adaugare imagine pe Docker Hub.
=========================================================
Pentru a putea partaja containerul, acesta poate fi incarcat pe Docker Hub.
Aceasta varianta este utila pentru ca permite foarte usor accesul altor persoane.

(Alta variata ar fi exportul imaginii intr-o arhiva: 
    
    sudo docker export <imagine> > <arhiva.tgz>

    iar apoi importul:
    
    sudo docker import <arhiva>)

Varianta cu Docker Hub prezinta avantajul ca acest site este usor accesibil si
pune la dispozitie fara plata un spatiu de stocare foarte generos (sute de containere)

Este nevoie de un cont pe https://hub.docker.com (pentru Docker Hub)

Pentru a pun containerul trebuie urmati urmatorii pasi (din terminal):

------------
    docker login
    Username: <username dockerhub>
    Password: <parola dockerhub> 

Tagare container astfel incat numele sa includa si username-ul de Docker Hub:

-------------
    docker tag sysinfo:v01 <username>/sysinfo:v01

    (docker tag <nume imagine> <username>/<nume_imagine>)


Incarcare (push) pe dockerhub

-------------
    docker push <username>/<nume_imagine>

ex:
    docker push cchende/sysinfo:v01

Aceasta comanda pune container-ul pe serverul Docker Hub
(login-ul pe docker hub din consola este obligatoriu

Comanda logout
--------------
    docker logout
)

Executie container de pe Docker Hub.

Oricine vrea apoi sa ruleze containerul poate sa o faca cu comanda:

----------------
    docker run -name <nume> -d -p 8020:5011 <username>/<nume imagine>

ex:
    sudo docker run --name cchende_syinfo -d -p 8020:5011 cchende/sysinfo:v01

Aceasta comana va downloada imaginea si va porni executia containerului


Lista de comenzi docker utile
===============
Creere container:           sudo docker build ...
Vizualizare imagini         sudo docker images
Vizualizare containere      sudo docker ps / sudo docker ps -a
Rulare container            sudo docker run
Stop container              sudo docker stop
Start container             sudo docker start

