from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/user/signin', methods=['POST'])
def signin():
    response_data = {'code': 2010,
                     'msg': '参数有误',
                     'data': {}
                     }
    if request.json:
        phone = request.get_json().get('phone', False)
        password = request.get_json().get('password', False)
        if phone and password:
            if phone == '12345678901' and password == '123456':
                response_data['code'] = 2000
                response_data['msg'] = 'ok'
                response_data['data'] = {'name': '姓名',
                                         'gender': 0,
                                         'age': 20
                                         }
                return jsonify(response_data)
            response_data['code'] = 2050
            response_data['msg'] = '账号信息有误'
            return jsonify(response_data)
        return jsonify(response_data)
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)
