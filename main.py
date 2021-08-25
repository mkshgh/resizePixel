# import library 

from resizePixel.resizePixel import rpImage,reduce_qualtiy
from PIL import Image

# image path
image_path = "img.jpg"

# open the image and check the current quality
image_file = Image.open(image_path)
my_image = rpImage(image_path,image_file)
info = my_image.get_image_meta()
print(info)

# decrease quality explained above
new_image = reduce_qualtiy(image_path,image_file,quality=50)
print(new_image)