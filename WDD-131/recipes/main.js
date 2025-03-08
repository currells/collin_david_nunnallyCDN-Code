// Wait for the DOM to load before executing any code
document.addEventListener("DOMContentLoaded", () => {
    // Example Recipe Data (You can update this data or fetch it from an external source)
    const recipes = [
      {
        title: "Spaghetti Bolognese",
        description: "A classic Italian dish made with a rich and savory meat sauce.",
        image: "images/spaghetti-bolognese.jpg",
        rating: 4,
      },
      {
        title: "Chicken Alfredo",
        description: "Creamy alfredo sauce with tender chicken pieces and pasta.",
        image: "images/chicken-alfredo.jpg",
        rating: 5,
      },
      {
        title: "Vegan Tacos",
        description: "Delicious and fresh tacos filled with plant-based ingredients.",
        image: "images/vegan-tacos.jpg",
        rating: 3,
      },
      {
        title: "Chocolate Cake",
        description: "A rich and moist chocolate cake with creamy frosting.",
        image: "images/chocolate-cake.jpg",
        rating: 5,
      },
    ];
  
    // Function to create recipe elements dynamically
    function createRecipeElement(recipe) {
      const recipeElement = document.createElement("div");
      recipeElement.classList.add("recipe");
  
      // Create recipe title
      const titleElement = document.createElement("h2");
      titleElement.textContent = recipe.title;
      recipeElement.appendChild(titleElement);
  
      // Create recipe description
      const descriptionElement = document.createElement("p");
      descriptionElement.classList.add("description");
      descriptionElement.textContent = recipe.description;
      recipeElement.appendChild(descriptionElement);
  
      // Create recipe image
      const imageElement = document.createElement("img");
      imageElement.setAttribute("src", recipe.image);
      imageElement.setAttribute("alt", recipe.title);
      recipeElement.appendChild(imageElement);
  
      // Create recipe rating (using stars)
      const ratingElement = document.createElement("span");
      ratingElement.classList.add("rating");
      ratingElement.setAttribute("role", "img");
      ratingElement.setAttribute("aria-label", `Rating: ${recipe.rating} out of 5 stars`);
  
      // Add filled and empty stars based on rating
      for (let i = 0; i < 5; i++) {
        const star = document.createElement("span");
        star.classList.add(i < recipe.rating ? "icon-star" : "icon-star-empty");
        star.textContent = i < recipe.rating ? "⭐" : "☆";
        star.setAttribute("aria-hidden", "true");
        ratingElement.appendChild(star);
      }
      recipeElement.appendChild(ratingElement);
  
      return recipeElement;
    }
  
    // Function to display recipes on the page
    function displayRecipes(recipes) {
      const recipeContainer = document.querySelector(".recipes");
      recipeContainer.innerHTML = ""; // Clear any previous recipes
  
      recipes.forEach((recipe) => {
        const recipeElement = createRecipeElement(recipe);
        recipeContainer.appendChild(recipeElement);
      });
    }
  
    // Event listener for the search form (if implemented)
    const searchForm = document.querySelector(".search form");
    if (searchForm) {
      searchForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const searchQuery = event.target.querySelector("input").value.toLowerCase();
        
        // Filter recipes based on the search query
        const filteredRecipes = recipes.filter((recipe) =>
          recipe.title.toLowerCase().includes(searchQuery) ||
          recipe.description.toLowerCase().includes(searchQuery)
        );
        
        // Display the filtered recipes
        displayRecipes(filteredRecipes);
      });
    }
  
    // Initial display of all recipes
    displayRecipes(recipes);
  });
  