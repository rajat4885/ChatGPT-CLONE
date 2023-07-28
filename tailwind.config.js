/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.html"],
  theme: {
    extend: {
      colors:{
        chatwhite: {50: '#d9d9e3cc'},
        butcolor:{30:'#F7F7F8'},
        hovvolor:{20:'#F0F5FF'},
        shadowcol:{10: '#E5E5E5'},
        lefcolor:{40:'#202123'}
      }
    },
  },
  plugins: [],
}

