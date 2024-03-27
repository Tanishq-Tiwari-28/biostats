<!-- Result.svelte -->
<script>
  export let result;
</script>

<style>
@import '../result.css';
</style>

<link href='https://fonts.googleapis.com/css?family=Lato:300,400,700' rel='stylesheet' type='text/css'>
  <link rel="stylesheet" href="/background.css">
  <div id='stars'></div>
  <div id='stars2'></div>
  <div id='stars3'></div>
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
