from PIL import Image
import numpy as np

raw_image = Image.open("raw.jpeg")
raw_pixels = raw_image.getdata()

secret_data = [1, 0, 0, 1]
secret_data.append(1)
secret_data.extend([0] * (len(raw_pixels) - len(secret_data)))

processed_pixels = []
for i, pixel in enumerate(raw_pixels):
    processed_pixels.append(((pixel[0] >> 2 << 2) + secret_data[i], pixel[1], pixel[2]))

Image.fromarray(np.array(processed_pixels, dtype=np.uint8).reshape(raw_image.size[1], raw_pixels.size[0], 3)).save("processed.png")
