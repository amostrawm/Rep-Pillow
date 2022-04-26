from PIL import Image
import os

os.chdir('D:\\RepositorioPy\\image-mani\\resources\\sources-base')
testeSource = Image.open('source-teste.png')
copySourceimg = testeSource.copy()
os.close(1)

os.chdir('D:\\RepositorioPy\\image-mani\\resources\\sources-img')
imgTeste = Image.open('rato-fumando-editado.png')
copyImg = imgTeste.copy()

copySourceimg.paste(imgTeste, (0, 0))
copySourceimg.save('Teste2.png')


