document.getElementById('predictionForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const submitBtn = document.getElementById('submitBtn');
    const resultContainer = document.getElementById('result-container');
    const resultText = document.getElementById('result-text');
    const resultIcon = document.getElementById('result-icon');
    
    // UI Loading State
    submitBtn.classList.add('loading');
    submitBtn.disabled = true;
    resultContainer.classList.add('hidden');
    resultContainer.className = ''; // Reset classes
    
    const data = {
        gender: parseFloat(document.getElementById('gender').value),
        income: parseFloat(document.getElementById('income').value),
        income_type: parseFloat(document.getElementById('incomeType').value),
        education: parseFloat(document.getElementById('education').value)
    };

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        
        // Artificial delay for better UX flow
        setTimeout(() => {
            submitBtn.classList.remove('loading');
            submitBtn.disabled = false;
            
            resultContainer.classList.remove('hidden');
            
            if (result.approved) {
                resultContainer.classList.add('result-approved');
                resultIcon.innerHTML = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>`;
                resultIcon.className = 'icon-approved';
                resultText.innerText = 'Application Approved';
            } else {
                resultContainer.classList.add('result-rejected');
                resultIcon.innerHTML = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>`;
                resultIcon.className = 'icon-rejected';
                resultText.innerText = 'Application Rejected';
            }
            
            document.getElementById('result-reason').innerHTML = result.reason;
        }, 800);
        
    } catch (error) {
        console.error("Error connecting to prediction server:", error);
        submitBtn.classList.remove('loading');
        submitBtn.disabled = false;
        alert("An error occurred while connecting to the server.");
    }
});
