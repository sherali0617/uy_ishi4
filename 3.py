import os
os.system("cls")

class User:
    def __init__(self, username: str):
        self.username = username
        self.friends = []

    def add_friend(self, friend: str) -> bool:
        if friend in self.friends:
            return False
        self.friends.append(friend)
        return True

    def remove_friend(self, friend: str) -> bool:
        if friend in self.friends:
            self.friends.remove(friend)
            return True
        return False

    def list_friends(self) -> list:
        return self.friends

    def is_friend(self, friend: str) -> bool:
        return friend in self.friends

    def mutual_friends(self, other_user: 'User') -> list:
        return [f for f in self.friends if f in other_user.friends]


user1 = User("Ali")
user2 = User("Vali")

print(user1.add_friend("Sami"))     
print(user1.add_friend("Vali"))   
print(user1.add_friend("Sami"))   

print(user2.add_friend("Ali"))      
print(user2.add_friend("Sami"))    

print(user1.list_friends())        
print(user2.list_friends())         

print(user1.is_friend("Vali"))    
print(user1.is_friend("Botir"))    
print(user1.mutual_friends(user2))  

print(user1.remove_friend("Vali"))
print(user1.remove_friend("Botir"))
print(user1.list_friends())       