let usageData = [];
let labels = [];

const ctx = document.getElementById('chart').getContext('2d');

const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: labels,
        datasets: [{
            label: 'Usage (KB)',
            data: usageData
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});

async function fetchData() {
    try {
        const res = await fetch("http://127.0.0.1:8000/data");
        const data = await res.json();

        // Update UI
        document.getElementById("usage").innerText = data.usage + " KB";
        document.getElementById("devices").innerText = data.devices;

        const alertElement = document.getElementById("alert");
        alertElement.innerText = data.alert;

        // Change color based on alert
        if (data.alert.includes("Abnormal")) {
            alertElement.className = "alert";
        } else {
            alertElement.className = "normal";
        }

        // Update graph
        usageData.push(data.usage);
        labels.push(new Date().toLocaleTimeString());

        if (usageData.length > 10) {
            usageData.shift();
            labels.shift();
        }

        chart.update();

    } catch (err) {
        console.log("Error:", err);
    }
}

// Fetch every 2 seconds
setInterval(fetchData, 2000);