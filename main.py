from PIL import Image

def image_to_ascii(image_path):
    # Load the image
    image = Image.open(image_path)
    
    # Resize image
    width, height = image.size
    ascii_width = 100
    ascii_height = (height / width) * ascii_width * 0.55
    image = image.resize((ascii_width, int(ascii_height)))
    
    # Define ASCII characters
    ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    
    # Map brightness to ASCII characters
    ascii_str = ''
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))
            brightness = (r + g + b) / 3 / 255
            ascii_index = int(brightness * (len(ascii_chars) - 1))
            ascii_str += '\033[38;2;{};{};{}m{}\033[m'.format(r, g, b, ascii_chars[ascii_index])
        ascii_str += '\n'
    
    return ascii_str

ascii_art = image_to_ascii(r"./path/to/image")
print(ascii_art)