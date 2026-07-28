import os
from PIL import Image

def compress_images(directory, max_size_mb=1.0):
    count = 0
    total_saved_mb = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                filepath = os.path.join(root, file)
                
                try:
                    file_size_mb = os.path.getsize(filepath) / (1024 * 1024)
                    
                    if file_size_mb > max_size_mb:
                        # Open the image
                        img = Image.open(filepath)
                        
                        # Convert to RGB if necessary (e.g. RGBA pngs being saved as JPEG)
                        if img.mode in ("RGBA", "P"):
                            img = img.convert("RGB")
                            
                        # Resize if dimensions are extremely large
                        max_dim = 1920
                        if img.width > max_dim or img.height > max_dim:
                            img.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
                            
                        # Save the image with compression
                        img.save(filepath, optimize=True, quality=75)
                        
                        new_size_mb = os.path.getsize(filepath) / (1024 * 1024)
                        saved_mb = file_size_mb - new_size_mb
                        total_saved_mb += saved_mb
                        count += 1
                        print(f"Compressed {file}: {file_size_mb:.2f} MB -> {new_size_mb:.2f} MB")
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")
                    
    print(f"\nFinished compressing {count} images in {directory}.")
    print(f"Total space saved: {total_saved_mb:.2f} MB")

if __name__ == '__main__':
    print("Compressing media folder...")
    compress_images('media', max_size_mb=0.5)
    
    print("\nCompressing LAVIN QR folder...")
    if os.path.exists('LAVIN QR'):
        compress_images('LAVIN QR', max_size_mb=0.5)
