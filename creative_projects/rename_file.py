import os

def rename_file():
    #get files names from a folder 
    file_list = os.listdir(r"D:\Users\luzbog\Documents\imagenes")
    #print(file_list)
    save_path = os.getcwd
    print("Current workin Directory is " + save_path)

    #for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.transtale(None, "0123456789"))




if __name__ == "__main__":
    rename_file()