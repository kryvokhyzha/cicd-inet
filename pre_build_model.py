if __name__ == '__main__':
    import torch
    from torchvision import models

    model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)

