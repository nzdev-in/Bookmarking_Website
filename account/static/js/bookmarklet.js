const siteUrl = "https://127.0.0.1:8000/";
const styleUrl = siteUrl + 'static/css/bookmarklet.css';
const minWidth = 250;
const minHieght = 250;

//Load CSS
var head = document.getElementsByTagName('head')[0];
var link = document.createElement('link');
link.rel = 'stylesheet';
link.type = 'text/css';
link.href = styleUrl + '?r=' + Math.floor(Math.random()*999999999);
head.appendChild(link);

//Load HTML
var body = document.getElementsByTagName('body')[0];
boxHtml = `
<div id="bookmarklet">

    <div class="bookmarklet-header">

        <div class="bookmarklet-heading">
            <span class="bookmarklet-label">BOOKMARKS</span>
            <h1>Select an image</h1>
            <p>Choose something from this page worth keeping.</p>
        </div>

        <a href="#" id="close" aria-label="Close bookmarklet">
            &times;
        </a>

    </div>

    <div class="bookmarklet-divider"></div>

    <div class="images"></div>

</div>`;
body.insertAdjacentHTML('beforeend',boxHtml);

//bookmarklet launch function
function bookmarklet_launch(){
    bookmarklet = document.getElementById('bookmarklet');
    var imagesFound = bookmarklet.querySelector('.images');

    imagesFound.innerHTML = "";
    bookmarklet.style.display = 'block';
    bookmarklet.querySelector('#close').addEventListener('click',function(){
        bookmarklet.style.display = 'none';
    });
    //Find images in DOM with minimum dimensions
    images = document.querySelectorAll("img");
    images.forEach(image => {
        if(image.naturalWidth >= minWidth && image.naturalHeight >= minHieght){
            var imageFound = document.createElement('img');
            imageFound.src = image.currectSrc || image.src;
            imagesFound.append(imageFound)
        }
    })

    //select image event
    imagesFound.querySelectorAll("img").forEach(image => {
        image.addEventListener('click',function(event){
            imageSelected = event.target;
            bookmarklet.style.display = 'none';
            window.open(siteUrl + "images/create/?url=" + encodeURIComponent(imageSelected.src) + "&title" + encodeURIComponent(document.title), '_blank');
        })
    })



}

bookmarklet_launch();

