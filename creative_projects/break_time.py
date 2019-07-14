import webbrowser 
import time

def take_break(total_break, break_count):
    print("This program started on " + time.ctime())
    while (break_count < total_break):
        time.sleep(10)
        webbrowser.open(url)
        break_count = break_count + 1
        
    
if __name__ == "__main__":
    total_break = 3
    break_count = 0
    url = "https://www.youtube.com/watch?v=SXcFYnHSG08"
    take_break(total_break, break_count)
    
    