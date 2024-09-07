const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();
const port = 3000;

// Set the notes file path
const notesFile = path.join("/app", 'notes.txt');

// To parse JSON bodies
app.use(express.json());

// Route to add a note.
app.post('/add-note', (req, res) =>
{
    const note = req.body.note;
    if (!note)
    {
        return res.status(400).send('Note is required');
    }

    fs.appendFile(notesFile, note + '\n', (err) =>
    {
        if (err)
        {
            return res.status(500).send('Error saving the note');
        }
        res.send('Note saved!');
    });
});

// Route to view notes.
app.get('/notes', (req, res) =>
{
    fs.readFile(notesFile, 'utf8', (err, data) =>
    {
        if (err)
        {
            return res.status(500).send('Error reading the notes');
        }
        res.send(data || 'No notes available');
    });
});

app.listen(port, () =>
{
    console.log(`Server running on http://localhost:${port}`);
});
