class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, user):
        if not 5 <= len(user) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = user
    # def __str__(self):
    #     return "You have a profile with username: "{self.username}" and password: "{'*' len(self.password)}".

profile_with_invalid_username = Profile('Too_long_userasdasda', 'Any') 
print(profile_with_invalid_username.username)