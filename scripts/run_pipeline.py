import mimetypes, pathlib, shutil, tempfile
from PIL import Image, ImageOps
from pillow_heif import register_heif_opener

register_heif_opener()

INPUTS_DIR  = pathlib.Path("data/inputs")
OUTPUTS_DIR = pathlib.Path("data/outputs")
READY_DIR   = pathlib.Path("data/ready")

OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
READY_DIR.mkdir(parents=True, exist_ok=True)

# ── helpers ───────────────────────────────────────────────────────────────────

def is_image(path):
    try:
        t, _ = mimetypes.guess_type(path)
        if "image" not in t: return False
        Image.open(path).verify()
        return True
    except:
        return False

def optimize(src, dst, max_size=(1920, 1920)):
    img = ImageOps.exif_transpose(Image.open(src))
    has_alpha = img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info)
    img.thumbnail(max_size, Image.Resampling.LANCZOS)
    if has_alpha:
        img = img.convert("RGBA")
        dst = dst.with_suffix(".png")
        img.save(dst, format="PNG", optimize=True, compress_level=6)
    else:
        img = img.convert("RGB")
        dst = dst.with_suffix(".jpg")
        img.save(dst, format="JPEG", quality=85, optimize=True, progressive=True)
    return dst

def make_zip(files, zip_path):
    with tempfile.TemporaryDirectory() as tmp:
        for f in files: shutil.copy(f, tmp)
        shutil.make_archive(str(zip_path.with_suffix("")), "zip", tmp)
    print(f"  -> {zip_path}")

# ── pipeline ──────────────────────────────────────────────────────────────────

images = [f for f in INPUTS_DIR.glob("*") if f.is_file() and is_image(f)]
print(f"Found {len(images)} images")

# Step 1: zip raw
print("\n[1] Zipping raw images...")
make_zip(images, OUTPUTS_DIR / "images.zip")

# Step 2 + 3: optimize and zip
print("\n[2] Optimizing...")
optimized = []
for src in images:
    out = optimize(src, READY_DIR / src.name)
    print(f"  {src.name} -> {out.name}")
    optimized.append(out)

print("\n[3] Zipping optimized images...")
make_zip(optimized, OUTPUTS_DIR / "images-optimized.zip")

print("\nDone!")