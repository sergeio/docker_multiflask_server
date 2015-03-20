from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from bingo import make_board

app = Flask(__name__, static_folder="static")


@app.route('/')
def serious():
    return 'This is the serious server!'


@app.route('/bingo')
def bingo():
    html = '''<div style="margin-top:100" align=center>
                <table style="border-collapse:collapse; font-size:200%; color:#333" cellpadding="15">'''
    for elm in 'BINGO':
        html += '<th style="border:1px solid; border-collapse:collapse">{0}</th>'.format(elm)
    for row in make_board():
        html += '<tr>'
        for elm in row:
            html += '<td style="border:1px solid; border-collapse:collapse">{0}</td>'.format(elm)
        html += '</tr>'
    html += '</table></div>'
    return html


def main():
    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run()


if __name__ == '__main__':
    main()
