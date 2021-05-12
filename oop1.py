"""calculations"""

# m=float(input('m= '))
# n=float(input('n= '))
# a=float(input('a= '))
# b=float(input('b= '))
a=2
b=1
n=4
m=3

S=0
for j in range(b, m+1):
    S=S+(1/j)
print((S)*(n-a+1))

def multiply(a):
    b=[]
    for i in a:
        b.append(i*2)
    return b


test_data = [
    {
        'input': [1, 4, 9, 10],
        'expected': [2, 8, 18, 20]
    },
   {
        'input': [],
        'expected': []
    },
   {
        'input': [9, 0, 1, 0, 9],
        'expected': [18, 0, 2, 0, 18]
    },
]

for value in test_data:
    print("-" * 30)
    print("Input:", value['input'])
    print("Expected:", value['expected'])
    print("Result:", multiply(value['input']))
    print("Success:", multiply(value['input']) == value['expected'])
