document.addEventListener('DOMContentLoaded', function() {
    // Replace <game_code> with the actual game code
    const currentURL = document.URL;
    const gameCode = currentURL.split('/',-1)[4];
    console.log('Current URL: '+currentURL);
    console.log('Current game code: '+gameCode);
    
    function updateWordStatus() {
        console.log('Updated')
        fetch(`/api/get_game_data/${gameCode}`)
            .then(response => response.json())
            .then(data => {
                for (let i = 1; i <= 25; i++) {
                    const wordContainer = document.getElementById(i.toString());
                    const wordTextElement = wordContainer.querySelector('.word-text');

                    wordTextElement.textContent = data[`word${i}`];
                    wordContainer.setAttribute('value', data[`word${i}color`]);

                    // Add a class based on the color
                    wordContainer.classList.add(data[`word${i}color`]);

                    // Add a class if the word status is 1 (true)
                    if (data[`word${i}status`]) {
                        wordContainer.classList.add('guessed-word');
                        wordContainer.classList.remove('unguessed-word');
                    } else {
                        wordContainer.classList.remove('guessed-word');
                        wordContainer.classList.add('unguessed-word');
                    }
                }
            })
            .catch(error => console.error('Error fetching game data:', error));
    }

    //setInterval(updateWordStatus, 1000);

    // Initial update
    updateWordStatus();
});