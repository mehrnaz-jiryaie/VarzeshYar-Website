function filterSelection(category) {
    var elements = document.getElementsByClassName("filterDiv");
    if (category === "all") category = "";

    for (var i = 0; i < elements.length; i++) {
        removeClass(elements[i], "show");
        if (elements[i].className.indexOf(category) > -1) {
            addClass(elements[i], "show");
        } else {
            addClass(elements[i], "hide");
        }
    }
}

function addClass(element, name) {
    var arr1 = element.className.split(" ");
    var arr2 = name.split(" ");
    for (var i = 0; i < arr2.length; i++) {
        if (arr1.indexOf(arr2[i]) == -1) {
            element.className += " " + arr2[i];
        }
    }
}

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

function display_contact_info(num) {
    var phone_numbr = document.getElementsByClassName("contact-info")[num].innerHTML;
    document.getElementsByClassName("display-info")[num].innerHTML = phone_numbr;
    document.getElementsByClassName("display-info")[num].classList.add("displayed-info");
}




function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}