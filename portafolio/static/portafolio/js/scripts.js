// Ocultar el navbar al bajar y mostrarlo al subir
let prevScrollPosicion = window.pageYOffset;
const navbar = document.getElementById("navbar");
window.onscroll = function () {
    let actualScrollPosicion = window.pageYOffset;
    if(prevScrollPosicion > actualScrollPosicion) {
        navbar.style.top = "0";
    } else {
        navbar.style.top = "-180px"; // Depende del ancho de la barra
    }
    prevScrollPosicion = actualScrollPosicion;
};