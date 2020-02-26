from io import BytesIO
from PIL import Image
from django.core.files import File


def compress_image(image):
    """ Compress image in format JPEG and specific quality
    """
    img = Image.open(image)

    im_io = BytesIO()

    #Saving the image
    img.save(im_io, format='PNG', quality=100)
    image_optimized = File(im_io, name=image.name)

    return image_optimized


def thumbnail_image(image):
    """ Create thumbnail of the image with basewidth of 150, format PNG and quality of 100
    """
    basewidth = 150

    img = Image.open(image)

    im_io = BytesIO()

    #Calculating the new size considerings its aspect ratio
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))

    #Resize/modify the image
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)

    #Saving the image
    img.save(im_io, format='PNG', quality=100)
    image_thumbnail = File(im_io, name=image.name)

    return image_thumbnail
