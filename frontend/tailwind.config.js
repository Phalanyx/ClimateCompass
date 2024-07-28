/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',  // Include all files in pages directory and its subdirectories
    './components/**/*.{js,ts,jsx,tsx,mdx}', // Include all files in components directory and its subdirectories
    './app/**/*.{js,ts,jsx,tsx,mdx}',  // Include all files in app directory and its subdirectories
    './*.{js,ts,jsx,tsx,mdx}',  // Include any root level JS/TS/JSX/TSX/MDX files
  ],
  theme: {
    extend: {
      colors: {
        green: {
          50: '#30AF5B',
          90: '#292C27',
          Figma: '#14AE5C'
        },
        gray: {
          10: '#EEEEEE',
          20: '#A2A2A2',
          30: '#7B7B7B',
          50: '#585858',
          90: '#141414',
        },
        orange: {
          50: '#FF814C',
        },
        blue: {
          70: '#021639',
        },
        yellow: {
          50: '#FEC601',
        },
        earth_green: '#78866B', 
        light_green: '#A9BA9D', 
        slate_green: '#D0D9CD', 
        lighter_gray: '#B2BEB5', 
        darker_gray: '#828E84'
      },
      backgroundImage: {
        'bg-img-1': "url('/img-1.png')",
        'bg-img-2': "url('/img-2.png')",
        'feature-bg': "url('/feature-bg.png')",
        pattern: "url('/pattern.png')",
        'pattern-2': "url('/pattern-bg.png')",
      },
      screens: {
        xs: '400px',
        '3xl': '1680px',
        '4xl': '2200px',
      },
      maxWidth: {
        '10xl': '1512px',
      },
      borderRadius: {
        '5xl': '40px',
      },
    },
  },
  plugins: [],
};
