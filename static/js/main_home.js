window.addEventListener('scroll', () => {
    const nav = document.querySelector('nav');
    if (window.scrollY > 82) {
        nav.style.top = '-82px'; // Mover la barra fuera de la pantalla
    } else {
        nav.style.top = '0';
    }
});


const opcionesPerfilButton = document.getElementById('OpcionesPerfilButton');
        const menuDesplegable = document.getElementById('MenuDesplegable');
      
        // Agrega un controlador de eventos al botón
        opcionesPerfilButton.addEventListener('click', () => {
          menuDesplegable.classList.toggle('active');
        });
      
        // Agrega un controlador de eventos al documento para cerrar el menú desplegable si se hace clic fuera de él
        document.addEventListener('click', (event) => {
          if (menuDesplegable.classList.contains('active') && event.target !== opcionesPerfilButton) {
            menuDesplegable.classList.remove('active');
          }
        });