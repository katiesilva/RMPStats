import urllib2, sys, json
from person import Person
from review import Review
from dataAnalysis import DataAnalysis
from bs4 import BeautifulSoup



#Takes in all of the html for the professor's page and returns
#a string with all of the html relevant to each individual review,
#making sure to go to all of the pages of reviews and add
#all of them to the string.
def getAllRatings(soup):
    count = 1
    newsoup = soup
    ratingsHTML = []
    pageNo =  soup.find(id="pagination").find(id="back_1").find_next().find_next().find_next().find_next().get_text()
    while int(pageNo) >= count:
        newURL = baseURL + "&pageNo=" + str(count)
        newsoup = BeautifulSoup(urllib2.urlopen(newURL).read())
        ratingsHTML.append(newsoup.find_all('div',attrs={'class':'entry odd '}))
        ratingsHTML.append(newsoup.find_all('div',attrs={'class':'entry even '}))
        count = count + 1
    return str(ratingsHTML)


#Creates a list of all of the fields of a type given how they start
#and end within a string that encompasses all of the relevant html
#needed to find the fields of a review. So, if you pass in a string
#version of all of the HTML that has the reviews necessary, and strings
#that denote the beginning and end of a field, you get a list of all
#of those fields (A list of dates, or comments, or ratings, etc). 
def getFieldList(allRatings, startString, endString):
    fieldList = []
    ratingsString = allRatings
    remainingString = ""
    productString = ""
    while (ratingsString.partition(startString)[1] != ""):
        remainingString = ratingsString.partition(startString)[2]
        productString = remainingString.partition(endString)[0]
        if(not productString.isdigit() and productString != " "):
            fieldList.append(productString)
        elif(productString == " "):
            fieldList.append(0);
        else:
            fieldList.append(int(productString))
        ratingsString = remainingString.partition(endString)[2]
    return fieldList


#Creates a list of Review objects based on in order lists of each
#field in a Review object. Loops through each list, adding the ith
#item in each one to a new Review object, and then appending this
#Review object to a new list of Reviews.
def createReviewList(dateList, qualityList, easinessList, helpList, clarityList, interestList, commentList):
    reviewList = []
    for i in dateList:
        newReview = Review(dateList[dateList.index(i)], qualityList[dateList.index(i)], easinessList[dateList.index(i)], helpList[dateList.index(i)], clarityList[dateList.index(i)], interestList[dateList.index(i)], commentList[dateList.index(i)])
        reviewList.append(newReview)
    return reviewList

                
        
#-----------------PARSING--------------------------------------------------------------------------

    
#manual input
school = raw_input("Enter the school name: ")
name = raw_input("Enter the professor's full name: ")
outStr = name + " " + school
outStr = outStr.replace (" ", "%20")

#url build to get JSON object url
baseURL = "http://www.ratemyprofessors.com/solr/interim.jsp?select?facet=true&q="
baseURL += outStr
baseURL += "&facet.field=schoolname_s&facet.field=teacherdepartment_s&facet.field=schoolcountry_s&facet.field=schoolstate_s&facet.limit=50&rows=20&facet.mincount=1&json.nl=map&fq=content_type_s%3ATEACHER&wt=json"

#gets the json object for the base page (aka the search results as a JSON
soup = json.loads(urllib2.urlopen(baseURL).read())

#finds the content of the fields we want from the json object
#Right now we assume we have one result on the page but we need
#to do a check to make sure that we have one result in the first
#place (if there are no results they probably typed the name or school wrong,
#so allow them to try again), and possibly define what we will do if we
#have more than one result.
pk_id = soup['response']['docs'][0]["pk_id"]
department = soup['response']['docs'][0]["teacherdepartment_s"]
hot = soup['response']['docs'][0]["averagehotscore_rf"]

#Gets the professor's indivdual page
baseURL = "http://www.ratemyprofessors.com/ShowRatings.jsp?tid=" + str(pk_id)

#Then sets soup to HTML of professor's page
soup = BeautifulSoup(urllib2.urlopen(baseURL).read())


#-----------------BUILDING--------------------------------------------------------------------------

#Builds the person from the HTML/JSON
currentPerson = Person(soup, pk_id, department, hot)

#Creates the string of all of the reviews that we can parse for the fields we want
ratingsList = getAllRatings(soup)
#Creates lists of dates, quality ratings, easiness ratings, etc. Each index from one
#list should correspond to the same index in every other list.
#The strings tell you were to start looking for each field and where to end.
dateList = getFieldList(ratingsList, "<div class=\"date\">", "</div>")
qualList = getFieldList(ratingsList, "Quality\">", " Quality")
easeList = getFieldList(ratingsList, "Easiness</strong><span>", "<")
helpList = getFieldList(ratingsList, "Helpfulness</strong><span>", "<")
clarList = getFieldList(ratingsList, "Clarity</strong><span>", "<")
intrList = getFieldList(ratingsList, "Interest</strong><span>", "<")
commList = getFieldList(ratingsList, "\"commentText\">", "<")    

#Builds the review lists out of all of our lists of dates, lists of qualities, etc.
reviewList = createReviewList(dateList, qualList, easeList, helpList, clarList, intrList, commList)

#Creates a DataAnalysis object using the person we created above and a list of
#Review objects holding all of the data from their reviews
dataAnalyzer = DataAnalysis(currentPerson, reviewList)

#------------------PRINTING-------------------------------------------------------------------

#Prints out the professor/person data.
print "\n\n"
print "--------Professor summary"
currentPerson.toString()
print "\n\n"

#Prints out all the review data.
'''for item in reviewList:
    item.toString()
    print "\n"'''
#Prints out the first review.
print "--------Example review"
reviewList[0].toString()
print "\n\n"

#Prints how many poor, average and good ratings the professor recieved.
PAGTuple = dataAnalyzer.sumOfPAGs()
print "--------GAP (Good, Average, Poor) frequency"
print "Good:    " + str(PAGTuple[0][1])
print "Average: " + str(PAGTuple[1][1])
print "Poor:    " + str(PAGTuple[2][1])
print "\n\n"

#Prints out a list of all of the common adjectives matched from the list with
#their frequency across all comments
print "--------Common adjective frequency"
frequencyList = dataAnalyzer.compareAdjs()
for item in frequencyList:
    print item
