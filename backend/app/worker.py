from celery import Celery

from app.core.config import settings

celery_app = Celery(
    "firewatch",
    broker=settings.redis_url,
    backend=settings.redis_url,
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

# Alias expected by `celery -A app.worker`
app = celery_app
