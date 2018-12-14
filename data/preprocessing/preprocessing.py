
# coding: utf-8

# In[50]:


import os
import os.path
from PIL import Image


# In[32]:


dir_path = "./screenshot"
task_num = 20
human_iter = 10
robot_num = 21
human_num = 16


# In[62]:


# robot data
for i in range(1,task_num+1) :
    task_name = "{}_task_robot".format(i)
    task_name_2 = "{:02d}_task_robot".format(i)
    iter_name = "1_iter"
    path = dir_path + "/" + task_name + "/" + iter_name
    save_path = "./sample_data" + "/" + task_name_2 + "/" + iter_name 
    num_files = len(os.listdir(path))
    l = list(range(1,num_files+1))
    step = num_files/robot_num
    select_list = []
    t = 1
    k = 0
    while True :
        if k == robot_num :
            break
        if int(t / step) == k :
            select_list.append(t)
            t += 1
            k += 1
        else : 
            t += 1
    for s in select_list :
        image = Image.open(path+"/CameraTOP_img_{:02d}_{:03d}.png".format(i,s))
        image.resize((100,100),Image.ANTIALIAS)
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        image.save(save_path + "/CameraTOP_img_{:02d}_{:03d}.png".format(i,s))


# In[64]:


# human data
for i in range(14,task_num+1) :
    for j in range(1,human_iter+1) :
        task_name = "{}_task".format(i)
        task_name_2 = "{:02d}_task_human".format(i)
        iter_name = "{}_iter".format(j)
        iter_name_2 = "{:02}_iter".format(j)
        path = dir_path + "/" + task_name + "/" + iter_name
        save_path = "./sample_data" + "/" + task_name_2 + "/" + iter_name_2 
        num_files = len(os.listdir(path))
        l = list(range(1,num_files+1))
        step = num_files/human_num
        select_list = []
        t = 1
        k = 0
        while True :
            if k == human_num :
                break
            if int(t / step) == k :
                select_list.append(t)
                t += 1
                k += 1
            else : 
                t += 1
        for s in select_list :
            image = Image.open(path+"/CameraTOP_img_{:02d}_{:03d}.png".format(i,s))
            image.resize((100,100),Image.ANTIALIAS)
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            image.save(save_path + "/CameraTOP_img_{:02d}_{:03d}.png".format(i,s))

