# _*_ coding:utf-8 _*_
f=open('sougou.txt','r',encoding='utf-8')
w=open('sougou1.txt','w',encoding='utf-8')
i=0
for line in f:

    i+=1
    print(line.strip())
    w.writelines(line)
    if i>10:
        break

f.close()
w.close()