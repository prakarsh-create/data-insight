async function processData() {
    const fileInput = document.getElementById('file-upload');
    if (fileInput.files.length === 0) {
        alert("Please select a file!");
        return;
    }

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) throw new Error('Failed to upload file');

        const result = await response.json();
        console.log("Result:", result);

        // ✅ Display the plot
        const plotImage = document.getElementById('plot-image');
        plotImage.src = result.plot_url;
        plotImage.style.display = 'block';

        // ✅ Display the summary
        const summaryDiv = document.getElementById('summary');
        summaryDiv.innerText = JSON.stringify(result.summary, null, 2);
        summaryDiv.style.display = 'block';

    } catch (error) {
        console.error("Error:", error);
        alert("Failed to process file.");
    }
}

function toggleMode() {
    document.body.classList.toggle("light-mode");
 }
