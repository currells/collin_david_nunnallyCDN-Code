const reviews = [
    {
        title: "The Great Gatsby",
        author: "F. Scott Fitzgerald",
        review: "A classic novel about wealth, love, and the American Dream.",
        image:  "images/great-gatsby-cover-1.webp"
    },
    {
        title: "To Kill a Mockingbird",
        author: "Harper Lee",
        review: "A powerful novel about race, justice, and moral growth.",
        image: "images/To-Kill-a-Mockingbird-by-harper-lee-book-cover-e1553130216100.webp"
    },
    {
        title: "1984",
        author: "George Orwell",
        review: "A dystopian classic that explores surveillance and totalitarianism.",
        image: "images/9780451524935.RH.0.l.webp"
    }
];

const reviewsSection = document.getElementById("reviews");

reviews.forEach(book => {
    const article = document.createElement("article");
    article.classList.add("review");

    article.innerHTML = `
        <h2>${book.title}</h2>
        <img src="${book.image}" alt="${book.title} cover" class="book-cover">
        <p><strong>Author:</strong> ${book.author}</p>
        <p><strong>Review:</strong> ${book.review}</p>
    `;

    reviewsSection.appendChild(article);
});
