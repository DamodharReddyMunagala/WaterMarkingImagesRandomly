# WaterMarkingImagesRandomly
from PIL import Image, ImageDraw
import random

def watermarkingImage(ImagePath):
    main = Image.open(ImagePath)
    width, height = main.size
    watermarkText = 'Damodhar'
    pixelWidth = random.randrange((width - (len(watermarkText)*6)))
    pixelHeight = random.randrange(height - (10))
    watermark = Image.new("RGBA", main.size)
    waterdraw = ImageDraw.ImageDraw(watermark, "RGBA")
    waterdraw.text((pixelWidth, pixelHeight), watermarkText)
    watermask = watermark.convert("L").point(lambda x: min(x, 100))
    watermark.putalpha(watermask)
    main.paste(watermark, None, watermark)
    main.show()
    main.save("Damodharwatermarked.jpg", "JPEG")
watermarkingImage("DamodharPassportSizePhoto.jpg")
