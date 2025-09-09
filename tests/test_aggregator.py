import pytest
from app.aggregator import add_event, get_user_event_counts, get_action_counts, get_latest_timestamp_per_user
from app.models import Event

@pytest.fixture(autouse=True)
def clear_events():
    # Clear EVENTS list before each test
    from app.aggregator import EVENTS
    EVENTS.clear()
    
def test_add_event_and_user_counts():
    e1 = Event(user_id="alice", action="login", timestamp="2023-10-01T12:00:00Z")
    e2 = Event(user_id="bob", action="logout", timestamp="2023-10-01T12:05:00Z")
    e3 = Event(user_id="james", action="purchase", timestamp="2023-10-01T12:10:00Z")
    
    add_event(e1)
    add_event(e2)
    add_event(e3)
    
    user_counts = get_user_event_counts()
    assert user_counts["alice"] == 1
    assert user_counts["bob"] == 1
    assert user_counts["james"] == 1
    
def test_action_counts():
    e1 = Event(user_id="alice", action="login", timestamp="2023-10-01T12:00:00Z")
    e2 = Event(user_id="bob", action="logout", timestamp="2023-10-01T12:05:00Z")
    e3 = Event(user_id="james", action="purchase", timestamp="2023-10-01T12:10:00Z")
    e4 = Event(user_id="alice", action="login", timestamp="2023-10-01T12:15:00Z")
    
    add_event(e1)
    add_event(e2)
    add_event(e3)
    add_event(e4)
    
    action_counts = get_action_counts()
    assert action_counts["login"] == 2
    assert action_counts["logout"] == 1
    assert action_counts["purchase"] == 1
    
def test_latest_timestamp_per_user():
    e1 = Event(user_id="alice", action="login", timestamp="2023-10-01T12:00:00Z")
    e2 = Event(user_id="bob", action="logout", timestamp="2023-10-01T12:05:00Z")
    e3 = Event(user_id="alice", action="purchase", timestamp="2023-10-01T12:10:00Z")
    
    add_event(e1)
    add_event(e2)
    add_event(e3)
    
    latest_timestamps = get_latest_timestamp_per_user()
    assert latest_timestamps["alice"] == "2023-10-01T12:10:00Z"
    assert latest_timestamps["bob"] == "2023-10-01T12:05:00Z"