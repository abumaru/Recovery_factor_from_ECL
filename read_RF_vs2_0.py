# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 20:14:32 2019

@author: GOGUT
"""
import os
os.chdir(r"Y:\ressim\lavani-deep\dg2\simu1\ref_case_Swcr_sens")
def get_FGIP_FGPT(file):
    date_simu_Start = '1-JAN-2027'
    date_simu_end ='1-JAN-2060'
    vector_name_1 = 'FGPT'
    vector_name_2 = 'FGIP'
    with open(file) as fobj:
        vectors = fobj.read()
    vector_1 = vectors.find(vector_name_1)
    vector_name_f = vectors[vector_1:vector_1+4]
    if vector_name_f != vector_name_1:
        print("error!! in Vector name ")
    else:
        pass
    date_v = vectors.find(date_simu_end,vector_1)
    date_v_f = vectors[date_v:date_v+13]
    if date_v_f != date_simu_end:
        print("error!! in date name ")
        print(date_v_f,date_simu_end)
        print(len(date_v_f),len(date_simu_end))
    else:
        pass
    list_v =vectors[date_v:date_v+129].split(' ')
    list_v_filtered = []
    for elem in list_v:
        if elem != '':
            list_v_filtered.append(elem)
    #print(list_v_filtered)
    if len(list_v_filtered) ==10:
#print("data is fine")
#print(float(list_v_filtered[7])*10E6)
        global FGPT_final
        FGPT_final = float(list_v_filtered[7])*10E6
    else:
        print("lenght of list is not 10, something is missing!")
#print(FGPT_final)
    vector_2 = vectors.find(vector_name_2)
    vector_name_f = vectors[vector_2:vector_2+4]
    if vector_name_f != vector_name_2:
        print("error!!")
    else:
        pass
    date_v = vectors.find(date_simu_Start,vector_2)
    date_v_f = vectors[date_v:date_v+13]
    if date_v_f != date_simu_end:
        print("error!!")
        print(len(date_v_f),len(date_simu_Start))
    else:
        pass
    list_v =vectors[date_v:date_v+129].split(' ')
    list_v_filtered = []
    for elem in list_v:
        if elem != '':
            list_v_filtered.append(elem)
    #print(list_v_filtered)
    if len(list_v_filtered) ==10:
        #print("data is fine")
        #print(float(list_v_filtered[1])*10E6)
        global FGIP_final
        FGIP_final = float(list_v_filtered[1])*10E6
        global RF_final
        RF_final = FGPT_final/FGIP_final
    print(RF_final)
    print(RF_final*100)
    

file_list=[]
for root, dirs, files in os.walk(".", topdown = True):
   for file in files:
       if file.endswith('.RSM'):
           rel_file= os.path.join(root,file)
           abs_file= os.path.abspath(rel_file)
           abs_file_frwd = abs_file.replace('\\','/')
           file_list.append(abs_file_frwd)
print(file_list)
RF_list=[]
FGIP_ll=[]
FGPT_ll=[]
for pathh in file_list:
    rec_fact = get_FGIP_FGPT(pathh)
    RF_list.append(RF_final)
    FGIP_ll.append(FGIP_final)
    FGPT_ll.append(FGPT_final)
print(RF_list)
output_list=list(zip(file_list,RF_list))
print('===='*10)
print('gas production total [Sm3]:', FGPT_ll)
print('gas in place[Sm3]:', FGIP_ll)
print('===='*10)
print(output_list)

#for m ,n in zip(file_list,RF_list):
#    output_list.app()