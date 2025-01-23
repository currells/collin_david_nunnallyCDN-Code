// Select elements
const number1 = document.getElementById('number1');
const number2 = document.getElementById('number2');
const addButton = document.getElementById('addButton');
const result = document.getElementById('result');

// Add event listener to the button
addButton.addEventListener('click', () => {
  // Convert input values to numbers
  const num1 = parseFloat(number1.value || 0); // Default to 0 if empty
  const num2 = parseFloat(number2.value || 0); // Default to 0 if empty

  // Check if the inputs are valid numbers
  if (!isNaN(num1) && !isNaN(num2)) {
    const sum = num1 + num2; // Perform the addition
    result.textContent = sum; // Display the sum
  } else {
    result.textContent = 'Please enter valid numbers!';
  }
});
