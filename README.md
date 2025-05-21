# 🌟 FastAPI-Celery-Redis Project

<sub>ENG / HRV</sub>

## 📖 Overview / Pregled

This lightweight application showcases seamless integration of **FastAPI**, **Celery**, **Redis**, **Flower**, and **PostgreSQL**.  
Ova lagana aplikacija prikazuje besprijekornu integraciju **FastAPI-ja**, **Celery-ja**, **Redisa**, **Flower-a** i **PostgreSQL-a**.

The core feature is generating random items and scheduling them to be saved into a PostgreSQL database.  
Osnovna funkcionalnost je generiranje nasumičnih stavki i njihovo zakazano spremanje u bazu podataka.

---

## 🛠️ Technologies Used / Korištene tehnologije

- **FastAPI** 🚀 – Modern web framework for APIs / Moderan web framework za API-je  
- **Celery** ⏳ – Distributed task queue / Distribuirani red zadataka  
- **Redis** ⚡ – Message broker & result backend / Posrednik poruka i pozadina za rezultate  
- **Flower** 🌸 – Task monitoring dashboard / Nadzorna ploča za zadatke  
- **PostgreSQL** 🗄️ – Relational database / Relacijska baza podataka  

---

## 🔍 Core Features / Osnovna funkcionalnost

✅ Generate random items (e.g. `Item123`)  
✅ Schedule saving to PostgreSQL on a specific date  
✅ Celery workers handle tasks asynchronously via Redis  
✅ Use **Celery Beat** for recurring or scheduled tasks  
✅ Visual task tracking with **Flower**

---

## 🚀 Setup & Run / Postavljanje i pokretanje

### 1. Start Redis via Docker / Pokreni Redis putem Dockera

```bash
docker run -d -p 6379:6379 --name redis redis
```

### 2. Run Celery Worker / Pokreni Celery radnika

```bash
celery -A celery_worker worker --pool=solo --loglevel=info
```

### 3. Run Celery Beat / Pokreni Celery Beat

```bash
celery -A celery_worker beat --loglevel=info
```

### 4. Run Flower Dashboard / Pokreni Flower nadzornu ploču

```bash
celery -A celery_worker flower
```

Visit / Posjeti: [http://localhost:5555](http://localhost:5555)

---

## 📝 Notes / Napomene

- Ensure **Docker** is installed and running  
  Provjeri da je Docker instaliran i pokrenut  
- Celery worker and beat must run **in separate terminals**  
  Celery radnik i Beat moraju raditi u **zasebnim terminalima**  
- Configure your **PostgreSQL URI** in the FastAPI app  
  Ispravno konfiguriraj **PostgreSQL vezu** u aplikaciji  
- Install required dependencies:  
  Instaliraj potrebne biblioteke:

```bash
pip install fastapi celery redis psycopg2
```

---

✅ Ready to scale async jobs with FastAPI + Celery + Redis + PostgreSQL!  
✅ Spreman za skaliranje asinkronih zadataka uz FastAPI + Celery + Redis + PostgreSQL!
