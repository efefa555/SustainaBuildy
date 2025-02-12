<template>
  <form @submit.prevent="submitForm">
    <div class="form-group">
      <label for="name">Building Name</label>
      <input type="text" class="form-control" id="name" v-model="name">
    </div>
    <div class="form-group">
      <label for="area">Area</label>
      <input type="number" class="form-control" id="area" v-model="area">
    </div>
    <div class="form-group">
      <label for="materials">Materials</label>
      <input type="text" class="form-control" id="materials" v-model="materials">
    </div>
    <div class="form-group">
      <label for="windows">Number of Windows</label>
      <input type="number" class="form-control" id="windows" v-model="windows">
    </div>
    <div class="form-group">
      <label for="orientation">Orientation</label>
      <input type="text" class="form-control" id="orientation" v-model="orientation">
    </div>
    <div class="form-group">
      <label for="insulation">Insulation</label>
      <input type="text" class="form-control" id="insulation" v-model="insulation">
    </div>
    <div class="form-group">
      <label for="hvac">HVAC</label>
      <input type="text" class="form-control" id="hvac" v-model="hvac">
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      area: '',
      materials: '',
      windows: '',
      orientation: '',
      insulation: '',
      hvac: '',
    };
  },
  methods: {
    submitForm() {
      const building = {
        name: this.name,
        area: this.area,
        materials: this.materials,
        windows: this.windows,
        orientation: this.orientation,
        insulation: this.insulation,
        hvac: this.hvac,
      };
      this.$store.commit('setBuilding', building);
      this.$router.push('/simulation');
    },
  },
};
</script>