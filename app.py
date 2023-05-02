from flask import Flask, send_file, request
import cairosvg
import io

app = Flask(__name__)

@app.route('/svg/png')
def get_image():
    url = request.args.get('url')
    print(url)
    png_output = cairosvg.svg2png(url=url)
    return send_file(io.BytesIO(png_output), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)