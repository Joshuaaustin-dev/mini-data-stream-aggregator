# Implement Fast API server to handle event ingestion and metrics retrieval
from fastapi import FastAPI
from pydantic import BaseModel
from app.aggregator import (
    add_event,
    get_user_event_counts,
    get_action_counts,
    get_latest_timestamp_per_user,
)

app = FastAPI()

# Define event object
class Event(BaseModel):
    user_id: str
    action: str
    timestamp: str


@app.post("/events")
def ingest_event(event: Event):
    """
    Ingest a single event into the aggregator.
    """
    add_event(event.user_id, event.action, event.timestamp)
    return {"status": "success"}


@app.get("/metrics")
def fetch_metrics():
    """
    Retrieve all aggregated metrics.
    """
    return {
        "user_event_counts": get_user_event_counts(),
        "action_counts": get_action_counts(),
        "latest_timestamp_per_user": get_latest_timestamp_per_user(),
    }
