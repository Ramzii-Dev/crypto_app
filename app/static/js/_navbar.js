const menuIcon = document.querySelector('.hamburger-menu');
const sidebar = document.querySelector('.sidebar');
const darkbtn = document.querySelector('.dark');
const navColor = document.querySelectorAll('.nav-link');
const cartTable = document.querySelector('.table');
const awsomeColor = document.querySelectorAll('.awsome ');
let chemin = document.location.pathname;
let i ;
let j ;

const body = document.getElementById('body');


menuIcon.addEventListener('click',()=> {
    sidebar.classList.toggle("sidebar-click");
})
darkbtn.addEventListener('click',()=> {
    body.classList.toggle("body-dark");
    sidebar.classList.toggle("sidebar-color");
    if (chemin === '/compte/mes-commande/' ) {
        cartTable.classList.toggle("table-color");
    }
    for (i = 0;i<awsomeColor.length;i++){
        awsomeColor[i].classList.toggle("awsome-color");
    }
    for (j = 0;j<navColor.length;j++){
        navColor[j].classList.toggle("nav-color");
    }
    if(body.classList.contains('body-dark')){ //when the body has the class 'dark' currently
        localStorage.setItem('darkMode', 'disabled'); //store this data if dark mode is off
    }else{
        localStorage.setItem('darkMode', 'enabled'); //store this data if dark mode is on
    }
})



if(localStorage.getItem('darkMode') == 'enabled'){
   body.classList.toggle('body-dark');
   darkbtn.toggleAttribute('checked')
    sidebar.classList.toggle("sidebar-color");
    for (j = 0;j<navColor.length;j++){
        navColor[j].classList.toggle("nav-color");
    }
    if (chemin === '/compte/mes-commande/' ) {
        cartTable.classList.toggle("table-color");
    }
    for (i = 0;i<awsomeColor.length;i++){
        awsomeColor[i].classList.toggle("awsome-color");
    }
}
