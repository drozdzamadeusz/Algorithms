a = ""
if not a:
    print("aaa")

board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]


choices = [[i for i in range(len(board[0]))], [i for i in range(len(board))]]


print(choices)