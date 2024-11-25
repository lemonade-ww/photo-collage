from PIL import Image
import os
import random

# Replace 'image_folder' with the actual path to your image folder
image_folder = '/Users/henrywang/Pictures/'

# Replace 'output_path' with the desired output path
output_path = '/Users/henrywang/Pictures/collage.jpg'

output_dpi = 300
num = 20
size = num * 400

collage_size = (size, size)


def crop_to_square(image):
    width, height = image.size
    size = min(width, height)
    left = (width - size) // 2
    top = (height - size) // 2
    right = (width + size) // 2
    bottom = (height + size) // 2
    return image.crop((left, top, right, bottom))


def create_collage(image_folder, output_path, collage_size, number):
    collage = Image.new('RGB', collage_size)
    slot_size = collage_size[0] // number

    images = []

    for filename in os.listdir(image_folder):
        if filename[0] != '.':
            image_path = os.path.join(image_folder, filename)
            img = Image.open(image_path)
            img = crop_to_square(img)
            img = img.resize((slot_size, slot_size))
            images.append(img)

    random.shuffle(images)

    count = 0
    for i in range(number):
        for j in range(number):
            print(i, j)
            collage.paste(images[count], (j * slot_size, i * slot_size))
            count += 1

    collage.save(output_path,  dpi=(output_dpi, output_dpi))
    # collage.show()


create_collage(image_folder, output_path, collage_size, num)
