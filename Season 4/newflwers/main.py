import instaloader
import getpass

f = open('followers.txt', "r")
old_followers = []
for line in f:
    old_followers.append(line)
f.close()

L = instaloader.Instaloader()

username = input("enter your username: ")
password = getpass.getpass('enter your password: ')

L.login(username, password)
print("hooora!! successfully login!")

profile = instaloader.Profile.from_username(L.context, input("please enter an id: "))

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower)

for old_followers in old_followers:
    if old_followers not in new_followers:
        print("unfollowers: ", old_followers)

for new_follower in new_followers:
    if new_follower not in old_followers:
        print("newfollowers : ", new_followers)


f = open('followers.txt', 'w')
for follower in new_followers:
    f.write(follower + "/n")
f.close()
