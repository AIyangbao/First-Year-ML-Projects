def add(a,b):
    return a + b
print(add(3,5))

def factorial(n):
    if n == 1 :
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

def greet(name="同学"):
    return f"你好,{name}"
print(greet("小明"))
print(greet())

def sum_all(*args):
    return sum(args)

print(sum_all(1,2,3,4))

def print_info(name,age,city):
    print(f"姓名:{name},年龄,{age},城市:{city}")

print_info(name="小红",age=20,city="广州")

multiply = lambda x,y:x*y
print(multiply(4,5))

def outer():
    message="Hello"
    def inner():
        return message + "World"
    return inner()
print(outer())

x=10 #全局变量
def test_scope():
    x = 20
    print("局部变量x =",x)
    test_scope()
    print("全局变量 x =",x)

def fibonacci(n):
    a,b =0,1
    for _ in range(n):
        yield a
        a,b = b,a + b

for num in fibonacci(5):
    print(num,end=" ")

def calculator(a,b,op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b !=0 else "除数不能为0"
    else:
        return "无效操作符"
print(calculator(10,5,'+'))
print(calculator(10,0,'/'))
