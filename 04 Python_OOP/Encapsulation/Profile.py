class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_upper(self, value):
        is_upper = [el for el in value if el.isupper()]
        if is_upper:
            return True
        return False

    def is_digit(self, value):
        is_digit = [el for el in value if el.isdigit()]
        if is_digit:
            return True
        return False

    @property
    def username(self):

        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) < 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if not len(value) >= 8 or\
            not self.is_upper(value) or\
            not self.is_digit(value):
            raise ValueError("The password must be 8 or more characters"
                             " with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f"You have a profile with username: \"{self.username}\" and password: {'*'*len(self.password)}"



# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)





































# def password(password):
#     return ["*" for x in range(len(password))]
#
# class Profile:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#     @property
#     def username(self):
#         return self.__username
#
#     @username.setter
#     def username(self, user):
#         if not 5 <= len(user) <= 15:
#             raise ValueError("The username must be between 5 and 15 characters.")
#         self.__username = user
#     @property
#     def password(self):
#         return self.__password
#     @password.setter
#     def password(self, password):
#         digit = [x for x in password if x.isdigit()]
#         upper_case = [x for x in password if x.isupper()]
#         if not (len(password) >= 8 and digit and upper_case):
#             raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
#         self.__password = password
#
#
#
#     def __str__(self):
#         p = "".join(password(self.__password))
#         return f'You have a profile with username: "{self.username}" and password: {p}'
#
#
#
# # profile_with_invalid_username = Profile('Too_long_userasdasda', 'Any')
# # print(profile_with_invalid_username.username)
# # correct_profile = Profile("Username", "Passw0rd")
# # print(correct_profile)
#
# # profile_with_invalid_password = Profile('My_username', 'My-password')