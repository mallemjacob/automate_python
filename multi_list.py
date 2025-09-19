# spam = ['cat','bat','fat','mat']

# multi_spam = [['cat','fat'],['elephant','dog']]

# print(multi_spam[0][1])
# print(multi_spam[1][1])


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for i in range(len(grid[0])): #0, 0, 0
    for j in range(len(grid)): #0, 1, 2
        print(grid[j][i],end='') #[0,0], [1,0], [2,0]
    print()
               
# ..OO.OO..
# .OOOOOOO.
# .OOOOOOO.
# ..OOOOO..
# ...OOO...
# ....O....

# for i in range(len(grid)): #0, 0
#     for j in range(len(grid[i])): #0, 1
#         print(grid[i][j],end='')
#     print()
# 