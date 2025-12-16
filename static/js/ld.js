function switchSlider(enabled) {
    slider = document.getElementById('home-page-slider');
    if (enabled) {
        slider.style.display = 'block';
    } else {
        slider.style.display = 'none';
    }
}

function switchPromo(enabled, id) {
    promo = document.getElementById('coffee-promo-' + id);
    if (enabled) {
        promo.style.display = 'block';
    } else {
        promo.style.display = 'none';
    }
}

function switchSection() {
    section = document.getElementById('coffee-promo-section');
    promo1 = document.getElementById('coffee-promo-1');
    promo2 = document.getElementById('coffee-promo-2');
    if (promo1.style.display !== 'none' || promo2.style.display !== 'none') {
        section.style.display = 'block';
    } else {
        section.style.display = 'none';
    }
}

function getBannerText() {
    fetch('/api/banner')
        .then(response => response.json())
        .then(data => {
            const bannerText = data.primaryBanner;
            const heroBanner = document.getElementById('hero-banner');
            heroBanner.textContent = bannerText;
        })
        .catch(error => {
            console.error('Error fetching banner text:', error);
        });
}