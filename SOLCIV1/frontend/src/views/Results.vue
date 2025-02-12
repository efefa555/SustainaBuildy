<template>
  <div>
    <h1>Results</h1>
    <energy-report></energy-report>
    <optimization-suggestions></optimization-suggestions>
  </div>
</template>

<script>
import EnergyReport from '@/components/EnergyReport.vue';
import OptimizationSuggestions from '@/components/OptimizationSuggestions.vue';

export default {
  components: {
    EnergyReport,
    OptimizationSuggestions,
  },
};
</script>