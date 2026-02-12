from PIL import Image
import os

def optimize_images():
    # Optimize images in static/images
    images_dir = 'static/images'
    for filename in os.listdir(images_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(images_dir, filename)
            try:
                img = Image.open(filepath)
                # Convert to RGB if needed
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                # Resize if too large (max 1200px width)
                if img.width > 1200:
                    ratio = 1200 / img.width
                    new_size = (1200, int(img.height * ratio))
                    img = img.resize(new_size, Image.LANCZOS)
                # Save with optimization
                img.save(filepath, optimize=True, quality=85)
                print(f"Optimized: {filename}")
            except Exception as e:
                print(f"Error with {filename}: {e}")
    
    # Optimize project images
    projects_dir = 'static/projects'
    for filename in os.listdir(projects_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            filepath = os.path.join(projects_dir, filename)
            try:
                img = Image.open(filepath)
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                # Resize project images (max 800px width)
                if img.width > 800:
                    ratio = 800 / img.width
                    new_size = (800, int(img.height * ratio))
                    img = img.resize(new_size, Image.LANCZOS)
                img.save(filepath, optimize=True, quality=80)
                print(f"Optimized: {filename}")
            except Exception as e:
                print(f"Error with {filename}: {e}")

if __name__ == '__main__':
    optimize_images()
    print("Image optimization complete!")
