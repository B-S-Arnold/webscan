<template>
    <div class="splash-page">
        <h1>Welcome to WebScan</h1>
        <p>Scan your website for vulnerabilities</p>
        <form @submit.prevent="startScan">
            <label for="url">Enter the URL to scan:</label>
            <input type="text" id="url" v-model="url" placeholder="https://example.com" required />
            <button type="submit">Start Scan</button>
        </form>

        <!-- Display scan results based on condition -->
        <div v-if="showResults" class="scan-results">
            <ul>
                <li>
                    <img v-if="isSafe" src="@/assets/check.png" alt="Safe" />
                    <img v-else src="@/assets/x.png" alt="Dangerous" />
                    <p>{{ resultMessage }}</p>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SplashPage',
    data() {
        return {
            url: '', // Stores the user's input URL
            showResults: false, // Initially, hide scan results
            isSafe: true, // Assume the URL is safe by default
        };
    },
    computed: {
        resultMessage() {
            return this.isSafe ? 'This is safe.' : 'This is dangerous!';
        },
    },
    methods: {
        startScan() {
            // Simulate scanning logic for demonstration
            // You can replace this with your actual scan logic

            // For demonstration purposes, randomly determine if the URL is safe or not
            this.isSafe = Math.random() >= 0.5;
            this.showResults = true; // Show scan results
        },
    },
};
</script>

<style scoped src="./SplashPage.css"></style>
