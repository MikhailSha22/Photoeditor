from PIL import Image, ImageEnhance, ImageFilter
import os

path = "./imgs"# В папку imgs кладется первичная фото
# в папку editedImgs выходит уже обработанное фото указать путь для этой папки
pathOut = "./editedImgs"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")


    #sharpending

    edit = img.filter(ImageFilter.SHARPEN)

    clean_name = os.path.splitext(filename)[0]
    edit.save(f'{pathOut}/{clean_name}_edited.jpg')