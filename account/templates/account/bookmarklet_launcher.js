(function(){
    if(!window.bookmarklet){
        bookmarklet_js = document.body.appendChild(document.createElement("script"));
        bookmarklet_js.src = "https://bookmarking-website-1.onrender.com//static/js/bookmarklet.js?r=" + Math.floor(Math.random()*9999999);
        window.bookmarklet = true;
    }
    else{
        bookmarklet_launch();
    }
})();