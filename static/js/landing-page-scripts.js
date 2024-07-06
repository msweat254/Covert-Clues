document.addEventListener('DOMContentLoaded', function() {
    const joinGameButton = document.getElementById('join-game-button');
    const joinGameForm = document.getElementById('join-game-form');

    joinGameButton.addEventListener('click', function() {
        joinGameForm.classList.toggle('hidden');
    });
});
