document.addEventListener('DOMContentLoaded', () => {
    // Mobile Navigation
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navLinks.classList.toggle('active');
        });
    }

    // Mobile Dropdown Toggle
    const dropdowns = document.querySelectorAll('.dropdown');
    dropdowns.forEach(dropdown => {
        const link = dropdown.querySelector('a');
        if (link) {
            link.addEventListener('click', (e) => {
                if (window.innerWidth <= 900) {
                    e.preventDefault(); // Prevent navigation on mobile to show submenu
                    dropdown.classList.toggle('active');
                }
            });
        }
    });

    // Product Specs Toggle
    const specsToggles = document.querySelectorAll('.specs-toggle');
    specsToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const content = toggle.nextElementSibling;
            toggle.classList.toggle('active');
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    });

    // FAQ Accordion
    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const item = question.parentElement;
            const answer = question.nextElementSibling;

            // Close other open items
            document.querySelectorAll('.faq-item').forEach(otherItem => {
                if (otherItem !== item && otherItem.classList.contains('active')) {
                    otherItem.classList.remove('active');
                    otherItem.querySelector('.faq-answer').style.maxHeight = null;
                }
            });

            // Toggle current
            item.classList.toggle('active');
            if (item.classList.contains('active')) {
                answer.style.maxHeight = answer.scrollHeight + "px";
            } else {
                answer.style.maxHeight = null;
            }
        });
    });

    // Hero Slider
    const slides = document.querySelectorAll('.slide');
    if (slides.length > 0) {
        let currentSlide = 0;
        const slideInterval = 5000; // 5 seconds

        function nextSlide() {
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
        }

        setInterval(nextSlide, slideInterval);
    }

    // Manufacturing Process Animations
    const sections = document.querySelectorAll(".section");
    const techProcesses = document.querySelectorAll(".tech-process");

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("animate");

                    // If the section contains a tech-process, animate that too
                    const process = entry.target.querySelector(".tech-process");
                    if (process) {
                        process.classList.add("animate");
                        const steps = process.querySelectorAll(".process-step");
                        steps.forEach((step, index) => {
                            setTimeout(() => {
                                step.classList.add("animate");
                            }, index * 200); // staggered flow
                        });
                    }

                    // Specific case for tech-process if observed directly (e.g. BIS section)
                    if (entry.target.classList.contains("tech-process")) {
                         const steps = entry.target.querySelectorAll("li"); // BIS list items
                         // Add animate class to LI if we want to stagger them too, or just the container
                         // The user asked for "same animation flow".
                         // The BIS section uses UL > LI. The process section uses div.process-step.
                         // Let's add 'process-step' class functionality to LIs conceptually or just animate the block.
                    }

                    observer.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.2 }
    );

    sections.forEach(sec => observer.observe(sec));
    techProcesses.forEach(tp => observer.observe(tp));
    // Generic Reveal Animation
    const revealElements = document.querySelectorAll('.reveal');
    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if(entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.15 });

    revealElements.forEach(el => revealObserver.observe(el));

    // Existing Sections Observer (Kept for backward compatibility if needed, or merged)
    // The previous code handled .section.animate separately. We can leave it or enhance it.
    // For now, let's keep the .reveal system independent for new control.
});
