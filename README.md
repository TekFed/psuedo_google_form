# Pseudo Google Forms

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![SurveyJS](https://img.shields.io/badge/SurveyJS-FF6F00?style=flat&logoColor=white)](https://surveyjs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**A clean, minimal, open-source clone/starter of Google Forms** built with **FastAPI** (backend) + **SurveyJS** (frontend).

Create beautiful forms with a drag-and-drop builder, share them, collect responses, and view results.

## ✨ Features

- Drag-and-drop form builder (Survey Creator) with many question types
- Responsive form filling experience (SurveyJS Form Library)
- Save forms to SQLite via FastAPI REST API
- List all created forms + quick actions (edit / fill / results)
- View responses with clean list + detail modal
- Modern UI with Tailwind CSS (no Node.js / build step required)
- CORS enabled — works when opening HTML files directly from disk
- Error handling + debug panel on fill page

## 📸 Screenshots

Here are some quick glimpses of the app in action:

<div align="center">
  <table>
    <tr>
      <td><b>Form Builder</b></td>
      <td><b>Fill Form</b></td>
      <td><b>Results View</b></td>
    </tr>
    <tr>
      <td>
        <img src="https://raw.githubusercontent.com/TekFed/psuedo_google_form/screenshots/home.png" alt="Form Builder Interface" width="320"/>
      </td>
      <td>
        <img src="https://raw.githubusercontent.com/TekFed/psuedo_google_form/screenshots/desktop_preview.png" alt="Form Filling Page" width="320"/>
      </td>
      <td>
        <img src="https://raw.githubusercontent.com/TekFed/psuedo_google_form/screenshots/responses.png" alt="Responses & Results Page" width="320"/>
      </td>
    </tr>
  </table>
</div>

## 🛠 Tech Stack

| Layer       | Technology                              | Notes                              |
|-------------|-----------------------------------------|------------------------------------|
| Backend     | FastAPI, SQLAlchemy, Pydantic, SQLite   | Async-ready, auto docs at /docs    |
| Frontend    | SurveyJS (Creator + Core), Tailwind CDN | Vanilla JS, no framework           |
| Database    | SQLite (file-based)                     | Zero setup                         |
| Deployment  | Ready for Railway / Render / Fly.io     | Or local with uvicorn              |

## 📁 Project Structure

```
pseudo-google-forms/
├── backend/
│   ├── main.py             # FastAPI app + endpoints
│   ├── models.py           # SQLAlchemy models
│   ├── schemas.py          # Pydantic schemas
│   ├── database.py         # DB setup
│   └── requirements.txt
├── frontend/
│   ├── index.html          # Form builder + My Forms list
│   ├── fill.html           # Form filling page (?id=...)
│   ├── results.html        # View responses page (?id=...)
│   └── style.css           # Optional custom styles
├── screenshots/            # Add your images here!
└── README.md
```

## 🚀 Quick Start (2 minutes)

### 1. Backend

```bash
cd backend

# Recommended: virtual environment
python -m venv venv
# Windows:   venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

pip install -r requirements.txt

# Start server (auto-reload on changes)
uvicorn main:app --reload --port 8000
```

→ API will be available at http://127.0.0.1:8000  
→ Interactive docs: http://127.0.0.1:8000/docs

### 2. Frontend

Just open any of these files in your browser:

- Builder + form list: `frontend/index.html`
- Fill a form:       `frontend/fill.html?id=1`  
- View results:      `frontend/results.html?id=1`

No server needed for frontend — it talks directly to the backend via fetch.

## 🎯 How to Use

1. Open `index.html`  
2. Click **New Form** → build your form visually  
3. Click **Save Survey** (top toolbar) → get form ID  
4. Fill: open `fill.html?id=YOUR_ID`  
5. View responses: open `results.html?id=YOUR_ID` or click **Results** in My Forms

## 📡 API Endpoints (main ones)

| Method | Path                            | Description                     |
|--------|---------------------------------|---------------------------------|
| POST   | `/api/forms`                    | Create form                     |
| GET    | `/api/forms`                    | List all forms                  |
| GET    | `/api/forms/{id}`               | Get form JSON                   |
| PUT    | `/api/forms/{id}`               | Update form                     |
| POST   | `/api/forms/{id}/responses`     | Submit answers                  |
| GET    | `/api/forms/{id}/responses`     | Get all responses for form      |

Full Swagger UI → `/docs`

## ⚡ Troubleshooting

- **"Form not found" on fill page** → Make sure backend is running (`uvicorn`)  
- **CORS / fetch errors** → Backend must be on http://127.0.0.1:8000  
- **Database reset** → Delete `backend/forms.db`  
- **SurveyJS styling broken** → Hard refresh (Ctrl+Shift+R)

## 🔮 Next Steps / Ideas to Extend

- Add user authentication (FastAPI Users / JWT)
- Public / shareable links with short UUIDs
- Export responses → CSV / Google Sheets
- Basic charts on results page (Chart.js)
- Custom themes / branding
- Deploy frontend (Netlify / Vercel) + backend (Railway / Render)

## 📄 License

MIT License — free to use and modify.

## ❤️ Acknowledgments

- [SurveyJS](https://surveyjs.io) — amazing open-source form engine
- FastAPI team
- Tailwind CSS (via CDN — zero build!)

Built with help from Grok and lots of ☕· March 2026
