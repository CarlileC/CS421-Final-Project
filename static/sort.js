
function sort(){
    var parentDiv = document.getElementById('main');
    var itemDivs = parentDiv.getElementsByTagName('div');
    var returnItems = [];
    for (i = 0; i < itemDivs.length; i++) {
        returnItems.push(itemDivs.item(i));
    }
    returnItems.sort(function(a, b) {
        var compA = a.getAttribute('id').toUpperCase(); //Sorting logic breaks on uppercase vs lower case
        var compB = b.getAttribute('id').toUpperCase();
        return (compA < compB) ? -1 : (compA > compB) ? 1 : 0; //JavaScript's sort function is weird, had to come up with my own logic but its the same as any other sort()
    });

    document.getElementById("bookLabel").innerHTML = ""; //This hides the labels when sorting by theme
    document.getElementById("gameLabel").innerHTML = "";
    for (i = 0; i < returnItems.length; i++) {
        parentDiv.appendChild(returnItems[i]); 
    }
}

function house(){
    var description = document.getElementById('coffeeDescription').innerText
    var comments = document.getElementById('comments').innerText
    blueHouseDescription = description.replaceAll("house", "<span style='color:blue;'>house</span>").replaceAll("minotaur", "<span style='color:red;'>Minotaur</span>")
    blueHouseComments = comments.replaceAll("house", "<span style='color:blue;'>house</span>").replaceAll("minotaur", "<span style='color:red;'>Minotaur</span>")
    document.getElementById('coffeeDescription').innerHTML = blueHouseDescription
    document.getElementById('comments').innerHTML = blueHouseComments
}