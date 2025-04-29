class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player1_name = ""
        self.player2_name = ""
        self.player1_symbol = ''
        self.player2_symbol = ''
        self.current_player_symbol = ''
        self.current_player_name = ""
        self.game_status = 'running'
        self.num_moves = 0

    def display_board(self):
        print("\n  0 1 2")
        print("-------")
        for i, row in enumerate(self.board):
            print(f"{i} | {' '.join(row)} |")
        print("-------")

    def get_player_names(self):
        self.player1_name = input("הזן את שם השחקן הראשון: ")
        self.player2_name = input("הזן את שם השחקן השני: ")

    def choose_symbols(self):
        while True:
            symbol1 = input(f"{self.player1_name}, בחר את הסימן שלך (X או O): ").upper()
            if symbol1 in ['X', 'O']:
                self.player1_symbol = symbol1
                self.player2_symbol = 'O' if symbol1 == 'X' else 'X'
                print(f"{self.player2_name} שלך הוא הסימן: {self.player2_symbol}")
                break
            else:
                print("בחירה לא חוקית. אנא בחר 'X' או 'O'.")
        self.current_player_symbol = self.player1_symbol
        self.current_player_name = self.player1_name

    def is_valid_move(self, row, col):
        try:
            row = int(row)
            col = int(col)
            if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
                return True
            else:
                return False
        except ValueError:
            return False

    def make_move(self, row, col):
        row = int(row)
        col = int(col)
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player_symbol
            self.num_moves += 1
            return True
        else:
            print("מהלך לא חוקי. אנא בחר שורה ועמודה קיימים וריקים.")
            return False

    def check_win(self, player_symbol):
        # בדיקה לפי שורות
        for row in self.board:
            if all(cell == player_symbol for cell in row):
                return True
        # בדיקה לפי עמודות
        for col in range(3):
            if all(self.board[row][col] == player_symbol for row in range(3)):
                return True
        # בדיקה לפי אלכסונים
        if (self.board[0][0] == player_symbol and self.board[1][1] == player_symbol and self.board[2][2] == player_symbol) or \
           (self.board[0][2] == player_symbol and self.board[1][1] == player_symbol and self.board[2][0] == player_symbol):
            return True
        return False

    def is_board_full(self):
        return self.num_moves == 9

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.game_status = 'running'
        self.num_moves = 0
        self.current_player_symbol = self.player1_symbol
        self.current_player_name = self.player1_name

    def switch_player(self):
        if self.current_player_symbol == self.player1_symbol:
            self.current_player_symbol = self.player2_symbol
            self.current_player_name = self.player2_name
        else:
            self.current_player_symbol = self.player1_symbol
            self.current_player_name = self.player1_name

    def run_game(self):
        self.get_player_names()
        self.choose_symbols()
        self.display_board()

        while self.game_status == 'running':
            print(f"\nתורו של {self.current_player_name} ({self.current_player_symbol})")
            row = input("הזן מספר שורה (0-2): ")
            col = input("הזן מספר עמודה (0-2): ")

            if self.make_move(row, col):
                self.display_board()

                if self.check_win(self.current_player_symbol):
                    print(f"מזל טוב, {self.current_player_name} ניצח!")
                    self.game_status = 'win'
                elif self.is_board_full():
                    print("תיקו!")
                    self.game_status = 'draw'
                else:
                    self.switch_player()
            # If the move is not valid, the loop continues for the same player

        self.play_again_prompt()

    def main_menu(self):
        while True:
            print("\n--- תפריט ראשי - איקס עיגול ---")
            print("1. התחל משחק חדש")
            print("2. צא")
            choice = input("בחר אפשרות (1-2): ")

            if choice == '1':
                self.reset_game()
                self.run_game()
            elif choice == '2':
                print("תודה ששיחקת!")
                break
            else:
                print("בחירה לא חוקית. אנא בחר 1 או 2.")

    def play_again_prompt(self):
        while True:
            choice = input("רוצה לשחק שוב? (כן/לא): ").lower()
            if choice == 'כן':
                self.reset_game()
                self.run_game()
                break
            elif choice == 'לא':
                print("תודה ששיחקת!")
                break
            else:
                print("בחירה לא חוקית. אנא הקלד 'כן' או 'לא'.")

if __name__ == "__main__":
    game = TicTacToe()
    game.main_menu()