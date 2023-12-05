import uuid
import pymysql

class InsertQuery:
    def __init__(self, skt_id):
        self.skt_id = skt_id
        self.conn=pymysql.connect(host='127.0.0.1', user='root', password='qzwx1596',  charset='utf8')
        self.cur=self.conn.cursor()

    def insertNewChat(self):
        new_cht_id=str(uuid.uuid4())
        self.cur.execute(f'INSERT INTO tct.tct_mst (skt_id, cht_id) VALUES(\'{self.skt_id}\', \'{new_cht_id}\')')
        self.conn.commit()
        print(new_cht_id)

        result_dict={}
        result_dict['data']=[]

        temp_list=[]
        temp_list.append(new_cht_id)

        result_dict['data'].append(temp_list)

        return result_dict

    def insertHistory(self, req, output):
        cht_id=req['cht_id']
        context=req['context']
        self.cur.execute(f'INSERT INTO tct.tct_hst (cht_id, question, answer) VALUES(\'{cht_id}\', \'{context}\', \'{output}\')')
        self.conn.commit()


    def __str__(self):
        return f"{self.id}, {self.type}, {self.context}"
