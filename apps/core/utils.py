from io import BytesIO
from PIL import Image
from django.core.files import File


def compress_image(image):
    """
    Compress image in format JPEG and specific quality
    """
    img = Image.open(image)

    im_io = BytesIO()

    #Saving the image
    img.save(im_io, format="PNG", quality=100)
    image_optimized = File(im_io, name=image.name)

    return image_optimized


def thumbnail_image(image):
    """
    Create thumbnail of the image with basewidth of 150, format PNG and quality of 100
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
    img.save(im_io, format="PNG", quality=100)
    image_thumbnail = File(im_io, name=image.name)

    return image_thumbnail


def create_img_linkedin(image):

    #resizing of the badge to 550px of height
    baseheight = 550

    #Size of the final image
    width = 1050
    height = 550

    #Opening the image
    img = Image.open(image)

    #Calculating the new size of "width" considerings its aspect ratio
    wpercent = (baseheight/float(img.size[1]))
    new_width_size = int((float(img.size[0])*float(wpercent)))

    #Resize/modify the image
    img = img.resize((new_width_size, baseheight))

    #Getting the size of the image after resizing
    img_width, img_height = img.size

    #Creating a new image
    img_badge_in = Image.new("RGB", (width, height), color="white")

    #Calculating the ubication of the badge over the new image
    offset = ((width - img_width) // 2, (height - img_height) // 2)

    #Pasting the badge over the new image based on the previous calculation
    img_badge_in.paste(img, offset, mask=img.split()[-1])

    #Saving the image
    im_io = BytesIO()
    img_badge_in.save(im_io, format="PNG", quality=100)
    img_badge_in = File(im_io, name=image.name)

    return img_badge_in
