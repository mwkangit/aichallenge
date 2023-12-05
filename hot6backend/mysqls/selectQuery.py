import pymysql
import uuid

class SelectQuery:

    def __init__(self, skt_id):
        self.skt_id = skt_id
        self.conn=pymysql.connect(host='127.0.0.1', user='root', password='qzwx1596',  charset='utf8')
        self.cur=self.conn.cursor()

    # 사용자가 생성한 채팅 목록을 조회한다. 이때 cht_id 기준 가장 처음에 생성한 질문들을 조회한다.
    # cht_id, question, answer 을 응답한다.
    def selectHistory(self):
        self.cur.execute(f'select * from tct.tct_mst where skt_id=\'{self.skt_id}\';')
        self.conn.commit()
        skt_id_mst=self.cur.fetchall()
        result_dict={}
        result_dict['data']=[]

        for row in skt_id_mst:
            cht_id=row[2]
            self.cur.execute(f'select * from tct.tct_hst where cht_id=\'{cht_id}\' order by creation_time limit 1;')
            self.conn.commit()
            hst_row=self.cur.fetchall()
            print(hst_row)
            question=hst_row[0][2]
            answer=hst_row[0][3]
            temp_list=[]
            temp_list.append(cht_id)
            temp_list.append(question)
            temp_list.append(answer)
            result_dict['data'].append(temp_list)

        return result_dict
    
    def selectHistoryDetail(self, cht_id):
        self.cur.execute(f'select * from tct.tct_hst where cht_id=\'{cht_id}\' order by creation_time;')
        self.conn.commit()
        cht_id_hst=self.cur.fetchall()

        result_dict={}
        result_dict['data']=[]


        for row in cht_id_hst:
            print(row)
            question=row[2]
            answer=row[3]
            temp_list=[]
            temp_list.append(cht_id)
            temp_list.append(question)
            temp_list.append(answer)
            result_dict['data'].append(temp_list)

        return result_dict

    def selectQuestion(self, req):
        cht_id=req['cht_id']
        self.cur.execute(f'select * from tct.tct_hst where cht_id=\'{cht_id}\' order by creation_time desc limit 1;')
        self.conn.commit()
        cht_id_hst=self.cur.fetchall()
        question=cht_id_hst[0][2]
        return question

    def __str__(self):
        return f"{self.id}, {self.type}, {self.context}"
