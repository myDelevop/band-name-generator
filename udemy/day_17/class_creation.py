class UserTmp:
    pass


user_1 = UserTmp()
user_1.id = "001"
user_1.username = "Rocco"

print(user_1.username)

user_2 = UserTmp()
user_2.id = "002"
user_2.username = "Jack"

print(user_2.id)


# Much Better to use constructors with __init__(self)

class User:
    def __init__(self, user_id, username):
        print("New user has been created")
        self.id = user_id
        self.username = username
        self.followers = 0  # default values
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


new_user_1 = User("128", "Angela")
print(new_user_1.id + " " + new_user_1.username + " " + str(new_user_1.following) + " " + str(new_user_1.followers))

new_user_2 = User("241", "Gianni")

new_user_1.follow(new_user_2)
print(new_user_1.id + " " + new_user_1.username + " " + str(new_user_1.following) + " " + str(new_user_1.followers))
print(new_user_2.id + " " + new_user_2.username + " " + str(new_user_2.following) + " " + str(new_user_2.followers))
