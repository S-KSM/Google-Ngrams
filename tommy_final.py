
# coding: utf-8

# In[5]:

from google_ngram_downloader import readline_google_store
import operator
import nltk
import re
import string


total = {}

for n in range(1,5):
    fname, url, records = next(readline_google_store(ngram_len = n, lang = 'chi-sim'))
    notEoF = True
    try:
        while notEoF:
            myrecord = next(records)
            temp = ""
            for i in myrecord[0] :
                if re.search(r'[A-Za-z0-9\s\_]', i):
                    pass
                    #print("yes")
                else:
                    temp += i
    #print(c)
            temp = re.sub('[%s]' % re.escape(string.punctuation), '', temp,re.UNICODE) #Gets rid of punctuations
            if len(temp) == 4:    
                num = myrecord[2] #the number of times it was shown up
                if temp in total: #if the ngram is in our total dictionary
                    total[temp] += num # add the number of times it is repeated in this new instance
                else:
                    total[temp] = num # adding the ngram to our dictionary
    except:
        notEoF = False    

        
sorted_x = sorted(total.items(), key=operator.itemgetter(1),reverse=True)
top_100 = sorted_x[0:100] # change the numbers in brackets to expand the list. For instance, [0:10] shows the top 10
top_100

f = open("top_100_updated.txt","w",encoding='utf-8')

for ngram in top_100:
    f.write(ngram[0]+","+str(ngram[1])+"\n")
    

f.close()


# In[6]:

g = open("total.txt","w",encoding='utf-8')
for ngram in sorted_x:
    g.write(ngram[0]+","+str(ngram[1])+"\n")
    
g.close()


# In[ ]:



