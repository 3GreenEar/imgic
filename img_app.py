from logging import debug
from pywebio.input import input, input_group, file_upload, NUMBER
from pywebio.output import put_html, put_image, put_text
from pywebio import start_server
from pyecharts.charts import Bar
from PIL import Image
from io import BytesIO

def _im_upload(imgObj):
    img = Image.open(BytesIO(imgObj['content']))
    return img

def _resize():
    inputs = input_group('Upload image and set new size', [
        input('width', type=NUMBER, name='width'),
        input('height', type=NUMBER, name='height'),
        file_upload(name='img')
        ])

    img = _im_upload(inputs['img'])
    newsize = (inputs['width'], inputs['height'])
    put_image(img.resize(newsize))

def main():
    _resize()

if __name__ == "__main__":
    start_server(main, port=8080, debug=True)




