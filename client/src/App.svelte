<!-- App.svelte -->

<script>
    let message = '';
    let finalResult;
    let file = null; // Initialize file variable

    fetch('http://localhost:5000/')
        .then(response => response.json())
        .then(data => {
            message = data.message;
        });

    import Question from "./components/Question.svelte";
    import Result from "./components/Result.svelte";

    function handleFinalResult(event) {
        finalResult = event.detail.result;
    }


</script>

<main>
    <h1>{message}</h1>
    <div class="logo"></div>

    {#if finalResult === undefined}
        <Question id={0} on:finalResult={handleFinalResult} />
    {:else}
        <Result result={finalResult} />
    {/if}
</main>