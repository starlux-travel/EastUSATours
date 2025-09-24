/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",   // 掃描 Django 模板
    "./**/templates/**/*.html",// 掃描 app 裡的模板
    "./static/**/*.js",        // 掃描靜態 JS
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
