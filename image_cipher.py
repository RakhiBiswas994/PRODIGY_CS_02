from PIL import Image

def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save(output_path)
    print("Image Encrypted and saved as", output_path)

def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path).convert("RGB")
    pixels = img.load()

    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save(output_path)
    print("Image Decrypted and saved as", output_path)

base_path = "C:/Users/RAKHI/Desktop/CyberSecurity_Project_Tasks/Pixel Manipulation for Image Encryption/"

encrypt_image(base_path + "kolkata.png", base_path + "encrypted.png", 50)
decrypt_image(base_path + "encrypted.png", base_path + "decrypted.png", 50)
