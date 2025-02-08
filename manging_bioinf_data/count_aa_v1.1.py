seq = "CCCHAJEAFIELAKJNFVLAIFEJLIEFJDCCCEFLEFJ"
query = "ABEFJ"
for COURT_1 in query:               #for i in nn语句应是从nn中取出一个元素作为自变量i，用i去执行冒号后面的代码，直至列表nn中的元素耗尽
    result = seq.count(COURT_1)
    print(COURT_1, result)         #直接把COURT_1变量加入到打印函数中，即可实现同时打印aa和aa的数目


