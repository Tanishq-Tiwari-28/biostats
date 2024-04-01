<!-- Question.svelte -->
<script>
  
  import { onMount , onDestroy} from 'svelte';
  import { writable } from 'svelte/store';
  import { createEventDispatcher } from 'svelte';
  import { typewriter } from '../transition'; // Import typewriter function


  export let onNext;
  export let isFirstOption;
  // Define a writable store to hold the question and options
  export const questionData = writable(null);
  

  let started = writable(false);

  // Define variables to track the current question and the stack of visited questions
  let currentQuestion = 0; // Assuming the initial question number is 1
  let questionStack = []; // Stack to keep track of visited question

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
  // Fetch question data when the component mounts
  onMount(async () => {
      fetchQuestion(currentQuestion);
     
  });
  const dispatch = createEventDispatcher();


export function selectOption(optionIndex) {
    const selectedOption = questionData.update(data => {
      if (optionIndex === 'back') {
        if (questionStack.length > 0) {
                currentQuestion = questionStack.pop(); // Pop the stack to get the previous question
                fetchQuestion(currentQuestion);
                
        } else {
            console.log("Already at the first question");
        }
      }
        
        if (typeof data.next[optionIndex] === 'number') {
            // Fetch the next question if the next is a number
            questionStack.push(currentQuestion); // Push current question onto the stack
            currentQuestion = data.next[optionIndex]; // Update current question number
            fetchQuestion(currentQuestion);
            fetch(`http://127.0.0.1:5000/question/${data.next[optionIndex]}`)
                .then(response => response.json())
                .then(nextQuestion => {
                    questionData.set(nextQuestion);
                    if (typeof onNext === 'function') {
                        onNext(nextQuestion);
                    }
                })
                .catch(error => {
                    console.error('Error fetching next question:', error);
                });
        } else if (typeof data.next[optionIndex] === 'string') {
            // Check if the next is a string representing the final result
            dispatch('finalResult', { result : data.next[optionIndex] });
            console.log(data.next[optionIndex])
        } else {
            console.error('Invalid next type:', typeof data.next[optionIndex]);
        }
        return data;
    });
    

    onDestroy(() => {
      unsubscribe(); // Unsubscribe when component is destroyed
    });

    let isFirstOption = true; //for back button 
    

}


</script>
<style>
  @import '../question.css';
</style>


{#if $questionData !== null}
<link href='https://fonts.googleapis.com/css?family=Lato:300,400,700' rel='stylesheet' type='text/css'>
<link rel="stylesheet" href="/background.css">
<div id='stars'></div>
<div id='stars2'></div>
<div id='stars3'></div>

  <div class="container">
    <div class="wrapper">
      <div class="box">
        <p class="question" >{$questionData.question}</p>
      </div>
    </div>
    <div class="options">
      {#each $questionData.options as option, index}
        <button class="option-button" on:click={() => selectOption(index)}>{option}</button>
      {/each}
      {#if $questionData.options.length > 1}
      <button class="option-button back-button" on:click={() => selectOption('back')}>Back</button>
      {/if}
    </div>
  </div>


{:else}
  <p>Loading...</p>
{/if}

<!-- <button class="option-button" on:click={() => selectOption('back')}>Back</button> -->

