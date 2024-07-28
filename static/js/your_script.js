// your_script.js

const questionContainer = document.getElementById('question-container');
const questionHeading = document.getElementById('question-heading');
const nextQuestionButton = document.getElementById('next-question-button');

const questions = [
    'What is the capital of France?',
    'Who wrote "Romeo and Juliet"?',
    'What is the largest mammal?',
    // Add more questions as needed
];

let currentIndex = 0;
let previousQuestion = null;
let previousAnswer = null;

function displayQuestion() {
    // Display the current question
    questionHeading.textContent = questions[currentIndex];
}

function handleNextQuestion() {
    // Store the previous question and answer
    previousQuestion = questions[currentIndex];
    previousAnswer = prompt(`Enter the answer to "${previousQuestion}"`);

    // Move to the next question
    currentIndex++;

    // Check if there are more questions
    if (currentIndex < questions.length) {
        displayQuestion();
    } else {
        // If no more questions, you can redirect or perform other actions
        alert('End of quiz');
    }
}

// Event listener for the "Next Question" button
nextQuestionButton.addEventListener('click', handleNextQuestion);

// Initial display of the first question
displayQuestion();
