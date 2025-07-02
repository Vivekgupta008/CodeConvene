import React from 'react';
import { motion } from 'framer-motion';
import { Users } from 'lucide-react';

const Hero: React.FC = () => {
    const container = {
        hidden: { opacity: 0 },
        show: {
            opacity: 1,
            transition: {
                staggerChildren: 0.2,
            },
        },
    };

    const item = {
        hidden: { opacity: 0, y: 20 },
        show: { opacity: 1, y: 0 },
    };

    return (
        <section className="relative min-h-screen flex items-center justify-center pt-24 pb-0 overflow-hidden">
            {/* Background elements */}
            <div className="absolute inset-0 pointer-events-none hidden md:block">
                <div className="absolute inset-0 bg-gradient-to-br from-dark via-dark to-gray-900 opacity-90"></div>

                <div className="absolute top-0 left-0 w-[1500px] h-[1500px] rounded-full bg-green-600/5 blur-[100px] -translate-x-1/3 -translate-y-1/3"></div>
                <div className="absolute bottom-0 right-0 w-[1200px] h-[1200px] rounded-full bg-blue-600/5 blur-[100px] translate-x-1/4 translate-y-1/4"></div>
                <div className="absolute top-1/2 right-1/4 w-[1000px] h-[1000px] rounded-full bg-purple-600/5 blur-[80px] -translate-y-1/2"></div>

                <div className="absolute inset-0 bg-[url('/grid-pattern.svg')] bg-center opacity-[0.15]"></div>

                <div className="absolute top-0 inset-x-0 h-40 bg-gradient-to-b from-green-500/10 to-transparent"></div>

                <div className="absolute inset-0 bg-radial-gradient"></div>
            </div>

            <div className="absolute bottom-0 left-0 right-0 h-48 bg-gradient-to-b from-transparent to-dark pointer-events-none"></div>

            <div className="container mx-auto px-6 z-10">
                <motion.div
                    variants={container}
                    initial="hidden"
                    animate="show"
                    className="max-w-5xl mx-auto text-center"
                >
                    <motion.div variants={item} className="mb-6">
                        <span className="px-5 py-2.5 rounded-full bg-green-500/10 text-green-500 text-base font-medium">
                            Developer Experience Reimagined
                        </span>
                    </motion.div>
                    <motion.h1
                        variants={item}
                        className="text-5xl md:text-7xl font-bold mb-8"
                    >
                        AI-Powered <span className="gradient-text">Developer Relations</span> Assistant
                    </motion.h1>

                    <motion.p
                        variants={item}
                        className="text-xl md:text-2xl text-gray-400 mb-6 max-w-4xl mx-auto"
                    >
                        CodeConvene.AI revolutionizes open-source community management by automating engagement,
                        streamlining onboarding, and delivering real-time project updates across Discord,
                        Slack, GitHub, CLI, Web Widget, and more. <br />
                        <span className="text-primary font-semibold">Personalized, multi-platform, and analytics-driven.</span>
                    </motion.p>
                    <motion.div
                        variants={item}
                        className="flex flex-col sm:flex-row gap-5 justify-center mb-6"
                    >
                        <a href="#waitlist" className="btn-primary flex items-center justify-center gap-2 text-lg py-4 px-8">
                            <Users size={20} />
                            Join the Waitlist
                        </a>
                        <a href="#features" className="btn-secondary text-lg py-4 px-8">
                            Explore Features
                        </a>
                    </motion.div>

                    <motion.div
                        variants={item}
                        className="max-w-6xl mx-auto"
                    >
                        <div className="relative rounded-xl overflow-hidden border border-gray-800 shadow-2xl">
                            <div className="absolute inset-0 bg-gradient-to-b from-transparent via-transparent to-dark z-10"></div>
                            <img
                                src="/dashboard_preview.png"
                                alt="CodeConvene.AI Dashboard"
                                className="w-full h-auto"
                            />
                        </div>
                    </motion.div>
                </motion.div>
            </div>
        </section>
    );
};

export default Hero;