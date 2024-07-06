document.addEventListener('DOMContentLoaded', function() {
    // Fetch and assign words from the text file
    fetch('words.txt')
        .then(response => response.text())
        .then(data => {
            const words = data.split('\n').map(word => word.trim()).filter(word => word.length > 0);
            assignWords(words);
            assignColors();
        })
        .catch(error => console.error('Error fetching words:', error));

    // Setup the button event listener to assign colors
    setupColorAssignmentButton();
    guessedWord();
});

// Function to assign words to the word-text elements
function assignWords(words) {
    const containers = document.querySelectorAll('.word-container .word-text');
    const shuffledWords = shuffleArray(words);

    containers.forEach((container, index) => {
        if (shuffledWords[index]) {
            container.textContent = shuffledWords[index];
        }
    });
    assignColors();
}

// Function to shuffle an array
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

function assignColors() {
    // Create an array with the desired colors
    const colors = [
        ...Array(8).fill('blue'), 
        ...Array(8).fill('red'), 
        ...Array(8).fill('white'), 
        'black'
    ];

    // Shuffle the array to randomize the order of colors
    const shuffledColors = shuffleArray(colors);

    // Select all word-container divs
    const wordContainers = document.querySelectorAll('.word-container');

    // Assign colors to the value attribute and add corresponding classes
    wordContainers.forEach((container, index) => {
        const color = shuffledColors[index];
        container.classList.remove('blue', 'red', 'white', 'black','guessed-word');
        container.setAttribute('value', color);
        container.classList.add(color);
    });
}

// Function to set up the buttons that will trigger color and word assignment
function setupColorAssignmentButton() {
    const colorButton = document.getElementById('color-shuffle-button');
    const wordButton = document.getElementById('word-shuffle-button');

    if (colorButton) {
        colorButton.addEventListener('click', assignColors);
    }

    if (wordButton) {
        fetch('words.txt')
            .then(response => response.text())
            .then(data => {
                const words = data.split('\n').map(word => word.trim()).filter(word => word.length > 0);
                wordButton.addEventListener('click', () => assignWords(words));
            })
            .catch(error => console.error('Error fetching words:', error));
    }
}

function guessedWord() {
    const wordContainers = document.querySelectorAll('.word-container');

    wordContainers.forEach(container => {
        container.addEventListener('click', () => {
            container.classList.add('guessed-word');
        });
    }); 
}
