n=int(input())  #2. Snake
s=[]
b=[]
matrix=[]
for j in range(n):
    row=list(input())
    matrix.append(row)
    if 'S' in row:
        s.append([j,row.index('S')])
    if 'B' in row:
        b.append([j,row.index('B')])
moves={'up':(-1,0),'down':(1,0),'left':(0,-1),'right':(0,1)}
food=0
while True:
    move=input()
    next_row=s[0][0]+moves[move][0]
    next_col = s[0][1] + moves[move][1]
    matrix[s[0][0]][s[0][1]]='.'
    if 0<=next_row<n and 0<=next_col<n:
        if matrix[next_row][next_col]=='*':
            food+=1
            matrix[next_row][next_col]='S'
            s=[[next_row,next_col]]
            if food>=10:
                print("You won! You fed the snake.")
                break
        elif matrix[next_row][next_col]=='B':
            if matrix[next_row][next_col]==matrix[b[0][0]][b[0][1]]:
                matrix[b[1][0]][b[1][1]]='S'
                s=[[b[1][0],b[1][1]]]
            else:
                matrix[b[0][0]][b[0][1]] = 'S'
                s = [[b[0][0], b[0][1]]]
            matrix[next_row][next_col] = '.'
        else:
            matrix[next_row][next_col] = 'S'
            s=[[next_row,next_col]]
    else:
        print('Game over!')
        break
print(f'Food eaten: {food}')
print('\n'.join(''.join(i) for i in matrix))