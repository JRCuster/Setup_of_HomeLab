document.addEventListener('DOMContentLoaded', function() {
    // JavaScript code for interactivity and real-time updates will go here
    function fetchData() {
        fetch('/dashboard/data/')
            .then(response => response.json())
            .then(data => {
                // Update the dashboard with the fetched data
                // Example: document.getElementById('cluster-status').textContent = data.cluster_status;
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    // Fetch data every 15 seconds for real-time updates
    setInterval(fetchData, 15000);
});
});