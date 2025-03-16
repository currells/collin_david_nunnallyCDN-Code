document.addEventListener("DOMContentLoaded", () => {
  // Example Recipe Data
  const recipes = [
    {
      name: "Spaghetti Bolognese",
      description: "A classic Italian dish made with a rich and savory meat sauce.",
      image: "images/spaghetti-bolognese.jpg",
      rating: 4,
      tags: ["Italian", "Pasta", "Savory"],
      ingredients: ["Spaghetti", "Ground beef", "Tomato sauce", "Garlic"],
    },
    {
      name: "Chicken Alfredo",
      description: "Creamy alfredo sauce with tender chicken pieces and pasta.",
      image: "images/chicken-alfredo.jpg",
      rating: 5,
      tags: ["Italian", "Creamy", "Chicken"],
      ingredients: ["Chicken", "Alfredo sauce", "Fettuccine", "Garlic"],
    },
    {
      name: "Vegan Tacos",
      description: "Delicious and fresh tacos filled with plant-based ingredients.",
      image: "images/vegan-tacos.jpg",
      rating: 3,
      tags: ["Vegan", "Tacos", "Healthy"],
      ingredients: ["Tortillas", "Black beans", "Lettuce", "Avocado"],
    },
    {
      name: "Chocolate Cake",
      description: "A rich and moist chocolate cake with creamy frosting.",
      image: "images/chocolate-cake.jpg",
      rating: 5,
      tags: ["Dessert", "Chocolate"],
      ingredients: ["Cocoa powder", "Flour", "Sugar", "Eggs"],
    },
  ];

  // Function to get a random number
  function random(num) {
    return Math.floor(Math.random() * num);
  }

  // Function to get a random recipe from the list
  function getRandomListEntry(list) {
    return list[random(list.length)];
  }

  // Template for displaying tags
  function tagsTemplate(tags) {
    return tags.map(tag => `<li>${tag}</li>`).join('');
  }

  // Template for displaying ratings
  function ratingTemplate(rating) {
    let html = `<span class="rating" role="img" aria-label="Rating: ${rating} out of 5 stars">`;

    for (let i = 1; i <= 5; i++) {
      html += i <= rating
        ? `<span aria-hidden="true" class="icon-star">⭐</span>`
        : `<span aria-hidden="true" class="icon-star-empty">☆</span>`;
    }

    html += `</span>`;
    return html;
  }

  // Function to generate recipe HTML
  function recipeTemplate(recipe) {
    return `<figure class="recipe">
      <img src="${recipe.image}" alt="image of ${recipe.name}" />
      <figcaption>
        <ul class="recipe__tags">
          ${tagsTemplate(recipe.tags)}
        </ul>
        <h2><a href="#">${recipe.name}</a></h2>
        <p class="recipe__ratings">
          ${ratingTemplate(recipe.rating)}
        </p>
        <p class="recipe__description">${recipe.description}</p>
      </figcaption>
    </figure>`;
  }

  // Function to render recipes (display them on the page)
  function renderRecipes(recipeList) {
    const output = document.querySelector('#recipe-list');
    if (output) {
      output.innerHTML = recipeList.map(recipe => recipeTemplate(recipe)).join('');
    }
  }

  // Function to initialize the page with a random recipe
  function init() {
    const recipe = getRandomListEntry(recipes);
    renderRecipes([recipe]); // Render only one random recipe
  }

  // Function to filter recipes based on search query
  function filterRecipes(query) {
    console.log("Filtering recipes with query:", query); // Debugging line
    return recipes.filter(recipe => {
      return recipe.name.toLowerCase().includes(query) ||
        recipe.description.toLowerCase().includes(query) ||
        recipe.tags.some(tag => tag.toLowerCase().includes(query)) ||
        recipe.ingredients.some(ingredient => ingredient.toLowerCase().includes(query));
    }).sort((a, b) => a.name.localeCompare(b.name));
  }

  // Search functionality: handles the click event on the search button
  function searchHandler(e) {
    e.preventDefault();
    const query = document.querySelector('#search-input').value.toLowerCase(); // Get search input value
    console.log("Search button clicked. Query:", query); // Debugging line
    const filteredRecipes = filterRecipes(query); // Filter recipes based on the query
    renderRecipes(filteredRecipes); // Render the filtered recipes
  }

  // Event listener for the search button
  const searchButton = document.querySelector('#search-button');
  if (searchButton) {
    searchButton.addEventListener('click', searchHandler);
  }

  // Event listener for Enter key press to trigger search
  const searchInput = document.querySelector('#search-input');
  if (searchInput) {
    searchInput.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') {
        searchHandler(e);
      }
    });
  }

  // Initial page setup with a random recipe
  init();
});
