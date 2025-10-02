import random
from tkinter import messagebox
from players import Player
from AI_player import AI

class Game:
    def __init__(self, canvas,difficulty):
        self.player1 = Player(1, "blue")
        self.player2 = AI(difficulty)
        self.current_player = self.player1
        self.game_over = False
        self.cells_state = [["white" for _ in range(3)] for _ in range(3)]
        self.states_vector = [0] * 9
        self.canvas = canvas
        self.cells = []
        self.difficulty = difficulty
        self.button_back = False

    '''
    CREATE_MATRIX FOR UI ( APP)-------------------------------------------------------
    '''
    def create_game_matrix(self):
        cell_size = 170
        padding = 10
        matrix_start_x = 120
        matrix_start_y = 120

        self.cells_state = [["white" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            row_cells = []
            for col in range(3):
                x1 = matrix_start_x + col * (cell_size + padding)
                y1 = matrix_start_y + row * (cell_size + padding)
                x2 = x1 + cell_size
                y2 = y1 + cell_size

                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
                self.canvas.tag_bind(cell, "<Button-1>", lambda event, r=row, c=col: self.cell_click(r, c))
                row_cells.append(cell)
            self.cells.append(row_cells)
    '''
    DELETEING THE VISUAL MATRIX-------------------------------------------------------
    '''
    def delete_game_matrix(self):
        print("Deleting game matrix...")
        for row in self.cells:
            for cell in row:
                self.canvas.delete(cell) 
        self.cells = [] 
        print("Game matrix deleted.")
        
    '''
    IF IT WAS A CELL CLICK ION THE MATRIX -- PLAYER 1 - USER-------------------------------------------------------
    '''
    def cell_click(self, row, col):
        if self.game_over:
            return False
        if self.cells_state[row][col] != "white":
            return False
        if self.states_vector[row*3+col] != 0:
            return False
        if self.current_player != self.player1:
            return False

        self.cells_state[row][col] = self.player1.get_color()
        self.states_vector[row * 3 + col] = 1
        self.canvas.itemconfig(self.cells[row][col], fill=self.player1.get_color())

        if self.check_victory(self.player1.get_color()):
            self.game_over = True
            self.display_winner(self.player1.get_id())
            return True

        self.current_player = self.player2
        self.make_move_ai(self.difficulty)

        return True

    '''
    RESET THE GAME-------------------------------------------------------
    '''
    def reset_game_back(self):
        self.delete_game_matrix() 
        self.cells_state = [["white" for _ in range(3)] for _ in range(3)] 
        self.states_vector = [0] * 9
        self.current_player = self.player1 
        self.game_over = False
        self.create_game_matrix() 
        print("jocul a fost resetat pentru 'back'.")

    '''
    RESET FOR PLAY AGAIN-------------------------------------------------------
    '''
    def reset_game_play_again(self):
        self.delete_game_matrix() 
        self.cells_state = [["white" for _ in range(3)] for _ in range(3)] 
        self.states_vector = [0] * 9 
        self.game_over = False 
        self.current_player = self.player1 
        self.create_game_matrix() 
        print("jocul a fost resetat pentru 'play again'.")

    '''
        AI MANAGING THE MOVES DEPPENDING ON DIFFICULTY-------------------------------------------------------
    '''
    def make_move_ai(self, difficulty):

        if self.game_over or self.current_player != self.player2 or self.button_back == True:
            return False

        if difficulty == "easy":
            self.ai_make_move_easy()
        elif difficulty == "medium":
            self.ai_make_move_medium()
        elif difficulty == "hard":
            self.ai_make_move_hard()
        else:
            raise ValueError(f"Unknown difficulty level: {difficulty}")


        if self.check_victory(self.player2.get_color()):
            self.display_winner(self.player2.get_id())
            self.game_over = True

        if not self.game_over:
            self.current_player = self.player1

        return True

    '''
    DISPLAY THE WINNER WITH THE MESSAGE-------------------------------------------------------
    '''
    def display_winner(self, player_id):
        messagebox.showinfo("Game Over", f"Player {player_id} wins!")
        
        if player_id == self.player1.get_id():
            self.player1.increase_score()

        else:
            self.player2.increase_score()

    '''
    PLAYER 1 SCORE-------------------------------------------------------
    '''
    def get_player1_score(self):
        return self.player1.get_score()
    
    '''
    PLAYER 2 SCORE-------------------------------------------------------
    '''
    def get_player2_score(self):
        return self.player2.get_score()

    '''
    EASY AI-------------------------------------------------------
    '''
    def ai_make_move_easy(self):

        empty_cells = [(row, col) for row in range(3) for col in range(3) if self.states_vector[row * 3 + col] == 0]

        if empty_cells:
            row, col = random.choice(empty_cells)
            

            self.cells_state[row][col] = self.player2.get_color()
            self.states_vector[row * 3 + col] = -1 # AI cu -1 si player cu 1, altfel 0
            
    
            self.canvas.itemconfig(self.cells[row][col], fill=self.player2.get_color())

        
            self.current_player = self.player1
            
        
            if self.check_victory(self.player2.get_color()):
                self.game_over = True

        else:
           
            self.game_over = True
            messagebox.showinfo("Game Over", "It's a tie! (DRAW)")

    '''
    MEDIUM AI-------------------------------------------------------
    '''
    def ai_make_move_medium(self):
       
        if random.choice([True, False, False]): 
            self.ai_make_move_hard()
        else:
            self.ai_make_move_easy()

    '''
    HARD AI-------------------------------------------------------
    '''
    def ai_make_move_hard(self):
      
        best_score = float('-inf')
        best_move = None

        for row in range(3):
            for col in range(3):
                if self.states_vector[row * 3 + col] == 0: 
                    self.states_vector[row * 3 + col] = -1 
                    score = self.minimax(self.states_vector, False) 
                    self.states_vector[row * 3 + col] = 0 

                 
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

     
        if best_move:
            row, col = best_move
            self.states_vector[row * 3 + col] = -1 
            self.cells_state[row][col] = self.player2.get_color()  
            self.canvas.itemconfig(self.cells[row][col], fill=self.player2.get_color()) 
            self.current_player = self.player1

          
            if self.check_victory(self.player2.get_color()):
                self.game_over = True

    def minimax(self, board, is_maximizing):
 
        if self.check_victory(self.player2.get_color()):
            return 1 
        elif self.check_victory(self.player1.get_color()):
            return -1 
        elif all(cell != 0 for cell in board): 
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(9):
                if board[i] == 0: 
                    board[i] = -1 
                    score = self.minimax(board, False) 
                    board[i] = 0 
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == 0: 
                    board[i] = 1 
                    score = self.minimax(board, True) 
                    board[i] = 0 
                    best_score = min(score, best_score)
            return best_score

    '''
        CHECKING THE VICTORY-------------------------------------------------------
    '''
    def check_victory(self, player_color):
      
        for row in self.cells_state:
            if all(cell == player_color for cell in row):
                return True
        
     
        for col in range(3):
            if all(self.cells_state[row][col] == player_color for row in range(3)):
                return True
        
     
        if all(self.cells_state[i][i] == player_color for i in range(3)):
            return True
        
  
        if all(self.cells_state[i][2 - i] == player_color for i in range(3)):
            return True
        
        return False
    '''
    FINALLY  ALL GAME LOGICS IN ONLY ONE METHOD !!!!!!!!!!!!!!!!!!!!!!-------------------------------------------------------
    '''
    def all_game(self, difficulty, reset_scores=False):

        if reset_scores:
            self.player1.set_score(0)
            self.player2.set_score(0)

        # Inițializarea jocului
        self.reset_game_back()
        self.difficulty = difficulty
        self.current_player = self.player1 
        self.game_over = False

