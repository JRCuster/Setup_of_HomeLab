// Ensure the JavaScript functions for updating the dashboard are correctly defined
function updateDashboard() {
    // Example AJAX call to update dashboard elements
    fetch('/dashboard/data/')
        .then(response => response.json())
        .then(data => {
            console.log('Dashboard data:', data);
            // Update dashboard elements with new data
        })
        .catch(error => console.error('Error fetching dashboard data:', error));
}

// Call updateDashboard every 30 seconds
setInterval(updateDashboard, 30000);
function updatePiHoleStatus() {
    fetch('/dashboard/pihole-status/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('pihole-status-value').textContent = data.status;
        })
        .catch(error => console.error('Error fetching PiHole status:', error));
}

// Call updatePiHoleStatus every 30 seconds
setInterval(updatePiHoleStatus, 30000);
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