import React, { useEffect } from 'react';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';
import { motion } from 'framer-motion';

const PrivacyPolicy: React.FC = () => {
    useEffect(() => {
        window.scrollTo(0, 0);
        document.title = "Privacy Policy | CodeConvene.AI";
    }, []);

    return (
        <div className="min-h-screen bg-dark">
            <Navbar />
            <main className="pt-24 pb-16">
                <div className="container mx-auto px-6">
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="max-w-3xl mx-auto"
                    >
                        <h1 className="text-3xl md:text-4xl font-bold mb-8 gradient-text">Privacy Policy</h1>

                        <div className="prose prose-invert max-w-none">
                            <p className="text-gray-300 mb-4">Last updated: April 14, 2025</p>

                            <section className="mb-8">
                                <h2 className="text-xl font-semibold mb-4">Introduction</h2>
                                <p className="text-gray-300">
                                    At CodeConvene.AI, we respect your privacy and are committed to protecting your personal data. This Privacy
                                    Policy explains how we collect, use, disclose, and safeguard your information when you use our service.
                                </p>
                            </section>

                            <section className="mb-8">
                                <h2 className="text-xl font-semibold mb-4">Information We Collect</h2>
                                <p className="text-gray-300">When you use CodeConvene.AI, we may collect the following types of information:</p>
                                <ul className="list-disc pl-5 text-gray-300 space-y-2 mt-3">
                                    <li>
                                        <strong>Personal Information:</strong> Name, email address, and organization details provided
                                        during signup or when joining our waitlist.
                                    </li>
                                    <li>
                                        <strong>Platform Data:</strong> When you connect CodeConvene.AI to platforms like GitHub, Discord, or Slack,
                                        we collect necessary data to provide our services, such as repository information, conversation history,
                                        and community interactions.
                                    </li>
                                    <li>
                                        <strong>Usage Information:</strong> Data about how you interact with our service, including features used,
                                        actions taken, and time spent on the platform.
                                    </li>
                                </ul>
                            </section>

                            <section className="mb-8">
                                <h2 className="text-xl font-semibold mb-4">How We Use Your Information</h2>
                                <p className="text-gray-300">We use the collected information for various purposes, including:</p>
                                <ul className="list-disc pl-5 text-gray-300 space-y-2 mt-3">
                                    <li>Providing and maintaining our service</li>
                                    <li>Improving and personalizing the user experience</li>
                                    <li>Analyzing usage patterns to enhance our features</li>
                                    <li>Communicating with you about service updates and new features</li>
                                    <li>Protecting our services and addressing abuse</li>
                                </ul>
                            </section>

                            <section className="mb-8">
                                <h2 className="text-xl font-semibold mb-4">Data Sharing and Disclosure</h2>
                                <p className="text-gray-300">
                                    We do not sell your personal information. We may share information in the following circumstances:
                                </p>
                                <ul className="list-disc pl-5 text-gray-300 space-y-2 mt-3">
                                    <li>With service providers who help us operate our platform</li>
                                    <li>To comply with legal obligations</li>
                                    <li>With your consent or at your direction</li>
                                    <li>In connection with a merger, acquisition, or sale of assets</li>
                                </ul>
                            </section>

                            <section className="mb-8">
                                <h2 className="text-xl font-semibold mb-4">Data Security</h2>
                                <p className="text-gray-300">
                                    We implement appropriate security measures to protect your personal information from unauthorized access,
                                    alteration, disclosure, or destruction. However, no method of transmission over the internet or electronic
                                    storage is 100% secure, and we cannot guarantee absolute security.
                                </p>
                            </section>

                            <section className="mb-8">
                                <h2 className="text-xl font-semibold mb-4">Your Rights</h2>
                                <p className="text-gray-300">
                                    Depending on your location, you may have certain rights regarding your personal information, including:
                                </p>
                                <ul className="list-disc pl-5 text-gray-300 space-y-2 mt-3">
                                    <li>Accessing your personal data</li>
                                    <li>Correcting inaccurate information</li>
                                    <li>Deleting your data</li>
                                    <li>Restricting or objecting to processing</li>
                                    <li>Data portability</li>
                                </ul>
                                <p className="text-gray-300 mt-3">
                                    To exercise these rights, please contact us at privacy@CodeConvene.ai.
                                </p>
                            </section>

                            <section className="mb-8">
                                <h2 className="text-xl font-semibold mb-4">Changes to This Policy</h2>
                                <p className="text-gray-300">
                                    We may update our Privacy Policy from time to time. We will notify you of any changes by posting
                                    the new Privacy Policy on this page and updating the "Last updated" date. You are advised to review
                                    this Privacy Policy periodically for any changes.
                                </p>
                            </section>

                            <section>
                                <h2 className="text-xl font-semibold mb-4">Contact Us</h2>
                                <p className="text-gray-300">
                                    If you have any questions about this Privacy Policy, please contact us at: <br />
                                    <strong>Email:</strong> <a href="mailto:aossie.oss@gmail.com" className="text-primary hover:underline">aossie.oss@gmail.com</a>.
                                </p>
                            </section>
                        </div>
                    </motion.div>
                </div>
            </main>
            <Footer />
        </div>
    );
};

export default PrivacyPolicy;