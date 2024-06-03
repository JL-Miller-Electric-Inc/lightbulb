function showContent(contentId) {
    var content = document.getElementById(contentId).innerHTML;
    document.getElementById('dynamic-content').innerHTML = content;
}

// Get all the <li> elements in the menu
var menuItems = document.querySelectorAll('#terminology-nav li');

// Loop through each <li> element
menuItems.forEach(function(item) {
  // Add click event listener to each <li> element
  item.addEventListener('click', function() {
    // Remove the 'active' class from all <li> elements
    menuItems.forEach(function(item) {
      item.classList.remove('active');
    });
    // Add the 'active' class to the clicked <li> element
    this.classList.add('active');
  });
});