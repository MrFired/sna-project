// Get references to divs where text will be inserted
const div1 = document.querySelector('.column:nth-of-type(1) .text');
const div2 = document.querySelector('.column:nth-of-type(2) .text');
const div3 = document.querySelector('.column:nth-of-type(3) .text');

// Store file paths in variables
let file1 = "/static/Sergey.txt";
let file2 = "/static/Daria.txt";
let file3 = "/static/Rostislav.txt";

// Load contents of text files
fetch(file1)
    .then(response => response.text())
    .then(text => {
        // Split content by line breaks and create a <p> element for each line
        const lines = text.split('\n');
        const paragraphs = lines.map(line => `<p>${line}</p>`);

        // Set HTML content of div
        div1.innerHTML += paragraphs.join('');
    });

fetch(file2)
    .then(response => response.text())
    .then(text => {
        const lines = text.split('\n');
        const paragraphs = lines.map(line => `<p>${line}</p>`);

        div2.innerHTML += paragraphs.join('');
    });

fetch(file3)
    .then(response => response.text())
    .then(text => {
        const lines = text.split('\n');
        const paragraphs = lines.map(line => `<p>${line}</p>`);

        div3.innerHTML += paragraphs.join('');
    });