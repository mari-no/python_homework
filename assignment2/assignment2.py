    #Task 2: Read a CSV File

import csv
import traceback
import os
import custom_module 
from datetime import datetime

def read_employees():

    try:
        dict={}
        rows =[]

        with open('../csv/employees.csv', 'r') as employees:
            reader = csv.reader(employees)
            for i, row in enumerate(reader):
            
                if i==0:
                    dict["fields"]=row
                  
                else:
                    rows.append(row)
            dict["rows"]=rows
       #~ print("These are the rows of employees", rows)
       # print("This is dictionary", dict)
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []

        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}"
            )

        print(f"Exception type: {type(e).__name__}")

        message = str(e)
        if message:
            print(f"Exception message: {message}")

        print(f"Stack trace: {stack_trace}")
    return dict
employees=read_employees()


#print(employees)

    #Task 3: Find the Column Index
def column_index(param):
    index=employees["fields"].index(param)
    return index

employee_id_column = column_index("employee_id")


    #Task 4: Find the Employee First Name

def first_name(row_number):
    first=column_index("first_name")
    requested_row=employees["rows"][row_number]
    first_name_value=requested_row[first]
    return first_name_value


    #Task 5: Find the Employee: a Function in a Function

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    print (employee_match)
    matches=list(filter(employee_match, employees["rows"]))
    return matches
    
    #Task 6: Find the Employee with a Lambda
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

    #Task 7: Sort the Rows by last_name Using a Lambda

def sort_by_last_name():
   last_name_index=column_index("last_name")
   employees["rows"].sort(key=lambda row:row[last_name_index])
   return employees["rows"]



    #Task 8: Create a dict for an Employee

def employee_dict(row_list):
   
    
    keys_without_id=employees["fields"][1:]
   
   
    employee_dictionary=dict.fromkeys(keys_without_id, "Unknown")
  
    row_list=row_list[1:]
 
    for j in range(0, len(keys_without_id)):
        employee_dictionary[keys_without_id[j]]=row_list[j]
 
    return employee_dictionary



    #Task 9: A dict of dicts, for All Employees

def all_employees_dict():
    # employees_records=employees["rows"]
    # ids_list=[]
    # empl_data=[]
   

    # for row in employees_records:
    #     empl_id=row[0]
    #     empl_data_row=row
    #     ids_list.append(empl_id)
    #     empl_data.append(empl_data_row)
    # all_employees_dictionary=dict.fromkeys(ids_list, "Unknown")
    # for j in range (0, len(empl_data)):
    #     all_employees_dictionary[ids_list[j]]=employee_dict(empl_data[j])
    
    all_employees_dictionary = {}
    for row in employees["rows"]:
        all_employees_dictionary[row[0]] = employee_dict(row)
    return all_employees_dictionary


    #Task 10: Use the os Module

def get_this_value():

    return os.getenv("THISVALUE")
    #Task 11: Creating Your Own Module
def set_that_secret(new_secr):
    custom_module.set_secret(new_secr)


set_that_secret("I love Python")
print(custom_module.secret)


    #Task 12: Read minutes1.csv and minutes2.csv

def read_minutes_file(path):
    minutes={}
    minutes_rows =[]

    with open(path, 'r') as minutess:

        reader = csv.reader(minutess)
        for i, row in enumerate(reader):
            
            if i==0:
                minutes["fields"]=tuple(row)
                  
            else:
                minutes_rows.append(tuple(row))
        minutes["rows"]=tuple(minutes_rows)
    return minutes

def read_minutes():
    try:

        minutes1=read_minutes_file('../csv/minutes1.csv')
        minutes2=read_minutes_file('../csv/minutes2.csv')
    #     minutes1={}
    #     min_rows =[]
    #     minutes2={}
    #     min_rows_two =[]

    #     with open('../csv/minutes1.csv', 'r') as minutess1:

    #         reader = csv.reader(minutess1)
    #         for i, row in enumerate(reader):
            
    #             if i==0:
    #                 minutes1["fields"]=tuple(row)
                  
    #             else:
    #                 min_rows.append(tuple(row))
    #                 minutes1["rows"]=tuple(min_rows)
    #     #print("These are the rows of minutes", min_rows)
    #     #print("This is minutes dictionary", min_dict)


    #     with open('../csv/minutes2.csv', 'r') as minutess2:

    
    #         reader = csv.reader(minutess2)
    #         for i, row in enumerate(reader):
            
    #             if i==0:
    #                 minutes2["fields"]=tuple(row)
                  
    #             else:
    #                 min_rows_two.append(tuple(row))
    #                 minutes2["rows"]=tuple(min_rows_two)
    #    # print("These are the rows of minutes2", min_rows_two)
    #    # print("This is minutes dictionary2", min_dict_two)
        return minutes1,minutes2
    except Exception as e:
    
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"An exception occurred: {e}")

minutes1, minutes2=read_minutes()


    #Task 13: Create minutes_set
def create_minutes_set():
    minutes_set1=set(minutes1["rows"])
    minutes_set2=set(minutes2["rows"])
    minutes_set=minutes_set1.union(minutes_set2)
    return minutes_set

minutes_set=create_minutes_set()
    

    #Task 14: Convert to datetime

def create_minutes_list():
    minutes_list_converted=list(minutes_set)
  
    result=map(lambda x : (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list_converted)
    result=list(result)
    return result

minutes_list=create_minutes_list()




    #Task 15: Write Out Sorted List
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
 
    result_list=list(map(lambda x : (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))

    with open('./minutes.csv', 'w', newline='') as minutes:
        writer = csv.writer(minutes)
        writer.writerow(minutes1["fields"])
        writer.writerows(result_list)

    return result_list









