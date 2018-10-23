import random

subjects = ["Lab_1","Lab_2","DBMS","Java","CN","PC","BM"]
days_subj = []
weeks_subj = []

for i in range(0,5):
    for j in range(0,7):
        days_subj.append(random.choice(subjects))

    weeks_subj.append(days_subj)
    days_subj=[]




print(weeks_subj)
