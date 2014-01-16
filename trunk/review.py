class Review:
    def __init__(self, DATE, QUALITY, EASINESS, HELPFULNESS, CLARITY, INTEREST, COMMENT):
        self.date = DATE
        self.quality = QUALITY
        self.easiness = EASINESS
        self.helpfulness = HELPFULNESS
        self.clarity = CLARITY
        self.interest = INTEREST
        self.comment = COMMENT

    def toString(self):
        print "Date: " , self.date
        print "Quality: " , self.quality
        print "Easiness: " , self.easiness
        print "Helpfulness: " , self.helpfulness
        print "Clarity: " , self.clarity
        print "Interest: " , self.interest
        print "Comment: " , self.comment

    def getDate(self):
        return self.date

    def getQuality(self):
        return self.quality

    def getEasiness(self):
        return self.easiness

    def getHelpfulness(self):
        return self.helpfulness

    def getClarity(self):
        return self.clarity

    def getInterest(self):
        return self.interest

    def getComment(self):
        return self.comment
