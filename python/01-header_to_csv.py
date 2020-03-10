FILE='../data/ipl/README.txt'
lines=[]
with open(FILE) as f:
    lines = f.readlines()

BEGINNING_LINE=24
teams=set()
for line in lines[BEGINNING_LINE:]:
    [team1, team2] = line.split(" - ")[5].split('\n')[0].split(' vs ')
    teams.add(team1)
    teams.add(team2)

print(teams)

# By inspection, map each team name to a team_id.
# The team_id is the name that teams are commonly known as, e.g. "KKR".
team_id_mapping = {
    'Royal Challengers Bangalore': 'RCB',
    'Rising Pune Supergiants': 'RPS',
    'Rising Pune Supergiant': 'RPS',
    'Sunrisers Hyderabad': 'SRH',
    'Chennai Super Kings', 'CSK',
    'Gujarat Lions': 'GL',
    'Rajasthan Royals': 'RR',
    'Deccan Chargers': 'DC',
    'Kolkata Knight Riders': 'KKR',
    'Mumbai Indians': 'MI',
    'Delhi Capitals': 'DCI',
    'Pune Warriors': 'PWI',
    'Kings XI Punjab': 'KXIP',
    'Kochi Tuskers Kerala': 'KTK',
    'Delhi Daredevils': 'DD'
}