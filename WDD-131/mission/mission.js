const themeselector = document.getElementById("themeselector");
const logo = document.querySelector(".logo");

function changeTheme() {
    const theme = themeselector.value;
    
    if (theme === "dark") {
        document.body.classList.add("dark"); 
        logo.src = "byui-logo_white.png";
    } else {
        document.body.classList.remove("dark"); 
        logo.src = "byui-logo_blue.webp";
    }
}


themeselector.addEventListener("change", changeTheme);
