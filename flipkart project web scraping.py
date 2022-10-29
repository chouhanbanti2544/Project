#!/usr/bin/env python
# coding: utf-8

# In[160]:


pip install pandas


# In[5]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

r = requests.get('https://www.flipkart.com/q/best-laptops-under-rs-50000')
soup = BeautifulSoup(r.content,'html.parser')
containers = soup.find_all('div',{"class":"_2kHMtA"})
# print(containers)
print(len(containers)) 
print(type(containers),len(containers))


# In[8]:


#container of first page

for container in containers:
    product = container.find_all('div',{'class':'_4rR01T'})
    print(product)


# In[9]:


#container of first page

for container in containers:
    product = container.find_all('div',{'class':'_4rR01T'})
    print(product[0].text)
    break
    
# container is not a keyword   
# remove for all container access from all age


# In[10]:


#container of first page

for container in containers:
    product = container.find_all('div',{'class':'_4rR01T'})
    print(product[0].text)
    
    print(type(product[0].text))
    


# In[11]:


#container of first page

for container in containers:
    product = container.find_all('div',{'class':'_4rR01T'})
    print(product[0].text.split('-'))
    break
    
# container is not a keyword   
# remove for all container access from all age
# when i split this  will convered in to 3 part


# In[12]:


#container of first page

for container in containers:
    product = container.find_all('div',{'class':'_4rR01T'})
    print(product[0].text.split('-')[0])
    break

#[0]=[HP Pavilion Ryzen 5 Hexa Core AMD R5]
# container is not a keyword   
# remove for all container access from all age


# In[13]:


#container of first page

for container in containers:
    product = container.find_all('div',{'class':'_4rR01T'})
    print(product[0].text.split('-')[0])
  
#[0]=[HP Pavilion Ryzen 5 Hexa Core AMD R5]
# container is not a keyword   
# remove for all container access from all age


# In[14]:


#container of first page

for container in containers:
    product = container.find_all('div',{'class':'_4rR01T'})
    print(product[0].text.split('-')[0].strip())
  
#[0]=[HP Pavilion Ryzen 5 Hexa Core AMD R5]
# container is not a keyword   
# remove for all container access from all age
#find_all giving space in last strip is using to remove last space


# In[15]:


f = open('laaptops_info.csv','wb')
f.write('Productname,stars,Ratings,Reviews,currentprice,MRP,Processor,Ram,Storage,ImageURL\n'.encode())

   #finding product name
import re
for container in containers:
    product = container.find_all('div',{'class':'_4rR01T'})
    Productname = (product[0].text.split('-')[0].strip())
    
    
    #finding star
    star = container.find('div',{"class":"_3LWZlK"})
    try:
        stars = (star.text)
    except:
        stars = 0
        
    #finding rating and reviews
    Rating = container.find('span',{'class':'_2_R_DZ'})

    try:
        ratRev = re.findall('\d+,?\d*',Rating.get_text())
        Ratings =  ratRev[0].replace(',','')
        Reviews =  ratRev[1].replace(',','')
        
    except:
        Ratings = 0
        Reviews = 0
   
    #finding current price
    currentprices = container.find('div',{'class':'_30jeq3 _1_WHN1'})
    currentprice = currentprices.text.replace(',','')
    
    
    
    #finding mrp
    mrp = container.find('div',{'class':'_3I9_wc _27UcVY'})
    try:
        MRP = mrp.text.replace(',','')
    except:
        MRP = 0
    
    
    #find product feature info
    info = container.findAll('li',{'class':'rgWa7D'})
    Processor= info[0].text.replace(',','')
    Ram = info[1].text
    Storage = info[3].text
    
    
    Image = container.img
    ImageURL = Image.get('src')
    
    print(Productname,stars,Ratings,Reviews,currentprice,MRP,Processor,Ram,Storage,ImageURL)
    f.write(f"{Productname},{stars},{Ratings},{Reviews},{currentprice},{MRP},{Processor},{Ram},{Storage},{ImageURL}\n".encode())
    print('\n')
   
f.close()  



# In[16]:


for container in containers:
    Ratings = container.find('span',{'class':'_2_R_DZ'})
    try:
        print(Ratings.get_text())
    except:
        print(Ratings)
        
    
#     rare = Ratings.get_text()
#     print(rare)


# In[18]:


import pandas as pd


# In[20]:


pd.read_csv('laaptops_info.csv')


# In[ ]:




