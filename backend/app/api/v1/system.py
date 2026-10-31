from datetime import datetime, timezone

from fastapi import APIRouter

from app.schemas.system import DataStatusResponse

router = APIRouter()


@router.get("/system/data-status", response_model=DataStatusResponse)
def data_status() -> DataStatusResponse:
    # Scaffold: real ingestion status will be wired in later feature (F-03+).
    return DataStatusResponse(
        status="ok",
        last_successful_update=None,
        sources={"nasa_firms": "not_configured", "nasa_eonet": "not_configured"},
        checked_at=datetime.now(timezone.utc),
    )
