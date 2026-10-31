\# FireWatch AI — Agent Instructions



Перед изменениями прочитай SPEC.md. Работай по одной задаче из канбана.



\## Жёсткие правила

\- Только реальные данные NASA. Никаких моков, выданных за live.

\- Секреты только на сервере (.env), не в клиентском бандле.

\- Разделяй: наблюдение / статистика / аномалия / эвристический индекс / калиброванная вероятность.

\- Не называй эвристику вероятностью. Не заявляй о валидации модели без оценки.

\- Каждый UI-контрол должен реально работать.

\- Graceful degradation при недоступности NASA.

\- Тесты + миграции + README для каждой фичи.



\## Стек

Next.js App Router + TS strict, Tailwind, shadcn/ui, MapLibre GL, ECharts, TanStack Query, Zod.

FastAPI, SQLAlchemy 2.x, Alembic, PostgreSQL+PostGIS, Redis/Celery, pandas/numpy/scikit-learn.

Docker Compose, GitHub Actions, OpenAPI.



\## Процесс

\- Ветка: feat/<ID>-<slug> от main

\- Коммит: feat(scope): message (#ID)

