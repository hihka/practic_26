from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form action="/view_image" method="get">
            <label for="imgurl">URL картинки:</label>
            <input type="text" id="imgurl" name="imgurl" required>
            <br>
            <label for="imgtitle">Название картинки:</label>
            <input type="text" id="imgtitle" name="imgtitle" required>
            <br>
            <input type="submit" value="Отправить">
        </form>
    '''

@app.route('/view_image')
def view_image():
    imgurl = request.args.get('imgurl')
    imgtitle = request.args.get('imgtitle')
    return f'''
        <h1>{imgtitle}</h1>
        <img src="{imgurl}" alt="{imgtitle}">
    '''

if __name__ == '__main__':
    app.run(port=5500)
