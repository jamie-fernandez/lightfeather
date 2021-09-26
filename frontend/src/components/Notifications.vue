<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset">
      <h2>Notification Form</h2>
      <b-form-group id="input-group-1" label="First Name:" label-for="input-1">
        <ValidationProvider
          name="first name"
          rules="alpha|max:30"
          v-slot="{ errors }"
        >
          <b-form-input
            id="input-1"
            v-model="form.firstName"
            placeholder="Enter First Name"
            ref="firstName"
            autocomplete="off"
            required
          />
          <span id="firstNameError">{{ errors[0] }}</span>
        </ValidationProvider>
      </b-form-group>

      <b-form-group id="input-group-2" label="Last Name:" label-for="input-2">
        <ValidationProvider
          name="last name"
          rules="alpha|max:30"
          v-slot="{ errors }"
        >
          <b-form-input
            id="input-2"
            v-model="form.lastName"
            placeholder="Enter Last Name"
            ref="lastName"
            autocomplete="off"
            required
          />
          <span id="lastNameError">{{ errors[0] }}</span>
        </ValidationProvider>
      </b-form-group>

      <b-form-group
        label="How would you prefer to be notified?"
        v-slot="{ ariaDescribedby }"
      >
        <b-form-radio
          v-model="preference"
          :aria-describedby="ariaDescribedby"
          name="some-radios"
          value="phone"
          >Phone</b-form-radio
        >
        <b-form-radio
          v-model="preference"
          :aria-describedby="ariaDescribedby"
          name="some-radios"
          value="email"
          >Email</b-form-radio
        >
      </b-form-group>

      <b-form-group
        v-if="preference == 'email'"
        id="input-group-3"
        label="Email address:"
        label-for="input-3"
      >
        <ValidationProvider name="email" rules="email" v-slot="{ errors }">
          <b-form-input
            id="input-3"
            v-model="form.email"
            type="email"
            placeholder="Enter email"
            ref="email"
            autocomplete="off"
            required
          />
          <span id="emailError">{{ errors[0] }}</span>
        </ValidationProvider>
      </b-form-group>

      <b-form-group
        v-if="preference == 'phone'"
        id="input-group-4"
        label="Phone Number:"
        label-for="input-4"
      >
        <ValidationProvider
          name="phone"
          rules="numeric|max:10"
          v-slot="{ errors }"
        >
          <b-form-input
            id="input-4"
            v-model="form.phone"
            type="tel"
            placeholder="Enter phone"
            ref="phone"
            autocomplete="off"
            required
          />
          <span id="phoneError">{{ errors[0] }}</span>
        </ValidationProvider>
      </b-form-group>

      <b-form-group id="input-group-5" label="Supervisor:" label-for="input-5">
        <b-form-select
          id="input-5"
          v-model="form.supervisor"
          :options="form.supervisorOptions"
          :select-size="10"
          ref="supervisor"
          required
        />
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>

    <h2>Notifications that have already been saved</h2>
    <b-table id="notificationsTable" striped hover :items="notifications" />
  </div>
</template>

<script>
import axios from "axios";
import { ValidationProvider } from "vee-validate";

export default {
  name: "Notifications",
  components: {
    ValidationProvider,
  },
  data() {
    return {
      notifications: null,
      preference: null,
      form: {
        lastName: null,
        firstName: null,
        email: null,
        phone: null,
        supervisor: null,
        supervisorOptions: [],
      },
    };
  },
  created() {
    this.fetchNotifications();
    this.fetchSupervisors();
  },
  methods: {
    fetchNotifications() {
      axios
        .get("http://0.0.0.0:8000/api/notifications/")
        .then((response) => {
          this.notifications = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    fetchSupervisors() {
      axios
        .get("http://0.0.0.0:8000/api/supervisors/")
        .then((response) => {
          this.form.supervisorOptions = response.data.map((manager) => {
            return {
              text: `${manager.jurisdiction} - ${manager.lastName}, ${manager.firstName}`,
              value: manager.id,
            };
          });

          console.log(this.supervisorOptions);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    onSubmit(event) {
      event.preventDefault();
      const { firstName, lastName, email, phone, supervisor } = this.form;
      console.log(firstName, lastName, email, phone, supervisor);
    },
    onReset() {},
  },
};
</script>

