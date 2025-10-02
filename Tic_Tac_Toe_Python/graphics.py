import tkinter as tk
from PIL import Image, ImageTk
from game_logics import Game
from AI_player import AI
from players import Player
class App:
    def __init__(self, root):
        self.root = root
        self.root.resizable(False, False)
        self.root.geometry("800x800")
        
        self.bckgrd = Image.open("images/background_image1.jpg")
        self.bckgrd = ImageTk.PhotoImage(self.bckgrd)
        
        self.button_font = ("Arial", 26)
        self.button_width = 20
        self.button_height = 2
        self.button_fg = "black"
        self.button_bg = "Gainsboro"
        self.button_bg_exit = "red"
        self.button_fg_exit = "white"
        self.label_fg = "white"
        self.label_bg = "DimGray"
        self.label_fg_score1 = "white"
        self.label_bg_score1 = "DarkBlue"
        self.label_fg_score2 = "white"
        self.label_bg_score2 = "DarkRed"
        self.start = self.create_start()
        self.game = self.create_game()
        self.change_theme = self.create_change_theme()
        self.how_to_play = self.create_how_to_play()
        self.easy = self.create_easy()
        self.medium = self.create_medium()
        self.hard = self.create_hard()
        self.show_screen(self.start)
    '''
    MENU OF THE GAME WITH THE MAIN FRAME-------------------------------------------------------
    '''
  
    def create_start(self):
        frame = tk.Frame(self.root)
        canvas = tk.Canvas(frame, width=800, height=800)
        canvas.pack(fill="both", expand=True)

        self.background_canvas_start = canvas
        canvas.create_image(0, 0, image=self.bckgrd, anchor="nw", tags="background")
        
        label = tk.Label(frame, text="WELCOME TO TIC-TAC-TOE", 
                         font=("Cascadia Code Light", 32, "bold"),
                         pady=50, fg=self.label_fg, bg=self.label_bg)
        canvas.create_window(400, 100, window=label)

        start_button = tk.Button(frame, text="START NEW GAME",
                                 command=lambda: self.show_screen(self.game), font=self.button_font, 
                                 width=self.button_width, height=self.button_height, fg=self.button_fg,
                                   bg=self.button_bg)
        canvas.create_window(400, 250, window=start_button)

        change_theme_button = tk.Button(frame, text="CHANGE THEME", command=lambda: self.show_screen(self.change_theme), font=self.button_font, width=self.button_width, height=self.button_height, fg=self.button_fg, bg=self.button_bg)
        canvas.create_window(400, 400, window=change_theme_button)

        how_to_play_button = tk.Button(frame, text="HOW TO PLAY", command=lambda: self.show_screen(self.how_to_play), font=self.button_font, width=self.button_width, height=self.button_height, fg=self.button_fg, bg=self.button_bg)
        canvas.create_window(400, 550, window=how_to_play_button)

        exit_button = tk.Button(frame, text="EXIT GAME", command=self.root.quit, font=self.button_font, width=self.button_width, height=self.button_height, fg=self.button_fg_exit, bg=self.button_bg_exit)
        canvas.create_window(400, 700, window=exit_button)

        return frame
    
    '''GAME DIFFICULTIES IF U PRESS START BUTTON ----------------------------------------------------------------------------------'''
    def create_game(self):
        frame = tk.Frame(self.root)
        canvas = tk.Canvas(frame, width=800, height=800)
        canvas.pack(fill="both", expand=True)

        self.background_canvas_game = canvas
        canvas.create_image(0, 0, image=self.bckgrd, anchor="nw", tags="background")

        label = tk.Label(frame, text="SELECT GAME DIFFICULTY", font=("Cascadia Code Light", 32, "bold"), fg=self.label_fg, bg=self.label_bg)
        canvas.create_window(400, 100, window=label)

        easy_button = tk.Button(frame, text="EASY", command=lambda: self.show_screen(self.easy), font=self.button_font, width=self.button_width, height=self.button_height, fg=self.button_fg, bg=self.button_bg)
        canvas.create_window(400, 250, window=easy_button)

        medium_button = tk.Button(frame, text="MEDIUM", command=lambda: self.show_screen(self.medium), font=self.button_font, width=self.button_width, height=self.button_height, fg=self.button_fg, bg=self.button_bg)
        canvas.create_window(400, 400, window=medium_button)

        hard_button = tk.Button(frame, text="HARD", command=lambda: self.show_screen(self.hard), font=self.button_font, width=self.button_width, height=self.button_height, fg=self.button_fg, bg =self.button_bg)
        canvas.create_window(400, 550, window=hard_button)

        back_button = tk.Button(frame, text="BACK", command=lambda: self.show_screen(self.start), font=self.button_font, width=self.button_width, height=self.button_height, fg=self.button_fg_exit, bg=self.button_bg_exit)
        canvas.create_window(400, 700, window=back_button)

        return frame

    '''EASY----------------------------------------------------------------------------------''' 

    def create_easy(self):
        frame = tk.Frame(self.root)
        canvas = tk.Canvas(frame, width=800, height=800)
        canvas.pack(fill="both", expand=True)

        self.background_canvas_create_easy = canvas
        canvas.create_image(0, 0, image=self.bckgrd, anchor="nw", tags="background")

        self.game_easy = Game(canvas, "easy")
        self.game_easy.all_game("easy",True)
        
        self.easy_label = tk.Label(frame, text="EASY MODE", font=("Cascadia Code Light", 32, "bold"), fg=self.label_fg, bg=self.label_bg)
        canvas.create_window(150, 60, window=self.easy_label)

        self.score_label1_easy = tk.Label(frame, text=f"PLAYER 1: {self.game_easy.get_player1_score()}",
                                        font=("Cascadia Code Light", 16), fg=self.label_fg_score1, bg=self.label_bg_score1)
        canvas.create_window(350, 60, window=self.score_label1_easy)

        self.score_label2_easy = tk.Label(frame, text=f"PLAYER 2(AI): {self.game_easy.get_player2_score()}",
                                        font=("Cascadia Code Light", 16), fg=self.label_fg_score2, bg=self.label_bg_score2)
        canvas.create_window(550, 60, window=self.score_label2_easy)

        back_button = tk.Button(frame, text="BACK",
                                command=lambda: [
                                    self.show_screen(self.game),
                                    self.game_easy.all_game("easy",True),
                                    self.score_label1_easy.config(text=f"PLAYER 1: {self.game_easy.get_player1_score()}"),
                                    self.score_label2_easy.config(text=f"PLAYER 2(AI): {self.game_easy.get_player2_score()}"),
                                ],
                                font=self.button_font, fg=self.button_fg_exit, bg=self.button_bg_exit)
        canvas.create_window(200, 700, window=back_button)


        play_button = tk.Button(frame, text="PLAY AGAIN",
                                command=lambda: [
                                    self.show_screen(self.easy),
                                    self.game_easy.all_game("easy",False),
                                    self.score_label1_easy.config(text=f"PLAYER 1: {self.game_easy.get_player1_score()}"),
                                    self.score_label2_easy.config(text=f"PLAYER 2(AI): {self.game_easy.get_player2_score()}"),
                                ],
                                font=self.button_font, fg=self.button_fg_exit, bg=self.button_bg_exit)
        canvas.create_window(550, 700, window=play_button)

        frame.pack(fill="both", expand=True)
        return frame


    '''MEDIUM----------------------------------------------------------------------------------'''
    def create_medium(self):
        frame = tk.Frame(self.root)
        canvas = tk.Canvas(frame, width=800, height=800)
        canvas.pack(fill="both", expand=True)

        self.background_canvas_create_medium = canvas
        canvas.create_image(0, 0, image=self.bckgrd, anchor="nw")

        self.game_medium = Game(canvas, "medium")  
        self.game_medium.all_game("medium", True)  

        label = tk.Label(frame, text="MEDIUM MODE", font=("Cascadia Code Light", 20, "bold"), fg=self.label_fg, bg=self.label_bg)
        canvas.create_window(150, 60, window=label)


        self.score_label1_medium = tk.Label(frame, text=f"PLAYER 1: {self.game_medium.get_player1_score()}",
                                            font=("Cascadia Code Light", 16), fg=self.label_fg_score1, bg=self.label_bg_score1)
        canvas.create_window(350, 60, window=self.score_label1_medium)
        
        self.score_label2_medium = tk.Label(frame, text=f"PLAYER 2(AI): {self.game_medium.get_player2_score()}",
                                            font=("Cascadia Code Light", 16), fg=self.label_fg_score2, bg=self.label_bg_score2)
        canvas.create_window(550, 60, window=self.score_label2_medium)


        back_button = tk.Button(frame, text="BACK",
                                command=lambda: [
                                    self.show_screen(self.game),
                                    self.game_medium.all_game("medium", True),
                                    self.score_label1_medium.config(text=f"PLAYER 1: {self.game_medium.get_player1_score()}"),
                                    self.score_label2_medium.config(text=f"PLAYER 2(AI): {self.game_medium.get_player2_score()}"),
                                ],
                                font=self.button_font, fg=self.button_fg_exit, bg=self.button_bg_exit)
        canvas.create_window(200, 700, window=back_button)


        play_button = tk.Button(frame, text="PLAY AGAIN",
                                command=lambda: [
                                    self.show_screen(self.medium),
                                    self.game_medium.all_game("medium", False),
                                    self.score_label1_medium.config(text=f"PLAYER 1: {self.game_medium.get_player1_score()}"),
                                    self.score_label2_medium.config(text=f"PLAYER 2(AI): {self.game_medium.get_player2_score()}"),
                                ],
                                font=self.button_font, fg=self.button_fg_exit, bg=self.button_bg_exit)
        canvas.create_window(550, 700, window=play_button)

        return frame


    
    '''HARD----------------------------------------------------------------------------------'''
    def create_hard(self):
        frame = tk.Frame(self.root)
        canvas = tk.Canvas(frame, width=800, height=800)
        canvas.pack(fill="both", expand=True) 

        self.background_canvas_create_hard = canvas
        canvas.create_image(0, 0, image=self.bckgrd, anchor="nw")

        self.game_hard = Game(canvas, "hard")
        self.game_hard.all_game("hard", True)

        label = tk.Label(frame, text="HARD MODE", font=("Cascadia Code Light", 32, "bold"), fg=self.label_fg, bg=self.label_bg)
        canvas.create_window(150, 60, window=label)

        self.score_label1_hard = tk.Label(frame, text=f"PLAYER 1: {self.game_hard.get_player1_score()}",
                                        font=("Cascadia Code Light", 16), fg=self.label_fg_score1, bg=self.label_bg_score1)
        canvas.create_window(350, 60, window=self.score_label1_hard)

        self.score_label2_hard = tk.Label(frame, text=f"PLAYER 2(AI): {self.game_hard.get_player2_score()}",
                                        font=("Cascadia Code Light", 16), fg=self.label_fg_score2, bg=self.label_bg_score2)
        canvas.create_window(550, 60, window=self.score_label2_hard)

        back_button = tk.Button(frame, text="BACK",
                                command=lambda: [
                                    self.show_screen(self.game),
                                    self.game_hard.all_game("hard", True),
                                    self.score_label1_hard.config(text=f"PLAYER 1: {self.game_hard.get_player1_score()}"),
                                    self.score_label2_hard.config(text=f"PLAYER 2(AI): {self.game_hard.get_player2_score()}"),
                                ],
                                font=self.button_font, fg=self.button_fg_exit, bg=self.button_bg_exit)
        canvas.create_window(200, 700, window=back_button)

        play_button = tk.Button(frame, text="PLAY AGAIN",
                                command=lambda: [
                                    self.show_screen(self.hard),
                                    self.game_hard.all_game("hard", False),
                                    self.score_label1_hard.config(text=f"PLAYER 1: {self.game_hard.get_player1_score()}"),
                                    self.score_label2_hard.config(text=f"PLAYER 2(AI): {self.game_hard.get_player2_score()}"),
                                ],
                                font=self.button_font, fg=self.button_fg_exit, bg=self.button_bg_exit)
        canvas.create_window(550, 700, window=play_button)

        frame.pack(fill="both", expand=True) 
        return frame

    
    '''CHANGE THEME CANVA----------------------------------------------------------------------------------'''   
    def create_change_theme(self):
        frame = tk.Frame(self.root)
        canvas = tk.Canvas(frame, width=800, height=800)
        canvas.pack(fill="both", expand=True)

        self.background_canvas_change_theme = canvas
        canvas.create_image(0, 0, image=self.bckgrd, anchor="nw", tags="background")

        label = tk.Label(frame, text="CHANGE THEME", font=("Cascadia Code Light", 40, "bold"), fg=self.button_fg, bg=self.button_bg)
        canvas.create_window(400, 100, window=label)

        change_bg_light_button = tk.Button(frame, text="LIGHT", command=lambda: self.update_theme("light"), font=self.button_font, width=15, height=2, fg=self.button_fg, bg=self.button_bg)
        canvas.create_window(200, 250, window=change_bg_light_button)

        change_bg_dark_button = tk.Button(frame, text="DARK", command=lambda: self.update_theme("dark"), font=self.button_font, width=15, height=2, fg=self.button_fg, bg=self.button_bg)
        canvas.create_window(550, 250, window=change_bg_dark_button)

        change_bg_dark_blue_button = tk.Button(frame, text="DARK BLUE", command=lambda: self.update_theme("dark_blue"), font=self.button_font, width=15, height=2, fg=self.button_fg, bg=self.button_bg)
        canvas.create_window(200, 400, window=change_bg_dark_blue_button)

        change_bg_pink_button = tk.Button(frame, text="PINK", command=lambda: self.update_theme("pink"), font=self.button_font, width=15, height=2, fg=self.button_fg, bg=self.button_bg)
        canvas.create_window(550, 400, window=change_bg_pink_button)

        change_bg_old_button = tk.Button(frame, text="OLD", command=lambda: self.update_theme("old"), font=self.button_font, width=15, height=2, fg=self.button_fg, bg=self.button_bg)
        canvas.create_window(200, 550, window=change_bg_old_button)

        back_button = tk.Button(frame, text="BACK", command=lambda: self.show_screen(self.start), font=self.button_font, width=15, height=2, fg=self.button_fg_exit, bg=self.button_bg_exit)
        canvas.create_window(550, 700, window=back_button)

        return frame
    '''HOW TO PLAY CANVA----------------------------------------------------------------------------------''' 
    def create_how_to_play(self):
        frame = tk.Frame(self.root)
        canvas = tk.Canvas(frame, width=800, height=800)
        canvas.pack(fill="both", expand=True)

        self.background_canvas_how_to_play = canvas
        canvas.create_image(0, 0, image=self.bckgrd, anchor="nw", tags="background")

        label = tk.Label(frame, text="HOW TO PLAY", font=("Cascadia Code Light", 32, "bold"), pady=40, fg=self.label_fg, bg=self.label_bg)
        canvas.create_window(400, 100, window=label)

        rules_text = (
        "Tic Tac Toe is a game for two players .In this game you can play with an AI.\n"
        "This AI is capable of playing in three different difficulties: easy, medium and hard.\n"
        "The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game.\n"
        "If all 9 squares are filled and no player has three in a row, the game is a draw.\n"
        "The game starts with an empty 3x3 grid.\n" 
        "The first player is marked with color BLUE (YOU) and the second player is marked with color RED (AI).\n"
        "The game ends when one player wins or the board is full (draw)."

        "To make a move, simply click on an empty square and choose your color (BLUE or RED).\n"
        "If you want to quit the game, press the 'BACK TO START' button at the bottom.\n"
        "If you want to change the theme of the game, press the 'CHANGE THEME' button at the bottom.\n"
        "If you want to play against the AI, press the 'PLAY AGAIN' button at the bottom.\n"
        "Enjoy your game and have fun playing Tic Tac Toe!\n"
        "Good luck!"
        )

        rules_label = tk.Label(frame, text=rules_text, font=("Arial", 12), padx=20, pady=20, fg=self.label_fg, bg=self.label_bg, justify="left", wraplength=700)
        canvas.create_window(400, 400, window=rules_label)

        back_button = tk.Button(frame, text="BACK TO START", command=lambda: self.show_screen(self.start), font=self.button_font, width=self.button_width, height=self.button_height, fg=self.button_fg_exit, bg=self.button_bg_exit)
        canvas.create_window(400, 700, window=back_button)

        return frame
    
    '''
    UPDATE_THEMES----------------------------------------------------------------------------------------------
    '''
    def update_theme(self, theme):

        theme_paths = {
            "light": "images/background_image1.jpg",
            "dark": "images/background_image2.jpg",
            "dark_blue": "images/background_image3.jpg",
            "pink": "images/background_image4.jpg",
            "old": "images/background_image5.jpg"
        }


        if theme in theme_paths:
            self.bckgrd = Image.open(theme_paths[theme])
            self.bckgrd = ImageTk.PhotoImage(self.bckgrd)


            canvases = [
                self.background_canvas_start,
                self.background_canvas_game,
                self.background_canvas_change_theme,
                self.background_canvas_how_to_play,
                self.background_canvas_create_easy,
                self.background_canvas_create_medium,
                self.background_canvas_create_hard
            ]


            for canvas in canvases:
                if canvas:
                    canvas.create_image(0, 0, image=self.bckgrd, anchor="nw", tags="background")


        if theme == "dark":
            self.button_fg = "#b7bcbf"
            self.button_bg = "#373737"
            self.button_bg_exit = "SlateGray"
            self.button_fg_exit = "white"
            self.label_fg = "#a1bac9"
            self.label_bg = "#0b171e"
        elif theme == "light":
            self.button_fg = "black"
            self.button_bg = "Gainsboro"
            self.button_bg_exit = "red"
            self.button_fg_exit = "white"
            self.label_fg = "white"
            self.label_bg = "DimGray"
        elif theme == "dark_blue":
            self.button_fg = "#baf9f8"
            self.button_bg = "DarkCyan"
            self.button_bg_exit = "DarkSlateGray"
            self.button_fg_exit = "white"
            self.label_fg = "LightCyan"
            self.label_bg = "SteelBlue"
        elif theme == "pink":
            self.button_fg = "black"
            self.button_bg = "pink"
            self.button_bg_exit = "DarkMagenta"
            self.button_fg_exit = "white"
            self.label_fg = "#9a0f94"
            self.label_bg = "#f0a6e9"
        elif theme == "old":
            self.button_fg = "black"
            self.button_bg = "moccasin"
            self.button_bg_exit = "Chocolate"
            self.button_fg_exit = "white"
            self.label_fg = "black"
            self.label_bg = "#edeed2"


        for page in [self.start, self.game, self.change_theme, self.how_to_play, self.easy, self.medium, self.hard]:
            self.update_buttons(page)
            self.update_labels(page)


        self.game_easy = None
        self.game_medium = None
        self.game_hard = None


        if self.game_easy is None:
            self.game_easy = Game(self.background_canvas_create_easy, "easy")
            self.game_easy.canvas.create_image(0, 0, image=self.bckgrd, anchor="nw", tags="background")
            self.game_easy.all_game("easy", True) 

        if self.game_medium is None:
            self.game_medium = Game(self.background_canvas_create_medium, "medium") 
            self.game_medium.canvas.create_image(0, 0, image=self.bckgrd, anchor="nw", tags="background") 
            self.game_medium.all_game("medium", True)

        if self.game_hard is None:
            self.game_hard = Game(self.background_canvas_create_hard, "hard")
            self.game_hard.canvas.create_image(0, 0, image=self.bckgrd, anchor="nw", tags="background") 
            self.game_hard.all_game("hard", True) 

    '''
    UPDATE BUTTONS -------------------------------------------------------
    '''
    def update_buttons(self, frame):
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Button):
                if widget["text"] == "EXIT GAME" or widget["text"] == "BACK TO START" or widget["text"] == "BACK":
                    widget.config(fg=self.button_fg_exit, bg=self.button_bg_exit)
                else:
                    widget.config(fg=self.button_fg, bg=self.button_bg)

 
    '''
    UPDATE LABELS --------------------------------------------------------
    '''
    def update_labels(self, frame):
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Label):

                if "PLAYER 1:" in widget["text"]:
                    widget.config(fg=self.label_fg_score1, bg=self.label_bg_score1)
                elif "PLAYER 2(AI):" in widget["text"]:
                    widget.config(fg=self.label_fg_score2, bg=self.label_bg_score2)
                else:
                    widget.config(fg=self.label_fg, bg=self.label_bg)

    '''
    START GAME ------------------------------------------------------------
    '''

    def start_game(self, difficulty):
        print(f"Starting game on {difficulty} difficulty")


    '''
    SHOW SCREEN------------------------------------------------------------------
    ''' 

    def show_screen(self, screen):
        for widget in self.root.winfo_children():
            widget.pack_forget()
        screen.pack(fill="both", expand=True)

def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()