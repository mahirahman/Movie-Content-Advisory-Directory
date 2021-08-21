// Check if user input is nothing/blank
// If so display an error message

function validateForm() {
    var x = document.forms["movie_input"]["movie_title"].value;
    if (x == "") {
      alert("Please search for a Movie or TV Show Title");
      return false;
    }
}

// Check for element with ID img-exists in scroll-container
// If element exists then display "Previous Searched Titles" text

window.onload = function(){
  var element = document.getElementById("img-exist");
  //If it isn't "undefined" and it isn't "null", then it exists.
  if (typeof(element) != 'undefined' && element != null){
    element = document.querySelector('.previous-searched');
    element.style.visibility = 'visible';
  }
  else {
    element = document.querySelector('.previous-searched');
    element.style.visibility = 'hidden';
  }
};

