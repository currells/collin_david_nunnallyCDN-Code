const newParagraph = document.createElement("p");
newParagraph.innerText = "Added with Javascript!";
document.body.appendChild(newParagraph);


// Creates an image element
const img = document.createElement("img");

//Sets src and alt to the new img 
img.setAttribute('src', 'https://picsum.photos/200'); 
img.setAttribute('alt', 'given image');

//Appends the new 'img' to the doccument
document.body.appendChild(img); 



// APPENDING ELEMENTS TO A HTML
 //Adding the needed section h2 header and p for what is being added to the html
const new_section = document.createElement('section');
const new_h2 = document.createElement('h2');
const new_p = document.createElement('p');

// Giving the h2 and p text
new_h2.innerText = "DOM Basics"; 
new_p.innerText = "This was added through JS!";

// Appending the new h2 and p to the section
new_section.appendChild(new_h2);
new_section.appendChild(new_p);

// Appending the new section (with everything) to the document
document.body.appendChild(new_section);