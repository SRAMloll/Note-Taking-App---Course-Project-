//setting up the elements to be used
const nameInput = document.getElementById("nameInput");
const nameQuery = document.getElementById("nameQuery");
const addButton = document.getElementById("addButton");


// function to add item to the list and store in Local Storage

function addToList () {
  if (nameQuery.value != "") {
  const newItem = document.createElement("p");
  newItem.innerHTML = "Welcome " + nameQuery.value + "!";
  nameInput.innerHTML= newItem.innerHTML;
  }
}

function addToLocalStorage () {
  addToList ();
  if (nameQuery.value != "") {
  const position = localStorage.length + 1;
  localStorage.setItem (position, "Welcome back " + nameQuery.value + "!");
  nameQuery.value = "";
  }
}
  
// function to display items from local storage at refresh

function displaySavedItems() {
  for (let i = 1; i < localStorage.length +1; i++) {
    if (localStorage.getItem(i.toString()) !== null) {
        const savedItems = document.createElement("p");
        savedItems.innerHTML = localStorage.getItem(i.toString());
        nameInput.innerHTML = savedItems.innerHTML;
      }
    }
  }




// adding the event listeners to the buttons
addButton.addEventListener("click", addToLocalStorage);
displaySavedItems();

