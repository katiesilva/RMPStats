from review import Review

'''
fname, lname, school, department, overallQuality,
helpfulness, clarity, easiness, chiliPeppers, numRatings, allReviews
'''
class Person:
    def __init__(self, SOUP, PI_ID, DEPARTMENT, HOT):
        self.pk_id = PI_ID
        self.firstName = findFirstName(SOUP)
        self.lastName = findLastName(SOUP)
        self.school = findSchool(SOUP)
        self.department = DEPARTMENT
        self.overallQuality = findOverallQuality(SOUP)
        self.helpfulness = findHelpfulness(SOUP)
        self.clarity = findClarity(SOUP)
        self.easiness = findEasiness(SOUP)
        self.chiliPeppersReal = HOT
        self.numRatings = findNumRatings(SOUP)
        self.soup = SOUP
        
    def toString(self):
        print "First Name: " , self.firstName
        print "Last Name: " , self.lastName
        print "School: " , self.school
        print "Department: " , self.department
        print "Overall Quality: " , self.overallQuality
        print "Helpfulness: " , self.helpfulness
        print "Clarity: " , self.clarity
        print "Easiness: " , self.easiness
        print "Hotness Differential: " , self.chiliPeppersReal
        print "Number of Ratings: " , self.numRatings

    def getPk_id(self):
        return self.pk_id
    
    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName
    
    def getSchool(self):
        return self.school

    def getDepartment(self):
        return self.department
    
    def getOverallQuality(self):
        return self.overallQuality

    def getHelpfulness(self):
        return self.helpfulness
    
    def getClarity(self):
        return self.clarity

    def getEasiness(self):
        return self.easiness
    
    def getChiliPeppers(self):
        return self.chiliPeppers

    def getChiliPeppersReal(self):
        return self.chiliPeppersReal
    
    def getNumRatings(self):
        return self.numRatings

    def getSoup(self):
        return self.soup
    
def findFirstName(soup):
    desc = soup.findAll("meta", {"name":"prof_name"})
    firstLast = desc[0]['content'].encode('utf-8')
    firstLast = firstLast.replace(" ", "") 
    firstLast = firstLast.replace(",", " ")
    firstName = firstLast.split(" ")[1]
    return firstName

def findLastName(soup):
    desc = soup.findAll("meta", {"name":"prof_name"})
    firstLast = desc[0]['content'].encode('utf-8')
    firstLast = firstLast.replace(" ", "") 
    firstLast = firstLast.replace(",", " ")
    lastName = firstLast.split(" ")[0]
    return lastName

def findSchool(soup):
    desc = soup.findAll("meta", {"name":"school_name"})
    school = desc[0]['content'].encode('utf-8')
    return school

def findOverallQuality(soup):
    return soup.find(id="scoreCard").find(id="quality").find_next().find_next().get_text()
    
def findHelpfulness(soup):
    return soup.find(id="scoreCard").find(id="helpfulness").find_next().find_next().get_text()

def findClarity(soup):
    return soup.find(id="scoreCard").find(id="clarity").find_next().find_next().get_text()
    
def findEasiness(soup):
    return soup.find(id="scoreCard").find(id="easiness").find_next().find_next().get_text()

def findHotness(soup):
    return str(soup.find(id="scoreCard").find("script")).split(" ")[2].split("=")[1].split(";")[0]

def findNumRatings(soup):
    return soup.find(id="reportProblem").find(id="rateNumber").find_next().get_text()
