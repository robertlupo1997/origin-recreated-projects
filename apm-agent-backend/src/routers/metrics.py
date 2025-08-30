from fastapi import APIRouter, Query
from pydantic import BaseModel
from typing import List, Optional
import time
import random

router = APIRouter()

class MetricData(BaseModel):
    timestamp: int
    value: float
    labels: dict

class MetricsResponse(BaseModel):
    metric_name: str
    data: List[MetricData]

@router.get("/metrics", response_model=List[MetricsResponse])
async def get_metrics(
    service: Optional[str] = Query(None, description="Service name filter"),
    hours: int = Query(24, description="Hours of data to return")
):
    current_time = int(time.time())
    metrics = []
    
    for metric_name in ["response_time", "error_rate", "throughput"]:
        data = []
        for i in range(hours):
            timestamp = current_time - (i * 3600)
            value = random.uniform(0.1, 100.0) if metric_name == "response_time" else random.uniform(0, 1)
            data.append(MetricData(
                timestamp=timestamp,
                value=value,
                labels={"service": service or "demo-service", "environment": "production"}
            ))
        
        metrics.append(MetricsResponse(metric_name=metric_name, data=data))
    
    return metrics