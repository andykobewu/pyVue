import pymysql
import os,datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.decorators import api_view
class Addcase():
    def __init__(self,name,id,script,type,result):
        self.id = "case_" + id
        self.casename = name
        self.casedesc = script
        self.casetype= type
        self.caseresult = result

    def conMysql(self):
        # 连接数据库，需指定charset否则可能会报错
        db = pymysql.connect(host="localhost", user="root", password="root", db="pyvue", charset="utf8mb4")
        cursor = db.cursor()  # 创建一个游标对象
    @api_view(['GET', 'POST'])
    def getCase(self):
        return "test"
