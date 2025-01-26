from PIL import Image, ImageDraw

# Create a new image with a white background
size = (256, 256)
image = Image.new('RGB', size, 'white')
draw = ImageDraw.Draw(image)

# Draw a simple key symbol
draw.rectangle([78, 128, 178, 148], fill='blue')
draw.ellipse([48, 108, 88, 148], fill='blue')
draw.rectangle([128, 133, 188, 143], fill='blue')

# Save as ICO
image.save('app_icon.ico', format='ICO') 