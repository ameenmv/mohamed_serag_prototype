#!/usr/bin/env python3
"""Replace placeholder data with real product info and images in prototype files."""
import re, os

PROTO = os.path.dirname(os.path.abspath(__file__))

def read(f):
    with open(os.path.join(PROTO, f), 'r', encoding='utf-8') as fh:
        return fh.read()

def write(f, content):
    with open(os.path.join(PROTO, f), 'w', encoding='utf-8') as fh:
        fh.write(content)

# ========== Helper: image tag ==========
def img(src, alt, h='180px'):
    return f'<img src="./images/{src}" alt="{alt}" style="width:auto;height:{h};object-fit:contain">'

# ========== FRIDGE SVG patterns ==========
FRIDGE_SVG = r'<svg[^>]*viewBox="0 0 48 48"[^>]*>\s*<rect x="13" y="4" width="22" height="40" rx="3">\s*</rect>\s*<path d="M13 20h22M18 10v6M18 25v8">\s*</path>\s*</svg>'
WASHER_SVG = r'<svg[^>]*viewBox="0 0 48 48"[^>]*>\s*<rect x="9" y="4" width="30" height="40" rx="4">\s*</rect>\s*<circle cx="24" cy="28" r="10">\s*</circle>\s*<circle cx="24" cy="28" r="5">\s*</circle>\s*<path d="M15 11h8M31 11h2">\s*</path>\s*</svg>'
TV_SVG = r'<svg[^>]*viewBox="0 0 48 48"[^>]*>\s*<rect x="4" y="8" width="40" height="27" rx="3">\s*</rect>\s*<path d="M16 42h16M24 35v7">\s*</path>\s*</svg>'
AC_SVG = r'<svg[^>]*viewBox="0 0 48 48"[^>]*>\s*<rect x="4" y="10" width="40" height="16" rx="3">\s*</rect>\s*<path d="M10 21h28M14 32c2 3 2 5 0 8M24 32c2 3 2 5 0 8M34 32c2 3 2 5 0 8">\s*</path>\s*</svg>'
COOKER_SVG = r'<svg[^>]*viewBox="0 0 48 48"[^>]*>\s*<rect x="7" y="6" width="34" height="36" rx="3">\s*</rect>\s*<path d="M7 16h34">\s*</path>\s*<circle cx="14" cy="11" r="1.5">\s*</circle>\s*<circle cx="24" cy="11" r="1.5">\s*</circle>\s*<circle cx="34" cy="11" r="1.5">\s*</circle>\s*<rect x="12" y="22" width="24" height="15" rx="2">\s*</rect>\s*</svg>'

# ========== index.dc.html ==========
print("Processing index.dc.html...")
html = read('index.dc.html')

# Replace [الماركة] with real brands in flash sale section
html = html.replace('[الماركة]', 'Samsung', 1)
html = html.replace('ثلاجة نوفروست ديجيتال', 'ثلاجة سامسونج نوفروست بابين 450 لتر')
html = html.replace('[الماركة]', 'LG', 1)
html = html.replace('[الماركة]', 'Sharp', 1)
html = html.replace('[الماركة]', 'Samsung', 1)

# Replace prices in flash sale
html = html.replace("[السعر]</span><span style=\"font-size:14px;font-weight:600\">ج.م</span><span style=\"font-size:14px;color:#8A918C;text-decoration:line-through\">[السعر القديم]",
    "28,900</span><span style=\"font-size:14px;font-weight:600\">ج.م</span><span style=\"font-size:14px;color:#8A918C;text-decoration:line-through\">32,500", 1)
html = html.replace("[السعر]</span><span style=\"font-size:14px;font-weight:600\">ج.م</span><span style=\"font-size:14px;color:#8A918C;text-decoration:line-through\">[السعر القديم]",
    "24,500</span><span style=\"font-size:14px;font-weight:600\">ج.م</span><span style=\"font-size:14px;color:#8A918C;text-decoration:line-through\">27,000", 1)
html = html.replace("[السعر]</span><span style=\"font-size:14px;font-weight:600\">ج.م</span><span style=\"font-size:14px;color:#8A918C;text-decoration:line-through\">[السعر القديم]",
    "26,900</span><span style=\"font-size:14px;font-weight:600\">ج.م</span><span style=\"font-size:14px;color:#8A918C;text-decoration:line-through\">29,500", 1)
html = html.replace("[السعر]</span><span style=\"font-size:14px;font-weight:600\">ج.م</span><span style=\"font-size:14px;color:#8A918C;text-decoration:line-through\">[السعر القديم]",
    "21,900</span><span style=\"font-size:14px;font-weight:600\">ج.م</span><span style=\"font-size:14px;color:#8A918C;text-decoration:line-through\">24,500", 1)

# Replace phone number placeholder
html = html.replace('[رقم الهاتف]', '0100-123-4567')

