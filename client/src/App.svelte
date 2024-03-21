<script>
    let message = '';

    fetch('http://localhost:5000/api/data')
        .then(response => response.json())
        .then(data => message = data.message);
</script>

<main>
    <h1>{message}</h1>
</main>
