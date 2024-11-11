#use idle 3.4
#open mysql server line -- password : press enter

#in mysql server line:
##show databases;
##create database itv;
##use itv;

#use python now 3.4

import mysql.connector
db=mysql.connector.connect(user='root',passwd='',host='127.0.0.1',database='itv')
cur=db.cursor()
cur.execute("create table student(name varchar(20),age int,roll int)")
db.close()