# Replace bridal package prices
html = html.replace("""<span style="font-family:'Outfit',sans-serif;font-weight:800;font-size:24px;color:#FAF7EE">[السعر]</span> ج.م""",
    """<span style="font-family:'Outfit',sans-serif;font-weight:800;font-size:24px;color:#FAF7EE">52,900</span> ج.م""", 1)
html = html.replace("""<span style="font-family:'Outfit',sans-serif;font-weight:800;font-size:24px;color:#14201A">[السعر]</span> ج.م""",
    """<span style="font-family:'Outfit',sans-serif;font-weight:800;font-size:24px;color:#14201A">89,500</span> ج.م""", 1)

# Try to replace remaining [السعر] in bridal
html = html.replace("[السعر]</span> ج.م", "145,000</span> ج.م", 1)

# Replace flash sale SVGs with product images
html = re.sub(
    r'(<div style="position:relative;height:210px;border-radius:20px;background:#F4F1E6;display:flex;align-items:center;justify-content:center;color:#2A4D38">.*?<button[^>]*>.*?</button>\s*)' + FRIDGE_SVG,
    r'\1' + img('fridge-samsung.png', 'ثلاجة سامسونج', '170px'),
    html, count=1, flags=re.DOTALL
)
html = re.sub(
    r'(<div style="position:relative;height:210px;border-radius:20px;background:#F4F1E6;display:flex;align-items:center;justify-content:center;color:#2A4D38">.*?<button[^>]*>.*?</button>\s*)' + WASHER_SVG,
    r'\1' + img('washer-lg.png', 'غسالة LG', '170px'),
    html, count=1, flags=re.DOTALL
)
html = re.sub(
    r'(<div style="position:relative;height:210px;border-radius:20px;background:#F4F1E6;display:flex;align-items:center;justify-content:center;color:#2A4D38">.*?<button[^>]*>.*?</button>\s*)' + AC_SVG,
    r'\1' + img('ac-sharp.png', 'تكييف شارب', '170px'),
    html, count=1, flags=re.DOTALL
)
html = re.sub(
    r'(<div style="position:relative;height:210px;border-radius:20px;background:#F4F1E6;display:flex;align-items:center;justify-content:center;color:#2A4D38">.*?<button[^>]*>.*?</button>\s*)' + TV_SVG,
    r'\1' + img('tv-samsung.png', 'شاشة سامسونج', '170px'),
    html, count=1, flags=re.DOTALL
)

# Replace hero floating cards SVGs with images
# Main card - fridge
html = re.sub(
    r'(<div class="floaty" style="--r:0deg;[^"]*">\s*)(<svg viewBox="0 0 48 48" width="64%"[^>]*>.*?</svg>)',
    r'\1<img src="./images/fridge-samsung.png" alt="ثلاجات" style="width:64%;height:auto;object-fit:contain">',
    html, count=1, flags=re.DOTALL
)
# Washer card
html = re.sub(
    r'(<div class="floaty" style="--r:-5deg;[^"]*">\s*)(<svg viewBox="0 0 48 48" width="56%"[^>]*>.*?</svg>)',
    r'\1<img src="./images/washer-lg.png" alt="غسالات" style="width:56%;height:auto;object-fit:contain">',
    html, count=1, flags=re.DOTALL
)
# TV card
html = re.sub(
    r'(<div class="floaty" style="--r:5deg;[^"]*">\s*)(<svg viewBox="0 0 48 48" width="62%"[^>]*>.*?</svg>)',
    r'\1<img src="./images/tv-samsung.png" alt="شاشات" style="width:62%;height:auto;object-fit:contain">',
    html, count=1, flags=re.DOTALL
)
# AC card
html = re.sub(
    r'(<div class="floaty" style="--r:3deg;[^"]*">\s*)(<svg viewBox="0 0 48 48" width="50%"[^>]*>.*?</svg>)',
    r'\1<img src="./images/ac-sharp.png" alt="تكييفات" style="width:50%;height:auto;object-fit:contain">',
    html, count=1, flags=re.DOTALL
)

write('index.dc.html', html)
print("✅ index.dc.html updated!")

# ========== product.dc.html ==========
print("Processing product.dc.html...")
html = read('product.dc.html')

# Replace main product image (large)
html = re.sub(
    r'<svg viewBox="0 0 48 48" width="320" height="320"[^>]*>.*?</svg>',
    img('fridge-samsung.png', 'ثلاجة سامسونج نوفروست', '380px'),
    html, count=1, flags=re.DOTALL
)

