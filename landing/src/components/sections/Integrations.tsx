import React from 'react';
import { motion } from 'framer-motion';
import { Github, MessageSquare, Slack, MessageCircle, Code2, BookOpen } from 'lucide-react';

const Integrations: React.FC = () => {
    const integrations = [
        {
            icon: <Github size={28} />,
            name: 'GitHub',
            description: 'Automate issue triage, PR reviews, and contributor onboarding directly on GitHub.',
            features: [
                'Integration via GitHub Apps and Webhooks',
                'Automated issue labeling and PR review',
                'Contributor onboarding automation',
                'Repository insights and analytics'
            ]
        },
        {
            icon: <Slack size={28} />,
            name: 'Slack',
            description: 'Streamline team communication and project updates within your Slack workspace.',
            features: [
                'Integration via Slack Events API and Bot Users',
                'Real-time notifications and command center',
                'Interactive project management tools',
                'Automated knowledge sharing'
            ]
        },
        {
            icon: <MessageSquare size={28} />,
            name: 'Discord',
            description: 'Build an engaging community space for developers with automated assistance.',
            features: [
                'Integration via Discord Bot API and Webhooks',
                'Community support and moderation',
                'Developer onboarding and guidance',
                'Knowledge base access and retrieval'
            ]
        },
        {
            icon: <MessageCircle size={28} />,
            name: 'Discourse',
            description: 'Enhance your community forum experience with AI-powered assistance.',
            features: [
                'Integration via Discourse API and Webhooks',
                'Automated topic categorization',
                'Knowledge management and FAQs',
                'Community engagement tools'
            ]
        },
        {
            icon: <Code2 size={28} />,
            name: 'CLI',
            description: 'Command-line interface for direct access to documentation, tutorials, and project health checks.',
            features: [
                'API key authentication',
                'Interactive tutorials and guided workflows',
                'Local environment setup assistance',
                'Contextual help based on current project'
            ]
        },
        {
            icon: <BookOpen size={28} />,
            name: 'Web Widget',
            description: 'Embeddable widget for documentation search, contextual help, and onboarding on your website.',
            features: [
                'Easy snippet integration',
                'Customizable appearance and behavior',
                'Documentation search and contextual help',
                'Analytics for common queries'
            ]
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
        <section id="integrations" className="section">
            <div className="container mx-auto px-6">
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.5 }}
                    className="text-center mb-16"
                >
                    <h2 className="text-3xl md:text-4xl font-bold mb-4">
                        Platform <span className="gradient-text">Integrations</span>
                    </h2>
                    <p className="text-gray-400 max-w-2xl mx-auto">
                        Connect CodeConvene.AI with the tools you already use to enhance developer experience and community management.
                    </p>
                </motion.div>

                <motion.div
                    variants={container}
                    initial="hidden"
                    whileInView="show"
                    viewport={{ once: true }}
                    className="grid grid-cols-1 md:grid-cols-2 gap-8"
                >
                    {integrations.map((integration, index) => (
                        <motion.div
                            key={index}
                            variants={item}
                            className="bg-dark-card border border-gray-800 rounded-xl p-6 hover:border-primary transition-all hover-lift"
                        >
                            <div className="flex items-center gap-4 mb-4">
                                <div className="p-3 rounded-lg bg-dark-lighter text-primary">
                                    {integration.icon}
                                </div>
                                <h3 className="text-xl font-semibold">{integration.name}</h3>
                            </div>
                            <p className="text-gray-400 mb-4">{integration.description}</p>
                            <ul className="space-y-2">
                                {integration.features.map((feature, featIndex) => (
                                    <li key={featIndex} className="flex items-center gap-2 text-sm text-gray-300">
                                        <span className="text-primary text-lg leading-none">•</span>
                                        <span>{feature}</span>
                                    </li>
                                ))}
                            </ul>
                        </motion.div>
                    ))}
                </motion.div>
            </div>
        </section>
    );
};

export default Integrations;