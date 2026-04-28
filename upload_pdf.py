import cloudinary
import cloudinary.uploader

# 🔐 Cloudinary config
cloudinary.config(
    cloud_name="djxsxxnbu",
    api_key="642457568517121",
    api_secret="vAcexrZfAmCqCVJWKhuif25bEv0"
)

# 📂 All PDFs list
files = [
    ("1mm.pdf", "catalogues/1mm"),
    ("elite.pdf", "catalogues/elite"),
    ("lemore.pdf", "catalogues/lemore"),
]

for file_path, public_id in files:
    try:
        print(f"\nUploading {file_path}...")

        with open(file_path, "rb") as f:
            response = cloudinary.uploader.upload_large(
                f,
                resource_type="raw",
                public_id=public_id,
                overwrite=True,
                chunk_size=6000000
            )

        print("✅ Upload Successful!")
        print("URL:", response["secure_url"])

    except Exception as e:
        print(f"❌ Upload Failed for {file_path}:", e)
