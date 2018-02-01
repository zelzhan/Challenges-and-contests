class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

                                                                    #basic class operations
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):      #constructor
        super().__init__(firstName, lastName, idNumber)             #inheritance
        self.scores = scores
    
    def calculate(self):                                            #some routine stuff
        mean = sum(self.scores) / float(len(self.scores))
        if (mean >= 90 and mean <= 100):
            return("O")
        elif(mean >= 80 and mean < 90):
            return("E")
        elif(mean >= 70 and mean < 80):
            return("A")
        elif(mean >= 55 and mean < 70):
            return("P")
        elif(mean>= 40 and mean < 50):
            return("D")
        else:
            return("T")

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
