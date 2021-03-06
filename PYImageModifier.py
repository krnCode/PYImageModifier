from PIL import Image
from PIL import ImageFilter
from datetime import datetime
import os

time_start = datetime.now()

# 1 - Access the folder containing the files that you want to modify
rawDir = r'C:\Users\conta\Pictures\Wallpapers'

# 2 - Set the folder to save the modified images
modDir = r'C:\Users\conta\Pictures\WallsConverted'

# 3 - Make sure to have a folder to store the converted images
if os.path.exists(modDir) == False:
    os.makedirs(r'C:\Users\conta\Pictures\WallsConverted')

# 4 - Choose the filters to apply (comment out filters you don't want)
for rawImage in os.listdir(rawDir):
    start = datetime.now()
    img = Image.open(rawDir + "/" + str(rawImage))
    rgbImg = img.convert('RGB')
    img_sharpen = rgbImg.filter(ImageFilter.SHARPEN)
    img_sharpen.save(modDir + '/' + rawImage[:-4] + '-sharp.jpg')
    img_blur = rgbImg.filter(ImageFilter.BLUR)
    img_blur.save(modDir + '/' + rawImage[:-4] + '-blur.jpg')
    img_smooth = rgbImg.filter(ImageFilter.SMOOTH)
    img_smooth.save(modDir + '/' + rawImage[:-4] + '-smooth.jpg')
    img_contour = rgbImg.filter(ImageFilter.CONTOUR)
    img_contour.save(modDir + '/' + rawImage[:-4] + '-contour.jpg')
    img_detail = rgbImg.filter(ImageFilter.DETAIL)
    img_detail.save(modDir + '/' + rawImage[:-4] + '-detail.jpg')
    img_findEdges = rgbImg.filter(ImageFilter.FIND_EDGES)
    img_findEdges.save(modDir + '/' + rawImage[:-4] + '-findEdges.jpg')
    img_edgeEnchanceMore = rgbImg.filter(ImageFilter.EDGE_ENHANCE_MORE)
    img_edgeEnchanceMore.save(
        modDir + '/' + rawImage[:-4] + '-edgeEnhanceMore.jpg')
    # img_emboss = rgbImg.filter(ImageFilter.EMBOSS)
    # img_emboss.save(modDir + '/' + rawImage[:-4] + '-emboss.jpg')
    end = datetime.now()
    print(f'{rawImage} done in {end - start}!')

time_end = datetime.now()

# 5 - Print message telling that everything is done
print(
    f'All done! The process took {time_end - time_start} in total to finish.' '\n'
    'Check the folder to see your modified images')
