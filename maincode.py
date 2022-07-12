import json
from pathlib import Path
import random
import re
import string
import os

class Management:
    __database="student_teacher_data.json"
    __info=[]
    try:
        if not Path(__database).exists:
            with open (__database,'w') as fw:
                fw.write(json.dumps(__info))
        else:
            with open(__database,'r') as fr:
                __info=json.loads(fr.read())
    except Exception as err:
        print("ERROR >> ",err)
    def __generateid(self):
        seq1=(random.choices(string.ascii_letters,k=3))
        seq2=(random.choices(string.digits,k=3))
        seq3=(random.choices(list('@#$*'),k=2))
        x=seq1+seq2+seq3
        random.shuffle(x)
        return ("".join(x))
    def __str__(self):
        return "CANNOT ACCESS DATA DIRECTLY."
    def RegisteredEmployee(self):
        return self.__info
    @classmethod
    def ShowAllEmpployee(cls):
        return cls.__info
    
    def InsertData(self):
        try:
            data={}
            data["id"]=self.__generateid()
            data["name"]=input("Enter Name: ")
            data["status"]=input("Enter status (Student/teacher): ")
            data["contact"]=int(input("Enter contact number: "))
            Management.__info.append(data)
            with open(Management.__database,'w') as fw:
                fw.write(json.dumps(Management.__info))
                return f"Name: {data['name']}\nID: {data['id']}\nREGISTERED SUSSESFULLY!\n-- please !!! note down your id to access again --"
        except Exception as err:
            print("ERROR >> ",err)
#2
    def Read_SingleStu_Data(self):
        self.id=input("Enter Your ID: ")
        try:
            with open(Management.__database) as f:
                data=json.load(f)
            for i in data:
                if self.id==i["id"]:
                    return f"{i}"
                    break
            return False
        except Exception as err:
            print("ERROR >> ",err)
    def ReadSameKey(self):
        self.key=input("Enter the key(id,name,status,contact): ").strip().lower()
        try:
            with open(Management.__database) as f:
                data=json.load(f)
            for i in data:
                print(i[self.key])
        except Exception as err:
            print("ERROR >> ",err)
    #5
    def ReadAll(self):
        self.pas=input("Enter the passward which was given by developer: ").strip()
        if self.pas=="12345":
            try:
                with open(Management.__database) as f:
                    data=json.load(f)
                    print(data)
            except Exception as err:
                print("ERROR >> ",err)
        else:
            print("-- WRONG PASSWORD --")
        
    def ReadUnit(self):
        self.single=self.Read_SingleStu_Data()
        self.key=input("Enter the key(id,name,status,contact): ").strip().lower()
        try:
            data=eval(self.single)
            print(data[self.key])    
        except Exception as err:
            print("ERROR >> ",err)
# COMPLETED 
#3
    def FileUpdate(self):
        self.getdata=res.Read_SingleStu_Data()
        print(self.getdata)
        # self.getdata=eval(self.get)
        self.ask=input("Enter keys to update in keys(except id): ").strip()       
#4  
    def FileDelete(self):
        self.filepath=input("enter the directory/path of json file: ")
        os.remove(self.filepath)
        print("-- file delected succesfully --")
        
    def FiledataDelete(self):
        self.get=res.Read_SingleStu_Data()
        
            
        print("-- id is comletety delected  --")
        
# main menu
res=Management()
while True:
    print("1.Insert data of student/teacher")
    print("2.Read Single data of student/teacher ('id' is required)")
    print("3.Update data of student/teacher ('id' is required)")
    print("4.Delete data of student/teacher ('id' is required)")
    print("5.Read all data from jsons (password required: )")
    print("0.Exit Application")
    try:
        n=int(input("Enter Your choice: "))
        if n==1:
            print(res.InsertData())
        elif n==2:
            ask=int(input("1.read single student/teacher all data\n2.read all keyvalue data\n3.Single unit data\nChoose any one option: "))
            if ask==1:
                print(res.Read_SingleStu_Data())
            elif ask==2:
                (res.ReadSameKey())
            elif ask==3:
                res.ReadUnit()
            else:
                print("-- invalid option --")
        # COMPLETED
        elif n==3:
            print(res.FileUpdate())
        elif n==4:
            ask=int(input("1.delete the json file\n2.Delete in json file\nchoose any one option: "))
            if ask==1:
                res.FileDelete()
                
            elif ask==2:
                res.FiledataDelete()
            else:
                print("-- wrong input --")
        elif n==5:
            res.ReadAll()
        elif n==0:
            print("--- HELLO WORLD ---")
            break
    except Exception as err:
        print("ERROR >> ",err)