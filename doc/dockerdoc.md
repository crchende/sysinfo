# Cuprins

1. [Containerizarea unei aplicatii](#containerizarea-unei-aplicatii)
1. [Configurarea necesara pentru containerizare. Fisierul Dockerfile.](#configurarea-necesara-pentru-containerizare-fisierul-dockerfile)
1. [Instalare unelte docker pe calculator](#instalare-unelte-docker-pe-calculator)
1. [Utilizare docker](#utilizare-docker)

    - creare imagine pentru container (echivalent cu un fel de kit de instalare)
    - creare container si executia acestuia (kit-ul de mai sus instalat)
    - vizualizare containere / imagini
    - oprire / pornire container
    - tratare probleme (cand avem probleme sa cream, pornim containerul)
    - inspectare container
    - curatenie - stergere imagini, containere (deoarece ocupa loc pe hard)
    - publicare imagine pe `dockerhub`
    - lista comenzi utile

# Containerizarea unei aplicatii

Ne dorim ca aplicatia noastra sa poata fi executata pe diverse calculatoare / servere. Acestea (calculatoarele) pot rula diverse sisteme de operare, cu diverse versiuni si poate fi nevoie de configurare diferita pe fiecare in parte pentru a instala pachetele software de care nevoie aplicatia noastra sa poata fi lansata in executie.

Asadar, pentru a distribui o aplicatie poate fi nevoie de kit de instalare specific pentru diverse tipuri de sisteme de operare, si aceste kit-uri de instalare ar trebui actualizate in viitor pentru noile versiuni de sisteme de operare.
Operatiunile acestea nu sunt banale si daca nu sunt bine facute, riscam sa ajungem in situatia ca aplicatia noastra sa nu mai poata fi executata din cauza kit-ului de instalare neactualizat.

Problema aceasta este o problema generala care tine de cum putem distribui o aplicatie. O solutie eleganta pentru a distribui o aplicatie - si sa nu mai fie nevoie sa ne preocupam de kit-uri de instalare specifice, este `containerizarea` aplicatiei.

`Containerizarea` unei aplicatii, inseamna `'impachetarea'` acesteia impreuna cu pachetele software de care are nevoie aplicatia pentru a putea fi executata.

Exemplul de fata se refera la containerizarea unei aplicatii Python (sysinfo) folosind setul de unelte pus la dispozitie de compania `Doker` si care poate fi instalat usor pe Linux.

Pentru mai multe detalii despre ce inseamna containerizare cu setul de unelte de la `Docker` accesati documentatia: https://docs.docker.com/get-started/

# Configurarea necesara pentru containerizare. Fisierul Dockerfile.

In aplicatia pe care vream sa o containerizam, trebuie adaugat un fisier, in care sa descriem ce container de baza folosim, ce vrem sa contina containerul, comenzile necesare pentru a copia in container directoarele si fisierele relevante, ce program sa se porneasca la pornirea containerului.

Acesta este fisierul: Dockerfile

Se gaseste chiar in directorul 'sysinfo'.

Continutul acestuia si explicatii (textul comentat cu #):.

        FROM python:3.8-alpine                                                       # Containerul de baza folosit
        
        ENV FLASK_APP sysinfo                                                        # Setare variabila de environment
        #ENV FLASK_CONFIG = docker
        
        #3.8 booster
        #RUN useradd -rm -d /home/site -s /bin/bash -g root -G sudo -u 1001 site
        
        #3.8 alpine
        RUN adduser -D sysinfo                                                       # Creare user in container
        
        USER sysinfo                                                                 # su sysinfo (schimbare user)
        
        WORKDIR /home/sysinfo/                                                       # cd in directorul indicat
        
        COPY app app                                                                 # copiez in container app
        COPY dockerstart.sh dockerstart.sh                                           #   si dockerstart.sh
        COPY pytest.ini pytest.ini                                                   #   si pytest.ini
        COPY quickrequirements.txt quickrequirements.txt                             #       -//-
        COPY sysinfo.py sysinfo.py                                                   #       -//-
        
        RUN python3 -m venv .venv                                                    # rulare comanda creare venv in dir .venv
        RUN .venv/bin/pip install -r quickrequirements.txt                           # rulare comanda instalare dependinte     
        
        #WORKDIR /home/sysinfo/app
        
        # runtime configuration
        EXPOSE 5011                                                                  # expunere port 5011 pe care va rula aplicatia
        ENTRYPOINT ["./dockerstart.sh"]                                              # entrypoint - ce trebuie executat la pornire container
        #CMD flask run --host 0.0.0.0 -p 5010

# Instalare unelte docker pe calculator

Setul de unelte de la `docker` sa fie disponibil pe calculator.

Pentru instalarea docier pe Ubuntu, consultati documentatia: https://docs.docker.com/desktop/setup/install/linux/ubuntu/

Setul de unelte docker, ar trebui sa poata fi instalat usor, folosind `apt`:

    sudo apt-get update
    sudo apt-get install ./docker-desktop-amd64.deb

Documentatia indicata la link-ul de mai sus este actualizata de catre compania `docker`. In caz ca comenzile de mai sus nu functioneaza, consultati link-ul.

# Utilizare docker

## Creare imagine container

Dupa crearea Dockerfile, in acelasi director cu acest fisier - pentru acest caz
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

## Creare container si executie

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
         
## Vizualizare containere

    - vizualizare continere care ruleaza


    sudo docker ps

    CONTAINER ID   IMAGE                            COMMAND              CREATED          STATUS          PORTS                                       NAMES
    0e9388ac0d7d   sysinfo:v01                      "./dockerstart.sh"   2 hours ago      Up 22 minutes   0.0.0.0:8020->5011/tcp, :::8020->5011/tcp   sysinfo

    - vizualizarea tuturor containerelor (inclusiv cele oprite)

    
    sudo docker ps -a

    CONTAINER ID   IMAGE                            COMMAND              CREATED          STATUS                     PORTS                                       NAMES
    0e9388ac0d7d   sysinfo:v01                      "./dockerstart.sh"   2 hours ago      Exited (0) 6 seconds ago                                               site



## Oprire / pornire container - cu aplicatia din container

    sudo docker stop site
    sudo docker start site


## Tratare probleme (Debugging)

In cazul in care containerul nu porneste poate fi folosita comanda de mai jos pentru a
crea un container cu imaginea cu probleme care in loc entrypoint-ul configurat va
folosi shell ca entrypoint.

    docker run -it --rm --entrypoint sh <image:tag>


## Inspectare container - conectare la container-ul care ruleaza cu shell

sudo docker exec -it cchende_sysinfo sh

    - vizualizare procese pe container (pot fi date si alte comenzi LINUX)
    
~/app $ ps
PID   USER     TIME  COMMAND
    1 site      0:02 {flask} /home/sysinfo/sysinfo.venv/bin/python /home/sysinfo/sysinfo/.venv/bin/flask run -h 0.0.0.0 -p 5011 --reload
    8 site      0:30 /home/sysinfo/sysinfo/.venv/bin/python /home/sysinfo/sysinfo/.venv/bin/flask run -h 0.0.0.0 -p 5011 --reload
   11 site      0:00 sh
   17 site      0:00 ps
   
(inchiderea terminalului pe container se face cu 'exit')



## Curatenie - stergere containere / imagini

    sudo docker rm  <container (id, nume)r>
    sudo docker rmi <imagine (id, nume:tag ...)>


## Adaugare imagine pe Docker Hub.

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


## Lista de comenzi docker utile:

        Creere container:            sudo docker build -t <nume>:<tag>
        Vizualizare imagini:         sudo docker images
        Vizualizare containere:      sudo docker ps / sudo docker ps -a
        Rulare container:            sudo docker run -name <nume> -p <port PC>:<port Container> <imagine> [-d] # -d pentru a rula in background
        Stop container:              sudo docker stop
        Start container:             sudo docker start
        Executie shell:              sudo docker exec -it <nume> sh
        Atasare la container:        sudo docker atach <nume>

