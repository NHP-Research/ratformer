import torch
from tranformers import SamModel, SamProcessor, SegGptImageProcessor, SegGptForImageSegmentation

def generate_sam():
    checkpoint = "facebook/sam-vit-base"
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = SamModel.from_pretrained(checkpoint).to(device)
    processor = SamProcessor.from_pretrained(checkpoint)
    return model, processor

def generate_seggpt():
    checkpoint = "BAAI/seggpt-vit-large"
    model = SegGptForImageSegmentation.from_pretrained(checkpoint)
    processor = SegGptImageProcessor.from_pretrained(checkpoint)
    return model, processor