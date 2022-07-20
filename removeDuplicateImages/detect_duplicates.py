from PIL import Image, ImageChops

def compare_images(path_one, path_two):
    """
    compare images
    :param path_one: first image
    :param path_two: second image
    :return: same is True, otherwise is False
    """
    image_one = Image.open(path_one)
    image_two = Image.open(path_two)
    try:
        diff = ImageChops.difference(image_one, image_two)
        if diff.getbbox() is None:
            # same
            return True
        else:
            return False
    except ValueError as e:
        return False