<!-- Question.svelte -->
<script>
  import { onMount } from 'svelte';
  import { writable } from 'svelte/store';
  import { createEventDispatcher } from 'svelte';

  export let id;
  export let onNext;

  // Define a writable store to hold the question and options
  const questionData = writable(null);
  
  // Fetch question data when the component mounts
  onMount(async () => {
      fetch(`http://127.0.0.1:5000/question/${id}`)
          .then(response => response.json())
          .then(data => {
              questionData.set(data);
              console.log(data.question)
          });
          
  });
  const dispatch = createEventDispatcher();

  // Function to handle option selection
  // Function to handle option selection
// Function to handle option selection
function selectOption(optionIndex) {
    const selectedOption = questionData.update(data => {
        // Check if the next is a number
        if (typeof data.next[optionIndex] === 'number') {
            // Fetch the next question if the next is a number
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
}


</script>

{#if $questionData !== null}
  <div>
      <p>{$questionData.question}</p>
      <div>
          {#each $questionData.options as option, index}
              <button on:click={() => selectOption(index)}>{option}</button>
          {/each}
      </div>
  </div>
{:else}
  <p>Loading...</p>
{/if}
