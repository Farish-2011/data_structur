
stack = []

#push ----> add elements
def push(value):
    stack.append(value)
    print(value, "pushed into atack") 

push(10)
push(90)
push(330)

#pop ----> remove element 
def Pop():
    if len(stack) == 0:
        print("stack is empty")
    else:
        print("popped:",stack.pop())

Pop()
Pop()

#isEpmty ---> chacks if the stack is empty or not
def isEmpty():
    return len(stack) == 0

print("is stack empty?", isEmpty())


print("stack:",stack)