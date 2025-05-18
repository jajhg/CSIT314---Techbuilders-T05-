document.addEventListener('DOMContentLoaded', function() {
    // Add any client-side functionality needed
    console.log('Cleaner Matching System loaded');
    
    // Example: Form validation can be added here
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // Basic validation example
            const inputs = this.querySelectorAll('input[required]');
            let isValid = true;
            
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.classList.add('error');
                } else {
                    input.classList.remove('error');
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                alert('Please fill in all required fields');
            }
        });
    });

    // Confirm before submitting update form
    const updateForms = document.querySelectorAll('form[onsubmit]');
    updateForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!confirm('Are you sure you want to update this user?')) {
                e.preventDefault();
            }
        });
    });
    
    // Confirm before suspending user
    const suspendButtons = document.querySelectorAll('.suspend-btn');
    suspendButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to suspend this user?')) {
                e.preventDefault();
            }
        });
    });
});