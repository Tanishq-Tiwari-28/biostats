<!-- Result.svelte -->
<script>
  export let result;
</script>

<style>
  /* Add your CSS styles here */
  .result-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: auto; /* Adjust height to fit content */
    margin-top: 20px; /* Add some margin to separate the result and the GIF */
    font-family: 'Your Fancy Font', cursive;
  }

  .result-container p {
    font-size: 30px;
    color: #333;
    text-align: center; /* Center align the result text */
  }

  .gif-container {
    margin-top: 20px; /* Add some margin to separate the result and the GIF */
  }
</style>

<div class="result-container">
  <p>Here is the result of the Best Statistical method which you should apply: Thank Me later🤗</p>
  <p>{result}</p>
  
  <!-- Embed the Tenor GIF using an iframe -->
  <div class="gif-container">
    <img src="/giphy.gif" alt="Statistical Tests GIF" />
  </div>
</div>
