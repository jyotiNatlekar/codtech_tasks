function submitData() {
    const submitBtn = document.getElementById("submitBtn");
    const reportBtn = document.getElementById("reportBtn");

    fetch("http://127.0.0.1:5000/submit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: document.getElementById("name").value,
            score: document.getElementById("score").value,
            remarks: document.getElementById("remarks").value
        })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Submit failed");
        }

        alert("Data stored successfully!");
        window.open("http://127.0.0.1:5000/generate-report");
        // generateReport();
    })
    .catch(error => {
        console.error(error);
        alert("Submit failed");
    });
}

// Function to generate and download PDF
function generateReport() {
    console.log("Generate PDF Report function...");
    window.open("http://127.0.0.1:5000/generate-report");
}
