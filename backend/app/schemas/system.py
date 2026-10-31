from datetime import datetime
from typing import Dict, Optional

from pydantic import BaseModel


class DataStatusResponse(BaseModel):
    status: str
    last_successful_update: Optional[datetime] = None
    sources: Dict[str, str]
    checked_at: datetime
