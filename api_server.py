# -*- coding:utf-8 -*-

from flask import Flask,request,redirect,url_for
from flask import jsonify
from werkzeug import secure_filename
import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = BASE_PATH + '/uploads' #你的路径
ALLOWED_EXTENSIONS = set(['html','txt','png','jpg','jpeg','gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello_world():
    return "Hello World"

# 判断文件后缀名
def allow_file(filename):
    #判断返回的结果是否为真或是假
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

#文件上传接口
@app.route('/upload',methods=['GET','POST'])
def upload_file():
    if request.method == "POST":
        file = request.files['file']
        print("调试1：",file)
        if file and allow_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            response = {"code":200,"message":"文件上传成功！"}
        else:
            response ={"code":401,"message":"文件格式不符，需符合后缀('html','txt','png','jpg','jpeg','gif')"}
        return jsonify(response)
    elif request.method == "GET":
        return jsonify({"code":404,"message":"请求方式未开发，敬请期待！"})

if __name__ == "__main__":
    #外部可访问的服务器  -- 先注释
    app.run(host="0.0.0.0")
    #app.run(debug=True)
