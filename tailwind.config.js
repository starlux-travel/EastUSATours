module.exports = {
  content: [
    "./templates/**/*.html",                // 專案全域 templates
    "./eastusatours/templates/**/*.html",   // 主 app
    "./tours/templates/**/*.html",          // tours app
    "./cruise/templates/**/*.html",         // cruise app
    "./accounts/templates/**/*.html",       // accounts app
    "./**/templates/**/*.html",             // 保險，全域 templates
    "./static/src/**/*.{js,ts,css,jsx,tsx}" // 前端 js / css
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
