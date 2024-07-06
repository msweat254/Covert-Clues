function toggleRole(playerId) {
    const roleElement = document.querySelector(`#${playerId} .player-role`);
    if (roleElement.textContent === "Guesser") {
        roleElement.textContent = "Hint Giver";
    } else {
        roleElement.textContent = "Guesser";
    }
}

function toggleTeam(playerId) {
    const teamElement = document.querySelector(`#${playerId} .player-team`);
    if (teamElement.textContent === "Red") {
        teamElement.textContent = "Blue";
    } else {
        teamElement.textContent = "Red";
    }
}
