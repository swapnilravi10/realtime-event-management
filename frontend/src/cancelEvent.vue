<template>
    <div class="container">
      <h5 class="text-center">
          Cancel Event
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
        <button class="btn btn-primary" @click="onSubmit" id="submit-button">Submit</button>
      </form>
    </div>
  </template>
  <script>
  import axios from "axios";
  export default {
    data() {
      return {
        event_id: 0
      };
    },
    methods: {
        onSubmit(event) {
      event.preventDefault();
      axios.delete(`http://127.0.0.1:8000/api/delete-event/${this.event_id}`).then((response) =>{
        this.clearTable()
        this.$emit('getEventInfo')
      });
    },
       clearTable() {
        this.event_id=0
      },
    },
    mounted() {},
  };
  </script>