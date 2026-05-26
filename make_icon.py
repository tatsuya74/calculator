from PIL import Image, ImageDraw, ImageFont

SIZE = 256
img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# オレンジの円
draw.ellipse([8, 8, SIZE - 8, SIZE - 8], fill="#D97706")

# 白い「C」の文字
try:
    font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 160)
except Exception:
    font = ImageFont.load_default()

text = "C"
bbox = draw.textbbox((0, 0), text, font=font)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
x = (SIZE - tw) // 2 - bbox[0] + 4
y = (SIZE - th) // 2 - bbox[1] - 8
draw.text((x, y), text, fill="white", font=font)

img.save("C:/Claude/claude_icon.ico", format="ICO", sizes=[(256,256),(64,64),(32,32),(16,16)])
print("アイコン作成完了")
