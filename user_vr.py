class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name= first_name
        self.last_name= last_name
        self.email= email
        self.age= age
        self.is_rewards_member=False
        self.gold_card_points=0

def display_info(self):
	print(f"Customer {self.first_name} {self.last_name}'s email address is {self.email}. They are {self.age} years old.")

def enroll(self):
	self.is_rewards_member=True
	self.gold_card_points=200
	print(f"Customer {self.first_name} {self.last_name}'s email address is {self.email}. They are {self.age} years old and they have {self.gold_card_points} new gold card points.")

def spend_points(self,amount):
	self.gold_card_points -= amount
	print(f"{self.first_name} now has {self.gold_card_points} gold card points.")



monger=User('Attilla', 'Hun', 'a.hun@mail.com', 42)
display_info(monger)   #not sure if with print
enroll(monger)

tator=User('Adolf', 'Hitler', 'a.hitler@mail.com', 18)
statistic=User('Josef', 'Stalin', 'j.stalin@mail.com', 52)

spend_points(monger,50)

enroll(tator)
spend_points(tator,80)

display_info(monger)
display_info(tator)
display_info(statistic)
