from flask import Flask, request
from core.decorators import registry

app = Flask(__name__)
register = {}


@app.route('/hook', methods=['GET', 'POST'])
def main():
    """
    主程序
    :return:
    """
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
