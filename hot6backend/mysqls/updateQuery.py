import uuid
import pymysql

class UpdateQuery:
    def __init__(self, skt_id):
        self.skt_id = skt_id
        self.conn=pymysql.connect(host='127.0.0.1', user='root', password='qzwx1596',  charset='utf8')
        self.cur=self.conn.cursor()
    
    def updateAnswer(self, req, output):
        cht_id=req['cht_id']
        self.cur.execute(f'UPDATE tct.tct_hst SET answer=\'{output}\' where cht_id=\'{cht_id}\'')

    def __str__(self):
        return f"{self.id}, {self.type}, {self.context}"
