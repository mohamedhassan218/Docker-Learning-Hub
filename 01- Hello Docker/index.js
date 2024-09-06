const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) =>
{
    res.send('Hello from containerized express.js');
});

app.get('/hello/:name', (req, res) =>
{
    const name = req.params.name;
    res.send(`Hello ${name} from containerized express.js`);
});

app.listen(port, () =>
{
    console.log(`Server running on http://localhost:${port}`);
});
