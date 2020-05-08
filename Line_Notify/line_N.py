# lineTool needs install
import os
import lineTool
import MySQLdb

# db_connect
db = MySQLdb.connect(host="",user="",passwd="",db="") 
cursor = db.cursor()

# lineNotify token
#box2
#token = "qSIminBfqWqHTOfhpydaNhoESAMtFKRiWQRuQAeIqa9"
#box1

#token = "Zo6Pt1KIP34ajCX9YrBxLAAlB07kv055bK1vwsQAsg1"
token = "BZ7MGdZvFwfE35pg05fO33jP7YIZ1Rc9Adp3QoYUhEE"
# put messege here
msg = "您的蜂箱受到危害"

def lineNotify():
  lineTool.lineNotify(token, msg)

# get data from db
# last data for humid
cursor.execute("SELECT Humidity FROM TNH ORDER BY Time DESC limit 1")
dataHumid = cursor.fetchone()
humid = int(dataHumid[0])
# print(humid)

# last data for temperature
cursor.execute("SELECT Temperature FROM TNH ORDER BY Time DESC limit 1")
dataTemp = cursor.fetchone()
temperature = int(dataTemp[0])
# print(temperature)

db.close()

if (temperature < 20 or temperature > 35 or humid < 40 or humid > 90):
  lineNotify()