import random
alphabet = "ATCG"
seq = ""
for i in range(10):             #range()函数产生0-9共10个元素，遍历10个元素for就循环了10次
  index = random.randint(0,3)   #random模块中的randint()函数随机输出1、2、3、4中的一个值用作index
  seq = seq + alphabet[index]   #通过索引值取得alphabet字符串中对应的1个元素，并进入seq对象中形成新的seq对象存入内存
print (seq)