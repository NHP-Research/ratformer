import json
import os

with open("annotations.json") as fi:
    anno = json.load(fi)

    for img in anno["images"]:
        name = img["file_name"]
        img["file_name"] = os.path.join(name.split("_image")[0], name)

with open("annotations.json", "w") as fo:
    json.dump(anno, fo, indent=2)