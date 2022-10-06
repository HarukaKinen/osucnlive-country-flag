from PIL import Image, ImageFont, ImageDraw
import io
import os

os.makedirs("Dist", exist_ok=True)

# otf
font = ImageFont.truetype("Font/Exo2-ExtraBold.otf", size = 70)

for flag in os.listdir("Base"):
    country_code = str(flag).replace(".png", "")
    
    print(country_code)

    flag = Image.open(f"Base/{flag}").convert("RGBA")
    mask = Image.open("MASK.png").convert("RGBA")

    draw = ImageDraw.Draw(mask)
    W, H = flag.size
    w, h = draw.textsize(country_code, font=font)
    size = ((W - w)/2, (H - h)/2 - 10)
    draw.text(size, country_code, font=font, fill=(255, 255 ,255), stroke_width=2, stroke_fill=(0, 0, 0))

    flag = Image.alpha_composite(flag, mask)

    flag.save(f"Dist/{country_code}.png")