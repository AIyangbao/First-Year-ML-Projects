#1.字符串的基本操作
from numpy import append


s1 ="hello, Python!"
print("长度:",len(s1))
print("第一个字符:",s1[0])
print("最后一个字符:",s1[-1])
#2.字符串的切片操作
s2 = "Python Programming"
print("前5个字符：",s2[:5])
print("后6个字符：",s2[-6:])
print("第2到第8个字符：",s2[1:8])
#3.字符串的拼接
s3="hello"
s4="world"
result = s3 + " " + s4
print(result)
#4.字符串的格式化
name="张三"
age=20
score=95.5
print(f"姓名:{name},年龄:{age},成绩:{score}分")
#5.字符串常用方法—查找和替换
s5="I like apple, apple is delicious."
print("apple首次出现的位置:",s5.find("apple"))
print("apple最后出现的位置:",s5.rfind("apple"))
new_s = s5.replace("apple","orange")
print("替换名:",new_s)
6.#字符串分割和连接
s6="Python Java C++ JavaScript"
words =s6.split()
print("分割结果:",words)
new_s = "-".join(words)
print("连接后:",new_s)
#7.字符串大小写转换
s7 = "hello world"
print("全大写:",s7.upper())
print("全小写:",s7.lower())
print("首字母大写:",s7.title())
#8.字符串去除空白字符
s8 ="  Python Programming  "
print("原始字符串:",f"{s8}")
print("去除两端空白:",f"{s8.strip()}")
print("去除左端空白:",f"{s8.lstrip()}")
print("去除右端空白:",f"{s8.rstrip()}")
#9.字符串判断方法
s9 ="Python123"
print("是否以'Py'开头:",s9.startswith("Py"))
print("是否以'123'结尾:",s9.endswith("123"))
print("是否全为数字:",s9.isdigit())
print("是否全为字母:",s9.isalpha())
print("是否全为字母或数字:",s9.isalnum())
#10.综合应用1-字符串处理
sentence ="Python is a great programming language"
words = sentence.split()
word_count = len(words)
reversed_words =[word[::-1] for word in words ]
result = " ".join(reversed_words)
print("原始句子:",sentence)
print("单词数量:",word_count)
print("单词反转后:",result)
#11.综合应用2-定义一个函数，实现股价计算
def func():
    name="传智播客"
    stock_price=19.99
    stock_code="003032"
    stock_price_daily_growth_factor=1.2
    growth_days=7
    growth_price=stock_price*stock_price_daily_growth_factor**growth_days
    print(f"公司：{name},股票代码:{stock_code},当前股价:{stock_price}")
    print("每日增长系数是%s,经过%s天的增长后，股价达到了:%s"%(stock_price_daily_growth_factor,growth_days,growth_price))
#12.综合应用3
def string_to_upper():
    a=input()
    b=a.lower()
    c=b.title()
    print(c)
#综合应用4
def word_count():
    a = input()
    input_tuple = eval(a)
    unique_elements = set(input_tuple)
    count_result={}
    for elem in unique_elements:
        count_result[elem]=input_tuple.count(elem)
    print(count_result)
if __name__ == "__main__":
    word_count()
