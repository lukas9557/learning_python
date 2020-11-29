#Automate the boring staff with Python book's exercise. Program should print grid, that it looks
#like heart
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

ny = len(grid) #9
nx = len(grid[0]) #6

for i in range(nx):
    for j in range(ny):
        print(grid[j][i],end="")
        if j == 8:
            print('\n')
