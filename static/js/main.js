document.addEventListener('DOMContentLoaded', () => {
    // Add any client-side JavaScript functionality here
    console.log('JavaScript loaded');

    function getProgressToDeadline(dueDate) {
        // Convert due date to Date object if string is provided
        const dueDateObj = dueDate instanceof Date ? dueDate : new Date(dueDate);
        const today = new Date();

        // Reset time parts for accurate calculation
        dueDateObj.setHours(0, 0, 0, 0);
        today.setHours(0, 0, 0, 0);

        // If due date is in the past, return 100
        if (dueDateObj < today) {
            return 100;
        }

        // If due date is today, return 100
        if (dueDateObj.getTime() === today.getTime()) {
            return 100;
        }

        // Calculate percentage based on days remaining
        const totalDays = (dueDateObj - today) / (1000 * 60 * 60 * 24);
        // Assume 30 days as full period for progress bar
        const percentage = 100 - ((totalDays / 30) * 100);

        // Clamp value between 0 and 100
        const prog = Math.max(0, Math.min(100, Math.round(percentage)));
        const bar = document.getElementById('prog');
        bar.value = prog;
        console.log(prog)
    };

    getProgressToDeadline('2024-11-27');

    // Example: Add event listener to flash messages to dismiss them
    const flashes = document.querySelectorAll('.flashes li');
    flashes.forEach(flash => {
        flash.addEventListener('click', () => {
            flash.style.display = 'none';
        });
    });
});
