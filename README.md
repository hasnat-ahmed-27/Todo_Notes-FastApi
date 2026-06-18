# 📝 Todo Notes — FastAPI

> **Day 3 Task** | Adept Tech Solutions — AI Engineering Internship Program

A personal notes API built with **FastAPI** — create, read, update, delete and search notes. Includes a glassmorphism frontend, custom middleware, nginx reverse proxy config, and ngrok internet exposure.

---

## 🚀 Live Demo

> Run locally and expose via ngrok (see setup below)

---

## 📁 Project Structure

```
Todo_Notes-FastApi/
├── main.py               # App entry point — wires everything together
├── core/
│   └── config.py         # Reads .env, shares settings across app
├── routers/
│   └── notes_router.py   # HTTP routes (GET, POST, PATCH, DELETE)
├── services/
│   └── notes_service.py  # All business logic (create, update, delete, search)
├── schemas/
│   └── note_schema.py    # Pydantic models — request/response validation
├── models/
│   └── note_model.py     # Note dataclass (in-memory data layer)
├── middleware/
│   └── logging_middleware.py  # Logs every request with method, path, status, time
├── utils/
│   └── helpers.py        # Reusable helper functions
├── static/
│   └── index.html        # Glassmorphism frontend (Plus Jakarta Sans)
├── nginx.conf            # Production reverse proxy configuration
└── requirements.txt      # Pinned dependencies
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/hasnat-ahmed-27/Todo_Notes-FastApi.git
cd Todo_Notes-FastApi
```

### 2. Create virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / Mac
python3 -m venv venv
source venv/bin/activate
```

> **Why virtual environment?** Isolates project dependencies from system Python — prevents version conflicts.

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 🌐 Access

| URL | Description |
|-----|-------------|
| `http://localhost:8000` | Frontend UI |
| `http://localhost:8000/docs` | Swagger UI — test all endpoints |
| `http://localhost:8000/redoc` | ReDoc documentation |
| `http://localhost:8000/health` | Health check |

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/api/v1/notes/` | Create a new note |
| `GET` | `/api/v1/notes/` | Get all notes (newest first) |
| `GET` | `/api/v1/notes/?search=keyword` | Search notes by title or content |
| `GET` | `/api/v1/notes/{id}` | Get a single note by ID |
| `PATCH` | `/api/v1/notes/{id}` | Partially update a note |
| `DELETE` | `/api/v1/notes/{id}` | Delete a note |

### Example Request
```json
POST /api/v1/notes/

{
  "title": "FastAPI Day 3",
  "content": "Learned about routers, schemas, middleware and services.",
  "tags": ["internship", "fastapi"]
}
```

### Example Response
```json
{
  "id": "abc-123-def-456",
  "title": "FastAPI Day 3",
  "content": "Learned about routers, schemas, middleware and services.",
  "tags": ["internship", "fastapi"],
  "created_at": "2026-06-17T10:00:00",
  "updated_at": "2026-06-17T10:00:00"
}
```

---

## 🌍 Expose to Internet (ngrok)

Open a second terminal and run:
```bash
ngrok http 8000
```

Copy the `https://xxxx.ngrok-free.app` URL — your API is now live on the internet.

---

## 🔧 Nginx (Production Bonus)

For production deployment on a Linux server:

```bash
# Install nginx
sudo apt install nginx

# Copy config
sudo cp nginx.conf /etc/nginx/sites-available/notesapi
sudo ln -s /etc/nginx/sites-available/notesapi /etc/nginx/sites-enabled/

# Test and reload
sudo nginx -t
sudo systemctl reload nginx
```

Nginx acts as a reverse proxy — sits in front of Uvicorn on port 80, forwards traffic to FastAPI on port 8000.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **FastAPI** | Python web framework |
| **Uvicorn** | ASGI server |
| **Pydantic** | Data validation and schemas |
| **Python-dotenv** | Environment variable management |
| **Nginx** | Production reverse proxy |
| **ngrok** | Internet tunnel for local server |

---

## 🎨 Frontend

- **Glassmorphism** design with green accent theme
- **Plus Jakarta Sans** — modern startup font
- **DM Mono** — technical monospace for dates, tags, logo
- Real-time **search**, **char/word counter**, toast notifications
- Fully connected to the FastAPI backend via `fetch()`

---

## 👨‍💻 Author

**Hasnat Ahmed**
AI Engineering Intern — Adept Tech Solutions
BS Artificial Intelligence — PAF-IAST
