import torch
from .model import generate_sam, generate_seggpt

def main():
    sam_model, sam_processor = generate_sam()
    seggpt_model, seggpt_processor = generate_seggpt()

    

    