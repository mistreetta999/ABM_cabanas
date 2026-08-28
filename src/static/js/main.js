// Script principal para inicializar funciones comunes

document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ Frontend cargado correctamente.");

    // Navbar dinámica
    const navToggle = document.querySelector("#nav-toggle");
    const navMenu = document.querySelector("#nav-menu");

    if (navToggle && navMenu) {
        navToggle.addEventListener("click", () => {
            navMenu.classList.toggle("is-active");
        });
    }
});