# Replace [SKU]
html = html.replace('[SKU]', 'SR-RF-450-SL')
# Replace [التكلفة]
html = html.replace('[التكلفة]', '150 ج.م')
# Replace [المدة]
html = html.replace('[المدة]', '24 ساعة')
# Replace warranty
html = html.replace('[مدة الضمان]', '5 سنوات', 2)
# Replace dimensions
html = html.replace('[العرض × العمق × الارتفاع]', '70 × 67 × 185 سم')
# Replace origin
html = html.replace('[بلد الصنع]', 'كوريا الجنوبية')
# Replace return policy
html = html.replace('[اكتب سياسة الاسترجاع: المدة، والشروط، وحالة العبوة].', 'يمكن استرجاع المنتج خلال 14 يوم من تاريخ الاستلام بشرط أن يكون في حالته الأصلية مع العبوة والضمان. رسوم الشحن على المشتري في حالة الاسترجاع.')
# Replace maintenance data
html = html.replace('[بيانات الصيانة]', 'مركز خدمة سامسونج المعتمد - الخط الساخن: 16580')

# Replace phone in product page
html = html.replace('[رقم الهاتف]', '0100-123-4567')

# Replace discount percentage placeholder
html = html.replace('[نسبة الخصم]', '5% على المجموعة')

# Replace related products SVGs with images
html = re.sub(FRIDGE_SVG, img('fridge-toshiba.png', 'ثلاجة توشيبا', '90px'), html, count=3, flags=re.DOTALL)
html = re.sub(WASHER_SVG, img('washer-lg.png', 'غسالة LG', '90px'), html, count=1, flags=re.DOTALL)

# Replace "[صورة المنتج هنا]" label
html = html.replace('[صورة المنتج هنا]', 'صورة حقيقية')

write('product.dc.html', html)
print("✅ product.dc.html updated!")

# ========== checkout.dc.html ==========
print("Processing checkout.dc.html...")
html = read('checkout.dc.html')
html = html.replace('[رقم الهاتف]', '0100-123-4567')
html = html.replace('[المدة]', '24 ساعة')

# Replace checkout product images with real ones
html = re.sub(FRIDGE_SVG, img('fridge-samsung.png', 'ثلاجة سامسونج', '34px'), html, count=1, flags=re.DOTALL)
html = re.sub(WASHER_SVG, img('washer-lg.png', 'غسالة LG', '34px'), html, count=1, flags=re.DOTALL)
html = re.sub(TV_SVG, img('tv-samsung.png', 'شاشة سامسونج', '34px'), html, count=1, flags=re.DOTALL)

write('checkout.dc.html', html)
print("✅ checkout.dc.html updated!")

# ========== order-confirmed.dc.html ==========
print("Processing order-confirmed.dc.html...")
html = read('order-confirmed.dc.html')
html = html.replace('[رقم الهاتف]', '0100-123-4567')

# Replace confirmation product images
html = re.sub(FRIDGE_SVG, img('fridge-samsung.png', 'ثلاجة سامسونج', '30px'), html, count=1, flags=re.DOTALL)
html = re.sub(WASHER_SVG, img('washer-lg.png', 'غسالة LG', '30px'), html, count=1, flags=re.DOTALL)
html = re.sub(TV_SVG, img('tv-samsung.png', 'شاشة سامسونج', '30px'), html, count=1, flags=re.DOTALL)

write('order-confirmed.dc.html', html)
print("✅ order-confirmed.dc.html updated!")

# ========== cart.dc.html ==========
print("Processing cart.dc.html...")
html = read('cart.dc.html')
html = html.replace('[رقم الهاتف]', '0100-123-4567')
write('cart.dc.html', html)
print("✅ cart.dc.html updated!")

# ========== login.dc.html ==========
print("Processing login.dc.html...")
html = read('login.dc.html')
html = html.replace('[رقم الهاتف]', '0100-123-4567')
write('login.dc.html', html)
print("✅ login.dc.html updated!")

# ========== account.dc.html ==========
print("Processing account.dc.html...")
html = read('account.dc.html')
html = html.replace('[رقم الهاتف]', '0100-123-4567')
html = html.replace('[اسم العميل]', 'أحمد محمود')
html = html.replace('[000]', '1,250', 2)
html = html.replace('[العنوان بالتفصيل]', 'شارع الجلاء، عمارة 15، الدور 3، شقة 7', 1)
html = html.replace('[العنوان بالتفصيل]', 'شارع النصر، برج الأمل، الدور 5', 1)
html = html.replace('[المحافظة، المدينة]', 'الدقهلية، طلخا')
write('account.dc.html', html)
print("✅ account.dc.html updated!")

# ========== Header.dc.html ==========
print("Processing Header.dc.html...")
html = read('Header.dc.html')
html = html.replace('[رقم الهاتف]', '0100-123-4567')
write('Header.dc.html', html)
print("✅ Header.dc.html updated!")

# ========== shop.dc.html ==========
print("Processing shop.dc.html...")
html = read('shop.dc.html')
html = html.replace('[رقم الهاتف]', '0100-123-4567')
write('shop.dc.html', html)
print("✅ shop.dc.html updated!")

print("\n🎉 All files updated with real data and images!")
