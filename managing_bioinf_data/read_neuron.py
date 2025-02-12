#Python3.7.3
#读取和简单统计neuron_data.txt文件内容
#统计项包括：总个数、个数总值、平均值、最大值、最小值。
#将结果格式化地写入neu_results.txt文件中。文件会在当前工作文件夹找到。
neu = []
for value in open('neuron_data.txt', 'r'):
  neu.append(
    float(value.strip())
    )


n = len(neu)
total = sum(neu)
average = total / n
shortest = min(neu)
longest = max(neu)

neu.sort() #易错点1. sort代码的位置，在output之前一步
output = open('neu_results.txt', 'w')
output.write('number of dendritic length:   % 4i \n' % (n)) #易错点2. 两个%都在write()的括号里
output.write('total dendritic length:        % 7.2f \n' % (total)) #而第二个%用作指定输入变量，不应在引号内变成字符
output.write('mean dendritic length:        % 7.2f \n' % (average))
output.write('shortest dentritic length:    % 7.2f \n' % (shortest))
output.write('longest dengdritic length:    % 7.2f \n' % (longest))
output.write('% 37.2f \n % 37.2f \n' % (neu[-2], neu[-3]))
output.close() #易错点3. output作为缓存对象，要及时关闭。不关闭第一次运行出错，代码改对再运行也会出同样的错，除非重启python。
             




