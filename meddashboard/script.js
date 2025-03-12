// Get the context of the canvas
const ctx = document.getElementById('heartRateChart').getContext('2d');

// Data for the chart
const heartRateData = {
    labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], // Example labels
    datasets: [{
        label: 'Heart Rate (bpm)',
        data: [68, 72, 75, 70, 74, 73, 69], // Example data
        borderColor: '#ff6f61',
        backgroundColor: 'rgba(255, 111, 97, 0.2)',
        tension: 0.4, // Adds smooth curves to the line
        borderWidth: 3,
        pointRadius: 5,
        pointBackgroundColor: '#ff6f61'
    }]
};

// Configuration for the chart
const config = {
    type: 'line', // Line chart
    data: heartRateData,
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: true,
                labels: {
                    color: '#ffffff',
                }
            }
        },
        scales: {
            x: {
                ticks: {
                    color: '#ffffff',
                },
                grid: {
                    color: 'rgba(255, 255, 255, 0.1)',
                }
            },
            y: {
                ticks: {
                    color: '#ffffff',
                },
                grid: {
                    color: 'rgba(255, 255, 255, 0.1)',
                }
            }
        }
    }
};

// Create the chart
new Chart(ctx, config);
// Function to fetch simulated real-time heart rate data
function getHeartRateData() {
    // Simulated data (replace with API call for live data)
    const simulatedData = Array.from({ length: 7 }, () => Math.floor(Math.random() * (80 - 60 + 1) + 60));
    return simulatedData;
}

// Update the chart dynamically
function updateHeartRateChart(chart) {
    const newData = getHeartRateData();
    chart.data.datasets[0].data = newData;
    chart.update();
}

// Add interval to update data every 5 seconds
setInterval(() => {
    updateHeartRateChart(heartRateChart);
}, 5000);
