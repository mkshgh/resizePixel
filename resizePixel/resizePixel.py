# Import the Images module from pillow
from PIL import Image
from PIL.ExifTags import TAGS

class rpImage():

    def __init__(self,name:str,image_blob):
        self.img_name = name
        self.img_blob = image_blob

    def get_image_meta(self):
        width, height,  = self.img_blob.size
        size = str(len(self.img_blob.fp.read()))
        return {"name":self.img_name,
                "witdth": width,
                "height":height,
                "size":size}


def reduce_qualtiy(img_name,img_blob,quality=50):
    # reduce
    img_output = 'output_'+img_name
    img_blob.save(img_output, quality=quality)

    new_img_blob = Image.open(img_output)
    img_obj = rpImage(img_output,new_img_blob)
    
    return img_obj.get_image_meta()