from PIL import Image

# You need to save the attached image as 'app_icon.png' first
try:
    img = Image.open('app_icon.png')
    # Create icon with multiple sizes
    img.save('icon.ico', format='ICO', sizes=[
        (256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)
    ])
    print("Icon created successfully: icon.ico")
except FileNotFoundError:
    print("Please save the attached image as 'app_icon.png' in the project root first")
except Exception as e:
    print(f"Error: {e}")
