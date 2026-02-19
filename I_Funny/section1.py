class Section1:

    def __init__(self):
        self.title = ["LIGHTEN UP (section 1)","------------------------------"]
        self.contents = ['Technique 1','Techinque 2','Technique 3']
        self.ch1 = ["Anyone but Literal Larry!",
                   "literal, serious, and predictable comments are never",
                   "funny. Tap into your inner child and learn to play",
                   "more."]
        self.ch2 = ["Laugh at Yourself First",
                   "if you're too insecure and uptight, you'll have a hard",
                   "time making anyone laugh (even Jimmy Fallon---and",
                   "he laughs at everything).",
                   '',"If you want to be funny you must laugh at yourself first!"]
        self.ch3 = ["Dont be an energy vampire!",
                    "The difference between funny and 'meh,' and be-",
                    "tween engaging and unengagin, often comes down",
                    "to the nonverbal delivery of words and not the",
                    "words themselves",'',"The Energy you put in gets reflected by the other person!!!"]
        self.homework = ["Improve your energy and nonverbal delivery",
                    "There's no point in learning to be funny if you can't have good delivery!",
                    " ","Practice imitating masters like Aziz until you develop your own style.",
                    "Next, record yourself telling a story; listen and",
                    "watch how you deliver the words. Do this over",
                    "and over until you notice improvement and find",
                    "a style of delivery that works for your personality."]

    def getTitle(self):
        return self.title
    
    def getContents(self):
        return self.contents
    
    def getCh1(self):
        return self.ch1
    
    def getCh2(self):
        return self.ch2
    
    def getCh3(self):
        return self.ch3
    
    def getHome(self):
        return self.homework