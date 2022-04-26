from PIL import Image, ImageDraw, ImageFilter
import os

os.chdir('D:\\RepositorioPy\\image-mani\\resources\\sources-base')
baseSourceImg = Image.open('source-teste.png')
copySourceimg = baseSourceImg.copy()
os.close(1)

os.chdir('D:\\RepositorioPy\\image-mani\\resources\\sources-img')
baseImg = Image.open('gato.jpg')
baseCopyImg = baseImg.copy()

copySourceimg.paste(baseCopyImg)
copySourceimg.save('gatinho.png')