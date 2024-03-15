#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install pytest-shutil


# In[2]:


import os
import shutil


# In[3]:


#path=r"/Users/benhood/Downloads"
path1= os.path.expanduser(r'/Users/benhood/Downloads')
#r stands for raw string
#had to chage backslash to forwardslash


# In[4]:


print(os.getcwd())


# In[5]:


#file_type = os.listdir(r"/Users/benhood/Downloads")
#will show all files in path
file_type = os.listdir(path1)


# In[6]:


#import os
#import shutil
#path1= os.path.expanduser(r'\Users\benhood\Downloads')
#path1= os.path.expanduser(r'/Users/benhood/Downloads')
#file_type = os.listdir(path1)

for file in file_type:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]
    
    if os.path.exists(os.path.join(path1,extension)):
        shutil.move(os.path.join(path1,file), os.path.join(path1,extension,file))
    else:
        os.makedirs(os.path.join(path1,extension))
        shutil.move(os.path.join(path1,file), os.path.join(path1,extension,file))



# In[7]:


#resources
#https://www.youtube.com/watch?v=KBjBPQExJLw
#https://www.youtube.com/watch?v=gs0FNQR0njI


# In[8]:


#os.path.exists(path+ 'csv files')


# In[ ]:





# In[ ]:





# In[9]:


#shutil.move(r'/Users/benhood/Downloads'+'/'+file, r'/Users/benhood/Downloads/jpeg')


# In[10]:


#folder_names = ['csv files', 'image files', 'text files']


#for loop in range(0,3):
        #if not os.path.exists(path + folder_names[loop]):
            #print(path + folder_names[loop])
            #os.makedirs(path + folder_names[loop])
            


# In[ ]:





# In[11]:


#for file in file_type:
    #if ".csv" in file and not os.path.exists(path + 'csv files/'+ file):
        #shutil.move(path + file,path +'csv files/'+ file)


# In[ ]:





# In[12]:


#https://www.youtube.com/watch?v=HiOtQMcI5wg
#import time
# timer
#while (true):
    #Variable to run()
    #time.sleep(5)


# In[13]:


#for file in files:
        #filename,extension  = os.path.split(file)
        #extension = extension[1:]
        
        #if os.path.exsists(path+)


# In[ ]:





# In[ ]:




