
// Makes the #menu-btn class toggle the .hide class when clicked
const menuButton = document.querySelector("#menu-btn");
function toggleMenu() {
    const menu = document.querySelector("#menu-list");
    menu.classList.toggle("hide");
}

menuButton.addEventListener("click", toggleMenu);


// Only resizes the image on a width more than 1000px; doesn't work on smaller screens
function handleResize() {
    const menu = document.querySelector("#menu-list");
    if (window.innerWidth > 1000) {
        menu.classList.remove("hide");
    } else {
        menu.classList.add("hide");
    }
}


// Made from given website, but generates the HTML code for the pop-up to work properly and display the full-screen image
function viewerTemplate(pic, alt) {
    return `
        <div class="viewer">
            <button class="close-viewer">❌</button>
            <img src="${pic}" alt="${alt}" class="full-screen-img">
        </div>`;
}


// This allows the image to pull up the full-screen image when the small image is clicked
function viewHandler(event) {
    if (event.target.tagName !== "IMG") return; //Only triggers on "img" and not anything else

    const clickedImage = event.target;
    const fullImageSrc = clickedImage.src.replace('-sm.jpeg', '-full.jpeg'); //Replaces the image with the full image when clicked

    document.body.insertAdjacentHTML("afterbegin", viewerTemplate(fullImageSrc, clickedImage.alt));

    const viewer = document.querySelector(".viewer");
    viewer.style.visibility = "visible";
    viewer.style.opacity = "1"; //Adds these setting when the image is clicked to the .css file

    document.querySelector(".close-viewer").addEventListener("click", closeViewer); 
}

document.querySelector(".gallery").addEventListener("click", viewHandler); //looks for clicks on any of the small images in the .gallery and executes the viewHandler function above


//Closes the big image when I click the x
function closeViewer() {
    document.querySelector(".viewer").remove();
}
