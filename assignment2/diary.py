    ##Task 1

try:
    with open('diary.txt', 'a') as diary:
        first = True
        record=""
        while  record != "done for now":
            if first==True:
                record = input("What happened today? ")
                first=False
                record = input("What else? ")
                diary.write(record+"\n")
            else:
                diary.write(record+"\n")
                break


        



except Exception as e
    print(f"An exception occurred: {e}")
