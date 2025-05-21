ENG
 FastAPI-Celery-Redis Project
    
📖 Overview
This project showcases a lightweight application demonstrating the seamless integration of FastAPI, Celery, Redis, Flower, and PostgreSQL. The core functionality revolves around generating random items with random quantities and automatically saving them to a PostgreSQL database on a scheduled date using Celery tasks. Redis serves as the message broker and result backend, while Flower provides a sleek interface for task visualization.

🛠️ Technologies Used

FastAPI 🚀: A modern, high-performance web framework for building APIs with Python.
Celery ⏳: A distributed task queue for handling asynchronous tasks and scheduling.
Redis ⚡: An in-memory data store used as a message broker and result backend for Celery.
Flower 🌸: A web-based tool for monitoring and managing Celery tasks.
PostgreSQL 🗄️: A robust, open-source relational database for storing application data.


🔍 Core Functionality
The application:

Generates random items (item name(number)).
Schedules these items to be saved into a PostgreSQL database on a specified date.
Uses Celery workers with Redis as the message broker to process tasks.
Employs Celery Beat for task scheduling.
Provides a Flower dashboard for real-time task monitoring and visualization.


🚀 Setup and Running the Project
Follow these steps to get the project up and running:
1. Start Redis with Docker
Launch a Redis container using Docker:
docker run -d -p 6379:6379 --name redis redis

2. Run the Celery Worker
In one terminal, navigate to the project directory and start a Celery worker:
celery -A celery_worker worker --pool=solo --loglevel=info

3. Run Celery Beat
In a separate terminal, start Celery Beat for task scheduling:
celery -A celery_worker beat --loglevel=info

4. Run Flower for Task Visualization
In another terminal, launch Flower to monitor Celery tasks:
celery -A celery_worker flower

5. Access the Flower Dashboard
Open your browser and visit http://localhost:5555 to explore the Flower dashboard.

📝 Notes

Ensure Docker is installed and running before starting the Redis container.
The Celery worker and Celery Beat must run concurrently in separate terminals.
Verify that PostgreSQL is properly configured with the correct database connection settings in your FastAPI application.
Install required Python dependencies (fastapi, celery, redis, psycopg2) before running the project.

HRV
 FastAPI-Celery-Redis Projekt
    
📖 Pregled
Ovaj projekt demonstrira laganu aplikaciju koja prikazuje besprijekornu integraciju FastAPI-ja, Celery-ja, Redisa, Flower-a i PostgreSQL-a. Osnovna funkcionalnost uključuje generiranje nasumičnih stavki s nasumičnim količinama i njihovo automatsko spremanje u PostgreSQL bazu podataka na zakazani datum putem Celery zadataka. Redis služi kao posrednik poruka i pozadina za rezultate, dok Flower pruža elegantno sučelje za vizualizaciju zadataka.

🛠️ Korištene tehnologije

FastAPI 🚀: Moderan, visokoučinkovit web framework za izgradnju API-ja s Pythonom.
Celery ⏳: Distribuirani red zadataka za obradu asinkronih zadataka i zakazivanje.
Redis ⚡: Pohrana podataka u memoriji, korištena kao posrednik poruka i pozadina za rezultate Celery-ja.
Flower 🌸: Web-bazirani alat za praćenje i upravljanje Celery zadacima.
PostgreSQL 🗄️: Robusna relacijska baza podataka otvorenog koda za pohranu podataka aplikacije.


🔍 Osnovna funkcionalnost
Aplikacija:

Generira nasumične stavke s nasumičnim brojevima u nazivu.
Zakazuje spremanje tih stavki u PostgreSQL bazu podataka na određeni datum.
Koristi Celery radnike s Redisom kao posrednikom poruka za obradu zadataka.
Upotrebljava Celery Beat za zakazivanje zadataka.
Omogućuje Flower nadzornu ploču za praćenje zadataka u stvarnom vremenu.


🚀 Postavljanje i pokretanje projekta
Slijedite ove korake za pokretanje projekta:
1. Pokrenite Redis putem Dockera
Pokrenite Redis kontejner koristeći Docker:
docker run -d -p 6379:6379 --name redis redis

2. Pokrenite Celery radnika
U jednom terminalu, navigirajte do direktorija projekta i pokrenite Celery radnika:
celery -A celery_worker worker --pool=solo --loglevel=info

3. Pokrenite Celery Beat
U drugom terminalu, pokrenite Celery Beat za zakazivanje zadataka:
celery -A celery_worker beat --loglevel=info

4. Pokrenite Flower za vizualizaciju zadataka
U zasebnom terminalu, pokrenite Flower za praćenje Celery zadataka:
celery -A celery_worker flower

5. Pristupite Flower nadzornoj ploči
Otvorite preglednik i posjetite http://localhost:5555 za istraživanje Flower nadzorne ploče.

📝 Napomene

Provjerite je li Docker instaliran i pokrenut prije pokretanja Redis kontejnera.
Celery radnik i Celery Beat moraju raditi istovremeno u zasebnim terminalima.
Provjerite je li PostgreSQL ispravno konfiguriran s točnim postavkama veze s bazom podataka u vašoj FastAPI aplikaciji.
Instalirajte potrebne Python dependencije (fastapi, celery, redis, psycopg2) prije pokretanja projekta.

