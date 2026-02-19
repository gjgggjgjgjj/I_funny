class Games:
    
    def __init__(self):
        self.title = ["GAMES [0]","------------------------------"]
        self.contents = ["* Exagerate!, game [0]","* Painting more with Details!, game [1]","* Painting more with Metaphors!, game [2]","* Stick A label to It!, game [3]","* (More is still in development)"]
        self.exagerate = {"I have a lot of work to do":["I have so much work to do, it feels like I'm trying to move a mountain with a teaspoon"],"It's a warm day":["It's so warm outside that the pavement is melting into a river of lava"],
                          "I'm feeling a bit tired":["I'm so tired that if I lie down, I might hibernate until next year"],"My backpack is heavy":["My back pack is so heavy that it's like carrying a ton of bricks on my shoulders"],
                          "I'm hungry":["I'm so hungry that I could devour an entire pizza, plus a mountain of ice cream for dessert"],"There's a lot of traffic today":["There's so much traffic that it's as if the entire world decided to have a parade on this road"],
                          "This line is long":["The line is so long that I think I'll have time to write a novel before reaching the front"],"It's raining lightly":["It's raining so heavily that it's as if the sky opened up and dumped an ocean on us"],
                          "I have a few missed calls":["I have so many missed calls that my phone might as well be a hotline for the entire planet"],"I have some things to carry":["I have so many things to carry that it's like I'm lugging around a circus tent and elephant"],
                          "I need a break":["I need a break so desperately that it's as if I've been running a marathon on the sun"],"The queue is moving slowly":["The queue is moving so slowly that a sloth on a leisurely stroll would beat us to the finish line"],
                          "I have a few emails to answer":["I have so many emails to answer that it's like trying to swim through an ocean of messages"],"The coffee is strong":["The coffee is so strong that it could wake the dead and grant them superpowers"],
                          "My phone battery is low":["My phone battery is so low that it's on life support and clinging to existence"],"The room is dark":["The room is so dark that it feels like a black hole in here, swallowing all the light."],
                          "I'm running late":["I'm running so late that I'll be arriving at the speed of a snail with a broken leg"],"I'm a bit stressed":["I'm so stressed that it's as if I'm juggling a dozen chainsaws while tightrope-walking over a volcano"],
                          "The music is loud":["I have so many errands to run that it's like I've become the personal assistant for the entire town"],"I need to clean my room":["I need to clean my room so badly that it resembles a post-apocalyptic wasteland"],
                          "I'm a little stressed about the test":["I'm so stressed about the test that I feel like I'm preparing for a cosmic battle against an army of exam demons"],"I have a few notifications on my phone":["I have so many notifications on my phone that it's like a digital fireworks display that never ends"],
                          "The traffic is congested":["The traffic is so congested that it's like a parking lot for time travelers from the 22nd century"],"I've got a small problem":["I've got such a colossal problem that it's like dealing with an erupting volcano in my backyard"],
                          "The room is a little chilly":["The room is so chilly that it's like I've been transported to the frozen tundra of Antarctica"]}
        self.stickLabel = {"Vehicle Description": ["We drive a soccer mom's dream van."],
                        "Personality Description": ["I'm a total tech geek, computer wizard."],
                        "Home Description": ["My place is like a cozy log cabin."],
                        "Favorite Food Description": ["My favorite dish is the classic comfort food, mac 'n' cheese."],
                        "Hobbies Description": ["My hobbies are like a whirlwind of adventure and adrenaline."],
                        "Job Description": ["I work in the concrete jungle as a number-crunching spreadsheet warrior."],
                        "Morning Routine Description": ["My morning routine is as chaotic as a circus juggling act."],
                        "Friend Description": ["My friends are a bunch of movie buffs and popcorn connoisseurs."],
                        "Weekend Description": ["My weekends are like a Netflix marathon of relaxation."],
                        "Style of Dressing Description": ["My style is as colorful as a peacock's tail."],
                        "Travel Destination Description": ["I'm heading to a tropical paradise, a beach bum's heaven."],
                        "Favorite Book Description": ["My favorite book is an epic fantasy, a doorstopper of a read."],
                        "Music Genre Description": ["I'm all about classic rock, a time-traveling air guitarist."],
                        "Pet Description": ["My pet is a furry tornado, a living, breathing furball."],
                        "Coffee Order Description": ["My coffee order is like a sugar overdose, a caramel macchiato with extra whipped cream."],
                        "Holiday Celebration Description": ["Our holiday celebration is a family comedy show, a chaotic mix of laughter and chaos."],
                        "Cooking Style Description": ["My cooking style is like a mad scientist, an experiment in every dish."],
                        "Fitness Routine Description": ["My fitness routine is a workout warrior's dream, a daily sweat-soaked boot camp."],
                        "Dream Job Description": ["My dream job is a creative playground, a lifelong imagination expedition."],
                        "TV Show Description": ["My favorite TV show is like a binge-watcher's paradise, a gripping suspense rollercoaster."],
                        "Favorite Movie Description": ["My favorite movie is an emotional rollercoaster, a tearjerker with a happy ending."],
                        "Vacation Spot Description": ["My ideal vacation spot is a postcard paradise, a tranquil beach with crystal-clear waters."],
                        "Social Media Habits Description": ["My social media habits are like a digital nomad, a constant journey through posts and stories."],
                        "Personality Trait Description": ["One of my personality traits is like a ray of sunshine, a perpetual optimist."],
                        "Gardening Style Description": ["My gardening style is a green thumb's fantasy, a jungle of blooms and vegetables."],
                        "Morning Beverage Description": ["My morning beverage is like a hug in a mug, a warm and comforting cup of coffee."],
                        "Neighborhood Description": ["My neighborhood is like a small-town movie set, a close-knit community with a touch of nostalgia."],
                        "Computer Usage Description": ["My computer usage is like a digital wizard, a multitasking maestro with a thousand tabs open."],
                        "Vacation Activity Description": ["My favorite vacation activity is like a kid in a candy store, an adventure seeker exploring new places."],
                        "Art Style Description": ["My art style is like a colorful dream, a canvas filled with vibrant, abstract expressions."]
                        }








    def getTitle(self):
        return self.title
    
    def getContents(self):
        return self.contents
    
    def getExagerate(self):
        return self.exagerate
    
    def addToExagerate(self,key,example):
        if example:
            self.exagerate[key].append(example)
            # Open a file in append mode ('a')
            with open('colorExagerate.txt', 'a') as file:
                # Append the user's input to the file
                file.write(example + '\n') 
    
    #stick label game methods
    def getStickLabel(self):
        return self.stickLabel
    
    def addToStickLabel(self,key,example):
        if example:
            self.stickLabel[key].append(example)
            # Open a file in append mode ('a')
            with open('colorLabel.txt', 'a') as file:
                # Append the user's input to the file
                file.write(example + '\n') 
        