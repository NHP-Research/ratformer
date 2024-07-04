from transformers import SamModel, SamProcessor
from .model import generate_sam
import json

dataset_root = "/home/nhphucqt/Downloads/RatSoles-20240609T085508Z-001 (1)/RatSoles"

prompt_paths = [
    "group_0/group_0_image_0.jpg",
    "group_0/group_0_image_20.jpg",
    "group_1/group_1_image_19.jpg",
    "group_1/group_1_image_33.jpg",
    "group_2/group_2_image_5.jpg",
    "group_2/group_2_image_9.jpg",
    "group_3/group_3_image_2.jpg",
    "group_3/group_3_image_7.jpg",
    "group_4/group_4_image_0.jpg",
    "group_4/group_4_image_3.jpg",
]

def main():
    sam_model, sam_processor = generate_sam()

    with open("annotationn.json") as fi:
        anno = json.load(fi)
    
    

