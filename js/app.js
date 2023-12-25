const { createApp } = require('vue');
const App = {
  data() {
    return {
      topologyData: null,
    };
  },
  methods: {
    async fetchTopologyData() {
      try {
        const response = await fetch('/topology/data');
        this.topologyData = await response.json();
      } catch (error) {
        console.error('Error fetching topology data:', error);
      }
    }
  },
  mounted() {
    this.fetchTopologyData();
  }
};

createApp(App).mount('#app');
