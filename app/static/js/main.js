const siteHeader = document.querySelector('.site-header');
if (siteHeader) {
  const updateHeader = function () {
    siteHeader.classList.toggle('is-scrolled', window.scrollY > 12);
  };
  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive: true });
}

document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(function (element) {
  new bootstrap.Tooltip(element);
});

const menu = document.getElementById('menu');
if (menu) {
  menu.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      const offcanvas = bootstrap.Offcanvas.getInstance(menu);
      if (offcanvas) offcanvas.hide();
    });
  });
}

const toastElement = document.getElementById('toast-unfd');

document.querySelectorAll('.needs-validation').forEach(function (form) {
  form.addEventListener('submit', function (event) {
    event.preventDefault();

    if (!form.checkValidity()) {
      form.classList.add('was-validated');
      const firstInvalid = form.querySelector(':invalid');
      if (firstInvalid) firstInvalid.focus();
      return;
    }

    form.reset();
    form.classList.remove('was-validated');

    const modalElement = form.closest('.modal');
    if (modalElement) bootstrap.Modal.getOrCreateInstance(modalElement).hide();

    if (toastElement) {
      toastElement.querySelector('.toast-body').textContent = form.dataset.success;
      bootstrap.Toast.getOrCreateInstance(toastElement).show();
    }
  });
});
