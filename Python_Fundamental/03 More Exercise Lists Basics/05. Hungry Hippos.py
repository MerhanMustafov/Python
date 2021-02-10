the_rows_of_the_matrix = int(input())
lst_of_rows = []
for line in range(the_rows_of_the_matrix):
    row = input().split()
    row = list(map(int, row))
    lst_of_rows.append(row)

tracking_lst = 0
tracking_position = 0
final_counter = 0
for lst in range(len(lst_of_rows)):
    current_lst = lst_of_rows[tracking_lst]
    current_position = current_lst[tracking_position]
    if current_position == 1:
       if lst_of_rows[tracking_lst - 1][tracking_position] == 0 or lst_of_rows[tracking_lst - 1][tracking_position]== 1:
           if lst_of_rows[tracking_lst + 1][tracking_position] == 0:
               if lst_of_rows[tracking_lst][tracking_position + 1] == 0:
                   final_counter += 1
           if current_lst[tracking_position - 1] == 0:
    tracking_position += 1
    if current_position == 1 and current_position+1 == 0:
        print(0)



print(lst_of_rows)

