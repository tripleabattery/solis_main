var nightmode = "";
$(function() {
    if(nightmode) {
        $("html").toggleClass("nightmode-on");
    }

    else if(!nightmode) {
        $("html").toggleClass("nightmode-off");
    }

    else {
        console.log("Error");
    }
});
