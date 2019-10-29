from PIL import Image


image = Image.open('mona.png')
rgb = image.convert('RGB')
rgb.save('mona.png')
