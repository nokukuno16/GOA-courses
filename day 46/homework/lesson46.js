const burger = document.getElementById('burger');
const navLinks = document.getElementById('navLinks');

// Toggle nav and animate burger on click
burger.addEventListener('click', () => {
    navLinks.classList.toggle('nav-active');
    burger.classList.toggle('toggle');
});
