document.addEventListener('DOMContentLoaded', function() {
    // Replace <game_code> with the actual game code
    const currentURL = document.URL;
    const gameCode = currentURL.split('/', -1)[4];
    console.log('Current URL: ' + currentURL);
    console.log('Current game code: ' + gameCode);

    const allContainers = document.querySelectorAll('.word-container');

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

    function sendDataToFlask(gameCode, wordId) {
        fetch('/api/process_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ game_code: gameCode, value: String(wordId) }) // Include game_code and convert wordId to a string
        })
        .then(response => response.json())
        .then(result => {
            console.log('Success:', result);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    function wordClicked(event) {
        const container = event.currentTarget;
        const containerId = container.id;
        
        sendDataToFlask(gameCode,containerId);
        console.log('Clicked word with id: ' + containerId);
    }

    allContainers.forEach(container => {
        container.addEventListener('click', wordClicked);
    });

    // Update word status every 500 milliseconds
    //setInterval(updateWordStatus, 1000);

    // Initial update
    updateWordStatus();
});
