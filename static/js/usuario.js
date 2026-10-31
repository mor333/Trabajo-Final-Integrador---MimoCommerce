const serviceOptions = document.querySelectorAll('input[name="servicio"]');
const productOptions = document.querySelectorAll('input[name="productos"]');
const serviceDate = document.getElementById('service-date');
const dateSection = document.getElementById('fecha-servicio');
const productSection = document.getElementById('productos');
const selectedService = document.getElementById('selected-service');
const selectedDate = document.getElementById('selected-date');
const selectedProducts = document.getElementById('selected-products');
const clearSelection = document.getElementById('clear-selection');

function updateSelection() {
    const service = document.querySelector('input[name="servicio"]:checked');
    const products = [...document.querySelectorAll('input[name="productos"]:checked')];
    dateSection.hidden = !service;
    productSection.hidden = !service || !serviceDate.value;
    selectedService.textContent = service ? service.dataset.serviceName : 'Ningún servicio seleccionado';
    selectedDate.textContent = serviceDate.value ? serviceDate.value.split('-').reverse().join('/') : 'Fecha sin elegir';
    selectedProducts.textContent = `${products.length} ${products.length === 1 ? 'producto seleccionado' : 'productos seleccionados'}`;
    clearSelection.disabled = !service && !serviceDate.value && products.length === 0;
}

serviceOptions.forEach((option) => {
    let selectedBeforeInteraction = '';
    const label = option.closest('label');
    label.addEventListener('pointerdown', () => {
        selectedBeforeInteraction = document.querySelector('input[name="servicio"]:checked')?.value || '';
    });
    option.addEventListener('keydown', (event) => {
        if (event.code === 'Space') {
            selectedBeforeInteraction = document.querySelector('input[name="servicio"]:checked')?.value || '';
        }
    });
    option.addEventListener('click', () => {
        if (selectedBeforeInteraction === option.value) {
            window.setTimeout(() => {
                if (!option.checked) return;
                option.checked = false;
                serviceDate.value = '';
                productOptions.forEach((product) => { product.checked = false; });
                updateSelection();
            }, 0);
            return;
        }
        serviceDate.value = '';
        productOptions.forEach((product) => { product.checked = false; });
    });
    option.addEventListener('change', updateSelection);
});
serviceDate.addEventListener('change', updateSelection);
productOptions.forEach((option) => option.addEventListener('change', updateSelection));
clearSelection.addEventListener('click', () => {
    serviceOptions.forEach((option) => { option.checked = false; });
    serviceDate.value = '';
    productOptions.forEach((option) => { option.checked = false; });
    updateSelection();
});
updateSelection();