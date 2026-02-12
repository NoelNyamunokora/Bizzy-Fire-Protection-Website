// Quick Contact Form Handler
document.addEventListener('DOMContentLoaded', function() {
    const quickForm = document.getElementById('quickContactForm');
    if (quickForm) {
        quickForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const name = document.getElementById('quickName').value;
            const phone = document.getElementById('quickPhone').value;
            const message = document.getElementById('quickMessage').value;
            
            const whatsappMessage = `*Quick Contact Form*%0A%0A*Name:* ${name}%0A*Phone:* ${phone}%0A*Message:* ${message}`;
            
            window.open(`https://wa.me/263717124414?text=${whatsappMessage}`, '_blank');
            
            this.reset();
            alert('Thank you! Your message will be sent via WhatsApp.');
        });
    }
});
