from person import Person
from review import Review

class DataAnalysis:

    def __init__(self, PERSON, REVIEWLIST):
        self.person = PERSON
        self.reviewList = REVIEWLIST
        self.wordList = ["impossible","hilarious","useless","pointless","effective","cute","superb","great","fair","derpy","bad","wise","rude","hard","easy","neat","honest","grumpy","above average","amusing","ambitious","amazing","artistic","assertive","attentive","awful","awesome","below average","blunt","brave","bright","brilliant","callous","candid","capable","careful","caustic","cautious","charming","childish","cheerful","competent","civil","clean","clever","clumsy","conceited","condescending","confident","confused","cool","considerate","conscientious","cooperative","cordial","courageous","cowardly","crabby","crafty","cranky","crass","critical","cruel","curious","cynical","dainty","decisive","deep","deferential","deft","delicate","dependent","delightful","demure","depressed","devoted","diligent","direct","dirty","disagreeable","discerning","discreet","disruptive","dramatic","dreary","drowsy","dull","eager","earnest","easy-going","efficient","egotistical","emotional","energetic","enterprising","enthusiastic","evasive","even-tempered","excellent","excitable","experienced","fabulous","fastidious","ferocious","fervent","fiery","flabby","flaky","flashy","frank","friendly","funny","fussy","generous","gentle","gloomy","good","grave","groggy","grouchy","guarded","hateful","hearty","helpful","hesitant","hot-headed","hypercritical","hysterical","idiotic","idle","illogical","imaginative","immature","immodest","impatient","imperturbable","impetuous","impractical","impressionable","impressive","impulsive","inactive","incompetent","inconsiderate","inconsistent","independent","indiscreet","indefatigable","industrious","inexperienced","insensitive","inspiring","intelligent","interesting","intolerant","inventive","irascible","irritable","irritating","jocular","jovial","joyous","judgmental","keen","kind","lame","lazy","lean","leery","lethargic","level-headed","listless","lithe","lively","local","logical","long-winded","lovable","lovely","mature","mean","meddlesome","mercurial","methodical","meticulous","mild","miserable","modest","moronic","morose","motivated","musical","naive","nasty","natural","naughty","negative","nervous","noisy","normal","nosy","numb","obliging","obnoxious","old-fashioned","one-sided","orderly","ostentatious","outgoing","outspoken","passionate","passive","patient","peaceful","peevish","pensive","persevering","persnickety","petulant","picky","plain","plain-speaking","playful","pleasant","plucky","polite","popular","positive","powerful","practical","prejudiced","proficient","proud","provocative","prudent","punctual","quarrelsome","querulous","quick","quick-tempered","quiet","realistic","reassuring","reclusive","reliable","reluctant","resentful","reserved","resigned","resourceful","respected","respectful","responsible","restless","revered","ridiculous","sad","sassy","self-assured","selfish","sensible","sensitive","sentimental","serene","serious","sharp","short-tempered","shrewd","shy","silly","sincere","sleepy","slight","sloppy","slothful","slovenly","slow","smart","snazzy","sneering","snobby","somber","sober","sophisticated","soulful","soulless","sour","spirited","spiteful","stable","steady","stern","stoic","striking","strong","stupid","sturdy","subtle","sullen","superficial","surly","suspicious","sweet","tactful","tactless","talented","testy","thinking","thoughtful","thoughtless","timid","tired","tolerant","touchy","tranquil","unaffected","unbalanced","uncertain","uncooperative","undependable","unemotional","unfriendly","unguarded","unhelpful","unimaginative","unmotivated","unpleasant","unpopular","unreliable","unsophisticated","unstable","unsure","unthinking","unwilling","versatile","vigilant","warm","warmhearted","watchful","weak","well-intentioned","well-respected","well-rounded","willing","wonderful","vulnerable","zealous","hottie","hater","meow"]

    def getPerson(self):
        return self.person

    def getReviewList(self):
        return self.reviewList

#Using a list of common adjectives used in review comments,
#finds the frequency of each word in the combined comments
#for the professor and lists these in descending order in a
#tuple (word, frequency). 
    def compareAdjs(self):
        allComments = ""
        tupleList = []
        wordList = self.wordList
        for rev in self.reviewList:
            allComments += rev.getComment()
        for word in wordList:
            if allComments.find(word) != -1:
                tupleList.append((word, allComments.count(word)))
        tupleList.sort(key=lambda tup: tup[1], reverse=True)
        return tupleList
                

#Counts the number of poor, average and good review scores
#the professor recieved and stores them in a tuple
#("Good", freq), ("Average", freq), ("Poor", freq)
    def sumOfPAGs(self):
        thisReviewList = self.reviewList
        numP = 0
        numA = 0
        numG = 0
        for rev in thisReviewList:
            if rev.getQuality() == "Poor": 
                numP = numP + 1
            elif rev.getQuality() == "Average":
                numA = numA + 1
            else:
                numG = numG + 1
        return [("Good", numG), ("Average", numA), ("Poor", numP)]

#Wishlist
    #Function to calculate 1-var stats/interpret spread of EHC ratings
    #Function to analyze spread of EHC over time
    #Compare to another professor or to school data
    #Compare to hogwarts professors because we can
    #Compare to department averages
    #Track hotness differential changes per review

