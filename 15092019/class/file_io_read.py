import os


if __name__ == "__main__":

    print("File name is ", __file__)
    current_path = os.path.dirname(os.path.abspath(__file__))
    print("Current path is ", current_path)
    file_name = "test.txt"
    file_path = os.path.join(current_path, file_name)
    print("File path is ", file_path)
    try:
        file_obj = open(file_path, "r") # r is mode i.e read. BY DEFAULT MODE IS r  
    except FileNotFoundError as file_exctn:
        print("Exception Method is ", dir(file_exctn))
        print("Error No. is", file_exctn.errno)
        print("{} {} please create file".format(file_exctn.filename,
                                               file_exctn.strerror))
    else:
        file_data = file_obj.readlines()
        print("All file data is ", file_data)
        file_obj.seek(0)
        one_line = file_obj.readline()
        print("Line is ", one_line)
        file_obj.seek(0) # to change position of file pointer
        for each_line in file_obj:
            print("Each line using iterable ", each_line)
        file_obj.close()
        