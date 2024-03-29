/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/frontend/templates/**/*.{html,j2}",
    "./src/frontend/static/**/*.js",
  ],
  theme: {
    extend: {
      fontFamily: {
        'monda': ['Monda', 'sans-serif']
      },
    },
  },
  plugins: [],
}
