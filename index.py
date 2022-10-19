from flask import Flask, render_template, request, redirect, url_for
import downloader

app = Flask(__name__)

@app.route('/')
def raiz():
    return render_template("index.html")

@app.route('/download', methods=['POST'])
def download():

    link = request.form.get("link")


    print(functions.GetNameFile(link))
    functions.DownloadVideoInLow(link)

    return "Iniciando Download..."


app.run(debug=True)