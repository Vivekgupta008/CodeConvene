/** @type {import('tailwindcss').Config} */
export default {
    content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
    theme: {
        extend: {
            colors: {
                primary: {
                    DEFAULT: '#22c55e', // green-500
                    hover: '#16a34a', // green-600
                },
                dark: {
                    DEFAULT: '#09090b', // gray-950
                    lighter: '#18181b', // gray-900
                    card: '#27272a', // gray-800
                },
            },
            fontFamily: {
                sans: ['Inter', 'system-ui', 'sans-serif'],
            },
            animation: {
                'spin-slow': 'spin 8s linear infinite',
            },
        },
    },
    plugins: [],
};
