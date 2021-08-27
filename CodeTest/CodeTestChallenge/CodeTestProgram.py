# output format:
# last name
# first name
# gender
# date of birth
# favorite color


# input format:
# The pipe-delimited file lists each record as follows:
# LastName | FirstName | MiddleInitial | Gender | FavoriteColor | DateOfBirth
# The comma-delimited file looks like this:
# LastName, FirstName, Gender, FavoriteColor, DateOfBirth
# The space-delimited file looks like this:
# LastName FirstName MiddleInitial Gender DateOfBirth FavoriteColor
import datetime
class Person:
    def __init__(self, lastname, firstname, gender, dob, favcolor):
        self.lastname=lastname
        self.firstname=firstname
        self.gender=gender
        self.dob=datetime.datetime.strptime(dob, "%m-%d-%Y")
        self.favcolor=favcolor
    def __str__(self):
        return self.lastname+" "+self.firstname+" "+self.gender+" "+self.dob.strftime("%m/%d/%Y")+" "+self.favcolor
class Process_Files:
    def __init__(self, input_files, output_file):
        self.input_files=input_files
        self.output_file=output_file
        self.data=[]
    def read_data(self):
        for filename in self.input_files:
            with open(filename,"r") as file:
                d=file.readlines()
                if "," in d[0]:
                    indexes=[0,1,2,4,3]
                    delimiter=", "
                    dt_delimiter="/"
                elif "|" in d[0]:
                    indexes=[0,1,3,5,4]
                    delimiter=" | "
                    dt_delimiter="-"
                else:
                    indexes=[0,1,3,4,5]
                    delimiter=" "
                    dt_delimiter="-"
                for line in d:
                    line=line.strip("\n")
                    line=line.split(delimiter)
                    lastname=line[indexes[0]]
                    firstname=line[indexes[1]]
                    gender=line[indexes[2]]
                    if gender=="M":
                        gender="Male"
                    if gender=="F":
                        gender="Female"
                    dateofbirth=line[indexes[3]]
                    dateofbirth="-".join(dateofbirth.split(dt_delimiter))
                    favoritecolor=line[indexes[4]]
                    person=Person(lastname, firstname, gender, dateofbirth, favoritecolor)
                    self.data.append(person)
                    print(person)

if __name__ == '__main__':
    input_files=["space.txt", "pipe.txt", "comma.txt"]
    processdata=Process_Files(input_files, "result.txt")
    processdata.read_data()


        