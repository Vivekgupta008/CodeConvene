import React from 'react';
import { motion } from 'framer-motion';
import {
    Users,
    GitPullRequest,
    BookOpen,
    BarChart3,
    MessageSquareQuote,
    Code2
} from 'lucide-react';

const Features: React.FC = () => {
    const features = [
        {
            icon: <Users size={24} />,
            title: 'Personalized Experience',
            description: 'Context-aware recommendations, tailored notifications, and synchronized experience across all platforms including CLI and web widget.'
        },
        {
            icon: <GitPullRequest size={24} />,
            title: 'Automated Issue Triage & PR Assistance',
            description: 'AI-powered issue classification, duplicate detection, PR review suggestions, and contributor guidance.'
        },
        {
            icon: <BookOpen size={24} />,
            title: 'Knowledge Base & FAQ Automation',
            description: 'Dynamic documentation, code explanations, and instant answers with knowledge preservation.'
        },
        {
            icon: <BarChart3 size={24} />,
            title: 'Advanced Community Analytics',
            description: 'Real-time engagement metrics, contribution analysis, diversity tracking, and sentiment monitoring.'
        },
        {
            icon: <MessageSquareQuote size={24} />,
            title: 'Multi-Platform & CLI Integration',
            description: 'Unified experience across Discord, Slack, GitHub, Discourse, CLI, and web widget.'
        },
        {
            icon: <Code2 size={24} />,
            title: 'Technical Education & Advocacy',
            description: 'Interactive tutorials, live code assistance, and contextual code explanations for all skill levels.'
        }
    ];

    const container = {
        hidden: { opacity: 0 },
        show: {
            opacity: 1,
            transition: {
                staggerChildren: 0.1,
                delayChildren: 0.3,
            },
        },
    };

    const item = {
        hidden: { opacity: 0, y: 20 },
        show: { opacity: 1, y: 0 },
    };

    return (
        <section id="features" className="section pt-0 pb-12 md:pb-20 relative">
            <div className="container mx-auto px-6">
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.5 }}
                    className="text-center mb-10 md:mb-16"
                >
                    <h2 className="text-3xl md:text-4xl font-bold mb-4">
                        Powerful <span className="gradient-text">Features</span>
                    </h2>
                    <p className="text-gray-400 max-w-2xl mx-auto">
                        CodeConvene.AI comes packed with tools designed to reduce maintainer workload, improve contributor experience, and enhance project visibility.
                    </p>
                </motion.div>

                <motion.div
                    variants={container}
                    initial="hidden"
                    whileInView="show"
                    viewport={{ once: true }}
                    className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
                >
                    {features.map((feature, index) => (
                        <motion.div
                            key={index}
                            variants={item}
                            className="card hover-lift group"
                        >
                            <div className="mb-4 text-primary p-2 rounded-lg bg-primary/10 w-fit">
                                {feature.icon}
                            </div>
                            <h3 className="text-xl font-semibold mb-2 group-hover:text-primary transition-colors">
                                {feature.title}
                            </h3>
                            <p className="text-gray-400">
                                {feature.description}
                            </p>
                        </motion.div>
                    ))}
                </motion.div>
            </div>
        </section>
    );
};

export default Features;