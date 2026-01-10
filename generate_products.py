import os
import re
import urllib.parse

# Read product-detail.html to use as a template
with open('product-detail.html', 'r', encoding='utf-8') as f:
    template_content = f.read()

# Define the image map
image_map = {
    'School Bench': 'img/classroom 2.jpg',
    'School Chair': 'img/classroom 4.jpg',
    'Primary School Desk': 'img/classroom 6.jpg',
    'Junior School Table And Chair': 'img/classroom 3.jpg',
    'Class Room Table And Chair': 'img/classroom 10.jpg',
    'Senior School Furniture': 'img/classroom 8.jpg',
    'Play School Chair': 'img/kid bench.png',
    'Kids Chair': 'img/kid bench.png',
    'Kids Round Table': 'img/classroom 12.jpg',
    'Nursery School Plastic Furniture': 'img/kid bench.png',
    'Teacher Table for Classroom': 'img/staff 1.jpg',
    'Teacher Table and Chair': 'img/staff 2.jpg',
    'Maths Lab Table': 'img/scilab.jpg',
    'General Science Lab Table': 'img/scilab 1.jpg',
    'Physics Lab Furniture': 'img/scilab.jpg',
    'Science Lab Furniture': 'img/scilab 1.jpg',
    'Lab Stool': 'img/Staff .jpg',
    'Computer Lab Furniture': 'img/scilab.jpg',
    'Single Seater Classroom Desk': 'img/classroom 6.jpg',
    'Single Seater Desk with Chair': 'img/classroom 10.jpg',
    'Single Seater Open Shelf Desk': 'img/classroom 12.jpg',
    'Single Seater Combined Desk': 'img/classroom 15 (2).jpg',
    'Z Shaped Classroom Desk': 'img/classroom 2.jpg',
    'Classroom Dual Desk': 'img/classroom 7.jpg',
    'Dual Desk with Shelf': 'img/classroom 8.jpg',
    'Dual Combined Desk Without Shelf': 'img/classroom 9.jpg',
    'Two Seater Desk with Chairs': 'img/classroom 5.jpg',
    'Two Seater Desk with Perforated Seat': 'img/classroom 4.jpg',
    'Three Seater Combined Desk': 'img/classroom 3.jpg',
    'Three Seater Classroom Desk': 'img/classroom 15 (3).jpg',
    'Senior Class Desk': 'img/classroom 15 (4).jpg',
    'Modern Classroom Desk and Bench': 'img/classroom 11.jpg',
    'Without Back Desk': 'img/classroom 2.jpg',
    'Rectangular Pipe Classroom Desk': 'img/classroom 12.jpg',
    'Iron Writing Chair': 'img/classroom 15 (2).jpg',
    'Full Flap Arm Chair': 'img/classroom 15 (3).jpg',
    'Writing Arm Chair With Basket': 'img/classroom 15 (4).jpg',
    'Cushioned Seat and Back Arm Chair': 'img/classroom 15.jpg',
    'Plastic Institutional Chair': 'img/classroom 15 (2).jpg',
    'Institutional Wooden Chair': 'img/classroom 15 (3).jpg',
    'Coaching Chair': 'img/classroom 10.jpg',
    'Coaching Furniture': 'img/classroom 11.jpg',
    'Library Almirah': 'img/Library 8.jpg',
    'Staff Room Table': 'img/staff 1.jpg',
    'Staff Room Furniture': 'img/staff 2.jpg',
    'Library Table with partition': 'img/Library 4.jpg',
    'College Library Table': 'img/Library 5.jpg',
    'Modern Library Table': 'img/Library 6.jpg',
    'Library Table for Teachers and Staff': 'img/Library 7.jpg',
    'Table With Stool Set': 'img/Library 8.jpg',
    'Library Wooden Chairs': 'img/Library.jpg',
    'Library Chair with Cushioned Seat': 'img/Library 2.jpg',
    'Library Chairs for Staff': 'img/Libray 10.jpg',
    'Library Book Shelf': 'img/Library 3.jpg',
    'Wooden Bookshelf': 'img/Library 7.jpg',
    'Library Rack': 'img/Library 8.jpg',
    'Newspaper Stand': 'img/Library.jpg',
    'Magazine Stand': 'img/Library 2.jpg',
    'Office Revolving Chair': 'img/staff 1.jpg',
    'Office Visitor Chair': 'img/staff 2.jpg',
    'Office Sofa': 'img/reception.jpg',
    'Office Table': 'img/admin.jpg',
    'Conference Room Table': 'img/reception 4.jpg',
    'Reception Sofa Set': 'img/reception 2.jpg',
    'Wooden Reception Furniture': 'img/reception 3.jpg',
    'Office Reception Furniture': 'img/reception.jpg',
    'Office Filing Cabinet': 'img/Library 8.jpg',
    'Hostel Wardrobe': 'https://images.unsplash.com/photo-1595846519845-68e298c2edd8?auto=format&fit=crop&w=400&q=80',
    'Cafe Furniture': 'img/canteen.jpg',
    'Whiteboard': 'img/whiteboard.jpg',
    'Blackboard': 'img/blackboard.jpg',
    'Desk Bench': 'img/desk-bench.png',
    'Podium': 'img/podium.jpg',
    'Podium2': 'img/podium2.jpg',
    'Stand': 'img/stand.jpg'
}

