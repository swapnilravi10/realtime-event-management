<template>
    <div class="container">
      <h5 class="text-center">
          Join Event
      </h5>
      
      <br/>
      <form>
        <div class="form-group">
          <label for="eventId">Event ID</label>
          <input
          v-model="event_id"
            type="number"
            class="form-control"
            id="eventId"
            placeholder="Enter event ID"
          />
        </div>
        <div class="form-group">
          <label for="userName">User Name</label>
          <input
            v-model="username"
            type="text"
            class="form-control"
            id="userName"
            placeholder="Please enter your user name"
          />
        </div>
        <button class="btn btn-primary" @click="onSubmit" id="submit-button">Submit</button>
      </form>
    </div>
  </template>
  <script>
  import axios from "axios";
  export default {
    data() {
      return {
        username:'',
        event_id: 0
      };
    },
    methods: {
        onSubmit(event) {
      event.preventDefault();
      axios.post(`http://127.0.0.1:8000/api/join-event/${this.event_id}?username=${this.username}`).then((response) =>{
        this.clearTable()
        this.$emit('getEventInfo')
      });
    },
       clearTable() {
        this.username=''
        this.event_id=0
      },
    },
    mounted() {},
  };
  </script>