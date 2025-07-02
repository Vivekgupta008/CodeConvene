import React from 'react';
import Hero from '../components/sections/Hero';
import Features from '../components/sections/Features';
import HowItWorks from '../components/sections/HowItWorks';
import Integrations from '../components/sections/Integrations';
import Waitlist from '../components/sections/Waitlist';
import Footer from '../components/layout/Footer';
import Navbar from '../components/layout/Navbar';

const Landing: React.FC = () => {
    return (
        <div className="min-h-screen bg-dark">
            <Navbar />
            <main>
                <Hero />
                <Features />
                <HowItWorks />
                <Integrations />
                <Waitlist />
            </main>
            <Footer />
        </div>
    );
};

export default Landing;