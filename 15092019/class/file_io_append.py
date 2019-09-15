import os

def get_data(file_ptr):
    
    return file_data

if __name__ == "__main__":

    print("File name is ", __file__)
    current_path = os.path.dirname(os.path.abspath(__file__))
    print("Current path is ", current_path)
    file_name = "city_temerature.txt"
    file_path = os.path.join(current_path, file_name)
    print("File path is ", file_path)
    try:
        file_obj = open(file_path, "a+") # a is mode i.e append mode.  
    except FileNotFoundError as file_exctn:
        print("Exception Method is ", dir(file_exctn))
        print("Error No. is", file_exctn.errno)
        print("{} {} please create file".format(file_exctn.filename,
                                               file_exctn.strerror))
    else:
        temprature_data = "Mumbai 70c\nPune 60c\n"
        temprature_data_list = ["Delhi 50c", "Kolcutta 40c", "Karnatka 30c", "Chennai 60c\n"]
        file_obj.write(temprature_data) # using string data
        file_obj.writelines("\n".join(temprature_data_list)) # using list of data
        file_obj.seek(0)
        file_data = file_obj.readlines()
        print("File content is ", file_data)
        file_obj.close()
        