(function () {
  const STORAGE_KEY = 'unfd-theme';
  const root = document.documentElement;

  function readTheme() {
    try {
      return localStorage.getItem(STORAGE_KEY);
    } catch (error) {
      return null;
    }
  }

  function saveTheme(theme) {
    try {
      localStorage.setItem(STORAGE_KEY, theme);
    } catch (error) {}
  }

  function syncButton(theme) {
    const button = document.querySelector('.theme-toggle');
    if (!button) return;

    const label = theme === 'dark' ? 'Ativar tema claro' : 'Ativar tema escuro';
    button.setAttribute('aria-label', label);
    button.setAttribute('data-bs-title', label);

    const tooltip = window.bootstrap && bootstrap.Tooltip.getInstance(button);
    if (tooltip) tooltip.setContent({ '.tooltip-inner': label });
  }

  function applyTheme(theme) {
    root.setAttribute('data-bs-theme', theme);
    syncButton(theme);
  }

  applyTheme(readTheme() === 'light' ? 'light' : 'dark');

  document.addEventListener('DOMContentLoaded', function () {
    const button = document.querySelector('.theme-toggle');
    syncButton(root.getAttribute('data-bs-theme'));
    if (!button) return;

    button.addEventListener('click', function () {
      const next = root.getAttribute('data-bs-theme') === 'dark' ? 'light' : 'dark';
      applyTheme(next);
      saveTheme(next);
    });
  });
})();
