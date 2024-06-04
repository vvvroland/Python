players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]
"""
def single_player():
    for dict in players:
        print(dict)
        return dict
    
for x in players:
    print(x['name'])
"""


class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]

new_team=[]
for roster in players:
    #new_person=[]
    #for head in roster:
        #new_person.append(roster[head])
    new_person=Player(roster)
    new_team.append(new_person)

print(new_team)        


"""
kevin=Player(players[0]["name"], players[0]["age"], players[0]["position"], players[0]["team"])
jason=Player(players[1]["name"], players[1]["age"], players[1]["position"], players[1]["team"])
kyrie=Player(players[2]["name"], players[2]["age"], players[2]["position"], players[2]["team"])
damian=Player(players[3]["name"], players[3]["age"], players[3]["position"], players[3]["team"])
joel=Player(players[4]["name"], players[4]["age"], players[4]["position"], players[4]["team"])
demar=Player(players[5]["name"], players[5]["age"], players[5]["position"], players[5]["team"])
"""

"""
demian = {
    "name": "Damian Lillard", 
    "age":33,
    "position": "Point Guard", 
    "team": "Portland Trailblazers"
}

joel = {
    "name": "Joel Embiid", 
    "age":32,
    "position": "Power Foward", 
    "team": "Philidelphia 76ers"
}

deMar = {
    "name": "DeMar DeRozan",
    "age": 32,
    "position": "Shooting Guard",
    "team": "Chicago Bulls"
}
"""