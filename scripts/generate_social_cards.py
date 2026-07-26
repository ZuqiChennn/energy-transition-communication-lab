"""Generate original campaign cards without third-party logos or images."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "cards"
OUT.mkdir(parents=True, exist_ok=True)


def font(size: int, bold: bool = False):
    names = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for name in names:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()


def wrapped(draw, xy, text, fill, fnt, width, spacing=14):
    words = text.split()
    lines, line = [], ""
    for word in words:
        trial = f"{line} {word}".strip()
        if draw.textbbox((0, 0), trial, font=fnt)[2] <= width:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    draw.multiline_text(xy, "\n".join(lines), fill=fill, font=fnt, spacing=spacing)


cards = [
    ("01-one-better-hour.png", "#F3F1E8", "#153D37", "ONE FLEXIBLE APPLIANCE.", "ONE BETTER HOUR.", "Start with one routine—not the whole household."),
    ("02-no-universal-hour.png", "#173D34", "#F7E8BF", "MYTH:", "NIGHT IS ALWAYS CHEAPER.", "There is no universal best hour. Check the information available for your tariff, app or device."),
    ("03-four-question-check.png", "#EEF4F1", "#1B352F", "BEFORE YOU SHIFT", "ASK FOUR QUESTIONS.", "Flexible? Safe? Informed? Convenient? If one answer is no, not shifting is also valid."),
]

for filename, background, ink, kicker, title, body in cards:
    image = Image.new("RGB", (1080, 1350), background)
    d = ImageDraw.Draw(image)
    d.rounded_rectangle((72, 72, 1008, 1278), radius=38, outline=ink, width=5)
    d.ellipse((810, 110, 945, 245), outline="#D4A34F", width=18)
    d.arc((835, 135, 920, 220), 25, 320, fill=ink, width=8)
    d.text((110, 120), "SHIFT THE HOUR / 01", fill=ink, font=font(28, True))
    d.text((110, 390), kicker, fill="#B27322", font=font(38, True))
    wrapped(d, (110, 465), title, ink, font(86, True), 820, spacing=10)
    wrapped(d, (110, 875), body, ink, font(42), 780, spacing=16)
    d.line((110, 1190, 970, 1190), fill=ink, width=3)
    d.text((110, 1215), "Independent portfolio case · public information only", fill=ink, font=font(23))
    image.save(OUT / filename, quality=95)
    print(f"Wrote {OUT / filename}")
