import os
import re

# Footer HTML
footer_html = """<footer>
        <div class="container">
            <div class="footer-content">
                <!-- Contact Column -->
                <div class="footer-column footer-left">
                  <h3>Contact & Address</h3>
                  <ul>
                    <li><i class="fas fa-user"></i> Pro. Ramji Bhai</li>
                    <li><i class="fas fa-phone"></i> 8169285185 / 9870075755 / 8879605111</li>
                    <li><i class="fas fa-user-tie"></i> Mr. Anil Vishwakarma – 8169285185</li>
                    <li><i class="fas fa-envelope"></i> info@skinterios.com</li>
                    <li><i class="fas fa-globe"></i> skinterios.com</li>
                    <li><i class="fas fa-map-marker-alt"></i> Shop No.4, Shree Co.Op., Sector 7, Plot No.39,
                        Shree Nagar, Wagle Estate, Thane (W)</li>
                  </ul>
                </div>

                <!-- Quick Links Column -->
                <div class="footer-column footer-links">
                  <h3>Quick Links</h3>
                  <ul>
                    <li><a href="index.html"><i class="fas fa-home"></i> Home</a></li>
                    <li><a href="services.html"><i class="fas fa-cogs"></i> Services</a></li>
                    <li><a href="portfolio.html"><i class="fas fa-images"></i> Portfolio</a></li>
                    <li><a href="about.html"><i class="fas fa-info-circle"></i> About</a></li>
                    <li><a href="contact.html"><i class="fas fa-envelope-open-text"></i> Contact</a></li>
                  </ul>
                </div>

                <!-- Social Media Column -->
                <div class="footer-column footer-right">
                  <h3>Follow Us</h3>
                  <div class="footer-social">
                    <a href="https://wa.me/918169285185" target="_blank"><i class="fab fa-whatsapp"></i></a>
                    <a href="https://instagram.com/sk_furniture_fabrication_works" target="_blank"><i class="fab fa-instagram"></i></a>
                    <a href="mailto:info@skinterios.com"><i class="fas fa-envelope"></i></a>
                  </div>
                </div>
            </div>

            <div class="copyright">
                <p>&copy; 2026 Sai Krupa Furniture & Fabrication Works. All Rights Reserved.</p>
                <div class="developer-credit">
                    <span>Designed by</span>
                    <a href="https://developerbee.digital" target="_blank">
                        DeveloperBee
                        <img src="img/Design.jpeg" alt="DeveloperBee Logo">
                    </a>
                </div>
                <div style="text-align: center; margin-top: 10px;">
                    <a href="https://skinterios.com/" style="color: #6B7280; font-size: 0.8rem;">skinterios.com</a>
                </div>
            </div>
        </div>
    </footer>"""

# Services Section HTML (img fixed)
services_html = """<section class="services-section">
    <h1>Our Interior Design Services in Thane</h1>
    <p class="services-intro">As the best interior designers in Thane, we offer a comprehensive range of services, including custom furniture, residential and commercial interior design, and fabrication. Explore our offerings to see how we can transform your space.</p>
    <div class="services-grid">
      <!-- Desk Benches (main, 3D PNG) -->
      <a href="https://skinterios.com/portfolio.html#desk-benches" class="service-card-link">
      <div class="service-card main-service">
        <img src="img/desk-bench.png" alt="Custom Desk Benches" class="main-3d-img" />
        <h2>Custom Desk Benches</h2>
        <p>Tailor-made desk benches crafted for style, comfort, and functionality — perfect for modern offices and institutions.</p>
      </div>
      </a>
      <!-- Interior Design -->
      <a href="https://skinterios.com/portfolio.html#interior-design" class="service-card-link">
      <div class="service-card">
        <img src="img/img92.jpg" alt="Interior Design" />
        <h2>Interior Design</h2>
        <p>Complete design solutions for homes, offices, and commercial spaces — blending creativity with practicality.</p>
      </div>
      </a>
      <!-- Furniture Work -->
      <a href="https://skinterios.com/portfolio.html#furniture-work" class="service-card-link">
      <div class="service-card">
        <img src="img/img107.jpg" alt="Furniture Work" />
        <h2>Furniture Work</h2>
        <p>Custom furniture production and installation, combining modern aesthetics with durable materials.</p>
      </div>
      </a>
      <!-- P.O.P & Paint -->
      <a href="https://skinterios.com/portfolio.html#pop-paint" class="service-card-link">
      <div class="service-card">
        <img src="img/img106.jpg" alt="P.O.P & Paint" />
        <h2>P.O.P & Paint</h2>
        <p>Professional plaster and paint finishes for ceilings, walls, and custom designs.</p>
      </div>
      </a>
      <!-- Civil Work -->
      <a href="https://skinterios.com/portfolio.html#civil-work" class="service-card-link">
      <div class="service-card">
        <img src="img/img114.jpg" alt="Civil Work" />
        <h2>Civil Work</h2>
        <p>Foundational construction, wall partitions, false ceilings, and all small-scale civil needs.</p>
      </div>
      </a>
      <!-- Fabrication Work -->
      <a href="https://skinterios.com/portfolio.html#fabrication-work" class="service-card-link">
      <div class="service-card">
        <img src="img/img113.jpg" alt="Fabrication Work" />
        <h2>Fabrication Work</h2>
        <p>MS, SS and aluminum fabrication solutions for residential and commercial projects.</p>
      </div>
      </a>
      <!-- Electrical Work -->
      <a href="https://skinterios.com/portfolio.html#electrical-work" class="service-card-link">
      <div class="service-card">
        <img src="img/img121.jpg" alt="Electrical Work" />
        <h2>Electrical Work</h2>
        <p>Safe, reliable electrical installations, rewiring, lighting, and panel setups.</p>
      </div>
      </a>
      <!-- AC Installation -->
      <a href="https://skinterios.com/portfolio.html#ac-installation" class="service-card-link">
      <div class="service-card">
        <img src="img/img120.jpg" alt="AC Installation" />
        <h2>AC Installation</h2>
        <p>Expert air conditioning installation and servicing with clean setup and cabling.</p>
      </div>
      </a>
    </div>
  </section>"""

files = [
    'index.html', 'services.html'
]

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Update Footer
        footer_regex = re.compile(r'<footer>.*?</footer>', re.DOTALL)
        if footer_regex.search(content):
            content = footer_regex.sub(footer_html, content)
        else:
            if '</body>' in content:
                content = content.replace('</body>', footer_html + '\n</body>')
            else:
                content += footer_html

        # 2. Update Header (About Link)
        if '<li><a href="about.html">About</a></li>' not in content:
             if '<li><a href="index.html">Home</a></li>' in content:
                content = content.replace(
                    '<li><a href="index.html">Home</a></li>',
                    '<li><a href="index.html">Home</a></li>\n                <li><a href="about.html">About</a></li>'
                )
             elif '<li><a href="index.html" class="active">Home</a></li>' in content:
                content = content.replace(
                    '<li><a href="index.html" class="active">Home</a></li>',
                    '<li><a href="index.html" class="active">Home</a></li>\n                <li><a href="about.html">About</a></li>'
                )

        # 3. Add Services Section
        if file in ['index.html', 'services.html']:
            if 'class="services-section"' not in content:
                if '<footer>' in content:
                    content = content.replace('<footer>', services_html + '\n<footer>')

        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

print("Root files (index/services) updated.")
