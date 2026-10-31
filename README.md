# FireWatch AI

Geospatial platform for monitoring active wildfires, risk analysis and historical fire activity based on real NASA data.

This repository contains the scaffold (F-01/F-02): project structure, Docker Compose, FastAPI backend, Next.js frontend, PostgreSQL/PostGIS, Redis/Celery, Alembic migrations and baseline tests.

## Requirements

- Docker Desktop (with Docker Compose v2)
- Git

No local Python/Node installation is required; everything runs in containers.

## Quick start

1. Copy environment file:

   ```bash
   cp .env.example .env
   ```

   On Windows (PowerShell):

   ```powershell
   Copy-Item .env.example .env
   ```

2. Build and start all services:

   ```bash
   docker compose up --build
   ```

3. Open:

   - Frontend: http://localhost:3000
   - Backend API docs: http://localhost:8000/api/v1/docs
   - Health: http://localhost:8000/api/v1/health
   - Data status: http://localhost:8000/api/v1/system/data-status

## Services

| Service | Port | Description |
|---|---|---|
| frontend | 3000 | Next.js app |
| backend | 8000 | FastAPI API |
| db | 5432 | PostgreSQL + PostGIS |
| redis | 6379 | Redis for Celery |
| worker | - | Celery worker + beat |

## Migrations

Migrations run automatically on backend startup (`alembic upgrade head`).

Manual:

```bash
docker compose exec backend alembic upgrade head
docker compose exec backend alembic downgrade -1
```

## Tests

Backend:

```bash
docker compose exec backend pytest -q
```

Frontend (inside container or locally with Node 20):

```bash
docker compose exec frontend npm run test
docker compose exec frontend npm run typecheck
```

## Project structure

```
.
├── backend/          # FastAPI, SQLAlchemy, Alembic, Celery
├── frontend/         # Next.js (App Router, TS, Tailwind, shadcn/ui)
├── docker-compose.yml
├── .env.example
└── .github/workflows/ci.yml
```

## Configuration

Secrets stay server-side. `FIRMS_MAP_KEY` (NASA FIRMS) must be set in `.env` only; it is never exposed to the browser. Current scaffold keeps data connectors as `not_configured` until implemented (F-03+).

## Notes

- Graceful degradation: if NASA APIs are unavailable, the app keeps showing last known state with a freshness timestamp.
- Heuristic indices are never labeled as probabilities.
- This is an educational/research platform, not an operational emergency system.
