<template>
    <div class="container">
      <h5 class="text-center">
          All Events
      </h5>
      
      <br/>
      <table class="table">
  <thead>
    <tr>
        <th scope="col"> ID </th>
      <th scope="col">Title</th>
      <th scope="col">Organizer</th>
      <th scope="col">Date Time</th>
      <th scope="col">Duration</th>
      <th scope="col"> Location </th>
      <th scope="col"> Joiners </th>
    </tr>
  </thead>
  <tbody v-for="event in event_info" :key="event.title">
    <tr>
        <th scope="row">{{ event.id }}</th>
      <th>{{ event.title }}</th>
      <td>{{ event.organizer }}</td>
      <td>{{ event.date_time }}</td>
      <td>{{ event.duration }}</td>
      <td>{{ event.location }}</td>
      <td>{{ event.joiners.join(', ') }}</td>
    </tr>
  </tbody>
</table>

    </div>
  </template>
  <script>
  export default {
    data() {
      return {
        events: [],
        ws: null,
      };
    },
    props: {
      event_info: Array,
    },
    methods: {},
    mounted() {},
  };
  </script>