const express = require('express');
const app = express();

function escapeHtml(str) {
    return str
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#39;");
}

app.get('/search', (req, res) => {
    const query = req.query.q || '';

    // FIX: Encode user input before embedding into HTML
    const safeQuery = escapeHtml(query);

    res.send(`
        <h1>Search Results</h1>
        <p>You searched for: ${safeQuery}</p>
    `);
});

app.listen(3000);