(() => {
  const focusSearch = (query = '') => {
    const input = document.querySelector('[data-md-component="search-query"]');
    if (input) {
      const toggle = document.querySelector('[data-md-component="search"] label.md-header__button');
      if (toggle && !input.offsetParent) toggle.click();
      setTimeout(() => {
        input.focus();
        if (query) {
          input.value = query;
          input.dispatchEvent(new Event('input', { bubbles: true }));
        }
      }, 30);
    }
  };

  const enhance = () => {
    document.querySelectorAll('.ol-search-launch').forEach((el) => {
      if (el.dataset.bound) return;
      el.dataset.bound = '1';
      el.addEventListener('click', () => focusSearch());
      el.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); focusSearch(); }
      });
    });

    document.querySelectorAll('[data-ol-random]').forEach((el) => {
      if (el.dataset.bound) return;
      el.dataset.bound = '1';
      el.addEventListener('click', () => {
        const links = [...document.querySelectorAll('.ol-mini-card a[href]')]
          .map(a => a.href)
          .filter(h => h && !h.includes('#'));
        if (links.length) window.location.href = links[Math.floor(Math.random() * links.length)];
      });
    });

    document.querySelectorAll('[data-ol-search]').forEach((el) => {
      if (el.dataset.bound) return;
      el.dataset.bound = '1';
      el.addEventListener('click', () => focusSearch(el.dataset.olSearch || ''));
    });

    document.querySelectorAll('.md-clipboard').forEach((btn) => {
      if (btn.dataset.olCopyBound) return;
      btn.dataset.olCopyBound = '1';
      btn.addEventListener('click', () => {
        let toast = document.querySelector('.ol-copy-toast');
        if (!toast) {
          toast = document.createElement('div'); toast.className = 'ol-copy-toast'; toast.textContent = 'Copied'; document.body.appendChild(toast);
        }
        toast.classList.add('show');
        clearTimeout(window.__olCopyTimer);
        window.__olCopyTimer = setTimeout(() => toast.classList.remove('show'), 900);
      });
    });

    document.querySelectorAll('.md-typeset p').forEach((p) => {
      if (p.classList.contains('ol-meta')) return;
      const raw = p.textContent.trim();
      if (!raw.startsWith('Tool:')) return;
      const pieces = raw.split(/\s*·\s*/);
      const rows = [];
      for (const piece of pieces) {
        const m = piece.match(/^(Tool|Platform|Tags|Context|Requires|Noise|Version):\s*(.+)$/i);
        if (m) rows.push([m[1][0].toUpperCase() + m[1].slice(1).toLowerCase(), m[2]]);
      }
      if (!rows.length) return;
      p.className = 'ol-meta'; p.innerHTML = '';
      rows.forEach(([label,value]) => {
        const chip = document.createElement('span');
        chip.className = 'ol-chip' + (label === 'Context' ? ' ol-chip-context' : '') + (label === 'Requires' ? ' ol-chip-requires' : '') + (label === 'Version' ? ' ol-chip-version' : '') + (label === 'Noise' ? ' ol-chip-noise-' + value.toLowerCase().replace(/[^a-z]+/g,'-') : '');
        const b = document.createElement('b'); b.textContent = label;
        chip.appendChild(b); chip.appendChild(document.createTextNode(' ' + value));
        p.appendChild(chip);
      });
    });
  };

  document.addEventListener('keydown', (event) => {
    const active = document.activeElement;
    if (event.key === '/' && !['INPUT','TEXTAREA'].includes(active?.tagName) && !active?.isContentEditable) {
      event.preventDefault(); focusSearch();
    }
  });
  if (typeof document$ !== 'undefined') document$.subscribe(enhance);
  else document.addEventListener('DOMContentLoaded', enhance);
})();
