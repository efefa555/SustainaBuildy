<template>
  <div v-if="suggestions">
    <h2>Optimization Suggestions</h2>
    <ul>
      <li v-for="suggestion in suggestions" :key="suggestion">{{ suggestion }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  computed: {
    suggestions() {
      // Placeholder for optimization suggestions
      return [
        'Change orientation for better solar gain',
        'Optimize window placement',
        'Improve insulation',
        'Optimize HVAC system',
      ];
    },
  },
};
</script>