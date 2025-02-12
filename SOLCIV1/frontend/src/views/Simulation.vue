<template>
  <div>
    <h1>Simulation</h1>
    <three-d-view></three-d-view>
    <button @click="simulate" class="btn btn-primary">Run Simulation</button>
  </div>
</template>

<script>
import ThreeDView from '@/components/ThreeDView.vue';

export default {
  components: {
    ThreeDView,
  },
  methods: {
    async simulate() {
      await this.$store.dispatch('simulateEnergyConsumption', this.$store.state.building);
      this.$router.push('/results');
    },
  },
};
</script>