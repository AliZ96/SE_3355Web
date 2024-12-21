document.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('searchInput');
    const productItems = document.querySelectorAll('.product-item');

    searchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value.toLowerCase();
        productItems.forEach((item) => {
            const productName = item.querySelector('h3').textContent.toLowerCase();
            if (productName.includes(searchTerm)) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    });
});
