<!-- Question.svelte -->
<script>
  
  import { onMount , onDestroy} from 'svelte';
  import { writable } from 'svelte/store';
  import { createEventDispatcher } from 'svelte';
  import { typewriter } from '../transition'; // Import typewriter function
  export const questionData = writable(null);
  

  let started = writable(false);

  // Define variables to track the current question and the stack of visited questions
  let currentQuestion = 0; // Assuming the initial question number is 1
  let questionStack = []; // Stack to keep track of visited question


  function handleFileUpload() {
    const fileInput = document.createElement('input');
    fileInput.type = 'file';
    fileInput.onchange = async () => {
        const file = fileInput.files[0];
        if (file) {
            const formData = new FormData();
            formData.append('file', file);
            try {
                const response = await fetch('http://127.0.0.1:5000/upload', {
                    method: 'POST',
                    body: formData
                });
                if (response.ok) {
                  console.log('101')
                  fetchfileQuestion(101)
                } else {
                    console.error('Error uploading file:', response.statusText);
                }
            } catch (error) {
                console.error('Error uploading file:', error);
            }
        }
    };
    fileInput.click();
  }

  
  export function fetchfileQuestion(questionNumber) {
    console.log('file question fetching')
    fetch(`http://127.0.0.1:5000/filequestion/${questionNumber}`)
        .then(response => response.json())
        .then(nextQuestion => {
            console.log(nextQuestion)

            questionData.set(nextQuestion);
            // Update the current question number
            console.log(questionData)
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


export function selectOption(optionIndex , type) {
    
    const selectedOption = questionData.update(data => {
      if (optionIndex === 'back') {
        if (questionStack.length > 0) {
                currentQuestion = questionStack.pop();
                if(type === "file"){
                  fetchfileQuestion(currentQuestion);     
                }else{
                  fetchQuestion(currentQuestion); 
                }    // Pop the stack to get the previous question
                    
        } else {
            console.log("Already at the first question");
        }
      }
      if (typeof data.next[optionIndex] === 'number') {
          // Fetch the next question if the next is a number
          questionStack.push(currentQuestion); // Push current question onto the stack
          currentQuestion = data.next[optionIndex]; // Update current question number
          
          if(type === "file"){
            fetchfileQuestion(currentQuestion);     
          }else{
            fetchQuestion(currentQuestion); 
          }
          
      } else if (typeof data.next[optionIndex] === 'string') {
          // Check if the next is a string representing the final result
          dispatch('finalResult', { result : data.next[optionIndex] });
          console.log(data.next[optionIndex])
      } else {
          console.error('Invalid next type:', typeof data.next[optionIndex]);
      }
      return data;
    });     
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
      {#if $questionData.type === "file"}
          {#each $questionData.options.filter(option => option !== "Upload") as option, index}
            <button class="option-button" on:click={() => selectOption(index , $questionData.type)}>{option}</button>
          {/each}
          <!-- {#if $questionData.options.length > 1 && $questionData.options[0] !== "For General Data" && $questionData.options[1] !== "Upload" }
            <button class="option-button back-button" on:click={() => selectOption('back' , $questionData.type)}>Back</button>
          {/if} -->
      {:else}
          {#each $questionData.options.filter(option => option !== "Upload") as option, index}
            <button class="option-button" on:click={() => selectOption(index , $questionData.type)}>{option}</button>
          {/each}
          {#if $questionData.options.includes("Upload")}
            <!-- Render the "Upload File" button only if it's not already in the options -->
            <button class="option-button" on:click={handleFileUpload}>Upload File</button>
          {/if}
          {#if $questionData.options.length > 1 && $questionData.options[0] !== "For General Data" && $questionData.options[1] !== "Upload" }
            <button class="option-button back-button" on:click={() => selectOption('back' , $questionData.type)}>Back</button>
          {/if}
      {/if}
      

    </div>
  </div>


{:else}
  <p>Loading...</p>
{/if}

<!-- <button class="option-button" on:click={() => selectOption('back')}>Back</button> -->

