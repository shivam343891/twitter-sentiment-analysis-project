// Function to animate the output message
function animateOutputMessage() {
  var outputElement = document.querySelector(".output");
  outputElement.classList.add("animated", "bounce");
  setTimeout(function() {
      outputElement.classList.remove("animated", "bounce");
  }, 1000);
}

// Call the animateOutputMessage function when the form is submitted
document.querySelector(".form").addEventListener("submit", function() {
  animateOutputMessage();
});

// Get the date and time elements
var dateElement = document.getElementById("date");
var timeElement = document.getElementById("time");

// Update the date and time every second
setInterval(updateDateTime, 1000);

// Function to update the date and time
function updateDateTime() {
  var now = new Date();

  // Format the date as "Month Day, Year"
  var options = { year: "numeric", month: "long", day: "numeric" };
  var formattedDate = now.toLocaleDateString(undefined, options);

  // Format the time as "Hours:Minutes:Seconds"
  var formattedTime = now.toLocaleTimeString();

  // Update the date and time elements
  dateElement.textContent = formattedDate;
  timeElement.textContent = formattedTime;
}

function showResults() {
  // Make an AJAX request to the '/results' URL
  fetch('/results')
    .then(function(response) {
      // Check if the response was successful
      if (response.ok) {
        // Redirect the page to the '/results' URL
        window.location.href = '/results';
      } else {
        console.error('Error retrieving results');
      }
    })
    .catch(function(error) {
      console.error('Error:', error);
    });
}