const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send(`
        <h1>Search Dashboard</h1>
        <form method="GET" action="/search">
            <input name="q" placeholder="Search..." />
            <button type="submit">Search</button>
        </form>
    `);
});

app.get('/search', (req, res) => {
    const query = req.query.q || '';

    // VULNERABLE: User input is directly embedded into HTML without encoding
    const html = `
        <h1>Search Results</h1>
        <p>You searched for: ${query}</p>
        <a href="/">Back</a>
    `;

    res.send(html);
});

app.listen(3000, () => {
    console.log('App running on http://localhost:3000');
});