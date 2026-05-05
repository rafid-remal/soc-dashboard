async function loadAlerts() {
    try {
        const response = await fetch('/alerts');
        const data = await response.json();

        console.log("SOC Alerts:", data);

        // Optional: show on page
        document.getElementById("output").innerText =
            JSON.stringify(data, null, 2);

    } catch (err) {
        console.error("Error fetching alerts:", err);
    }
}

// Run on page load
loadAlerts();

// Optional: auto refresh every 5 seconds (SOC style)
setInterval(loadAlerts, 5000);
