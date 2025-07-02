import React from 'react';
import { Github, Twitter, Linkedin } from 'lucide-react';
import { useLocation, Link } from 'react-router-dom';

const Footer: React.FC = () => {
    const currentYear = new Date().getFullYear();
    const location = useLocation();
    const isHomePage = location.pathname === '/';

    return (
        <footer className="bg-dark-lighter py-12">
            <div className="container mx-auto px-6">
                <div className="flex flex-col md:flex-row justify-between items-start mb-8">
                    <div className="mb-6 md:mb-0">
                        <h3 className="text-2xl font-bold gradient-text mb-2">CodeConvene.AI</h3>
                        <p className="text-gray-400 text-sm max-w-xs">
                            Revolutionizing developer relations with AI-powered community management.
                        </p>
                    </div>
                    <div className="flex flex-row gap-12">
                        <div>
                            <h4 className="font-medium mb-3 text-white">Links</h4>
                            <ul className="space-y-2">
                                <li><a href={isHomePage ? "#features" : "/#features"} className="text-gray-400 hover:text-primary text-sm">Features</a></li>
                                <li><a href={isHomePage ? "#how-it-works" : "/#how-it-works"} className="text-gray-400 hover:text-primary text-sm">How It Works</a></li>
                                <li><a href={isHomePage ? "#integrations" : "/#integrations"} className="text-gray-400 hover:text-primary text-sm">Integrations</a></li>
                                <li><a href={isHomePage ? "#waitlist" : "/#waitlist"} className="text-gray-400 hover:text-primary text-sm">Join Waitlist</a></li>
                            </ul>
                        </div>
                        <div>
                            <h4 className="font-medium mb-3 text-white">Legal</h4>
                            <ul className="space-y-2">
                                <li><Link to="/privacy-policy" className="text-gray-400 hover:text-primary text-sm">Privacy Policy</Link></li>
                                <li><Link to="/terms-of-service" className="text-gray-400 hover:text-primary text-sm">Terms of Service</Link></li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div className="border-t border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center">
                    <p className="text-gray-500 text-sm mb-4 md:mb-0">
                        &copy; {currentYear} CodeConvene.AI. All rights reserved.
                    </p>
                    <div className="flex space-x-6">
                        <a href="https://github.com/AOSSIE-Org/CodeConvene.AI/" className="text-gray-400 hover:text-primary" target='_blank' rel="noreferrer">
                            <Github size={20} />
                        </a>
                        <a href="https://x.com/aossie_org?lang=en" className="text-gray-400 hover:text-primary" target='_blank'>
                            <Twitter size={20} />
                        </a>
                        <a href="https://www.linkedin.com/company/aossie/?originalSubdomain=au" className="text-gray-400 hover:text-primary" target='_blank'>
                            <Linkedin size={20} />
                        </a>
                    </div>
                </div>
            </div>
        </footer>
    );
};

export default Footer;