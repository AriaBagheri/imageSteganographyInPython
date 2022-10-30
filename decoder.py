from PIL import Image

encoded_image = Image.open("processed.png")
encoded_pixels = encoded_image.getdata()

secret_data = []
for pixel in encoded_pixels:
    secret_data.append(pixel[0] % 2)

secret_data = ''.join(map(lambda x: str(x), secret_data))
secret_data = secret_data[:secret_data.rfind('1')]
print(secret_data)
