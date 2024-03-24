class Golf():
    'Golf scoring class'       #Documentation string
    results = " "

    def __init__(self, hole, score, par):       #Initialization or constructor method
        self.hole = hole
        self.par = par

    def evaluateAndDisplayScore(self, hole, score):     #displayScore method of class Golf
    #Evaluate scores against par
        if (score > self.par):
            Golf.results = "Over Par"
        elif (score < self.par):
            Golf.results = "Under Par"
        else:
            Golf.results = "At Par"
        #Display results
        print("You scored", Golf.results, "on hole #", hole, "with a par of", self.par)

#Initialize variables
score = 0

#Create objects
hole1 = Golf(1, score, 3)
hole2 = Golf(2, score, 4)
hole3 = Golf(3, score, 5)

#Prompt user to enter hole and score
enterHole = int(input("Enter the hole number: "))
score = int(input("Enter your Score: "))

#Evaluate hole number and call appropriate class method to display score
if enterHole == 1:
    hole1.evaluateAndDisplayScore(enterHole, score)
if enterHole == 2:
    hole2.evaluateAndDisplayScore(enterHole, score)
if enterHole == 3:
    hole3.evaluateAndDisplayScore(enterHole, score)