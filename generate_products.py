import os
import re

# Read product-detail.html to use as a template
with open('product-detail.html', 'r', encoding='utf-8') as f:
    template_content = f.read()

# Define the image map (copied from the JS logic in product-detail.html)
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
    'Cafe Furniture': 'img/canteen.jpg'
}

extra_images = [
    'img/classroom 2.jpg', 'img/classroom 3.jpg', 'img/classroom 4.jpg',
    'img/classroom 5.jpg', 'img/classroom 6.jpg', 'img/classroom 7.jpg',
    'img/classroom 8.jpg', 'img/classroom 9.jpg', 'img/classroom 10.jpg',
    'img/classroom 11.jpg', 'img/classroom 12.jpg', 'img/classroom 15.jpg'
]

# Function to sanitize filename
def sanitize_filename(name):
    return re.sub(r'[^\w\s-]', '', name).strip().lower().replace(' ', '-')

for product_name, img_src in image_map.items():
    filename = sanitize_filename(product_name) + '.html'
    filepath = os.path.join('product', filename)

    # 1. Update Title
    content = template_content.replace('<title>Standard Dual Bench - skfurniture</title>', f'<title>{product_name} - skfurniture</title>')

    # 2. Update Breadcrumb
    # <a href="solutions.html">Solutions</a> &gt; <span>Standard Dual Bench</span>
    content = content.replace('<span>Standard Dual Bench</span>', f'<span>{product_name}</span>')

    # 3. Update H1
    # <h1 class="product-title">Standard Dual Bench for Classrooms (Heavy Duty)</h1>
    content = re.sub(r'<h1 class="product-title">.*?</h1>', f'<h1 class="product-title">{product_name}</h1>', content)

    # 4. SKU
    acronym = "".join([w[0].upper() for w in product_name.split() if w])[:4]
    sku = f"SK-{acronym}-001"
    content = re.sub(r'<span class="product-sku">.*?</span>', f'<span class="product-sku">SKU: {sku}</span>', content)

    # 5. Main Image
    # <img src="img/classroom 2.jpg" alt="Standard Dual Bench" id="currentImage"
    content = content.replace('src="img/classroom 2.jpg" alt="Standard Dual Bench" id="currentImage"', f'src="../{img_src}" alt="{product_name}" id="currentImage"')

    # 6. Description Text (this is JS generated in original, but let's pre-fill it in HTML)
    desc_text = f"The <strong>{product_name}</strong> by skfurniture is engineered to withstand the rigors of daily institutional use while providing maximum comfort. Designed with ergonomics in mind, it supports modern learning and working environments."
    # Find the paragraph in the description tab
    # <div id="desc" class="tab-content active">\s*<h3.*?</h3>\s*<p.*?>\s*<strong>SK Furniture</strong> presents...
    # We will replace the inner HTML of the first p tag in #desc or just replace a known block
    search_desc_block = """<p style="margin-bottom: 15px;">
                <strong>SK Furniture</strong> presents the robust Two Seater Classroom Desk, meticulously designed to meet the evolving needs of modern educational institutions. Engineered for longevity, this desk combines the strength of <strong>CRCA Steel</strong> with the aesthetic appeal of high-grade pre-laminated engineered wood. It is the ideal choice for schools, colleges, and coaching centers looking for furniture that withstands the rigors of daily use while maintaining its pristine condition for years.
            </p>"""
    content = content.replace(search_desc_block, f'<p style="margin-bottom: 15px;">{desc_text}</p>')

    # 7. WhatsApp Link
    # <a href="https://wa.me/918169285185?text=Hi,%20I%20am%20interested%20in%20bulk%20quote%20for%20Standard%20Dual%20Bench%20(SK-DB-001)"
    import urllib.parse
    encoded_name = urllib.parse.quote(product_name)
    new_wa_href = f'https://wa.me/918169285185?text=Hi,%20I%20am%20interested%20in%20bulk%20quote%20for%20{encoded_name}%20({sku})'
    content = re.sub(r'href="https://wa.me/918169285185\?text=.*?"', f'href="{new_wa_href}"', content)

    # 8. Thumbnails
    # Replace the thumbs manually to avoid JS reliance for initial load
    # <img src="img/classroom 4.jpg" class="gallery-thumb active"
    # <img src="img/classroom 5.jpg" class="gallery-thumb"
    # ...
    # We need to construct the gallery thumbs block
    thumbs_block_start = '<div class="gallery-thumbs">'
    thumbs_block_end = '</div>'

    # Find content between start and end
    start_idx = content.find(thumbs_block_start)
    end_idx = content.find(thumbs_block_end, start_idx)

    if start_idx != -1 and end_idx != -1:
        new_thumbs = '\n'
        # Main thumb
        new_thumbs += f'                <img src="../{img_src}" class="gallery-thumb active" onclick="changeImage(this.src)">\n'
        # Extra thumbs
        for i in range(1, 4):
             rot_index = (len(product_name) + i) % len(extra_images)
             extra_img = extra_images[rot_index]
             new_thumbs += f'                <img src="../{extra_img}" class="gallery-thumb" onclick="changeImage(this.src)">\n'

        content = content[:start_idx + len(thumbs_block_start)] + new_thumbs + '            ' + content[end_idx:]

    # 9. Fix Relative Paths
    # css/style.css -> ../css/style.css
    # js/script.js -> ../js/script.js
    # img/ -> ../img/ (already handled for specific img tags above mostly, but need global replace for others)
    # <a href="index.html"> -> <a href="../index.html">
    # Note: We need to be careful not to double replace if we already did ../img

    # Basic replacements
    content = content.replace('href="css/style.css"', 'href="../css/style.css"')
    content = content.replace('src="js/script.js"', 'src="../js/script.js"')
    content = content.replace('src="img/', 'src="../img/')
    # The previous main image replacement used ../img/, so if we replace img/ with ../img/ globally,
    # we might get ../../img/ if we are not careful.
    # Actually, my step 5 used src="../{img_src}". img_src had "img/...". So it became src="../img/...".
    # If I now replace 'src="img/' with 'src="../img/', it will become 'src="../../img/'.
    # So I should have done global replace first or be smarter.

    # Let's revert the step 5 change locally in memory or fix it.
    # Actually, let's just fix the double dots.
    content = content.replace('src="../../', 'src="../')

    # Fix links
    links = ['index.html', 'solutions.html', 'manufacturing.html', 'services.html', 'projects.html', 'blog.html', 'inquiry.html',
             'solution-school.html', 'solution-classroom.html', 'solution-institutional.html', 'solution-library.html', 'solution-office.html', 'solution-hostel.html']

    for link in links:
        content = content.replace(f'href="{link}"', f'href="../{link}"')

    # Also fix links inside dropdown
    # <a href="solutions.html#classroom">
    content = content.replace('href="solutions.html#', 'href="../solutions.html#')

    # Fix Logo link
    # <a href="index.html" class="logo"> is covered above

    # Customer images in review tab
    # <img src="img/classroom 15.jpg" ...
    # These are caught by src="img/ -> src="../img/ replacement?
    # I haven't done the global src="img/ replacement yet. Let's do it.
    content = content.replace('src="img/', 'src="../img/')
    # Fix potential double ../ from Step 5
    content = content.replace('src="../../', 'src="../')

    # 10. Disable the dynamic JS loader since we are making static pages?
    # The JS block at the bottom: document.addEventListener('DOMContentLoaded', function() { ... })
    # We should probably remove it or comment it out so it doesn't override our static changes.
    # However, keeping it might be harmless if it doesn't find ?product= param.
    # But wait, we are not passing ?product= param to these pages. So the JS will not execute the "if (productName)" block.
    # So it is safe to leave it.

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Generated product pages.")
