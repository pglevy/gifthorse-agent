document.addEventListener('DOMContentLoaded', () => {
    // Add any client-side JavaScript functionality here
    console.log('JavaScript loaded');

    // Example: Add event listener to flash messages to dismiss them
    const flashes = document.querySelectorAll('.flashes li');
    flashes.forEach(flash => {
        flash.addEventListener('click', () => {
            flash.style.display = 'none';
        });
    });
});
