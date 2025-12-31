const toggleButton = document.getElementById('theme-toggle');
const htmlElement = document.documentElement; // Cible la balise <html>
const storageKey = 'bs-theme-mode';

/**
 * Définit le thème sur l'élément HTML et met à jour le texte du bouton.
 * @param {string} theme - 'light' ou 'dark'.
 */
function setTheme(theme) {
    htmlElement.setAttribute('data-bs-theme', theme);

    if (theme === 'dark') {
        toggleButton.innerHTML = '<i class="bi bi-sun-fill"></i>';
    } else {
        toggleButton.innerHTML = '<i class="bi bi-moon-stars"></i>';
    }
}

/**
 * 1. Vérification initiale : Charge le thème sauvegardé ou le thème système par défaut.
 */
function loadTheme() {
    const savedTheme = localStorage.getItem(storageKey);
    
    // Vérifie si l'utilisateur a une préférence enregistrée
    if (savedTheme) {
        setTheme(savedTheme);
    } else {
        // Sinon, vérifie si le système d'exploitation préfère le mode sombre
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        
        // Applique le thème système et le sauve pour les visites futures
        const initialTheme = prefersDark ? 'dark' : 'light';
        setTheme(initialTheme);
        localStorage.setItem(storageKey, initialTheme);
    }
}

/**
 * 2. Gestion du clic : Bascule et sauvegarde.
 */
function toggleTheme() {
    const currentTheme = htmlElement.getAttribute('data-bs-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';

    setTheme(newTheme);
    localStorage.setItem(storageKey, newTheme);
}

// 3. Initialisation
document.addEventListener('DOMContentLoaded', () => {
    loadTheme();
    
    if (toggleButton) {
        toggleButton.addEventListener('click', toggleTheme);
    }
});