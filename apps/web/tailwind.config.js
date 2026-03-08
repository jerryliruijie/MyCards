/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}"
  ],
  theme: {
    extend: {
      colors: {
        ink: "#0f172a",
        panel: "#f8fafc",
        line: "#cbd5e1",
        gain: "#166534",
        loss: "#991b1b"
      }
    }
  },
  plugins: [],
};
