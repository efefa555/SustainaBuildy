<template>
  <div v-if="report">
    <h2>Energy Report</h2>
    <p>Total Energy Consumption: {{ report.total_energy_consumption }}</p>
    <p>Thermal Losses: {{ report.thermal_losses }}</p>
    <p>Solar Gains: {{ report.solar_gains }}</p>
  </div>
</template>

<script>
export default {
  computed: {
    report() {
      return this.$store.state.simulationResults;
    },
  },
};
</script>