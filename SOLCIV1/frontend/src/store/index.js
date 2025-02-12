import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    building: null,
    simulationResults: null,
  },
  mutations: {
    setBuilding(state, building) {
      state.building = building;
    },
    setSimulationResults(state, results) {
      state.simulationResults = results;
    },
  },
  actions: {
    async simulateEnergyConsumption({ commit }, building) {
      // Placeholder for API call to simulate energy consumption
      const response = await fetch('/api/simulate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(building),
      });
      const data = await response.json();
      commit('setSimulationResults', data);
    },
  },
  modules: {},
});