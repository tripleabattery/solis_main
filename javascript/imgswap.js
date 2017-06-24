var curimg = "";
var nextimg = "";
function imgswap(img, img2) {
    if(!curimg) {
        curimg = img;
        nextimg = img2;
    }

    else {
        var tmpimg = nextimg;
        nextimg = curimg;
        curimg = tmpimg;
    };

    document.getElementById('itempic').src = "/img/uploads/" + nextimg;
};
