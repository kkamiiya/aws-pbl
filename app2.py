from flask import Flask, render_template,redirect,request
# 소문자 flask는 모듈명, 대문자 Flask는 클래스 명
import pymysql
import boto3

ssm = boto3.client('ssm')
parameter = ssm.get_parameter(Name ='/myweb/database1_password',WithDecryption=True)
db_password = parameter['Parameter']['Value']

app = Flask(__name__)
api = Api(app)

@app.route('/')  #route가 url을 지정해 줌.
def hell():
    return "<h1>hello Flask~~!! hahaha<h1>"

@app.route('/hello')
def hi() :
    name = 'choi bo ram'
    return render_template("hello.html", name = name)
    #render_template을 통해 리턴 , 앞에 name은 변수명. html파일은 templates 폴더에서 찾아서 플라스크가 실행시킴

@app.route('/test')
def test():
    #수행해야할 로직이 여기 들어온다.
    return "test"

@app.route('/')
def index() :
    return "url에 /board를 입력하세요"

@app.route('/board')
def board_list() :
    db = pymysql.connect(host='database-1.cd3lh4w1vr3o.ap-northeast-2.rds.amazonaws.com',db='pbldb',port=3306,passwd=db_password,user='admin')
    curs = db.cursor(pymysql.cursors.DictCursor)
    sql = 'SELECT * FROM board ORDER BY id DESC'
    curs.execute(sql)
    results = curs.fetchall()
    curs.close()
    db.close()
    print(results)
    return render_template('board_list.html',results=results)

@app.route('/board/writeform')
def board_writeform():
    return render_template('board_writeform.html')

@app.route('/board/write')
def write():
    return redirect('/board')

if __name__=='__main__':
    app.run("0.0.0.0", port ="8088")