'''国内阿里云服务器
https://mirrors.aliyun.com/pypi/simple/'''
from itertools import count
from shlex import join
import random

def reverse_string(s):
    words=s.split()
    list=[word[::-1] for word in words]
    new_str="".join(list)
    list_word=["a","e","i","o","u"]
    count_all=0
    for word in list_word:
        count=s.count(word)
        count_all+=count
    print(f"\"反转字符串为:{new_str},元音字母个数为:{count_all}\"")
reverse_string(s="abc")

def classify_numbers(n):
  try:
    numbers=[number for number in range(1,n+1)]
    dirt={}
    list_1=[number for number in numbers if number%2!=0]
    list_2=[number for number in numbers if number%2==0]
    dirt["奇数"]=[number for number in list_1]
    dirt["偶数"]=[number for number in list_2]
    print(f"\"奇数为：{dirt['奇数']},偶数为：{dirt['偶数']}\"")
  except:
     print("请输入正整数")
classify_numbers(n=5)
    

        




    





