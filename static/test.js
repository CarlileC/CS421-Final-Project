
function sort(){
    var parentDiv = document.getElementById('main');
    var itemDivs = parentDiv.getElementsByTagName('div');
    var returnItems = [];
    for (i = 0; i < itemDivs.length; i++) {
        returnItems.push(itemDivs.item(i));
    }
    returnItems.sort(function(a, b) {
        var compA = a.getAttribute('id').toUpperCase();
        var compB = b.getAttribute('id').toUpperCase();
        return (compA < compB) ? -1 : (compA > compB) ? 1 : 0;
    });

    document.getElementById("bookLabel").innerHTML = "";
    document.getElementById("gameLabel").innerHTML = "";
    for (i = 0; i < returnItems.length; i++) {
        parentDiv.appendChild(returnItems[i]);
    }
}