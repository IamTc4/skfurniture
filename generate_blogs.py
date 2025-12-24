import os
import re
import datetime

# Configuration - Reduced set to avoid file limits
PRODUCTS = {
    'School Bench': 'img/classroom 2.jpg',
    'School Chair': 'img/classroom 4.jpg',
    'Primary School Desk': 'img/classroom 6.jpg',
    'Junior School Table And Chair': 'img/classroom 3.jpg',
    'Class Room Table And Chair': 'img/classroom 10.jpg'
}

BLOG_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="canonical" href="https://skfurniture.com/blog/{filename}">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | skfurniture Blog</title>
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="../css/style.css">

    <!-- Schema.org Article -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{title}",
      "image": "https://skfurniture.com/{image}",
      "author": {{
        "@type": "Organization",
        "name": "skfurniture"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "skfurniture",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://skfurniture.com/logo.png"
        }}
      }},
      "datePublished": "{date}",
      "dateModified": "{date}"
    }}
    </script>
</head>
<body>

    <!-- Navigation -->
    <nav class="navbar">
        <div class="container">
            <a href="../index.html" class="logo">
                <i class="fas fa-layer-group"></i> skfurniture
            </a>
            <div class="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
            <ul class="nav-links">
                <li><a href="../index.html">Home</a></li>
                <li><a href="../solutions.html">Solutions</a></li>
                <li><a href="../manufacturing.html">Manufacturing</a></li>
                <li><a href="../projects.html">Projects</a></li>
                <li><a href="../blog.html" class="active">Blog</a></li>
                <li><a href="../inquiry.html" class="btn btn-primary" style="padding: 10px 24px; color: #212121;">Get Quote</a></li>
            </ul>
        </div>
    </nav>

    <!-- Breadcrumb -->
    <div class="breadcrumb">
        <div class="container">
            <a href="../index.html">Home</a> &gt; <a href="../blog.html">Blog</a> &gt; <span>{short_title}</span>
        </div>
    </div>

    <section class="section">
        <div class="container">
            <div class="blog-layout">
                <!-- Main Content -->
                <article>
                    <h1 style="margin-bottom: 20px; font-size: 2.5rem;">{title}</h1>
                    <div class="blog-meta">
                        <span><i class="far fa-calendar"></i> {date_display}</span>
                        <span><i class="far fa-user"></i> skfurniture Team</span>
                        <span><i class="fas fa-tag"></i> School Furniture</span>
                    </div>

                    <img src="../{image}" alt="{title}" class="blog-img">

                    <div class="blog-content" style="font-size: 1.1rem; line-height: 1.8; color: var(--body-text);">
                        <p>When it comes to setting up a conducive learning environment in <strong>Mumbai, Thane, and Pune</strong>, choosing the right furniture is paramount. {intro_text}</p>

                        <h2 style="margin-top: 30px; margin-bottom: 15px;">Why Choose {product_name}?</h2>
                        <p>The <strong>{product_name}</strong> is more than just a piece of furniture; it's a tool for effective learning. Schools across Maharashtra are increasingly upgrading their infrastructure to meet international standards. Here is why this product stands out:</p>

                        <ul style="list-style: disc; margin-left: 20px; margin-bottom: 20px;">
                            <li style="margin-bottom: 10px;"><strong>Ergonomic Design:</strong> Compliant with BIS standards to ensure student posture is corrected, reducing fatigue during long school hours.</li>
                            <li style="margin-bottom: 10px;"><strong>Durability:</strong> Made with high-grade materials that withstand the humid climate of Mumbai and heavy usage in schools.</li>
                            <li style="margin-bottom: 10px;"><strong>Safety First:</strong> Rounded corners and non-toxic finishes make it safe for students of all age groups.</li>
                        </ul>

                        <h2 style="margin-top: 30px; margin-bottom: 15px;">Manufacturing Quality at skfurniture</h2>
                        <p>At skfurniture, we take pride in our "Made in India" manufacturing process. Our facility in Thane utilizes advanced machinery for cutting, welding, and powder coating. The <strong>{product_name}</strong> undergoes a rigorous 7-tank anti-rust treatment to ensure longevity.</p>

                        <h2 style="margin-top: 30px; margin-bottom: 15px;">Serving Schools in Mumbai, Thane & Pune</h2>
                        <p>We understand the local needs of educational institutions. Whether you are a small coaching class in Thane or a large international school in Pune, our logistics team ensures timely delivery and professional installation.</p>

                        <div style="background-color: #F3F4F6; padding: 20px; border-left: 4px solid var(--primary-yellow); margin-top: 30px;">
                            <h3 style="margin-bottom: 10px;">Looking for a Quote?</h3>
                            <p>Contact us today for bulk pricing on {product_name}. We offer special rates for schools and institutions.</p>
                            <a href="https://wa.me/918169285185?text=Hi,%20I%20read%20your%20blog%20about%20{product_name_encoded}%20and%20want%20a%20quote." class="btn btn-primary" style="margin-top: 10px;">Get Best Price</a>
                        </div>
                    </div>
                </article>

                <!-- Sidebar -->
                <aside>
                    <div class="sidebar-box">
                        <h3 class="sidebar-title">Latest Products</h3>
                        <ul class="sidebar-list">
                            <li><a href="../product/school-bench.html">School Bench</a></li>
                            <li><a href="../product/school-chair.html">School Chair</a></li>
                            <li><a href="../product/library-table-with-partition.html">Library Tables</a></li>
                            <li><a href="../product/science-lab-furniture.html">Science Lab Furniture</a></li>
                        </ul>
                    </div>

                    <div class="sidebar-box">
                        <h3 class="sidebar-title">Service Areas</h3>
                        <ul class="sidebar-list">
                            <li><i class="fas fa-map-marker-alt" style="color: var(--primary-yellow); margin-right: 8px;"></i> Mumbai</li>
                            <li><i class="fas fa-map-marker-alt" style="color: var(--primary-yellow); margin-right: 8px;"></i> Thane</li>
                            <li><i class="fas fa-map-marker-alt" style="color: var(--primary-yellow); margin-right: 8px;"></i> Pune</li>
                            <li><i class="fas fa-map-marker-alt" style="color: var(--primary-yellow); margin-right: 8px;"></i> Navi Mumbai</li>
                            <li><i class="fas fa-map-marker-alt" style="color: var(--primary-yellow); margin-right: 8px;"></i> Nashik</li>
                        </ul>
                    </div>
                </aside>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <h3>skfurniture</h3>
                    <p>Specialists in educational furniture manufacturing.</p>
                </div>
                <div class="footer-col">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="../index.html">Home</a></li>
                        <li><a href="../solutions.html">Solutions</a></li>
                        <li><a href="../blog.html">Blog</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact</h4>
                    <ul>
                        <li><i class="fas fa-phone-alt" style="color: var(--primary-yellow); margin-right: 10px;"></i> 8169285185</li>
                    </ul>
                </div>
            </div>
            <div class="copyright">
                <p>&copy; 2025 skfurniture. All Rights Reserved.</p>
            </div>
        </div>
    </footer>
    <script src="../js/script.js"></script>
