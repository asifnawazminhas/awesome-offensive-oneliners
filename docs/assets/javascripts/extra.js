(() => {
  const focusSearch = () => {
    const input = document.querySelector('[data-md-component="search-query"]');
    if (input) {
      const toggle = document.querySelector('[data-md-component="search"] label.md-header__button');
      if (toggle && !input.offsetParent) toggle.click();
      setTimeout(() => input.focus(), 30);
    }
  };

  const enhance = () => {
    document.querySelectorAll('.ol-search-launch').forEach((el) => {
      if (el.dataset.bound) return;
      el.dataset.bound = '1';
      el.addEventListener('click', focusSearch);
      el.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); focusSearch(); }
      });
    });

    document.querySelectorAll('.md-typeset p').forEach((p) => {
      if (p.classList.contains('ol-meta')) return;
      const text = p.textContent.trim();
      const m = text.match(/^Tool:\s*(.*?)\s*·\s*Platform:\s*(.*?)\s*·\s*Tags:\s*(.*?)(?:\s*·\s*Context:\s*(.*))?$/);
      if (!m) return;
      p.className = 'ol-meta';
      p.innerHTML = '';
      const rows = [['Tool',m[1]],['Platform',m[2]],['Tags',m[3]]];
      if (m[4]) rows.push(['Context',m[4]]);
      rows.forEach(([label,value]) => {
        const chip = document.createElement('span');
        chip.className = 'ol-chip' + (label === 'Context' ? ' ol-chip-context' : '');
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
