function submitInput() {
    const input = document.getElementById("input-box").value;
  
    const apiUrl = "http://127.0.0.1:5000/process-user-input";
  
    const requestData = {
      input: input,
    };
  
    fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(requestData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Response:", data);
        displayResponse(data.message);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }
  
  function displayResponse(output) {
    const outputBox = document.getElementById("output-box");
    outputBox.value = output;
  }
  