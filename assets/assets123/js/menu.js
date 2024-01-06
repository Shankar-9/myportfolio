var nav = document.querySelector('nav');
var button = document.querySelector('.hamburger-menu')
button.addEventListener('click', (event) => {
    nav.classList.toggle('open')
})


window.onscroll=()=>{
    let header=document.querySelector('header');
    header.classList.toggle("sticky", window.scrollY>100);
}


    var preloader = document.querySelector(".preloader");
    setTimeout(function() {
        preloader.style.opacity='.8';
        preloader.style.display = "none";
    }, 3000);



