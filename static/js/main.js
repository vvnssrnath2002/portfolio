document.addEventListener('DOMContentLoaded', () => {
    // Scroll to projects preview on homepage
    const toggleButton = document.getElementById('toggleMessage');
    const projectsPreview = document.getElementById('projectsPreview');
    if (toggleButton && projectsPreview) {
        toggleButton.addEventListener('click', () => {
            projectsPreview.classList.remove('hidden');
            projectsPreview.scrollIntoView({ behavior: 'smooth' });
        });
    }

    // Handle contact form submission
    const contactForm = document.getElementById('contactForm');
    const formMessage = document.getElementById('formMessage');
    if (contactForm && formMessage) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(contactForm);
            try {
                const response = await fetch('/contact', {
                    method: 'POST',
                    body: formData
                });
                const result = await response.json();
                formMessage.textContent = result.message;
                formMessage.classList.remove('hidden');
                contactForm.reset();
            } catch (error) {
                formMessage.textContent = 'Error submitting form.';
                formMessage.classList.remove('hidden');
            }
        });
    }
});