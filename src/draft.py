# m, y, row
# n, x, column
# board[y][x]
# board[row - 1][column - 1]

def pre_main(itertools):
    def main(players, ask_user):
        def pre_game(m, n, k):
            def game(board):
                def make_move(player):
                    def process_move(y, x):
                        def check_victory(direction):
                            def count(dx, dy):
                                return len([*itertools.takewhile(lambda delta: (
                                        0 <= x + dx * delta < m and
                                        0 <= y + dy * delta < n and
                                        board[y + dy * delta][x + dx * delta] == player
                                ), itertools.count(1))])

                            return count(*direction) + count(-direction[0], -direction[1]) >= k - 1

                        return (board[y].__setitem__(x, player) or
                                all(all(map('.'.__ne__, row)) for row in board) and "Draw!" or
                                any(map(check_victory, [(0, 1), (1, 0), (1, 1), (1, -1)])) and f"Player {player} won!")

                    def validate_move(row, column):
                        return (column < 1 and "Column should be >= 1" or
                                row < 1 and "Row should be >= 1" or
                                column > n and f"Column should be <= {n}" or
                                row > m and f"Row should be <= {m}" or
                                board[row - 1][column - 1] != '.' and "This cell is already occupied")

                    def format_board():
                        return "\n".join(''.join(row) for row in board)  # todo: row and column numbers

                    return print(format_board()) or process_move(*(
                        c - 1 for c in ask_user(f"Player {player}, please, enter row and column", validate_move)
                    ))
                    # end make_move

                return next(itertools.dropwhile(lambda a: not a, map(make_move, players)))
                # end game

            return game([['.'] * n for _ in range(m)])
            # end pre_game

        def validate_mnk(m, n, k):
            return (min(m, n, k) <= 0 and "M, N, and K should be >0") or \
                   (k > max(m, n) and "K should not be bigger than both M and N")

        return pre_game(*ask_user("Enter MNK (M is height, N is width, K is the length of the winning sequence)",
                                  validate_mnk))
        # end main

    def print_if_not_false_and_return(something):
        return (print(something) if something else something) or something

    return main(
        itertools.cycle('XO'),
        lambda query, get_error: next(itertools.dropwhile(
            lambda t: print_if_not_false_and_return(get_error(*t)),
            ([*map(int, input(f"{query}:\n").split())] for _ in itertools.count())
        )))
    # end pre_main


if __name__ == '__main__':
    print(pre_main(__import__("itertools")))
