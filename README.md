# 🤖 Sebastian chatBot 

Este proyecto es un asistente de texto enfocado en brindar información sobre GitHub Copilot.

## **Índice**
- [Autores](#autores)
- [Aspectos Técnicos](#aspec-tech)
    - [Acerca de NTKL](#ntkl)
- [Guía de instalación](#guía-de-instalación)
    - [Paso 1](#paso-1)
    - [Paso 2](#paso-2)
    - [Paso 3](#paso-3)
    - [Paso 4](#paso-4)
    - [Paso 5](#paso-5)
    - [Paso 6](#paso-6)




## Integrantes 
<div id='autores' />
Este chatbot fue realizado por las siguientes personas:

* Ricardo Contreras Garzón @RickContreras

* Sara Galván Ortega @galvanic90

* Daniel León Danzo @DainXOR

Estudiantes de pregrado en Ingeniería de sistemas de la Universidad de Antioquia.

## Aspectos técnicos
<div id='aspec-tech' />

Sebastian fué elaborado utilizadndo Python 🐍 como lenguaje de programación. Además se empleó la librería:

* [ChatterBot](https://chatterbot.readthedocs.io/en/stable/) 

A su vez, Chatter emplea las siguientes librerías para funcionar:

* click==8.1.7
* flexcache==0.3
* flexparser==0.4
* joblib==1.4.2
* mathparse==0.1.2
* nltk==3.9.1
* Pint==0.24.4
* platformdirs==4.3.6
* pymongo==3.13.0
* python-dateutil==2.7.5
* pytz==2024.2
* PyYAML==3.13
* regex==2024.11.6
* six==1.16.0
* SQLAlchemy==1.2.19
* tqdm==4.67.0
* typing_extensions==4.12.2

De las cuales una de las más impotantes es [NLTK](https://www.nltk.org/)

### Acerca de NLTK 
<div id='ntkl' />

NLTK es una plataforma líder para crear programas Python que trabajen con datos del lenguaje humano. Proporciona interfaces fáciles de usar para más de 50 corpus y recursos léxicos como WordNet, junto con un conjunto de bibliotecas de procesamiento de texto para clasificación, tokenización, derivación, etiquetado, análisis y razonamiento semántico, contenedores para bibliotecas de procesamiento de lenguaje natural de nivel industrial y un foro de discusión activo.

## Guía de instalación
<div id='inst' />

Para usar Sebastian chatbot siga las siguientes instrucciones. 

### Paso 1
<div id='p1' />

Clonar este repositorio de GitHub, para clonar este repositorio escriba este comando en la terminal de su computador

```bash
git clone git@github.com:galvanic90/chatBot.git
```

### Paso 2
<div id='p2' />
Muévase al directorio que acaba de descargar de GitHub

```bash
cd chatBot
```

### Paso 3
<div id='p3' />
Cree un ambiente virtual de python, esto es importante para evitar colisiones entre diferentes versiones de la misma librería en su máquina, para esto ejecute el siguiente comando [^1] 

```bash
python3 -m venv .venv
```

[^1]: Antes de ejecutar este comando, verifique que tenga previamente instalada la librería [VENV](https://docs.python.org/3/library/venv.html) de python. También debe asegurarse que tenga previamente instalado una versión de python => 3.9

### Paso 4
<div id='p4' /> 
Activación del ambiente virtual de python.

```bash
source .venv/bin/activate
```
Para saber si ha activado el ambiente virtual de manera exitosa, en la terminal el promt debe verse similar a esto:

```bash
(.venv) user_name:~/chatBot$
```

### Paso 5 
<div id='p5' />
Instalación de las dependencias

```bash
pip install -r requirenments.txt
```

### Paso 6 
<div id='p6' />
Ejecución del script del chat

```bash
python3 bot.py
```

Si este último comando se ejecuta sin errores, entonces podrá interactuar con Sebastian chatbot, podría probar con un saludo :smile 

![img-ejemplo](/assets/Captura%20desde%202024-11-18%2010-39-48.png)

