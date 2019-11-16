import os
import datetime
import firebirdsql

def get_name_order(path_str):
    #print(str(str_))
    path_db = 'BASE.fdb'
    con = firebirdsql.connect(
        host='localhost',
        database = path_db,
        port = 3050,
        user='sysdba',
        password='masterkey'
        )
    cur = con.cursor()
    cur.execute("""select
                    a.OBJECT_LENGTH
                from
                    object a
                where a.PATH="""+str(path_str))
    str_ = ''
    for obj_len in cur.fetchall():
        str_ = obj_len
    print(str_)

def getTimeMSec(str):
    time = [int(i) for i in str.split(':')]
    res = (time[0]*60*60+time[1]*60+time[2])*1000
    return res

def shadelADS(file):
    inputFile = open(file, 'r', encoding='cp1251')
    words = inputFile.readline()
    listFile = []
    for line in inputFile:
        tmp= [str(i.replace('\n','').replace('"','')) for i in line.split('\t')]
        tmp += [str(getTimeMSec(tmp[1]))]
        listFile.append(tmp)

    for i in listFile:
        print(i)

shadelADS('2019-11-16.txt')