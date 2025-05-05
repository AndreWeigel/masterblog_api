# Masterblog

Masterblog is a full-stack blog platform with a Flask-based backend and a simple frontend. It supports creating, reading, updating, deleting, and searching blog posts. The backend also provides a Swagger UI for API documentation.

---

## 🗂 Project Structure

```
.
├── backend/
│   ├── instance/
│   │   └── blog.db                 # SQLite database
│   ├── models/
│   │   └── post.py                 # SQLAlchemy model for blog posts
│   ├── services/
│   │   └── post_service.py         # Business logic for post handling
│   ├── static/
│   │   └── masterblog.json         # Swagger JSON definition
│   ├── backend_app.py              # Main Flask app
│   └── extensions.py               # DB and other extensions initialization
├── frontend/
│   ├── static/
│   │   ├── main.js                 # JS logic (if any)
│   │   └── styles.css              # CSS styles
│   ├── templates/
│   │   └── index.html              # HTML frontend entry
│   └── frontend_app.py             # Python entry for frontend (if needed)
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AndreWeigel/masterblog.git
cd masterblog
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python backend/backend_app.py
```

By default, the backend will be available at `http://localhost:5002`.

---

## 📋 API Endpoints

| Method | Endpoint                | Description                   |
|--------|-------------------------|-------------------------------|
| GET    | `/api/posts`            | List posts with pagination    |
| POST   | `/api/posts`            | Create a new post             |
| PUT    | `/api/posts/<id>`       | Update a post                 |
| DELETE | `/api/posts/<id>`       | Delete a post                 |
| GET    | `/api/posts/search`     | Search posts by title/content|

---

## 📖 API Documentation

Swagger UI is available at:

```
http://localhost:5002/api/docs
```

---

## 🗃 Database

This project uses SQLite. The database file is stored in `backend/instance/blog.db`.

---

## 📌 Notes

- CORS is enabled for all routes.
- All database logic is abstracted in the `PostService` class.
- Frontend files are placed under `frontend/`, though frontend functionality is minimal.

---

## 🛠 Tech Stack

- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Docs**: Swagger (OpenAPI)

---
