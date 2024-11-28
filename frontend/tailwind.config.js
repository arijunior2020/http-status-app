/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{js,jsx,ts,tsx}'], // Verifica arquivos dentro do diretório src
  theme: {
    extend: {
      colors: {
        primary: '#1F2937', // Cinza escuro
        secondary: '#FFA500', // Verde neon
        accent: '#3B82F6', // Azul neon
      },
    },
  },
  plugins: [],
};
