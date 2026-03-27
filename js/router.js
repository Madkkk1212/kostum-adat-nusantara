/**
 * Smart Router for Kostum Adat Nusantara
 * Menghilangkan .html di produksi (Vercel) tapi tetap berfungsi di lokal (Live Server).
 */
(function () {
    const hostname = window.location.hostname;
    const isLocal = hostname === 'localhost' || hostname === '127.0.0.1' || window.location.protocol === 'file:';
    const path = (window.location.pathname || '').replace(/\\/g, '/');
    
    // --- 1. REDIRECT LOGIC (Produksi Saja) ---
    // Di Vercel: Jika URL mengandung .html, redirect ke versi bersih tanpa ekstensi.
    if (!isLocal && path.endsWith('.html') && !path.endsWith('/navbar.html')) {
        const newPath = path.replace(/\.html$/, '');
        window.location.replace(newPath);
        return;
    }

    // --- 2. CLICK INTERCEPTOR (Lokal Saja) ---
    // Di Live Server: Jika klik link tanpa .html, tambahkan secara otomatis agar tidak 404.
    if (isLocal) {
        document.addEventListener('click', function(e) {
            const link = e.target.closest('a');
            if (!link) return;
            
            const href = link.getAttribute('href');
            // Cek jika link internal dan tidak punya tanda titik (.) alias tidak punya ekstensi
            if (href && 
                !href.startsWith('http') && 
                !href.startsWith('#') && 
                !href.startsWith('mailto:') && 
                !href.startsWith('tel:') && 
                !href.includes('.')) {
                
                e.preventDefault();
                window.location.href = href + '.html' + (window.location.search || '') + (window.location.hash || '');
            }
        });
    }
})();
