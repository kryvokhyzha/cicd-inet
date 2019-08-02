import unittest
import os

from ImageNet.network import get_prediction
from torchvision import models


def test_street_output():
    model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    model.eval()

    dir =  os.getcwd() + '/tests/img/'
    filename = dir + 'street.jpg'
    pred_cls = get_prediction(img_path=filename, threshold=0.99, model=model)[1]

    assert 'car' in  pred_cls
    assert 'fire hydrant' in pred_cls
