const themeselector = document.getElementById("themeselector");

function changeTheme() {

    const theme = themeselector.value;
    
    if (theme === "dark") {
        document.body.classList.add("dark");
    } else {
        document.body.classList.remove("dark");
    }
}

themeselector.addEventListener("change", changeTheme);
