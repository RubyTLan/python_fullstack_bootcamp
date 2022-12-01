class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name=last_name
        self.email=email
        self.age=age

        self.is_rewards_member=False
        self.gold_card_points=0

    def display_info(self):
        results=[self.first_name, self.last_name, self.email, str(self.age)]
        print("\n".join(results))

    def enroll(self):
        if self.is_rewards_member==True:
            print("User already a member")
            return False
        else:
            self.is_rewards_member=True
            self.gold_card_points=200

    def spend_points(self,amount):
        if self.gold_card_points<amount:
            return "Gold card points insufficient!"
        else:
            self.gold_card_points-=amount
            return self.gold_card_points


user1=User("Tian","Lan","l@gmail.com",31)

user1.display_info()
user1.enroll()
print(user1.is_rewards_member)
print(user1.gold_card_points)
print(user1.spend_points(20))
