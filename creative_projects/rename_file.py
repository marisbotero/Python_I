import os

def rename_file():
    #(1)get files names from a folder 
    file_list = os.listdir(r"E:\Img")
    #print(file_list)
    save_path = os.getcwd
    print("Current workin Directory is " + save_path)
    os.chdir(r'E:\Img')
    


    #for each file, rename filename
    for file_name in file_list:
            print("old name - " + file_name)
            print("new name - " + file_name.transtale(None, "0123456789")
            os.rename(file_name, file_name.transtale(None, "0123456789"))
    os.chdir(save_path)




if __name__ == "__main__":
    rename_file()