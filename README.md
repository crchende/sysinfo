
`sysinfo`
===================================

# Cuprins

1. [Descriere aplicatie](#descriere-aplicatie)
1. [Descriere versiune](#descriere-versiune)
   1. [Buguri cunoscute](#probleme-cunoscute)
1. [Configurare](#configurare)
1. [Exemple pagina web](#exemple-pagina-web)
1. [Testare cu pytest](#testare-cu-pytest)
1. [Verificare statica. pylint - calitate cod](#verificare-statica-cu-pylint)
1. [Reprezentari grafice](#reprezentari-grafice)
1. [DevOps](#devops-ci)
   1. [Pipeline Jenkins](#exemplu-executie-pipeline-jenkins)
   1. [Workflow GitHub Actions](#exemplu-executie-workflow-in-github-actions)
1. [Bibliografie](#bibliografie)

# Descriere aplicatie

Aplicatia sysinfo citeste date despre sistemul de operare si despre retea si le afiseaza intr-o pagina web.
Poate fi executata doar pe Linux. A fost testata pe Ubuntu 22.04.
Componenta WEB a aplicatiei se bazeaza pe framework-ul `Flask`.
Aplicatia este simpla, citeste informatiile folosind modulul `subprocess` din Python si comenzi shell pentru a obtine informatiile despre sistemul de operare si despre retea.
Acestea sunt preluate apoi in functii `view` si returnate clientului WEB care apeleaza serverul.

Pentru o navigare mai usoara in browser, pagina principala contine link-uri catre celelalte pagini.
Fiecare pagina specifica (cea care afiseaza informatii despre memorie, cpu etc) contine un link catre pagina principala.

Am adaugat si un exemplu de afisare grafica folosind biblioteca Python `matplotlib`, pentru un set de valori al functiei `f(x) = x*x`.

Aplicatia include suport pentru containerizare in fisierul `Dockerfile` din directorul principal al aplicatiei.

Din punct de vedere al testarii, este inculs unit testing cu pytest, pentru o parte din functiile din biblioteca aplicatiei, aflate in directorul `app/lib`.

`DevOps CI`.
Pipeline-ul pentru Jenkins este definint in fisierul `Jenkinsfile`.
Worflow-ul (pipeline-ul) pentru GitHub Actions, in fisierul `.github/workflows/sysinfo_test.yml`.

Ambele pipeline-uri cloneaza codul, creaza mediul de lucru virtual (venv-ul), il activeaza si ruleaza testele (unit test - cu pytest, verificari statice cu pylint).

# Descriere versiune
## v03. Afisare intr-o forma mai prietenoasa, 
- folosire template-uri si flask-bootstrap
- structura mai complexa a aplicatiei
   - functiile view mutate intr-un blueprint
   - creare aplicatie in `app/__init__.py` cu ajutorul unei functii `factory function`
   - utilizare fisier configurare
- `unittest` cu pytest sub forma unei commenzi cli flask:
   - `cd` in directorul sysinfo
   - activare venv: `source activeaza_venv`   
   - executie teste cu comanda: `flask --app sysinfo test`

 * ruta standard '/' - URL: http://127.0.0.1:5011
 * rute in aplicatia WEB pentru:
   * versiune ubuntu: '/vos' - URL: 'http://127.0.0.1:5011/vos',
   * memorie:         '/mem' - URL: 'http://127.0.0.1:5011/mem'
   * cpu:             '/cpu' - URL: 'http://127.0.0.1:5011/cpu'
   * rute retea:      'retea/rute'      - URL: 'http://127.0.0.1:5011/retea/rute'
   * retea/interfete: 'retea/interfete' - URL: 'http://127.0.0.1:5011/retea/interfete'
  
## Probleme cunoscute
(Bug-uri)

--


# Configurare
[cuprins](#cuprins)

Configurare .venv si instalare pachete

In directorul 'app' rulati comenzile:

1) activeaza_venv: Incearca sa activeze venv-ul. 
                   Daca nu poate, configureaza venv-ul in directorul .venv si apoi instaleaza flask si flask-bootstrap.
                   La urmatoarea rulare, va activa doar venv-ul.
                
2) ruleaza_aplicatia: De rulat doar dupa activarea venv-ului. 
                      Va porni serverul pe IP: 127.0.0.1 si port: 5011.
                      Acces server din browser: http://127.0.0.1:5011

# EXEMPLU activare venv si rulare
```text
    cip@cip:sysinfo$ source activeaza_venv 
    SUCCESS: venv was activated.
    
    (.venv) cip@cip:sysinfo$ source ruleaza_aplicatia 
    sysinfo
    WARNING: rand 6 []
     * Serving Flask app 'sysinfo'
     * Debug mode: off
    WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
     * Running on http://127.0.0.1:5011
    Press CTRL+C to quit
     * Restarting with stat
    sysinfo
```
![image](https://user-images.githubusercontent.com/57460107/222927371-97c8c4b9-37c0-4d1f-b6ab-c2f3851c77f7.png)



# EXEMPLE pagina web 
## Pagina principala

### varianta v03 din branch-ul avansat_main
- implementare grafica avansata, folosind flask-bootstrap si template-uri

![image](https://github.com/crchende/sysinfo/assets/57460107/95bf735e-832b-4112-a10b-0240c3b1491e)

### varianta v02 din branch-ul simplu_main
- implementarea grafica simpla in cod dar nu prea prietenoasa pentru utilizator

![image](https://github.com/crchende/sysinfo/assets/57460107/2c106097-0954-4d6f-82ee-77fa5f052d1f)

## Vizualizare versiune ubuntu
![image](https://github.com/crchende/sysinfo/assets/57460107/0316f339-a277-4418-a1b0-d8ec0f022472)



# Testare cu pytest
[cuprins](#cuprins)

O parte din functiile din biblioteca de functii a aplicatie:
- directorul lib, fisierele:
  - ubuntu.py
  - network.py
au teste de tip 'unit - test' asociate - adica - este apelata functia si se asteapta o anumita valoare.
Testul compara valoarea obtinuta la apelul functie cu valoarea asteptata si returneaza PASS daca valoarea primita de la functie este cea asteptata si FAIL in caz contrar.

Pentru testare s-a folosit pachetul **pytest** din python. Acesta se afla in lista de pachete care trebuie instalate, in fisierul quickrequirements.txt.
Executia testelor se face cu oricare din comenzile de mai jos, apelate din directorul aplicatiei - *sysinfo*:
```
   pytest
   python -m pytest
   flask --app sysinfo test

   Ultima commanda este posibila datorita implementarii comenzii cli test in aplicatia sysinfo.
   Aceasta comanda CLI, apeleaza pytest din program/script:
       pytest.main(["."])
   
   Ultima varianta, desi echivalenta cu primele doua, este mai eleganta.
   Primele doua apeleaza pytest ca fiind ceva extern aplicatiei. 
   Aici insa avem optiunea de a se 'autotesta' inclusa in aplicatie.
```



# Verificare statica cu pylint
[cuprins](#cuprins)

- **pylint** - pachet python folosit la testarea calitatii codului (spatii, nume variabile, variabile neutilizate etc.)
- in cazul de fata, problemele returnate de pylint doar sunt afisate, nu sunt considerate erori



# Reprezentari grafice
[cuprins](#cuprins)
* Pachetul matplotlib pune la dispozitie o metoda de a face reprezentari grafice
* O aplicatie concretea pentru informatii de sistem, pot fi grafice cu utilizarea memoriei, a procesorului, retelei etc.
* Pentru simplitate aplicatia curenta genereaza valorile si afiseaza graficul unei functii de grad 2: **y = x*x**
    * valorile sunt discrete, x in {-10, -9, ... 9, 10}
    * matplotlib poate desena punctele sau un grafic continuu pe baza acestor puncte


## Exemplu pagina web cu grafice

* sunt mai multe grafice in pagina, captura cuprinde doar doua reprezentari cu puncte, cu culori si caractere diferite:
![image](https://github.com/crchende/sysinfo/assets/57460107/02c977f7-16b4-48c2-9747-3c6a3885af48)



# DevOps CI
[cuprins](#cuprins)
- CI = Continuous Integration

## Exemplu executie pipeline Jenkins
![image](https://github.com/crchende/sysinfo/assets/57460107/8fdaa372-44ee-409b-855c-053e78baf800)

## Exemplu executie Workflow in GitHub Actions
![image](https://github.com/crchende/sysinfo/assets/57460107/9981d699-aa34-4ec5-aa94-d0284ea93fca)


# Bibliografie:
[cuprins](#cuprins)
- [Github Actions](https://docs.github.com/en/actions)

