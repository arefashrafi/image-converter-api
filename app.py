from flask import Flask, send_file, request
import io
from PIL import Image
import requests

app = Flask(__name__)


@app.route('/<f>/<t>')
def get_image(f: str, t: str):
    print(f, t)
    url = request.args.get('url')
    if f == "svg" and t == "png":
        import cairosvg
        png_output = cairosvg.svg2png(url=url)
        return send_file(io.BytesIO(png_output), mimetype='image/png')
    if f == "jpeg" and t == "png":
        png_output = Image.open(io.BytesIO(requests.get(url=url).content))
        buffer = io.BytesIO()
        png_output.save(buffer, 'PNG')
        buffer.seek(0)
        return send_file(buffer, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)
