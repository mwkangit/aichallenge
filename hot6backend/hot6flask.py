from http import HTTPStatus
import uuid
import json
from flask import Flask, jsonify, redirect, render_template, request, url_for
from reqTemplate.searchRequest import searchReq
from reqTemplate.writeRequest import writeReq
from mysqls.selectQuery import SelectQuery
from mysqls.insertQuery import InsertQuery
from mysqls.updateQuery import UpdateQuery
from UUIDEncoder import UUIDEncoder

app = Flask(__name__)

# history 검색
@app.route('/hot6/history', methods=['GET'])
def history():
    skt_id = request.args.get('id')
    sQuery=SelectQuery(skt_id)
    result=sQuery.selectHistory()
    
    resultResponse=json.dumps(result, ensure_ascii=False)

    return resultResponse

# history detail 검색
@app.route('/hot6/history/detail', methods=['GET'])
def historyDetail():
    skt_id = request.args.get('id')
    cht_id = request.args.get('cht_id')
    sQuery=SelectQuery(skt_id)
    result=sQuery.selectHistoryDetail(cht_id)
    
    resultResponse=json.dumps(result, ensure_ascii=False)
    print(resultResponse)

    return resultResponse

# new chat
@app.route('/hot6/new/chat', methods=['GET'])
def newChat():
    skt_id = request.args.get('id')
    iQuery=InsertQuery(skt_id)
    result=iQuery.insertNewChat()

    resultResponse=json.dumps(result, ensure_ascii=False)
    print(resultResponse)

    return resultResponse

# 담당자 찾기
@app.route('/hot6/search/manager', methods=['POST'])
def searchManager():
    skt_id = request.args.get('id')
    req = request.get_json()
    
    # print(params['context'])
    # ------------- model request ------------
    
    
    
    # ------------- model output ------------
    # dummy
    output="개발자는 강민우 BSS Data Engineering팀 입니다."
    iQuery=InsertQuery(skt_id)
    iQuery.insertHistory(req, output)
    # uQuery=UpdateQuery(id)
    # uQuery.updateAnswer(req, output)

    # ------------- answer에서 이름, 팀 뽑은 후 사내114csv에서 네임카드에 필요한 정보 조회해서 output과 함께 리턴해야함 ------------

    return 'statusCode: 200'



# 이메일 쓰기
@app.route('/hot6/write/email', methods=['POST'])
def writeEmail():
    skt_id = request.args.get('id')
    req = request.get_json()
    sQuery=SelectQuery(skt_id)
    question=sQuery.selectQuestion(req)
    target=req['target']
    # ------------- 사내114csv에서 정보 가져오는 로직---------



    # ------------- model request ------------
    
    
    
    # ------------- model output ------------
    result_dict={}
    result_dict['data']=[]
    
    temp_list=[]
    temp_list.append(req['cht_id'])
    #dummy
    output='안녕하세요. BSS Data Engineering팀 강민우 입니다.'
    temp_list.append(output)

    result_dict['data'].append(temp_list)
    
    resultResponse=json.dumps(result_dict, ensure_ascii=False)

    return resultResponse

@app.route('/', methods=['GET'])
def home():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)