import csv
import traceback


def read_to_list():
    
    
    try:  
        with open("../csv/employees.csv", "r") as empl:
            reader=csv.reader(empl)
            
            return [row for row in reader]
    except Exception as e:
    
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        print(f"An exception occurred: {e}")
   
    
list_of_lists=read_to_list()  

def create_fullname_list():
    fullname_list = [row[1]+" "+row[2] for row in list_of_lists[1:]]
    return fullname_list


fullname_list = create_fullname_list()
def create_fullname_with_e_only():
    
    fullname_list_e_only =[ name for name in fullname_list if "e" in name]
    return fullname_list_e_only


print(create_fullname_list())
print(create_fullname_with_e_only())