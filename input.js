const userInput = document.getElementById('user-input').value; // Get user input from an input field

// Validate and sanitize the user input as needed

const apiUrl = 'https://api.example.com/endpoint'; // API endpoint URL

const requestData = {
  // Construct the request data based on user input
  userInput: userInput
};

fetch(apiUrl, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(requestData) // Convert the request data to JSON
})
  .then(response => response.json()) // Parse the response data as JSON
  .then(data => {
    // Handle the API response data
    // Update the user interface with the received data
  })
  .catch(error => {
    // Handle errors that occur during the API call
    console.error('Error:', error);
  });
