const sidebar = document.querySelector(".sidebar");
const closeBtn = document.querySelector("#btn");

// Al cargar, si quieres que empiece cerrado:
// sidebar.classList.add("close");

closeBtn.addEventListener("click", () => {
    sidebar.classList.toggle("close");
    menuBtnChange();
});

function menuBtnChange() {
    const icon = closeBtn.querySelector("i");

    if (sidebar.classList.contains("close")) {
        icon.classList.replace("fa-bars", "fa-bars"); // puedes cambiar por otro si quieres
    } else {
        icon.classList.replace("fa-bars", "fa-bars");
    }
}

/* ====== CAMBIO DE SECCIONES ====== */

function mostrarSeccion(seccion) {
    const contenido = document.getElementById("contenido");

    if (seccion === "inicio") {
        contenido.innerHTML = `
            <h1>Dashboard</h1>
            <p>Bienvenido al panel principal.</p>
        `;
    } 
    else if (seccion === "usuario") {
        contenido.innerHTML = `
            <h1>Usuarios</h1>
            <p>Aquí puedes gestionar los usuarios del sistema.</p>
        `;
    } 
    else if (seccion === "archivos") {
        contenido.innerHTML = `
            <h1>Archivos</h1>
            <p>Gestión de archivos y documentos.</p>
        `;
    }
}
