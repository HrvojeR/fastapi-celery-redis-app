# 🌟 FastAPI-Celery-Redis Project (ENG)

## 📖 Overview

This lightweight application showcases seamless integration of **FastAPI**, **Celery**, **Redis**, **Flower**, and **PostgreSQL**.

The core feature is generating random items and scheduling them to be saved into a PostgreSQL database.

---

## 🛠️ Technologies Used

- **FastAPI** 🚀 – Modern web framework for APIs  
- **Celery** ⏳ – Distributed task queue  
- **Redis** ⚡ – Message broker & result backend  
- **Flower** 🌸 – Task monitoring dashboard  
- **PostgreSQL** 🗄️ – Relational database  

---

## 🔍 Core Features

✅ Generate random items (e.g. `Item123`)  
✅ Schedule saving to PostgreSQL on a scheduled interval
✅ Celery workers handle tasks asynchronously via Redis  
✅ Use **Celery Beat** for recurring or scheduled tasks  
✅ Visual task tracking with **Flower**

---

## 🚀 Setup & Run

### 1. Start Redis via Docker

```bash
docker run -d -p 6379:6379 --name redis redis
```

### 2. Run Celery Worker

```bash
celery -A celery_worker worker --pool=solo --loglevel=info
```

### 3. Run Celery Beat

```bash
celery -A celery_worker beat --loglevel=info
```

### 4. Run Flower Dashboard

```bash
celery -A celery_worker flower
```

Visit: [http://localhost:5555](http://localhost:5555)

---

## 📝 Notes

- Ensure **Docker** is installed and running  
- Celery worker and beat must run **in separate terminals**  
- Configure your **PostgreSQL URI** in the FastAPI app  
- Install required dependencies:

```bash
pip install fastapi celery redis psycopg2
```

---

# 🌟 FastAPI-Celery-Redis Projekt(HRV)

## 📖 Pregled

Ova lagana aplikacija prikazuje besprijekornu integraciju **FastAPI-ja**, **Celery-ja**, **Redisa**, **Flower-a** i **PostgreSQL-a**.

Osnovna funkcionalnost je generiranje nasumičnih stavki i njihovo zakazano spremanje u PostgreSQL bazu podataka.

---

## 🛠️ Korištene Tehnologije

- **FastAPI** 🚀 – Moderan web framework za API-je  
- **Celery** ⏳ – Distribuirani red zadataka  
- **Redis** ⚡ – Posrednik poruka i pozadina za rezultate  
- **Flower** 🌸 – Nadzorna ploča za zadatke  
- **PostgreSQL** 🗄️ – Relacijska baza podataka  

---

## 🔍 Osnovna Funkcionalnost

✅ Generira nasumične stavke (npr. `Item123`)  
✅ Zakazuje spremanje u PostgreSQL na određeni datum  
✅ Celery radnici asinkrono obrađuju zadatke putem Redisa  
✅ Koristi **Celery Beat** za zakazane ili ponavljajuće zadatke  
✅ Omogućuje vizualno praćenje zadataka pomoću **Flower-a**

---

## 🚀 Postavljanje i Pokretanje

### 1. Pokreni Redis putem Dockera

```bash
docker run -d -p 6379:6379 --name redis redis
```

### 2. Pokreni Celery Radnika

```bash
celery -A celery_worker worker --pool=solo --loglevel=info
```

### 3. Pokreni Celery Beat

```bash
celery -A celery_worker beat --loglevel=info
```

### 4. Pokreni Flower nadzornu ploču

```bash
celery -A celery_worker flower
```

Posjeti: [http://localhost:5555](http://localhost:5555)

---

## 📝 Napomene

- Provjeri da je **Docker** instaliran i pokrenut  
- Celery radnik i Beat moraju raditi **u zasebnim terminalima**  
- Ispravno konfiguriraj **PostgreSQL vezu** u FastAPI aplikaciji  
- Instaliraj potrebne biblioteke:

```bash
pip install fastapi celery redis psycopg2
```

Created with dedication by Nebra98 and HrvojeR