extra_images_classroom = [
    'img/classroom 2.jpg', 'img/classroom 3.jpg', 'img/classroom 4.jpg',
    'img/classroom 5.jpg', 'img/classroom 6.jpg', 'img/classroom 7.jpg',
    'img/classroom 8.jpg', 'img/classroom 9.jpg', 'img/classroom 10.jpg',
    'img/classroom 11.jpg', 'img/classroom 12.jpg', 'img/classroom 15.jpg'
]

extra_images_office = [
    'img/staff 1.jpg', 'img/staff 2.jpg', 'img/admin.jpg', 'img/reception.jpg',
    'img/reception 2.jpg', 'img/reception 3.jpg', 'img/reception 4.jpg'
]

extra_images_library = [
    'img/Library 4.jpg', 'img/Library 5.jpg', 'img/Library 6.jpg',
    'img/Library 7.jpg', 'img/Library 8.jpg', 'img/Library.jpg',
    'img/Library 2.jpg', 'img/Library 3.jpg', 'img/Libray 10.jpg'
]

def sanitize_filename(name):
    return re.sub(r'[^\w\s-]', '', name).strip().lower().replace(' ', '-')

def get_extra_images(product_name):
    name_lower = product_name.lower()
    if 'office' in name_lower or 'reception' in name_lower or 'conference' in name_lower or 'staff' in name_lower:
        return extra_images_office
    elif 'library' in name_lower or 'book' in name_lower or 'shelf' in name_lower or 'magazine' in name_lower or 'newspaper' in name_lower:
        return extra_images_library
    else:
        return extra_images_classroom

