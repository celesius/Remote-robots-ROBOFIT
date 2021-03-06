Remote-robots-ROBOFIT [![Build Status](TODO)](TODO)
===============

# Úvod
Hlavní částí systému je server, jehož činnost je rozdělená do 3 podprocesů. 
 
# Server Implementations

## 1. Hlavní vlákno
Hlavní vlákno [server.py](server.py) zpracovává registrační požadavky od klientů, shromažduje a následně distribuuje metadata o klientech a robotech, řeší autentifikaci a autorizaci klienta a robota, vyřizuje práva a zahajuje kuminikační kanály mezi klientem a robotem. Toto vlákno je na stroji puštěné vždy jenom jednou a přetrvává po celou dobu běhu serveru. Řídící cyklus hlavního vlákna je založený na frameworku [twisted matrix](https://twistedmatrix.com/trac/) a funguje na bázi [reactoru](https://twistedmatrix.com/documents/13.1.0/core/howto/reactor-basics.html).

## 2. Komunikační vlákno
Komunikační vlákno [connectionmain.py], představuje proxy server mezi klientem a robotem doplněný o správu a kontrolu komunikace. Komunikaci mezi web klientem a komunikačním vláknem zajištuje navržený protokol [Remote web protocol](TODO), kde jsou zprávy přenášené pomocí websoketů. Komunikace mezi komunikačním vláknem a robotem je navržená podle stejného protokolu [Remote robots protocol](TODO) a zprávy jsou přenášené pomocí TCP/IP socketů. Zprávy určené pro robota jsou založené na [rosbridge v2 protocol](ROSBRIDGE_PROTOCOL.md) který je založený na JSON formáte.

## 3. Video stream
Poslední částí serveru je vlákno, které zajišťuje video stream [streamserver.py]. Od webového klienta očekává HTTP/GET [webstream protocol](TODO) hlavičku s přesně specifikovaným uzlem a parametry se kterými sa má video zpracovat. Tuto hlavičku dále server odešle procesu [video](TODO), který na robotovi zajištuje distribuci videostreamu a jeho úpravu.

# Server protocol [server.py](server.py)
Protokol serveru je rozdělený na tři části mezi klienty což jsou web, robot a podprocesy sloužící ke komunikaci. 
Základní strukturu zpráv tvoří trojice
```
WHAT:WHO|PARAMS
```
* **WHO** - rozlišuje od koho zpráva pochází, a která část protokolu se má použít
* **WHAT** - definuje požadavek klienta, na který reaguje server
* **PARAMS** - jsou specifické parametry pro jednotlivé požadavky
```
STARTWORKING:WEBCLIENT|xtichy09|xrobot00
```

# Packages
* **[server.py](server.py)** - hlavní proces
* **[connectionmain.py](connectionmain.py)** - komunikační vlákno
* **[streamserver.py](streamserver.py)** - vlákno určené k přenosu videa
* **[webportal.py](webportal.py)** - balíček obsahuje definici objektů
* **[database.sql](database.sql)** - databáze se startovacími datami

#### Clients
* [WEB](WEB)
* [ROBOT](ROBOT)

# Installation
Prvním krokem je instalace všech potřebných závislostí ke spuštění hlavního vlákna, webového klienta a databáze. 
## Server.py
* **[twisted matrix](https://twistedmatrix.com/trac/)** - python-twisted | 13.2.0-1ubuntu1
* **json**
* **threading**
* **socket**
* **[MySQLdb](https://github.com/farcepest/MySQLdb1)** - python-mysqldb | 1.2.3-2ubuntu1 | amd64
* **subprocess** 

## Web a databáze
* **PHP5** -  php5 | 5.5.9+dfsg-1ubuntu4.5
* **MySQL** - mysql-server-5.5 | 5.5.40-0ubuntu0.14.04.1 | amd64
* **Apache** - apache2 | 2.4.7-1ubuntu4.1 | amd64
* **phpMyAdmin**
## Instalace serveru
Vytvorříme si složku, kde chceme mít zdrojové kódy serveru.
```
mkdir remote_robots_server
cd remote_robots_server
wget https://github.com/xtichy09/Remote-robots-ROBOFIT/tree/master/SERVER
```
Pŕes aplikaci phpMyAdmin importujeme databázi na server. 

## Instalace webového klienta
Po správném nastavení apache zkopírujeme zdrojové kódy webového klienta do složky WWW.
```
wget https://github.com/xtichy09/Remote-robots-ROBOFIT/tree/master/WEB
```

Nyní je server připravený na spuštění.


## Running
* Spuštění servru
```
./server.py PORT
----------------
./server.py 9000
```

* **PORT** - port na kterém naslouchá server, standardně jsem zvolil port 9000, ale jinak je možné zvolit kterýkoliv volný port

#### Resources
TODO



