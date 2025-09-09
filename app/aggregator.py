from typing import List
from app.models import Event

#In-memory storage
EVENTS: List[Event] = []

def add_event(event):
    """Add an event to the in-memory storage"""
    EVENTS.append(event)
    
def get_user_event_counts():
    """Return count of events per user as a dictionary"""
    counts = {}
    for e in EVENTS:
        counts[e.user_id] = counts.get(e.user_id, 0) + 1
    return counts

def get_action_counts():
    """Return count of each action type"""
    counts = {}
    for e in EVENTS:
        counts[e.action] = counts.get(e.action, 0) + 1
    return counts

def get_latest_timestamp_per_user():
    """Return the most recent timestamp for each user"""
    latest = {}
    for e in EVENTS:
        if (e.user_id not in latest) or (e.timestamp > latest[e.user_id]):
            latest[e.user_id] = e.timestamp
    return latest