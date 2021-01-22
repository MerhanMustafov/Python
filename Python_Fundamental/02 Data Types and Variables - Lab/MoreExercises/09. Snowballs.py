n = int(input())

the_highest = 0
h_snow = 0
h_time = 0
h_quality = 0
h_value = 0
for per_ball in range(n):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snow_value = int(snowball_snow / snowball_time) ** snowball_quality

    if snow_value >= the_highest:

        the_highest = snow_value
        h_snow = snowball_snow
        h_time = snowball_time
        h_quality = snowball_quality
        h_value = snow_value

print(f"{h_snow} : {h_time} = {h_value} ({h_quality})")

# n_snowball = int(input())
# max = 0
# max_snowball_value = 0
# max_snowball_snow = 0
# max_snowball_time = 0
# max_snowball_quality = 0
#
# for x in range(n_snowball):
#     snowball_snow = int(input())
#     snowball_time = int(input())
#     snowball_quality = int(input())
#
#     snowball_value = int(snowball_snow / snowball_time) ** snowball_quality
#
#     if snowball_value >= max:
#
#         max = snowball_value
#
#         max_snowball_value = snowball_value
#         max_snowball_snow = snowball_snow
#         max_snowball_time = snowball_time
#         max_snowball_quality = snowball_quality
#
# print(f"{max_snowball_snow} : {max_snowball_time} = {max_snowball_value} ({max_snowball_quality})")
