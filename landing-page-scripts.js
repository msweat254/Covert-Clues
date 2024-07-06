document.addEventListener('DOMContentLoaded', function() {
    const joinGameButton = document.getElementById('join-game-button');
    const joinGameForm = document.getElementById('join-game-form');

    joinGameButton.addEventListener('click', function() {
        joinGameForm.classList.toggle('hidden');
    });

    // Host game button doesn't do anything yet
    document.getElementById('host-game-button').addEventListener('click', function() {
        alert('Host game functionality coming soon!');
    });
});
