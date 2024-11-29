Eliot.Decimal
=============

Obiectiv: sa avem un sistem care sa ne ajute sa navigam in "haos"-ul informational in care traim
pentru a lucra eficient.

Features
--------

1. Sistem de fisiere structurat pe 3-5 nivele tinut pe github

Nivel 1: Area (analogie: raf vertical)
Nivel 2: Category (analogie: cutie)
Nivel 3: Id (max 100) de forma: AC.II (A - area, C - categoria, II - nr id-ului). (analogie: un dosar/biblioraft din cutie)
Nivel 4 - un item intr-un Id, care poate fi folder
Nivel 5 - fisier intr-un folder de la nivelul 4

vezi https://johnnydecimal.com/ 

Tema:
1a. Identificat areas pentru sistemul Eliot

1b. Pentru fieare area de la 1a identificat categoriile

1c. Pentru fiecare categorie de la punctul 1b identificat id-urile

2. DSL centrat pe asistarea tratarii problemelor de prod (si nu numai)

Informatia pe care o primim e un mix de informatie formala (pusa in forme bine stabilite:
url-uri, query-uri, call-uri API cu parametrii si rezultate) si informala - descrierea 
problemei in limbaj uman.

Informatia din Eliot.Decimal va avea un grad de formalizare mai mare, va fi "digerata".

Tema: 
2a1. Scos de la naftalina X probleme concrete (bine ar fi 10, dar cat se poate) cu tot cu pasii
facut pentru rezolvarea lor. Bine ar fi sa fie cat mai consistente

2a. Identificat elementelor formale care apar in descrierea problemelor

2b. Pentru fiecare element de la 2a identificat setul complet de atribute

2c. Identificat tipurile de cereri venite de la client

2d. Pentru fiecare tip de cerere de la 2c identificat atributele care o descriu

2e. Identificat elementele structurale ale raspunsurilor catre clienti

2f. Pentru fiecare element structural de la 2e identificat atributele care il descriu

2g. Identificat tipurile de pasi folosite pentru diagnoza problemei

2h. Pentru fiecare tip de pas de la 2g identificat atributele sale

3. Dezvoltat engine care sa ne permita sa raspundem accesand DSL-ul

4. Integram informatia existenta in sistemul actual

4a. Integrat informatia despre aplicatii la modul general

4b. Acessul la tooluri (kibana, isql, swagger, oauth2, samd)

4c. Tabele - si unde sunt folosite

4d. Fluxuri (flow-uri) de date

4e. Identificat ce informatie mai e necesara conform experientei de la punctul 2

5. Stabilit reguli de "metabolizare" a informatiei

La nivelul lui Eliot.Decimal sunt 3 nivele pentru administrarea informatiei.

00 - la nivel general
A0.0 - la nivel de arie
AC.0 - la nivel de categorie

Fiecare nivel are 
0 - index
1 - inbox
2 - notes
3 - todos
4 - bookmarks
5 - templates
6,7 - unused
8 - sameday
9 - archive

Teme
5a. Validam ce ni se pare potrivit la Eliot. 
Daca tu ai face sistemul ce ai pastra de mai sus si ce ai adauga?

5b. Definit template-uri pt elementele de DSL identificate la 2

5c. Definit reguli de lucru pentru inbox, todo, template, archive, index