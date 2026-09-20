#PROBLEM 3
import csv
def add_user(sn, username, fullname):
    '''Adds a tuple (fullname, []) with an empty friends array into the dictionary sn with key username'''
    if username not in sn:
        sn[username] = (fullname, [])
        return True
    else: return False

def add_friend(sn, user1, user2):
    '''Adds user1 and user2 to each others friend arrays and returns True. If either is not found in dictionary sn returns False'''
    #check user1 and user2 exist in dict, and also check that they are not already friends
    if user1 in sn and user2 in sn and user1 not in sn[user2][1]:
        sn[user1][1].append(user2)
        sn[user2][1].append(user1)
        return True
    else: return False

def get_friends(sn, user1, distance):
    '''Gets the friend array of user1 in dictionary sn, and the friends of friends for distance > 1'''
    if user1 in sn and distance > 0:
        friends = sn[user1][1].copy()
        if friends != []:
            dist = 1
            #checked friends set saves time by caching already checked keys to not check them again
            checked_friends = set()
            while dist < distance:
                newfriends = []
                for friend in friends:
                    if friend not in checked_friends:
                        newfriends += sn[friend][1]
                        checked_friends.add(friend)
                friends += newfriends
                #clear duplicate friends
                friends = list(set(friends) - {user1})
                dist += 1
        return friends
    else: return [] 

def save_network(filename, sn):
    '''saves dictionary sn to a csv file filename'''
    try:
        with open(filename, "w") as outfile:
            writer = csv.writer(outfile)
            #break apart each entry in dict sn
            for username, (full_name, friends) in sn.items():
                writer.writerow([username, full_name] + friends)
    except IOError as err:
        print(f"An error has occurred! Error type: {err}")
        raise

def load_network(filename):
    '''takes a social network from a csv file at filename and returns a dictionary'''
    try:
        sn = {}
        with open(filename, "r") as infile:
            reader = csv.reader(infile)
            for row in reader:
                if row:
                    sn[row[0]] = (row[1], row[2:])
        return sn
    except IOError as err:
        print(f"An Error Occured! File {filename} not found")
        raise

def main():
    sn = {}
    add_user(sn, "alice", 'Alice Smith')
    add_user(sn, 'maria', 'Maria Cortez')
    add_user(sn, 'joe', 'Joseph Adams')
    add_user(sn, 'eve', 'Evelyn Cooper')
    add_user(sn, 'david', 'David Benson')

    add_friend(sn, 'alice', 'maria')
    add_friend(sn, 'maria', 'joe')
    add_friend(sn, 'maria', 'david')
    add_friend(sn, 'joe', 'eve')

    print(get_friends(sn, 'alice', 1))
    print(get_friends(sn, 'alice', 2))

    save_network('Homework2/network.csv', sn)
    print(load_network('Homework2/network.csv'))
    print("ERIC LEOCADIO Z23712790")

if __name__ == "__main__":
    main()