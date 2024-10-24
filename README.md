# Realtime Events Management App Project-Update

## Overview

This project is a simple real-time event management app, where users can create, join, unattend, and delete events. The application leverages WebSockets for real-time updates across all users and provides a straightforward UI using Vue.js.

## What Was Done

### 1. Backend Implementation:
- **FastAPI server**: Developed endpoints to create, join, unattend, and delete events.
- **WebSocket integration**: Implemented WebSockets to handle real-time updates for event status (joining or canceling).
- **In-memory event store**: Used in-memory storage to manage event data (title, organizer, time, and participants).
- **Error handling**: Added basic error handling for scenarios like duplicate joins, missing users, and missing events.
- **Unit testing**: Created two unit tests to verify event creation and joining functionality.

### 2. Frontend Implementation:
- **Vue.js interface**: Built a UI to list events, allowing users to join and unattend events.
- **WebSocket communication**: Integrated real-time updates on the frontend using WebSockets.
- **Axios for HTTP requests**: Used Axios to interact with the FastAPI backend.
- **Event display**: The app displays event details such as title, organizer, date/time, and attendees with real-time updates.

## Key Decisions
- **WebSockets for real-time updates**: Chose WebSockets due to their efficiency and simplicity for handling real-time data synchronization.
- **In-memory data storage**: For simplicity, used in-memory storage instead of a database. In a production environment, this would be replaced with persistent storage.
- **Vue.js for UI**: While the original task mentioned React, Vue.js was used for better alignment with the assignment requirements.

## Challenges & Solutions
- **Real-time synchronization**: Managing WebSocket connections across multiple clients required careful handling, especially with client disconnects and reconnections.
- **UI simplicity**: Focused on a minimalistic design to prioritize core functionality without overcomplicating the user interface.
