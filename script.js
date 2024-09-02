document.addEventListener('DOMContentLoaded', () => {
    const userTypePopup = document.getElementById('userTypePopup');
    const chatbot = document.getElementById('chatbot');

    // Show the popup immediately
    userTypePopup.style.display = 'flex';

    // Button click handlers
    document.getElementById('newUserBtn').addEventListener('click', () => {
        window.location.href = 'https://forms.gle/CYd6GThxfi1arymS9';
    });

    document.getElementById('registeredUserBtn').addEventListener('click', () => {
        userTypePopup.style.display = 'none';
        chatbot.style.display = 'block'; // Show the chatbot if they are registered
    });

    // Close chatbot handler
    document.getElementById('closeChatbot').addEventListener('click', () => {
        chatbot.style.display = 'none';
    });

    // Close popup when clicking outside the popup content
    window.addEventListener('click', (event) => {
        if (event.target === userTypePopup) {
            userTypePopup.style.display = 'none';
        }
    });
});
