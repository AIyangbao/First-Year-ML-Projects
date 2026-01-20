#关于列表的语法
#打印列表
def list_func():
    list = [1, 2, 3, 4, 5]
    print(list)
    # 将数字6添加到列表末尾
    list.append(6)
    print(list)
    list.insert(1, 99)
    # 删除第三位数字
    del list[2]
    print(list)
    # 将第一位数字修改为100
    list[0] = 100
    print(list)
    # 将列表升序排序
    list.sort()
    print(list)
    # 将列表降序排序
    list.sort(reverse=True)
    print(list)
    # 查询数字100的索引
    index = list.index(100)
    print(index)
    # 计算100在列表中出现的次数
    count = list.count(100)
    print(count)
    # 将列表倒序
    list.reverse()
    print(list)


#元组的语法
def tup_func():
    tup = (1, 2, 3)
    print(tup)
    print(tup[1])
    # tuple[0]=2
    # print(tuple)
    tup2 = (4, 5)
    new_tup = tup + tup2
    print(new_tup)
    print(2 in tup)
    print(tup.count(2))
    lst=list(tup)
    print(lst)
    print(tup[:2])
    for items in tup:
        print(items)
    for index, value in enumerate(tup):
        print(f"index={index},value={value}")
def dict():
    d = {'a': 1, 'b': 2, 'c': 3}
    print(d)
    d['d'] = 4
    print(d)
    d['a'] = 100
    print(d)
    del d['b']
    print(d.keys())
    print(d.values())
    print('a' in d)
    value = d.get('e','Not Found')
    print(value)
    d2={'e':5,'f':6}
    d.update(d2)
    print(d)
    for key, value in d.items():
        print(f"{key}:{value}")
def func_set():
    s={1,2,3,4,5}
    print(s)
    s.remove(3)
    print(s)
    print(4 in s)
    s2={4,5,6,7}
    print(s & s2)
    print(s | s2)
    print(s - s2)
    print(s.issubset(s2))
    lst=[1,2,2,3,4]
    s3 =set(lst) # type: ignore
    print(s3)
    s.clear()
    print(s)

def func1():
    my_list = [1,2,3,4,5,6,7,8,9,10]
    new_list = []
    #for循环法
    for x in my_list:
        if x % 2 ==0:
            new_list.append(x)
    print("通过for循环，从列表:",my_list,"取出偶数，组成新列表:",new_list)
    #while循环法
    i = 0
    while i <10:
        if my_list[i]%2 == 0:
            new_list.append(my_list[i])
        i +=1
    print("通过while循环，从列表：",my_list,"取出偶数，组成新列表:",new_list)

def func2():
    my_list = ["黑马程序员","传智播客","黑马程序员","传智播客","itheima","itcast","itheima","itcast","best"]
    my_set = set()
    for item in my_list:
        my_set.add(item)
    print("有列表:",my_list)
    print("存入集合后结果:",my_set)

if __name__=="__main__":
    dict()




