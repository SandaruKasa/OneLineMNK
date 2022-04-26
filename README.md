# What is this?

This is the MNK game (Tic-Tac-Toe but the field is M by N celss and the length of the winning sequence of X/O is K)
implemented as a single line of Python code. No `exec`/`eval` magic or escaping newline characters. Truly an FP-style hell.

# Why is this?

This was created for a ridiculous game jam where you had to write a game as one line of python code (not exceeding 4KB).
`exec` and `eval` were banned, so you really had to cover yourself with lambdas.

# How is this?

This was some hard to debug code written in one line using only lambdas, so at first I wrote
a [draft using regular python](src/draft.py), but in a manner that would allow me to easily inline variables and lambda
equivalents of the defined functions. The result of this can be found in [this file](src/one_line.py) and that's
probably what you want to look at.

# How to run this?
Well, you can just evaluate
```python
_ = X
```
in interactive mode where `X` is all the code from [this file](src/one_line.py).

Like this:
```python
_ = print((lambda itertools, math: (lambda players, ask_user: (lambda m, n, k: (lambda board, format_board: next(itertools.dropwhile(lambda a: not a, map((lambda player: print(format_board(board)) or (lambda y, x: (board[y].__setitem__(x, player) or all(all(map('.'.__ne__, row)) for row in board) and f"{format_board(board)}\n\nDraw!" or any(map(lambda direction: ((lambda count: count(*direction) + count(-direction[0], -direction[1]) >= k - 1)(lambda dx, dy: len([*itertools.takewhile(lambda delta: (0 <= x + dx * delta < n and 0 <= y + dy * delta < m and board[y + dy * delta][x + dx * delta] == player), itertools.count(1))]))), [(0, 1), (1, 0), (1, 1), (1, -1)])) and f"{format_board(board)}\n\nPlayer {player} won!"))(*(c - 1 for c in ask_user(f"Player {player}, please, enter row and column", (lambda row, column: column < 1 and "Column should be >= 1" or row < 1 and "Row should be >= 1" or column > n and f"Column should be <= {n}" or row > m and f"Row should be <= {m}" or board[row - 1][column - 1] != '.' and "This cell is already occupied"))))), players))))([['.'] * n for _ in range(m)], lambda board: "\n".join(' '.join(map(("{:>" + str(math.floor(math.log(max(m, n), 10) + 1)) + "}").format, [row_no] + ([[*range(1, n + 1)]] + board)[row_no])) for row_no in range(m + 1))))(*ask_user("Enter MNK (M is height, N is width, K is the length of the winning sequence)", (lambda m, n, k: (min(m, n, k) <= 0 and "M, N, and K should be >0") or (k > max(m, n) and "K should not be bigger than both M and N")))))(itertools.cycle('XO'), lambda query, get_error: next(itertools.dropwhile(lambda t: (lambda something: (print(something) if something else something) or something)(get_error(*t)), ([*map(int, input(f"{query}:\n").split())] for _ in itertools.count())))))(__import__("itertools"), __import__("math")))
```
