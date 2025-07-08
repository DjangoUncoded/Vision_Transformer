import torch
from ..src.ViT import *

def test_vit_outputs_shape():
    cfg = Config()
    model = ViTForClassfication(cfg)
    imgs = torch.randn(2, 3, 32, 32)
    logits, _ = model(imgs)
    assert logits.shape == (2, cfg.num_classes)
