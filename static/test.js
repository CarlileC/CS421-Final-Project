
function sort(){
    var mylist = document.getElementById('main');
    var divs = mylist.getElementsByTagName('div');
    var listitems = [];
    for (i = 0; i < divs.length; i++) {
        listitems.push(divs.item(i));
    }
    listitems.sort(function(a, b) {
        var compA = a.getAttribute('id').toUpperCase();
        var compB = b.getAttribute('id').toUpperCase();
        return (compA < compB) ? -1 : (compA > compB) ? 1 : 0;
    });

    document.getElementById("bookLabel").innerHTML = "";
    document.getElementById("gameLabel").innerHTML = "";
    for (i = 0; i < listitems.length; i++) {
        mylist.appendChild(listitems[i]);
    }
}