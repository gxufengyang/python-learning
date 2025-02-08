#计算ABEFJ各个字母在seq中的出现次数，用于计算氨基酸频率
seq = "CCCHAJEAFIELAKJNFVLAIFEJLIEFJDCCCEFLEFJ"
query = "ABEFJ"
for COURT_1 in query:
    result = seq.count(COURT_1)
    print(result)
    
#need to be done:
#打印时要显示出aa和aa的数目