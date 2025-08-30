from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

router = APIRouter()

class AlertStatus(str, Enum):
    ACTIVE = "active"
    RESOLVED = "resolved"
    ACKNOWLEDGED = "acknowledged"

class AlertSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class Alert(BaseModel):
    id: str
    title: str
    description: str
    severity: AlertSeverity
    status: AlertStatus
    service: str
    created_at: int
    updated_at: int

@router.get("/alerts", response_model=List[Alert])
async def get_alerts(
    status: Optional[AlertStatus] = Query(None, description="Filter by status"),
    severity: Optional[AlertSeverity] = Query(None, description="Filter by severity")
):
    import time
    current_time = int(time.time())
    
    alerts = [
        Alert(
            id="alert-001",
            title="High Response Time",
            description="Average response time exceeded 500ms threshold",
            severity=AlertSeverity.HIGH,
            status=AlertStatus.ACTIVE,
            service="api-gateway",
            created_at=current_time - 3600,
            updated_at=current_time - 1800
        ),
        Alert(
            id="alert-002", 
            title="Error Rate Spike",
            description="Error rate increased to 5.2% in the last 15 minutes",
            severity=AlertSeverity.CRITICAL,
            status=AlertStatus.ACKNOWLEDGED,
            service="payment-service",
            created_at=current_time - 900,
            updated_at=current_time - 600
        )
    ]
    
    filtered_alerts = alerts
    if status:
        filtered_alerts = [a for a in filtered_alerts if a.status == status]
    if severity:
        filtered_alerts = [a for a in filtered_alerts if a.severity == severity]
    
    return filtered_alerts