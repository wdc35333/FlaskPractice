from flask import Flask, render_template, request
import get_google_search as ggs
app = Flask(__name__)

@app.route('/',methods=('GET', 'POST'))  # 접속하는 url
def index():
    # 웹 페이지에서 name = "xxx"인 요소의 value 가져오기
    print(request.form.get('keyword1'))
    print(request.form.get('keyword2'))
    keyword1 = request.form.get('keyword1')
    keyword2 = request.form.get('keyword2')

    # 위의 값이 있을 때만 크롤링 검색 결과 반환
    if keyword1 is not None and keyword2 is not None:
        data = {
            keyword1 : ggs.get_search_count(keyword1).get('number'),
            keyword2 : ggs.get_search_count(keyword2).get('number')
        }
        return render_template('index.html', data=data)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    # host 등을 지정하고 싶다면
    # app.run(host="127.0.0.1", port = "5000", debug=True)