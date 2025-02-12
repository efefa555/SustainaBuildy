<template>
  <div>
    <h1>Welcome to the Energy Optimization App</h1>
    <building-form></building-form>
  </div>
</template>

<script>
import BuildingForm from '@/components/BuildingForm.vue';

export default {
  components: {
    BuildingForm,
  },
};
</script>