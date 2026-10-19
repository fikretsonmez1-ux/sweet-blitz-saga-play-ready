from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('icons', exist_ok=True)

for size in (192, 512):
    img = Image.new('RGBA', (size, size), (42, 15, 58, 255))
    d = ImageDraw.Draw(img)
    # center candy circle
    cx, cy = size//2, size//2
    radius = int(size * 0.33)
    d.ellipse((cx-radius, cy-radius, cx+radius, cy+radius), fill=(255,95,162,255))
    d.ellipse((cx-int(radius*0.5), cy-int(radius*0.5), cx+int(radius*0.5), cy+int(radius*0.5)), fill=(255,216,77,255))
    # optional text placeholder
    try:
        fsize = size//3
        font = ImageFont.truetype("DejaVuSans.ttf", fsize)
        d.text((cx-fsize//2, cy-fsize//2), "🍭", font=font, fill=(255,255,255,255))
    except Exception:
        # fallback: no font available
        pass
    img.save(f'icons/icon-{size}.png')

print('Icons generated: icons/icon-192.png and icons/icon-512.png')
