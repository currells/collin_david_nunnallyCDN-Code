// Select the dropdown and logo
const themeselector = document.getElementById("themeselector");
const logo = document.querySelector(".logo"); // Select the logo image

function changeTheme() {
    const theme = themeselector.value;
    
    if (theme === "dark") {
        document.body.classList.add("dark"); 
        logo.src = "byui-logo_white.png"; // Change to the dark mode logo
    } else {
        document.body.classList.remove("dark"); 
        logo.src = "byui-logo_blue.webp"; // Change back to the light mode logo
    }
}

// Listen for dropdown change
themeselector.addEventListener("change", changeTheme);
