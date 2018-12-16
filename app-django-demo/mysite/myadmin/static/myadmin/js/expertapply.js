window.onload = function () {
    var x = document.getElementsByClassName("flip-card");
    for (var i = 0; i < x.length; i++) {
        x[i].setAttribute("onclick", "window.location = 'http://127.0.0.1:8000/myadmin/expert_detail/'");
    }

}
