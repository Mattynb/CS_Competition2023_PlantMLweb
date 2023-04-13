const form = document.querySelector('form');
const resultElement = document.querySelector('#result');

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(form);
    const response = await fetch('/predict', {
        method: 'POST',
        body: formData
    });

    const result = await response.text();
    resultElement.innerText = result;
});