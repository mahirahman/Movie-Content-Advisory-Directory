// Enable dark/light mode from button toggling
// Loads script after HTML DOM is loaded

document.addEventListener("DOMContentLoaded", function(){

  const btn = document.querySelector(".btn-toggle");
  const currentTheme = localStorage.getItem("theme");

  if (currentTheme == "dark") {
    document.body.classList.add("dark-theme");
  }
  
  btn.addEventListener("click", function () {
    document.body.classList.toggle("dark-theme");
  
    let theme = "light";
    if (document.body.classList.contains("dark-theme")) {
      theme = "dark";
    }
    localStorage.setItem("theme", theme);
  });
});

function LightDark() {
  document.getElementById("toggle").innerHTML = "Light-mode";
}