# New Footer HTML for Product Pages (links need ../)
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
                    <li><a href="../index.html"><i class="fas fa-home"></i> Home</a></li>
                    <li><a href="../services.html"><i class="fas fa-cogs"></i> Services</a></li>
                    <li><a href="../portfolio.html"><i class="fas fa-images"></i> Portfolio</a></li>
                    <li><a href="../about.html"><i class="fas fa-info-circle"></i> About</a></li>
                    <li><a href="../contact.html"><i class="fas fa-envelope-open-text"></i> Contact</a></li>
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
                        <img src="../img/Design.jpeg" alt="DeveloperBee Logo">
                    </a>
                </div>
                <div style="text-align: center; margin-top: 10px;">
                    <a href="https://skinterios.com/" style="color: #6B7280; font-size: 0.8rem;">skinterios.com</a>
                </div>
            </div>
        </div>
    </footer>"""

for product_name, img_src in image_map.items():
    filename = sanitize_filename(product_name) + '.html'
    filepath = os.path.join('product', filename)

    # 1. Update Title - Improved Regex
    # Matches <title>...</title> regardless of content
    content = re.sub(r'<title>.*?</title>', f'<title>{product_name} - skinterios</title>', template_content)

    # 2. Update Breadcrumb
    content = content.replace('<span>Standard Dual Bench</span>', f'<span>{product_name}</span>')

    # 3. Update H1
    content = re.sub(r'<h1 class="product-title">.*?</h1>', f'<h1 class="product-title">{product_name}</h1>', content)

    # 4. Update Canonical Link
    # Old: <link rel="canonical" href="https://skinterios.com/product-detail.html">
    # New: <link rel="canonical" href="https://skinterios.com/product/{filename}">
    content = content.replace(
        '<link rel="canonical" href="https://skinterios.com/product-detail.html">',
        f'<link rel="canonical" href="https://skinterios.com/product/{filename}">'
    )

    # 5. SKU
    acronym = "".join([w[0].upper() for w in product_name.split() if w])[:4]
    sku = f"SK-{acronym}-001"
    content = re.sub(r'<span class="product-sku">.*?</span>', f'<span class="product-sku">SKU: {sku}</span>', content)

    # 6. Main Image
    content = content.replace('src="img/classroom 2.jpg" alt="Standard Dual Bench" id="currentImage"', f'src="../{img_src}" alt="{product_name}" id="currentImage"')

    # 7. Description Text
    desc_text = f"The <strong>{product_name}</strong> by skinterios is engineered to withstand the rigors of daily institutional use while providing maximum comfort. Designed with ergonomics in mind, it supports modern learning and working environments."
    search_desc_block = """<p style="margin-bottom: 15px;">
                <strong>SK Furniture</strong> presents the robust Two Seater Classroom Desk, meticulously designed to meet the evolving needs of modern educational institutions. Engineered for longevity, this desk combines the strength of <strong>CRCA Steel</strong> with the aesthetic appeal of high-grade pre-laminated engineered wood. It is the ideal choice for schools, colleges, and coaching centers looking for furniture that withstands the rigors of daily use while maintaining its pristine condition for years.
            </p>"""
    content = content.replace(search_desc_block, f'<p style="margin-bottom: 15px;">{desc_text}</p>')

    # 8. WhatsApp Link
    encoded_name = urllib.parse.quote(product_name)
    new_wa_href = f'https://wa.me/918169285185?text=Hi,%20I%20am%20interested%20in%20bulk%20quote%20for%20{encoded_name}%20({sku})'
    content = re.sub(r'href="https://wa.me/918169285185\?text=.*?"', f'href="{new_wa_href}"', content)

    # 9. Thumbnails
    thumbs_block_start = '<div class="gallery-thumbs">'
    thumbs_block_end = '</div>'

    start_idx = content.find(thumbs_block_start)
    end_idx = content.find(thumbs_block_end, start_idx)

    extra_images = get_extra_images(product_name)

    if start_idx != -1 and end_idx != -1:
        new_thumbs = '\n'
        new_thumbs += f'                <img src="../{img_src}" class="gallery-thumb active" onclick="changeImage(this.src)">\n'
        for i in range(1, 4):
             rot_index = (len(product_name) + i) % len(extra_images)
             extra_img = extra_images[rot_index]
             new_thumbs += f'                <img src="../{extra_img}" class="gallery-thumb" onclick="changeImage(this.src)">\n'

        content = content[:start_idx + len(thumbs_block_start)] + new_thumbs + '            ' + content[end_idx:]

    # 10. Update Customer Images (Review Section)
    review_images_start = '<div class="customer-images-grid">'
    review_images_end = '</div>'

    rev_start_idx = content.find(review_images_start)

    if rev_start_idx != -1:
        # Find the end of this div, accounting for nested divs if any (though here it's simple)
        rev_end_idx = content.find(review_images_end, rev_start_idx)
        if rev_end_idx != -1:
             new_rev_imgs = '\n'
             for i in range(0, 3):
                 rev_rot_index = (len(product_name) + i + 5) % len(extra_images) # Different offset
                 rev_img = extra_images[rev_rot_index]
                 new_rev_imgs += f'                    <img src="../{rev_img}" class="customer-img-thumb" onclick="changeImage(this.src)">\n'

             content = content[:rev_start_idx + len(review_images_start)] + new_rev_imgs + '                ' + content[rev_end_idx:]


    # 11. Fix Relative Paths
    content = content.replace('href="css/style.css"', 'href="../css/style.css"')
    content = content.replace('src="js/script.js"', 'src="../js/script.js"')

    # Global img fix
    content = content.replace('src="img/', 'src="../img/')
    content = content.replace('src="../../img/', 'src="../img/')
    content = content.replace('src="../../', 'src="../')

    # Fix links
    links = ['index.html', 'solutions.html', 'manufacturing.html', 'services.html', 'projects.html', 'blog.html', 'inquiry.html', 'about.html',
             'solution-school.html', 'solution-classroom.html', 'solution-institutional.html', 'solution-library.html', 'solution-office.html', 'solution-hostel.html']

    for link in links:
        content = content.replace(f'href="{link}"', f'href="../{link}"')

    # Fix dropdown links
    content = content.replace('href="solutions.html#', 'href="../solutions.html#')

    # --- Header Modification: Add About Link ---
    if '<li><a href="../about.html">About</a></li>' not in content:
        header_search = '<li><a href="../index.html">Home</a></li>'
        header_replace = '<li><a href="../index.html">Home</a></li>\n                <li><a href="../about.html">About</a></li>'
        content = content.replace(header_search, header_replace)

    # --- Fix Header Logo Text ---
    content = content.replace('skfurniture', 'skinterios')


    # --- Replace Entire Footer ---
    # Find footer block
    footer_regex = re.compile(r'<footer>.*?</footer>', re.DOTALL)
    content = footer_regex.sub(footer_html, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Generated product pages.")
