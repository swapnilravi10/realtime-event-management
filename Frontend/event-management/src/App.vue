<template>
  <div>
    <h1 class="text-center mb-5">Realtime Events Management</h1>
    <div class="container-fluid row mb-5">
      <live-event :event_info="events" />
    </div>
    <div class="container-fluid row mb-5">
      <div class="col-md">
        <button class="btn btn-primary" @click="toggleCreateView">Switch to {{ createView ? 'Cancel' : 'Create' }} Event</button>
        <component :is="currentEventView" @getEventInfo="setupWebSocket()"/>
      </div>
      <div class="col-md">
        <button class="btn btn-primary" @click="toggleAttendView">Switch to {{ attendView ? 'Reject' : 'Join' }} Event</button>
        <component :is="currentAttendView" @getEventInfo="setupWebSocket()"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CreateEvent from './createEvent.vue'
import JoinEvent from './joinEvent.vue'
import LiveEvent from './liveEvent.vue'
import CancelEvent from './cancelEvent.vue'
import RejectEvent from './rejectEvent.vue'

export default {
  components:{
    CreateEvent,
    JoinEvent,
    LiveEvent,
    CancelEvent,
    RejectEvent
  },
  data() {
    return {
      events: [],
      ws: null,
      createView: true,
      attendView: true,
    }
  },
  computed: {
    currentEventView() {
      return this.createView ? 'create-event' : 'cancel-event';
    },
    currentAttendView() {
      return this.attendView ? 'join-event' : 'reject-event';
    },
  },
  methods: {
    toggleCreateView() {
      this.createView = !this.createView;
    },
    toggleAttendView() {
      this.attendView = !this.attendView;
    },
    fetchEvents() {
        axios.get("http://127.0.0.1:8000/api/events").then((response) => {
          this.events = response.data;
        });
      },
      setupWebSocket() {
      this.ws = new WebSocket("ws://localhost:8000/ws");
      this.ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.action === "new_event") {
        const existingEvent = this.events.find(e => e.id === data.event.id);
        if (!existingEvent) {
          this.events.push(data.event);
        }
      } else if (data.action === "update_event") {
        const index = this.events.findIndex(e => e.id === data.event.id);
        if (index !== -1) {
          this.$set(this.events, index, data.event);  
        }
      } else if (data.action === "delete_event") {
        this.events = this.events.filter(e => e.id !== data.event.id);
      }
    };
    }
   
  },
  mounted() {
    this.fetchEvents()
    this.setupWebSocket()
    
    // Add Bootstrap CSS
let bootstrapCSS = document.createElement('link');
bootstrapCSS.setAttribute('rel', 'stylesheet');
bootstrapCSS.setAttribute('href', 'https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css');
bootstrapCSS.setAttribute('integrity', 'sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm');
bootstrapCSS.setAttribute('crossorigin', 'anonymous');
document.head.appendChild(bootstrapCSS);

// Add Popper.js
let popperScript = document.createElement('script');
popperScript.setAttribute('src', 'https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js');
popperScript.setAttribute('integrity', 'sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q');
popperScript.setAttribute('crossorigin', 'anonymous');
document.head.appendChild(popperScript);

// Add Bootstrap JS
let bootstrapScript = document.createElement('script');
bootstrapScript.setAttribute('src', 'https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js');
bootstrapScript.setAttribute('integrity', 'sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl');
bootstrapScript.setAttribute('crossorigin', 'anonymous');
document.head.appendChild(bootstrapScript);
  }
}
</script>
<style>

</style>
