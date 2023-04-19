// Espera a que el DOM se cargue antes de ejecutar el código
document.addEventListener('DOMContentLoaded', () => {
  markLink();
});

// Esta función marca el enlace de navegación activo
function markLink() {

  // Obtiene todos los enlaces de navegación
  const navLinks = document.querySelectorAll('.nav-link');

  // Para cada enlace, agrega un evento de clic que elimina la clase 'active'
  navLinks.forEach(navLink => {
    navLink.addEventListener('click', () => {
      navLink.classList.remove('active');
    });
  });

  // Agrega la clase 'active' al enlace de categorías
  document.getElementById('nav-link-categories').classList.add('active');
}