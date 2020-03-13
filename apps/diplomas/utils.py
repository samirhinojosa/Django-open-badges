from io import BytesIO
from PIL import Image
from django.core.files import File


def create_image_issuer(flag=False):
    """
    Create and update an image for test this attribute in the model
    """
    if flag:
        width, height = 525, 225
        color = "white"
    else:
        width, height = 1050, 550
        color = "red"

    image = Image.new("RGB", (width, height), color=color)
    im_io = BytesIO()
    image.save(im_io, format="PNG", quality=100)

    if flag:
        image = File(im_io, name=".jpg")
    else:
        image = File(im_io, name=".png")

    return image