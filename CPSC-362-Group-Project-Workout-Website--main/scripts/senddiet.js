function getFoodItems(event) {
  event.preventDefault(); // Prevent form submission
  const formData = new FormData(document.querySelector('form'));
  
  // Convert form data to JSON object (if needed)
  var jsonData = {};
  formData.forEach((value, key) => {
    jsonData[key] = value;
  });
  
  const foodGroup = document.getElementById('food_group').value;

  fetch('http://127.0.0.1:5000/send_diet', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ food_group: foodGroup })
  })
  .then(response => response.text()) // Receive HTML response instead of JSON
  .then(data => {
      var mess = document.getElementById('diet');
      mess.innerHTML = data; // Insert HTML content into the 'diet' element
  })
  .catch((error) => {
    alert(error);
    // Optionally, show an error message to the user
  });
}
