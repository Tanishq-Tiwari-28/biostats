<!-- Result.svelte -->
<script>
  export let result;
</script>

<style>
  /* Add your CSS styles here */
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
    height: auto; /* Adjust height to fit content */
    margin-top: 20px; /* Add some margin to separate the result and the GIF */
    font-family: 'Your Fancy Font', cursive;
  }

  .resultcss{
    font-size: 24px; /* Adjust font size as needed */
    margin-bottom: 50px; /* Add some spacing between question and options */
    text-align: center; /* Center align the text */
  }

  .gif-container {
    margin-top: 20px; /* Add some margin to separate the result and the GIF */
  }
</style>



<div class="container">
  <div class="wrapper">
    <div class="box">
      <p class="resultcss">Here is the result of the Best Statistical method which you should apply: Thank Me later🤗</p>
      <p class="resultcss">{result}</p>
    </div>
  </div>
  <div class="gif-container">
    <img src="/giphy.gif" alt="Statistical Tests GIF" />
  </div>
</div>
