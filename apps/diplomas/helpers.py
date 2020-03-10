from django.conf import settings
from django.utils.text import slugify


def upload_to_image(self, filename, flag):
    """
    Stores the image in a specific path regards object's name & class

    Structure of paths:
        - diplomas/issuer/
        - diplomas/issuer/thumbnail
    """
    ext = filename.split(".")[-1]
    file_path = ""
    filename = ""

    if self.__class__.__name__ == "Issuer":
        name = slugify(self.name)

        if flag == "image":
            file_path = "diplomas/issuers/"
            filename = "%s.%s" % (name, ext)
        elif flag == "thumb":
            file_path = "diplomas/issuers/thumbnails/"
            filename = "%s_thumb.%s" % (name, ext)

    return "%s/%s/%s" % (settings.MEDIA_ROOT, file_path, filename)


def issuer_image(instance, filename):
    return upload_to_image(instance, filename, "image")

def issuer_image_thumb(instance, filename):
    return upload_to_image(instance, filename, "thumb")
