
import random



if __name__ == "__main__":
    data = [random.randint(0,100) for i in range(10)]
    data.sort(reverse=True)
    #data.sort()
    print(data)