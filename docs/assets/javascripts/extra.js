document.addEventListener('DOMContentLoaded', () => {
  const focusSearch = () => {
    const input = document.querySelector('[data-md-component="search-query"]');
    if (input) input.focus();
  };
  document.addEventListener('keydown', (event) => {
    if (event.key === '/' && !['INPUT','TEXTAREA'].includes(document.activeElement.tagName)) {
      event.preventDefault();
      focusSearch();
    }
  });
});
