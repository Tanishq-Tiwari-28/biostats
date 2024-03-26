<!-- Question.svelte -->
<script>
  import Typed from 'typed.js';

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
              initTyped(data.question);
          });
          
  });
  function initTyped(question) {
    new Typed('.question', {
      strings: [question], // Pass the question as a string to Typed.js
      typeSpeed: 1.5 // Adjust the typing speed as needed
    });
  }
  
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
<style>
  @import url("https://fonts.googleapis.com/css?family=Raleway:400");

* {
	box-sizing: border-box;
}

@property --angle {
  syntax: '<angle>';
  initial-value: 90deg;
  inherits: true;
}

@property --gradX {
  syntax: '<percentage>';
  initial-value: 50%;
  inherits: true;
}

@property --gradY {
  syntax: '<percentage>';
  initial-value: 0%;
  inherits: true;
}
  
  :root {
	--d: 2500ms;
	--angle: 90deg;
	--gradX: 100%;
	--gradY: 50%;
	--c1: rgba(168, 239, 255, 1);
	--c2: rgba(168, 239, 255, 0.1);
}

.wrapper {
	min-width: min(40rem, 100%);
}

.box {
	font-size: 3vw;
	margin: max(1rem, 3vw);
	border: 0.35rem solid;
	padding: 3vw;
	border-image: conic-gradient(from var(--angle), var(--c2), var(--c1) 0.1turn, var(--c1) 0.15turn, var(--c2) 0.25turn) 30;
	animation: borderRotate var(--d) linear infinite forwards;
}


@keyframes borderRotate {
	100% {
		--angle: 420deg;
	}
}

@keyframes borderRadial {
	20% {
		--gradX: 100%;
		--gradY: 50%;
	}
	40% {
		--gradX: 100%;
		--gradY: 100%;
	}
	60% {
		--gradX: 50%;
		--gradY: 100%;
	}
	80% {
		--gradX: 0%;
		--gradY: 50%;
	}
	100% {
		--gradX: 50%;
		--gradY: 0%;
	}
}


  .container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 50vh; /* Make sure the container takes the full height of the viewport */
    font-family: 'Your Fancy Font', cursive; /* Replace 'Your Fancy Font' with your desired font */
    animation: borderRotate var(--d) linear infinite forwards;
    min-width: min(40rem, 100%);
  }

  /* Style the question text */
  .question {
    font-size: 24px; /* Adjust font size as needed */
    margin-bottom: 50px; /* Add some spacing between question and options */
    text-align: center;
    width: auto; /* Center align the text */
  }

  /* Style the options */
  .options {
    display: flex;
    flex-direction: row;
    justify-content: center;
  }

  /* Style individual option buttons */
  .option-button {
    margin: 5px; /* Add some spacing between options */
    padding: 10px 20px; /* Adjust padding for better visual appearance */
    font-size: 18px; /* Adjust font size as needed */
    width: 220px;
    height: 50px;
    border: none;
    outline: none;
    color: #fff;
    background: #111;
    cursor: pointer;
    position: relative;
    z-index: 0;
    border-radius: 10px;
  }

  .option-button:before {
    content: '';
    background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
    position: absolute;
    top: -2px;
    left:-2px;
    background-size: 400%;
    z-index: -1;
    filter: blur(5px);
    width: calc(100% + 4px);
    height: calc(100% + 4px);
    animation: glowing 20s linear infinite;
    opacity: 0;
    transition: opacity .3s ease-in-out;
    border-radius: 10px;
  }

  .option-button:active {
    color: #000
  }

  .option-button:active:after {
    background: transparent;
  }

  .option-button:hover:before {
    opacity: 1;
  }

  .option-button:after {
    z-index: -1;
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: #111;
    left: 0;
    top: 0;
    border-radius: 10px;
  }

  @keyframes glowing {
    0% { background-position: 0 0; }
    50% { background-position: 400% 0; }
    100% { background-position: 0 0; }
  }
  

</style>

{#if $questionData !== null}
  <div class="container">
    <div class="wrapper">
      <div class="box">
        <p class="question">{$questionData.question}</p>
      </div>
    </div>
    <div class="options">
      {#each $questionData.options as option, index}
        <button class="option-button" on:click={() => selectOption(index)}>{option}</button>
      {/each}
    </div>
  </div>    
{:else}
  <p>Loading...</p>
{/if}
