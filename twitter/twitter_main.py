from typing import Counter
from tweepy import auth
from tweepy.streaming import Stream
import twitterClass
from tweepy.api import API
import Con_posql
import Con_sql
import pdfClass
import fileClass

#to debug use this :-
#import pdb;pdb.set_trace()
#retrive_data.encode('latin-1','replace').decode('latin-1')





object = Con_sql.Mysql('localhost','temp_db','root','')
post_object = Con_posql.poconn('localhost','temp_db','postgres','')
pdf_object = pdfClass.PDF()
twitter_client = twitterClass.Twitterclient()
tweet_analyzer = twitterClass.tweetAnalyzer()
file_obj = fileClass.files('twitter_final.csv',',',encoding='utf-8')


""" api = twitter_client.get_client_api()
tweets = api.user_timeline(screen_name="ICC",Count= 10)

df = tweet_analyzer.tweet_to_data_frame(tweets)

print(df.head(10))
df.to_csv('twitter1.csv')
 
tweet_analyzer.clean_csv_twitterFile() """

#PSQL 
#push table
""" cursor = post_object.createCursor()
value1 = file_obj.parsefile()
ct = 'create table twitter3 (index_no varchar(100),tweets varchar(200),id varchar(100),tweet_len varchar(100),date varchar(100),source varchar(100),likes varchar(100),retweets varchar(100))'
post_object.createTable(ct)
post_object.fetchtable('twitter3')
post_object.pushTable(value1)
file_obj.closefile()
post_object.endConn()  """
 
#fetched_data and create pdf 
head = file_obj.getHeader()
post_object.createCursor()
post_object.fetchtable('twitter3')
post_object.retrive()
retrive_data=post_object.fetchData()
l = pdf_object.withIndex(head,retrive_data)
post_object.endConn()
pdf_object.output_table(l,8)
pdf_object.save_pdf('twitter_3.pdf') 




#MYSQL

#put data 
""" cursor=object.createCursor()
value=file_obj.parsefile()
ct = 'create table twitter (index_no varchar(100),tweets varchar(200),id varchar(100),tweet_len varchar(100),date varchar(100),source varchar(100),likes varchar(100),retweets varchar(100))'
object.createTable(ct)
object.fetchtable('twitter')
object.pushTable(value)
file_obj.closefile()
object.endConn()
print ("Done") """  

#fetched data and create pdf
""" head = file_obj.getHeader()
object.createCursor()
object.fetchtable('twitter')
#object.retrive()
retrive_data= object.fetchData()
import pdb;pdb.set_trace()                   #IMPORTANT 
retrive_data = retrive_data.encode('latin-1', 'replace').decode('latin-1')
l = pdf_object.withIndex(head,retrive_data) """


#tweet_analyzer.clean_tweet(str(l))
""" object.endConn()
#encode(encoding='ascii', errors='xmlcharrefreplace').decode()
pdf_object.output_table(l,8)
pdf_object.save_pdf('twitter_1.pdf')    """
