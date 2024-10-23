from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware
from dataModel import Event

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

clients: List[WebSocket] = []
events: Dict[int, Event] = {}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    '''
    Websocket endpoint to make a ws connection
    '''
    await websocket.accept()
    clients.append(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        clients.remove(websocket)

async def broadcast_event(event, action):
    '''
    Send broadcast event to all clients
    params:-
        event:`Event`
        action: str
    '''
    message = {"action": action, "event": event.dict()}
    for client in clients:
        await client.send_json(message)

@app.post("/api/create-event/")
async def create_event(event: Event):
    '''
    Create a new event
    '''
    event_id = len(events) + 1
    event.id = event_id
    events[event_id] = event
    await broadcast_event(event, "new_event")  
    return {"message": "Event created", "event_id": event_id}

@app.post("/api/join-event/{event_id}")
async def join_event(event_id: int, username: str):
    '''
    Join a event
    params:-
        event_id: int
        username: str
    '''
    if event_id in events:
        events[event_id].joiners.append(username)
        await broadcast_event(events[event_id], "update_event")
        return {"message": f"{username} joined event {event_id}"}
    return {"error": "Event not found"}

@app.get("/api/events")
async def get_events():
    '''
    Get all events
    '''
    return list(events.values())

@app.delete("/api/unattend-event/{event_id}")
async def unattend_event(event_id:int, username: str):
    '''
    Un-attend event
    params:-
        event_id: int
        username: str
    '''
    if event_id in events:
        if username in events[event_id].joiners:
            events[event_id].joiners.remove(username)
            await broadcast_event(events[event_id], "update_event")
            return {"message": "Unsubscribed successfully"}
        return {"error": "User not found"} 
    return {"error": "Event not found"}

@app.delete("/api/delete-event/{event_id}")
async def delete_event(event_id: int):
    '''
    Delete an event
    params:-
        event_id: int
    '''
    if event_id in events:
        deleted_event = events.pop(event_id)
        print(deleted_event)
        await broadcast_event(deleted_event, "delete_event")
        return {"message": "Event deleted"}
    return {"error": "Event not found"}
