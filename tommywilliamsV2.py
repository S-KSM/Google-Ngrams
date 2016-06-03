
# coding: utf-8

# # Top 100 4 letter Chinese Ngrams

# I recommend to you to download ``Anaconda``, the Python 3 version. 
# 
# First, import the google ngram downloader and operator.
# 
# If you get error in this importing it means you don't have the module, so just go to your Anaconda Prompt and type:
# 
# ```python
#     pip install google-ngram-downloader
# ```

# In[1]:

from google_ngram_downloader import readline_google_store
import operator
import nltk
import re
import string


# In this step, we load the `file name`,`url` of the ngram, and `record`. Records can be understood as the rows in
# the ngram files.
# 
# `lang = 'chi-sim'` means just load the Chinese-Simplified.
# 
# ** Remember you need to be connected to internet for this program to work **
# 

# In[9]:

fname, url, records = next(readline_google_store(ngram_len = 4, lang = 'chi-sim'))


# You can look at the `url` and use it to download the ngram file, if you want! (NOT RECOMMENDED :))

# First, I defined an empty `dictionary` called `total` to store the records and their word counts.
# 
# Next line, I set the `notEoF` variable to be `True`. This variable is supposed to be the flag for when we reach the end of the google ngram records.
# 
# Next, I used the try/except structure that is used for error handling in Python. It reads the next record from google ngram. After the last record is read by the script, there will be an error. This rise of an error moves the program to the `except` section. In the `except` section, the `notEoF` becomes `False` and that stops the `while` loop in the `try` section.
# 
# 

# In[10]:

total = {}
### function that returns True if there is a number in the string


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


# We need to sort our dictionary,`total`, in a descending format. But, dictionaries can not be sorted based on their values directly. We make a tuple, `sorted_x`, and sort the tuple. The `reverse = True` is the argument for the `sorted` function to sort from the highest number to the lowest.

# In[11]:

sorted_x = sorted(total.items(), key=operator.itemgetter(1),reverse=True)
top_100 = sorted_x[0:100] # change the numbers in brackets to expand the list. For instance, [0:10] shows the top 10
top_100


# This part of the code, writes the results into a file.

# In[12]:

f = open("top_100.txt","w",encoding='utf-8')

for ngram in top_100:
    f.write(ngram[0]+","+str(ngram[1])+"\n")
    

f.close()


#  
