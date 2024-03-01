from eloquent_edgeimpulse import Fomo
from PIL import Image
from pprint import pprint


if __name__ == '__main__':
    fomo = Fomo('./fomo_model.eim')
    image = Image.open('./fomo_sample.jpg').resize(fomo.shape[:2])
    bboxes = fomo.detect(image)
    pprint(bboxes)