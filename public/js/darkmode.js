document.addEventListener("DOMContentLoaded", function () {
  const btn = document.querySelector(".btn-toggle");
  const currentTheme = localStorage.getItem("theme");

  if (currentTheme === "dark") {
    document.body.classList.add("dark-theme");
  }

  btn.addEventListener("click", toggleDarkTheme);
});

function toggleDarkTheme() {
  document.body.classList.toggle("dark-theme");

  const theme = document.body.classList.contains("dark-theme") ? "dark" : "light";
  localStorage.setItem("theme", theme);
}

function setLightDarkButtonText() {
  document.getElementById("toggle").innerHTML = "Light-mode";
}
