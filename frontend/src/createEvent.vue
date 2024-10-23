<template>
  <div class="container">
    <h5 class="text-center">Create Event</h5>

    <br />
    <form>
      <div class="form-group">
        <label for="eventTitle">Title</label>
        <input
          v-model="title"
          type="text"
          class="form-control"
          id="eventTitle"
          placeholder="Enter Title"
        />
        <small id="emailHelp" class="form-text text-muted"
          >Title will be visible to all users</small
        >
      </div>
      <div class="form-group">
        <label for="eventOrganizer">Organizer</label>
        <input
          v-model="organizer"
          type="text"
          class="form-control"
          id="eventOrganizer"
          placeholder="Enter Organizer Name"
        />
      </div>
      <div class="form-group">
        <label for="eventDateAndTime">Date and Time</label>
        <input
          v-model="date_time"
          type="datetime-local"
          class="form-control"
          id="eventDateAndTime"
        />
      </div>
      <div class="form-group">
        <label for="eventDuration">Duration</label>
        <input
          v-model="duration"
          type="text"
          class="form-control"
          id="eventDuration"
          placeholder="Enter Duration"
        />
      </div>
      <div class="form-group">
        <label for="eventLocation">Location</label>
        <input
          v-model="location"
          type="text"
          class="form-control"
          id="eventLocation"
          placeholder="Enter Location"
        />
      </div>
      <button class="btn btn-primary" @click="onSubmit" id="submit-button">
        Submit
      </button>
    </form>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      title: "",
      organizer: "",
      date_time: "",
      duration: 0,
      location: "",
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      let requestBody = {title:this.title, organizer:this.organizer, date_time:this.date_time, duration:this.duration, location:this.location};
      console.log(requestBody)
      axios.post("http://127.0.0.1:8000/api/create-event", requestBody).then((response) => {
        this.clearTable()
        this.$emit('getEventInfo')
      });
    },
    clearTable(){
        this.title=""
        this.organizer=""
        this.date_time=""
        this.duration=0
        this.location=""
    }
  },
  mounted() {},
};
</script>