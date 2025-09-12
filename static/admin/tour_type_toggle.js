(function () {
  function qs(s) { return document.querySelector(s); }
  function qsa(s) { return document.querySelectorAll(s); }

  function toggleByType(value) {
    var busSets = qsa('fieldset.bus-only');
    var cruiseSets = qsa('fieldset.cruise-only');

    busSets.forEach(fs => fs.style.display = 'none');
    cruiseSets.forEach(fs => fs.style.display = 'none');

    if (value === 'bus_tour') busSets.forEach(fs => fs.style.display = '');
    if (value === 'cruise_tour') cruiseSets.forEach(fs => fs.style.display = '');
  }

  function init() {
    var select = qs('#id_tour_type');
    if (!select) return;
    toggleByType(select.value);
    select.addEventListener('change', function () { toggleByType(this.value); });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
