//setting up the elements to be used
const nameInput = document.getElementById("nameInput");
const nameQuery = document.getElementById("nameQuery");
const addButton = document.getElementById("addButton");
const clearButton = document.getElementById("clearButton");

// function to add item to the list and store in Local Storage

function addToList () {
  if (nameQuery.value != "") {
  const newItem = document.createElement("p");
  newItem.innerHTML = nameQuery.value + "!";
  nameInput.appendChild(newItem);
  }
}

function addToLocalStorage () {
  addToList ();
  if (nameQuery.value != "") {
  const position = localStorage.length + 1;
  localStorage.setItem (position, nameQuery.value + "!");
  nameQuery.value = "";
  }
}
  
// function to display items from local storage at refresh

function displaySavedItems() {
  for (let i = 1; i < localStorage.length +1; i++) {
    if (localStorage.getItem(i.toString()) !== null) {
        const savedItems = document.createElement("p");
        savedItems.innerHTML = localStorage.getItem(i.toString());
        nameInput.appendChild(savedItems);
      }
    }
  }


// function to clear local storage

function clearAll () {
  localStorage.clear();
  nameInput.innerHTML = "Welcome";
}

// adding the event listeners to the buttons
addButton.addEventListener("click", addToLocalStorage);
displaySavedItems();
clearButton.addEventListener("click", clearAll);
