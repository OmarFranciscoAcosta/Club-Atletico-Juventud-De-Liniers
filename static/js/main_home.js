window.addEventListener('scroll', () => {
    const nav = document.querySelector('nav');
    if (window.scrollY > 82) {
        nav.style.top = '-82px'; // Mover la barra fuera de la pantalla
    } else {
        nav.style.top = '0';
    }
});
