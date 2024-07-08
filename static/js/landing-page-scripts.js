document.addEventListener('DOMContentLoaded', function() {
    const joinGameButton = document.getElementById('join-game-button');
    const joinGameForm = document.getElementById('join-game-form');

    joinGameButton.addEventListener('click', function() {
        joinGameForm.classList.toggle('hidden');
    });

    document.getElementById('join-button').addEventListener('click', function() {
        const gameCode = document.getElementById('game-code-input').value;
        if (gameCode) {
            window.location.href = `/game/${gameCode}`;
        }
    });
});
