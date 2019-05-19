import random 

def searc(data):
    print(data)
    for i in range(len(data)):
        print(i)

if __name__ == "__main__":
    random.seed(20)
    data = [random.randint(0,100) for i in range(10)]
    a = input('Escribe el valor a buscar')
   
    print(data)
   
    