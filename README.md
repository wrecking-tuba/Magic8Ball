# Magic 8 Ball (Flask)

A simple, responsive **Magic 8 Ball** web app built with **Flask + HTML/CSS/JS**.  
Type a yes/no question, click **Ask**, and the ball “shakes” before revealing a random answer.

---

## Demo
Run locally and open: `http://127.0.0.1:5000`

---

## Features
- Clean UI with a “glass” card layout + animated shake effect
- Single-page experience (AJAX) — no full page reload on submit
- Simple JSON API endpoint for answers
- Mobile-friendly responsive layout

---

## Tech Stack
- **Backend:** Python, Flask  
- **Frontend:** HTML (Jinja template), CSS, Vanilla JavaScript

---

## Project Structure
```txt
Magic8Ball/
├─ app.py
├─ templates/
│  └─ index.html
└─ static/
   └─ style.css
```

---

## Getting Started (Local Setup)

### 1) Clone the repo
```bash
git clone <your-repo-url>
cd Magic8Ball
```

### 2) Create & activate a virtual environment (recommended)

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3) Install dependencies
If you don’t have a `requirements.txt`, install Flask directly:
```bash
pip install Flask
```

(Optional) Create `requirements.txt`:
```txt
Flask>=2.0
```

### 4) Run the app
```bash
python app.py
```

Then open: `http://127.0.0.1:5000`

---

## API

### `POST /api/ask`
Returns a random Magic 8 Ball response.

**Request (JSON)**
```json
{ "question": "Will I get the job?" }
```

**Response (JSON)**
```json
{ "question": "Will I get the job?", "answer": "Outlook good." }
```

**cURL example**
```bash
curl -X POST http://127.0.0.1:5000/api/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"Will I be happy tomorrow?"}'
```

---

## Roadmap / Improvements (Ideas)
- Add the full classic 8-ball answer set (positive / neutral / negative)
- Keep question history (session or local storage)
- Add keyboard submit + accessibility tweaks
- Add unit tests for the API endpoint

---
