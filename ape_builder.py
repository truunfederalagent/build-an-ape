import os, random
from PIL import Image


directory = os.path.dirname(os.path.abspath(__file__))
directory = os.path.join(directory, 'APEsAssets')
directories = [d for d in os.listdir(directory) if d[:2].isdigit()]
directories = sorted(directories, key=lambda d: int(d[:2]))
img = None
for d in directories:
    curr = os.path.join(directory, d)
    layers = []
    for asset in os.listdir(curr):
        path = os.path.join(curr, asset)
        if os.path.isfile(path):
            layers.append(path)
        else:
            for actual_asset in os.listdir(os.path.join(curr, asset)):
                layers.append(os.path.join(asset, actual_asset))
    layer = random.choice(layers)
    layer_path = os.path.join(curr, layer)
    print(layer_path)
    if img == None:
        img = Image.open(layer_path)
        print('creating image')
    else:
        new_layer = Image.open(layer_path)
        img.paste(new_layer, (0,0), new_layer)

img.save('rand-ape.png')