from os import sep
from bs4 import BeautifulSoup
import requests
from requests.api import post
import fileClass
import webscrapClass
import Con_posql
import Con_sql

obj_file = fileClass.files('filpcart_product.csv',',')
mysql_object = Con_sql.Mysql('localhost','demo_db','root','Sahil@123')
post_object = Con_posql.poconn('localhost','temp_db','postgres','sahil@123')
obj_web = webscrapClass.webScrap('https://www.flipkart.com/search?q=smartphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=smartphone%7CMobiles&requestId=68f958ae-d659-4359-bb1f-94262f285fc4&as-backfill=on')


containers = obj_web.findInfo("div","_13oc-S")
product_name = obj_web.findInfo("div","_4rR01T")
reviews = obj_web.findInfo("div","gUuXy-")
description = obj_web.findInfo("div","fMghEO")
price = obj_web.findInfo("div","_30jeq3 _1_WHN1")

headers = 'product_name,price,review,description\n'
obj_web.define_file('filpcart_product.csv',headers,'w')
obj_web.fetchDetails(containers,"_4rR01T","gUuXy-","fMghEO","_30jeq3 _1_WHN1")


#postgres

cur=post_object.createCursor()

v = obj_file.parsefile()

ct = 'create table product (product_name varchar(200),price varchar(100),review varchar(200),description varchar(300),empty varchar(100))'
post_object.createTable(ct)
post_object.fetchtable('product')
post_object.pushTable(v)

obj_file.closefile()
post_object.endConn()
print("DONE")


#MYSQL

cursor=mysql_object.createCursor()
value=obj_file.parsefile()
ct = "CREATE TABLE product (product_name varchar(100),price varchar(100),review varchar(100),description varchar(200),nn varchar(20))"
mysql_object.createTable(ct)
mysql_object.fetchtable('product')
mysql_object.pushTable(value)
obj_file.closefile()
mysql_object.endConn()
print ("Done") 

 
























    







