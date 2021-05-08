first_lst = input().split(", ")
second_lst = input().split(", ")
final_list = [w1 for w1 in first_lst for w2 in second_lst if w1 in w2]
final_list = list(dict.fromkeys(final_list))
# for word_first_lst in first_lst:
#     for word_second_lst in second_lst:
#         if word_first_lst in word_second_lst:
#             if word_first_lst in final_list:
#                 continue
#             final_list.append(word_first_lst)


print(final_list)
