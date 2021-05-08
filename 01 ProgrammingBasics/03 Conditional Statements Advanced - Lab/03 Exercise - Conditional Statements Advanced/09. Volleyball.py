# •	Първият ред съдържа думата "leap" (високосна година) или "normal" (невисокосна);
# •	Вторият ред съдържа цялото число p – брой празници в годината (които не са събота и неделя);
# •	Третият ред съдържа цялото число h – брой уикенди, в които Влади си пътува до родния град.
from math import floor

type_of_year = input()
holidays = int(input())
weekends = int(input())

if type_of_year == 'leap':
    total_weekends = 48
    in_sofia = (total_weekends - weekends) * (3 / 4)
    holidays_1 = holidays * (2 / 3)
    result = in_sofia + weekends + holidays_1
    result_2 = result * 0.15
    result_3 = floor(result + result_2)
    print(result_3)
elif type_of_year == 'normal':
    total_weekends = 48
    in_sofia = (total_weekends - weekends) * (3 / 4)
    holidays_1 = holidays * (2 / 3)
    result = in_sofia + weekends + holidays_1
    print(floor(result))
