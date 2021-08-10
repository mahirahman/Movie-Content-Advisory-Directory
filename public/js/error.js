// Check if user input is nothing/blank
// If so display an error message

function validateForm() {
    var x = document.forms["movie_input"]["movie_title"].value;
    if (x == "") {
      alert("Please search for a Movie or TV Show Title");
      return false;
    }
}