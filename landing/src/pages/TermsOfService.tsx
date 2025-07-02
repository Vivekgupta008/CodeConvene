import React, { useEffect } from 'react';
import Navbar from '../components/layout/Navbar';
import Footer from '../components/layout/Footer';
import { motion } from 'framer-motion';

const TermsOfService: React.FC = () => {
    useEffect(() => {
        window.scrollTo(0, 0);
        document.title = "Terms of Service | CodeConvene.AI";
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
                        <h1 className="text-3xl md:text-4xl font-bold mb-8 gradient-text">Terms of Service</h1>

                        <div className="prose prose-invert max-w-none">
                            <p className="text-gray-300 mb-4">Last updated: April 14, 2025</p>

                            <section className="mb-8">
                                <h2 className="text-xl font-semibold mb-4">1. Introduction</h2>
                                <p className="text-gray-300">
                                    Welcome to CodeConvene.AI, an AI-powered Developer Relations (CodeConveneel) assistant that integrates
                                    with platforms such as Discord, Slack, GitHub, and Discourse. This Terms of Service
                                    Agreement ("Agreement") governs your use of CodeConvene.AI, including its software, documentation,
                                    integrations, and related services (collectively, the "Project"). By accessing or using any
                                    part of the Project, you agree to be bound by these terms. If you do not agree with any
                                    portion of this Agreement, do not use the Project.
                                </p>
                            </section>

                            <section className="mb-8">
                                <h2 className="text-xl font-semibold mb-4">2. Grant of License</h2>
                                <p className="text-gray-300">
                                    Subject to your compliance with the terms of this Agreement, CodeConvene.AI hereby grants you a
                                    non-exclusive, worldwide, royalty-free license to use, reproduce, display, and distribute
                                    the Project in source and/or binary forms, with or without modifications.
                                </p>
                                <ul className="list-disc pl-5 text-gray-300 space-y-2 mt-3">
                                    <li>
                                        <strong>Permitted Uses:</strong> Integration within open-source communities, developer
                                        relations work, community engagement, issue triage, PR assistance, and community analytics.
                                    </li>
                                    <li>
                                        <strong>Restrictions:</strong> You agree not to use, modify, or distribute the Project
                                        in a manner that violates any applicable laws or infringes on the proprietary rights of
                                        third parties. Commercial use beyond the license grant may require additional written permission.
                                    </li>
                                </ul>
                            </section>

                            <section className="mb-8">
                                <h2 className="text-xl font-semibold mb-4">3. Intellectual Property Rights</h2>
                                <p className="text-gray-300">
                                    All right, title, and interest in and to the Project, including but not limited to all
                                    copyrights, trademarks, trade secrets, and other intellectual property rights, remain
                                    exclusively with the Project maintainers or their licensors.
                                </p>
                                <ul className="list-disc pl-5 text-gray-300 space-y-2 mt-3">
                                    <li>
                                        <strong>Third-Party Components:</strong> The Project may include components licensed
                                        from third parties. Your use of such components is subject to the respective third-party
                                        license agreements, and you are responsible for complying with those terms.
                                    </li>
                                </ul>
                            </section>

                            <section className="mb-8">
                                <h2 className="text-xl font-semibold mb-4">4. Disclaimer of Warranties</h2>
                                <p className="text-gray-300 uppercase font-semibold">
                                    The project is provided "as is" without warranty of any kind, either expressed or implied,
                                    including, but not limited to, the implied warranties of merchantability, fitness for a
                                    particular purpose, or non-infringement.
                                </p>
                                <ul className="list-disc pl-5 text-gray-300 space-y-2 mt-3">
                                    <li>
                                        <strong>No Guarantee:</strong> Neither the maintainers nor any contributors guarantee
                                        that the software will be error-free, secure, or available on an uninterrupted, timely, or safe basis.
                                    </li>
                                    <li>
                                        <strong>Risk Acknowledgment:</strong> You assume all risks associated with the use of
                                        the Project. It is your responsibility to ensure that any integration with external systems
                                        (such as Discord, Slack, GitHub, and Discourse) does not create legal or security issues for your deployment.
                                    </li>
                                </ul>
                            </section>

                            <section className="mb-8">
                                <h2 className="text-xl font-semibold mb-4">5. Limitation of Liability</h2>
                                <p className="text-gray-300 uppercase font-semibold">
                                    To the maximum extent permitted by applicable law, in no event shall the CodeConvene.AI project,
                                    its maintainers, contributors, or affiliates be liable for any indirect, incidental,
                                    special, consequential, or punitive damages (including, without limitation, damages for
                                    loss of profits, data, or other intangible losses) arising out of or related to the use
                                    or inability to use the project, even if advised of the possibility of such damages.
                                </p>
                            </section>

                            <section className="mb-8">
                                <h2 className="text-xl font-semibold mb-4">6. Contributions and Community Conduct</h2>
                                <ul className="list-disc pl-5 text-gray-300 space-y-2">
                                    <li>
                                        <strong>Contributor License:</strong> By contributing code, documentation, or other
                                        materials to the Project, you hereby grant the maintainers a perpetual, irrevocable,
                                        non-exclusive, worldwide license to use your contributions under the terms of this Agreement.
                                    </li>
                                    <li>
                                        <strong>Code of Conduct:</strong> Contributors and users are expected to maintain respectful,
                                        constructive, and professional interactions within community channels. Any behavior contrary
                                        to the spirit of open-source collaboration may result in revocation of access or other legal remedies.
                                    </li>
                                </ul>
                            </section>

                            <section className="mb-8">
                                <h2 className="text-xl font-semibold mb-4">7. Third-Party Services and Integrations</h2>
                                <p className="text-gray-300">
                                    CodeConvene.AI integrates with several third-party platforms (e.g., Discord, Slack, GitHub, and Discourse).
                                    Use of these integrations is subject not only to this Agreement but also to the respective terms
                                    and policies of the third-party providers.
                                </p>
                                <ul className="list-disc pl-5 text-gray-300 space-y-2 mt-3">
                                    <li>
                                        <strong>No Endorsement:</strong> The inclusion of these platforms and any reference to them
                                        does not imply an endorsement by CodeConvene.AI.
                                    </li>
                                    <li>
                                        <strong>User Responsibility:</strong> You are solely responsible for adhering to the
                                        third-party providers' terms, and the CodeConvene.AI maintainers disclaim any liability regarding
                                        issues arising from these integrations.
                                    </li>
                                </ul>
                            </section>

                            <section className="mb-8">
                                <h2 className="text-xl font-semibold mb-4">8. Data Privacy and Use</h2>
                                <ul className="list-disc pl-5 text-gray-300 space-y-2">
                                    <li>
                                        <strong>Data Collection:</strong> The Project may collect, store, and process data to
                                        support community engagement, contributor onboarding, and real-time analytics. The
                                        specifics of such data handling are detailed in our <a href="/privacy-policy" className="text-primary hover:underline">Privacy Policy</a>.
                                    </li>
                                    <li>
                                        <strong>Compliance:</strong> Users must comply with all applicable data protection
                                        regulations and ensure that any personal or sensitive data accessed or processed via
                                        the Project is handled in accordance with local laws.
                                    </li>
                                    <li>
                                        <strong>No Warranty for Data Security:</strong> While we strive to implement robust
                                        security measures, the maintainers do not warrant that unauthorized access or data
                                        breaches will be completely prevented.
                                    </li>
                                </ul>
                            </section>

                            <section className="mb-8">
                                <h2 className="text-xl font-semibold mb-4">9. Modification and Termination</h2>
                                <ul className="list-disc pl-5 text-gray-300 space-y-2">
                                    <li>
                                        <strong>Amendments:</strong> We reserve the right to update or modify this Agreement at any time.
                                        Continued use of the Project after changes have been posted constitutes acceptance of the revised terms.
                                    </li>
                                    <li>
                                        <strong>Termination:</strong> The maintainers may terminate or suspend your access to the
                                        Project at any time for any reason, including but not limited to breaches of this Agreement,
                                        without liability to you.
                                    </li>
                                </ul>
                            </section>

                            <section className="mb-8">
                                <h2 className="text-xl font-semibold mb-4">10. Governing Law and Dispute Resolution</h2>
                                <ul className="list-disc pl-5 text-gray-300 space-y-2">
                                    <li>
                                        <strong>Jurisdiction:</strong> This Agreement and any disputes related to it shall be
                                        governed exclusively by the laws of the jurisdiction in which the primary maintainers operate,
                                        without regard to its conflict of laws principles.
                                    </li>
                                    <li>
                                        <strong>Dispute Resolution:</strong> In the event of any dispute, controversy, or claim
                                        arising from or related to this Agreement, the parties agree to first seek resolution through
                                        informal negotiations. If a resolution cannot be reached, any unresolved dispute shall be subject
                                        to binding arbitration in accordance with applicable law.
                                    </li>
                                </ul>
                            </section>

                            <section>
                                <h2 className="text-xl font-semibold mb-4">11. Contact Information</h2>
                                <p className="text-gray-300">
                                    If you have any questions about this Agreement, please contact us at: <br />
                                    <strong>Email:</strong> <a href="mailto:aossie.oss@gmail.com" className="text-primary hover:underline">aossie.oss@gmail.com</a>
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

export default TermsOfService;