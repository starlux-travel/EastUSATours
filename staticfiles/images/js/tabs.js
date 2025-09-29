// static/js/tabs.js
document.addEventListener("DOMContentLoaded", function () {
  const tabs = document.querySelectorAll("[data-tab-target]");
  const tabContents = document.querySelectorAll("[data-tab-content]");

  tabs.forEach(tab => {
    tab.addEventListener("click", () => {
      const target = document.querySelector(tab.dataset.tabTarget);

      // 移除所有 active 樣式
      tabContents.forEach(content => {
        content.classList.add("hidden");
      });
      tabs.forEach(t => {
        t.classList.remove("active");
      });

      // 顯示被點到的內容
      target.classList.remove("hidden");
      tab.classList.add("active");
    });
  });
});
