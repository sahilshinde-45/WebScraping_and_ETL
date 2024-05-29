
from bs4 import BeautifulSoup
import requests

import csv

class webScrap():
    def __init__(self,link):
        self.link = link
        source = requests.get(link).text
        self.soup = BeautifulSoup(source,'lxml') 




    def findInfo(self,div,given_class):
        self.div = div
        self.given_class = given_class
        return self.soup.findAll(self.div,{'class':self.given_class})


    def fetchDetails(self,containers,name,review,description,price):
        self.containers = containers
        self.name= name
        self.review = review
        self.description = description
        self.price = price
        
        
        
        
        for container in self.containers:
            self.name_container = container.findAll(self.div,{'class':self.name})
            self.product_name = self.name_container[0].text

            self.review_container = container.findAll(self.div,{'class':self.review})
            self.product_review = self.review_container[0].text

            self.description_container = container.findAll(self.div,{'class':self.description})
            self.product_description = self.description_container[0].text

            self.price_container = container.findAll(self.div,{'class':self.price})
            self.product_price = self.price_container[0].text
            
            self.f.write((self.product_name.replace(',','') + ","  +self. product_price.replace(',','') + ','+ self.product_review.replace(',','') +','+ self. product_description.replace('|','')+'\n'))
    
        self.f.close()
            #print("product_name :" + self.product_name)
            #print("product_review:" + self.product_review)
            #print("product_description: "+self.product_description)
            #print("product_price :"+ self.product_price)


   # print(product_name + "|"  + product_price + '|'+ product_review +'|'+  product_description.replace('|',','))
    
    def define_file(self,filename,header,method):
        self.filename = filename
        self.header = header
        self.method = method
        self.f = open(filename,method)
        self.f.write(header)
        

    