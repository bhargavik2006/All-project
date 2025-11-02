# class User:
#     def __init__(self):
#         print("new use being created...")
# user_1=User()
# user_1.id="001"
# user_1.username="bhagu"
# print(user_1.id)
# user_2=User()
# user_2.id="002"
# user_2.username="kharvi"
# print(user_2.id)


# **************************************************************
class User:
    def __init__(self, id, username):
        self.id=id
        self.username=username
        self.follower=0
        self.following=0

    def follow(self,user):#METHOD
        user.follower+=1
        self.following+=1


user_1=User("001","bhargavi")
user_2=User("002","bhargavik")
# print(user_1.follower)
user_1.follow(user_2)
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)