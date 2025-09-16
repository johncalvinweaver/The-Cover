# The Cover

A modern, responsible, and transparent sports odds/projection API and reference UI.

## Features

- Mock odds, projections, and line movement endpoints (OpenAPI documented)
- Static UI preview
- Roadmap and compliance documentation
- Professional structure for rapid MVP development

## Quickstart

1. **Mock API**:  
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn app:app --reload
   ```
   Serves OpenAPI docs at `http://localhost:8000/docs`.

2. **Static UI**:  
   Open `static/index.html` in your browser.

## Directory Structure

- `api/` — OpenAPI spec
- `backend/` — Mock API server (FastAPI)
- `static/` — UI mockup
- `docs/` — Compliance, data sourcing, responsible gaming, etc.

## Roadmap

See [ROADMAP.md](ROADMAP.md)