import urllib.request

from flask import Flask, request
app = Flask(__name__)

@app.route('/search', methods=('GET', 'POST'))
def search():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    url = request.form['url']
    reg_url = url
    req = urllib.request.Request(url=reg_url, headers=headers)
    print(url)
    urls = []
    html = ""
    start = 0
    end = 0
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('ISO-8859-1')

    while html.find("<a", start) != -1:
        start = html.find("<a", end)
        end = html.find("</a>", start)
        urls.append(html[start:end] + "<br />")

    return ''.join(urls)

@app.route('/')
def hello():
    form = '''
        <form action="/search" method="post">
            url: <input type="text" name="url"><br />
            <input type="submit" value="Submit">
        </form>
    '''
    return form


if __name__ == '__main__':
    app.run()