</body>
</html>
"""

def sanitize_filename(name):
    return re.sub(r'[^\w\s-]', '', name).strip().lower().replace(' ', '-')

blog_entries = []

for product_name, image_path in PRODUCTS.items():
    slug = sanitize_filename(product_name)
    filename = f"benefits-of-{slug}-in-mumbai-schools.html"
    title = f"Why {product_name} is Perfect for Schools in Mumbai & Pune"
    short_title = f"{product_name} Benefits"
    description = f"Discover why the {product_name} is the top choice for schools in Mumbai, Thane, and Pune. Ergonomic, durable, and BIS compliant furniture by skfurniture."
    keywords = f"{product_name}, school furniture Mumbai, classroom furniture Thane, school bench manufacturer Pune, ergonomic school desk"

    today = datetime.date.today().isoformat()
    date_display = datetime.date.today().strftime("%B %d, %Y")

    intro_text = f"The <strong>{product_name}</strong> is an essential component of any modern educational facility. As schools evolve, the demand for furniture that supports active learning and provides comfort has skyrocketed."

    import urllib.parse
    product_name_encoded = urllib.parse.quote(product_name)

    content = BLOG_TEMPLATE.format(
        filename=filename,
        title=title,
        short_title=short_title,
        description=description,
        keywords=keywords,
        image=image_path,
        date=today,
        date_display=date_display,
        intro_text=intro_text,
        product_name=product_name,
        product_name_encoded=product_name_encoded
    )

    with open(os.path.join('blog', filename), 'w', encoding='utf-8') as f:
        f.write(content)

    blog_entries.append({'title': title, 'filename': filename, 'date': date_display, 'desc': description})

# Update main blog.html (simple list append or rewrite)
# For simplicity, I'll rewrite blog.html to list these generated blogs dynamically would be hard without backend,
# so I'll generate a static list in blog.html
# Wait, I should read the existing blog.html and replace the list?
# Or just overwrite it with a new template that lists all of them.

BLOG_LIST_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <link rel="canonical" href="https://skfurniture.com/blog.html">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>School Furniture Blog | Insights for Mumbai, Thane & Pune</title>
    <meta name="description" content="Read the latest insights on school furniture trends, maintenance tips, and product guides for schools in Mumbai, Thane, and Pune.">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>

    <!-- Navigation -->
    <nav class="navbar">
        <div class="container">
            <a href="index.html" class="logo">
                <i class="fas fa-layer-group"></i> skfurniture
            </a>
            <div class="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="solutions.html">Solutions</a></li>
                <li><a href="manufacturing.html">Manufacturing</a></li>
                <li><a href="projects.html">Projects</a></li>
                <li><a href="blog.html" class="active">Blog</a></li>
                <li><a href="inquiry.html" class="btn btn-primary" style="padding: 10px 24px; color: #212121;">Get Quote</a></li>
            </ul>
        </div>
    </nav>

    <!-- Page Header -->
    <div class="page-header">
        <div class="container">
            <h1>Our Blog</h1>
            <p>Insights, guides, and news about educational environments.</p>
        </div>
    </div>

    <section class="section">
        <div class="container">
            <div class="blog-grid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(350px, 1fr)); gap: 30px;">
                {blog_items}
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <h3>skfurniture</h3>
                    <p>Specialists in educational furniture manufacturing.</p>
                </div>
                <div class="footer-col">
                    <h4>Solutions</h4>
                    <ul>
                        <li><a href="solutions.html">Solutions</a></li>
                        <li><a href="manufacturing.html">Manufacturing</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h4>Contact</h4>
                    <ul>
                        <li><i class="fas fa-phone-alt" style="color: var(--primary-yellow); margin-right: 10px;"></i> 8169285185</li>
                    </ul>
                </div>
            </div>
            <div class="copyright">
                <p>&copy; 2025 skfurniture. All Rights Reserved.</p>
            </div>
        </div>
    </footer>
    <script src="js/script.js"></script>
</body>
</html>
"""

items_html = ""
for entry in blog_entries:
    items_html += f"""
    <div class="blog-card" style="border: 1px solid #E5E7EB; border-radius: 12px; padding: 24px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
        <h3 style="margin-bottom: 10px; font-size: 1.25rem;"><a href="blog/{entry['filename']}">{entry['title']}</a></h3>
        <p style="color: #6B7280; font-size: 0.9rem; margin-bottom: 15px;">{entry['date']}</p>
        <p>{entry['desc']}</p>
        <a href="blog/{entry['filename']}" style="color: var(--primary-yellow); font-weight: 600; display: inline-block; margin-top: 15px;">Read More <i class="fas fa-arrow-right"></i></a>
    </div>
    """

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(BLOG_LIST_TEMPLATE.format(blog_items=items_html))

print(f"Generated {len(blog_entries)} blog posts and updated blog.html")
