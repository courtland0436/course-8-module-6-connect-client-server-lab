// Select the form and input elements
const form = document.querySelector("form");
const titleInput = document.querySelector("#title");
const eventList = document.querySelector("#event-list");

// Function to render a single event
function renderEvent(event) {
  const li = document.createElement("li");
  li.textContent = event.title;
  eventList.appendChild(li);
}

// Fetch and display all events on page load
fetch("http://127.0.0.1:5000/events")
  .then(response => response.json())
  .then(events => {
    events.forEach(renderEvent);
  })
  .catch(error => console.error("Error fetching events:", error));

// Handle form submission
form.addEventListener("submit", (e) => {
  e.preventDefault(); // Prevent page reload
  const title = titleInput.value.trim();

  if (!title) {
    alert("Please enter a title");
    return;
  }

  // Send POST request to Flask server
  fetch("http://127.0.0.1:5000/events", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ title })
  })
    .then(response => {
      if (!response.ok) {
        throw new Error("Failed to add event");
      }
      return response.json();
    })
    .then(newEvent => {
      renderEvent(newEvent); // Add the new event to the list
      titleInput.value = ""; // Clear input
    })
    .catch(error => console.error("Error submitting event:", error));
});
