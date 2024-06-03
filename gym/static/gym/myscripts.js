function filterSelection(category) {
    var elements = document.getElementsByClassName("filterDiv");
    if (category === "all") category = "";

    // Loop through all elements and hide those who don't match the selected category
    for (var i = 0; i < elements.length; i++) {
        removeClass(elements[i], "show");
        if (elements[i].className.indexOf(category) > -1) {
            addClass(elements[i], "show");
        } else {
            addClass(elements[i], "hide");
        }
    }
}

// Show filtered elements
function addClass(element, name) {
    var arr1 = element.className.split(" ");
    var arr2 = name.split(" ");
    for (var i = 0; i < arr2.length; i++) {
        if (arr1.indexOf(arr2[i]) == -1) {
            element.className += " " + arr2[i];
        }
    }
}

// Hide elements that are not selected
function removeClass(element, name) {
    var arr1 = element.className.split(" ");
    var arr2 = name.split(" ");
    for (var i = 0; i < arr2.length; i++) {
        while (arr1.indexOf(arr2[i]) > -1) {
            arr1.splice(arr1.indexOf(arr2[i]), 1);
        }
    }
    element.className = arr1.join(" ");
}
