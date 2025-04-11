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


// Boton para subir al inicio de la pagina
const btnSubir = document.getElementById("btn-subir");
window.addEventListener("scroll", () => {
    btnSubir.style.display = window.scrollY > 300 ? "block" : "none";
});

btnSubir.addEventListener("click", () => {
    document.documentElement.scrollTo({ top: 0, behavior: 'smooth' });
});