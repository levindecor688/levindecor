import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mylevin.settings')
django.setup()

import cloudinary
import cloudinary.uploader
from django.conf import settings
from decouple import config

cloud_name = config('CLOUDINARY_CLOUD_NAME', default='')
api_key = config('CLOUDINARY_API_KEY', default='')
api_secret = config('CLOUDINARY_API_SECRET', default='')

if not cloud_name:
    print("ERROR: Please set CLOUDINARY_CLOUD_NAME in .env first!")
    exit(1)

cloudinary.config(
    cloud_name=cloud_name,
    api_key=api_key,
    api_secret=api_secret
)

media_root = settings.MEDIA_ROOT

print(f"Starting upload from {media_root} to Cloudinary ({cloud_name})...")

success_count = 0
fail_count = 0

for root, dirs, files in os.walk(media_root):
    for file in files:
        file_path = os.path.join(root, file)
        rel_path = os.path.relpath(file_path, media_root)
        # Cloudinary public_id without file extension or with path
        public_id = os.path.splitext(rel_path)[0].replace('\\', '/')
        
        try:
            print(f"Uploading: {rel_path} -> public_id: {public_id}...")
            cloudinary.uploader.upload(
                file_path,
                public_id=public_id,
                overwrite=True,
                resource_type="auto"
            )
            success_count += 1
        except Exception as e:
            print(f"Failed to upload {rel_path}: {e}")
            fail_count += 1

print(f"\nCompleted! {success_count} files uploaded successfully. {fail_count} failed.")
