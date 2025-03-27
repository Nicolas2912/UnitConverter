/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html"
  ],
  theme: {
    extend: {},
  },
  // Add daisyUI plugin
  plugins: [require("daisyui")],

  // Optional: DaisyUI configuration (themes, etc.)
  daisyui: {
    themes: ["light", "dark", "cupcake"], // You can specify themes you want to use
    // darkTheme: "dark", // name of one of the included themes for dark mode
    // base: true, // applies background color and foreground color for root element by default
    // styled: true, // include daisyUI colors and design decisions for all components
    // utils: true, // adds responsive and modifier utility classes
    // rtl: false, // rotate style direction from left-to-right to right-to-left. You also need to add dir="rtl" to your html tag and install `tailwindcss-flip` plugin for Tailwind CSS.
    // prefix: "", // prefix for daisyUI classnames (components, modifiers and responsive class names. Not colours)
    // logs: true, // Shows info about daisyUI version and used config in the console when building your CSS
  },
}