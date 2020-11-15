from jinja2 import Template as jinjaTemplate
from htmlmin import minify
from shutil import copy, rmtree, copytree
from os import mkdir, makedirs
from PIL import Image
import config


try:
    rmtree(config.generated_path)
except FileNotFoundError:
    pass

mkdir(config.generated_path)

with open(f'{config.assets_path}/template.jinja2', 'r') as template_file,\
        open(f'{config.generated_path}/index.html', 'w') as html_file:
    template = jinjaTemplate(template_file.read())
    html_file.write(minify(template.render(config.values)))

copytree(f'{config.assets_path}', f'{config.generated_path}/assets')
    
makedirs(f'{config.generated_path}/images/houses')
for _, images in config.houses.items():
    for f in images:
        filename = f.split('.')[:-1][0]
        src = Image.open(f'{config.images_path}/houses/{f}')
        src.resize((config.img_width, int(config.img_width * src.height / src.width)))\
        .save(f'{config.generated_path}/images/houses/{filename}.jpg')

for img in ['atto', 'azione', 'bruno']:
    copy(f'{config.images_path}/{img}.jpg', f'{config.generated_path}/images')
    copy(f'{config.images_path}/{img}-squared.jpg', f'{config.generated_path}/images')

copy(f'{config.images_path}/bg.jpg', f'{config.generated_path}/images')

copy(f'{config.assets_path}/cookie-policy.txt', f'{config.generated_path}/cookie-policy.txt')
copy(f'{config.assets_path}/privacy-policy.txt', f'{config.generated_path}/privacy-policy.txt')
copy(f'{config.assets_path}/statuto.pdf', f'{config.generated_path}/statuto.pdf')

copy('_redirects', config.generated_path)
