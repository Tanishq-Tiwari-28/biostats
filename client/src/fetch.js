export function fetchQuestion(questionNumber) {
    fetch(`http://127.0.0.1:5000/question/${questionNumber}`)
        .then(response => response.json())
        .then(nextQuestion => {
            questionData.set(nextQuestion);
            // Update the current question number
            currentQuestion = questionNumber;
            // Reset the stack if starting a new set of questions
            if (!started) {
                questionStack = [];
                started = true;
            }
        })
        .catch(error => {
            console.error('Error fetching question:', error);
        });
}