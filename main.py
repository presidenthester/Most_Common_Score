import os
import pandas as pd
from tkinter import *
from tkinter import ttk
from Score_Format import *
from tkinter import messagebox


# lists for combo box options by decade
cb_seasons = [
    "1966 AFL",
    "1966 NFL",
    "1967 AFL",
    "1967 NFL",
    "1968 AFL",
    "1968 NLF",
    "1969 AFL",
    "1969 NFL",
    "1970",
    "1971",
    "1972",
    "1973",
    "1974",
    "1975",
    "1976",
    "1977",
    "1978",
    "1979",
    "1980",
    "1981",
    "1982",
    "1983",
    "1984",
    "1985",
    "1986",
    "1987",
    "1988",
    "1989",
    "1990",
    "1991",
    "1992",
    "1993",
    "1994",
    "1995",
    "1996",
    "1997",
    "1998",
    "1999",
    "2000",
    "2001",
    "2002",
    "2003",
    "2004",
    "2005",
    "2006",
    "2007",
    "2008",
    "2009",
    "2010",
    "2011",
    "2012",
    "2013",
    "2014",
    "2015",
    "2016",
    "2017",
    "2018",
    "2019",
    "2020",
    "2021",
    "2022"
]



class ScoreApp():
    
    def __init__(self):
        
        self.file = None
        self.sorted_value_counts = pd.DataFrame()  # Initialize as an empty DataFrame
        self.yearval = None
        
    
    def main_screen(self):
        self.main = Tk()
        self.main.title('Most Common NFL Scores')
        self.main.geometry('1250x750')
        self.main.resizable(width=False, height=False)
        self.main.iconbitmap(r"D:\\MostCommonScore\\Images\\football.ico")

        
        self.cImg = PhotoImage(file=r"D:\\MostCommonScore\\Images\\center_image.png")


        # Initialize main screen canvas to place widgets
        canvas = Canvas(self.main, width=1250, height=750, bg='#154796')
        canvas.pack(fill='both', expand=True)


        canvas.create_text(650, 235, 
              text='See the most common scores in the NFL since the 1970 merger', 
              fill='white', 
              font=("Copperplate Gothic Bold", "18"))
        canvas.create_image(650, 10, image=self.cImg, anchor="n")
        canvas.create_text(625, 375, text="Search for score counts", font=("Copperplate Gothic Bold", "14"), fill="white")
        canvas.create_text(625, 400, text="Enter the winning score in the first field", font=("Copperplate Gothic Bold", "14"), fill="white")
        canvas.create_text(625, 425, text="and the losing score in the second fiels", font=("Copperplate Gothic Bold", "14"), fill="white")
        canvas.create_text(550, 460, text=" - ", font=("Copperplate Gothic Bold", "36"), fill="#b1c9f0")
    
    
        
        a_t_btn = Button(self.main, text="All Time Common Score", font= ("Copperplate Gothic Bold", "12"), command=self.all_time_scores)
        a_t_btn.place(x=650, y=230)
        
        get_scores_btn = Button(self.main, text="Get Scores", font= ("Copperplate Gothic Bold", "12"), command=lambda:[self.get_year(), self.year_win()])
        get_scores_btn.place(x=650, y=650)
        
        search_scores_btn = Button(self.main, text="Search Scores", font= ("Copperplate Gothic Bold", "10"), command=self.score_search)
        search_scores_btn.place(x=650, y=650)
        
        
        self.score_search_pts = Entry(self.main, width=50)
        self.score_search_pts_1 = Entry(self.main, width=50)
        
        
        
        # Initialize Combo Boxes
        self.seasons_combo = ttk.Combobox(self.main, value= cb_seasons, font= ("Copperplate Gothic Bold", "12"))
        self.seasons_combo["state"] = "readonly"
        self.seasons_combo.set("Select Year")
        
        

        self.canv_all_time = canvas.create_window(350, 275, anchor="n", width=225, window=a_t_btn)
        self.canv_all_time = canvas.create_window(900, 275, anchor="n", width=225, window=get_scores_btn)
        self.canv_all_time = canvas.create_window(720, 460, anchor="n", width=120, window=search_scores_btn)
        
        self.canv_all_time = canvas.create_window(625, 275, anchor="n", width=225, window=self.seasons_combo, height=25)
        
        self.canv_all_time = canvas.create_window(500, 460, anchor="n", width=50, window=self.score_search_pts, height=25)
        self.canv_all_time = canvas.create_window(600, 460, anchor="n", width=50, window=self.score_search_pts_1, height=25)
        
    
    
        self.main.mainloop()        
     
    def all_time_scores(self):
        self.a_t_win = Toplevel()
        self.a_t_win.iconbitmap(r"D:\\MostCommonScore\\Images\\football.ico")
        self.a_t_win.geometry("700x1000")
        self.a_t_win.title("")
        self.a_t_win.resizable(width=False, height=False)
        

        # Centers the top level to the main screen
        x = self.main.winfo_x()
        y= self.main.winfo_y()
        self.a_t_win.geometry("+%d+%d" %(x+350,y+0))
        self.a_t_win.wm_transient(self.main)
        
        
        canvas = Canvas(self.a_t_win, width=700, height=1000, bg='#7fadf5')
        canvas.pack(fill='both', expand=True)
        
        # Scrollbar Initialization and placement
        scrollbar = Scrollbar(canvas, orient=VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        
        canvas.create_text(350, 100,text='All scores and counts from 1966 to present', font= ("Copperplate Gothic Bold", "18"), fill="#000000")
        canvas.create_text(274, 175, text='Score', font= ("Copperplate Gothic Bold", "18"), fill="#000000")
        canvas.create_text(424, 175, text='Count', font= ("Copperplate Gothic Bold", "18"), fill="#000000")
        
        # Iterates through CSV to places result text on canvas 
        for index, row in allYearScores.sorted_value_counts.iterrows():
            score, count = row['Score'], row['Count']
            score_text = f"{score}"
            count_text = f"{count}"
            canvas.create_text(234, 225 + (index * 50), text=score_text, anchor="w", fill="#000000", font= ("Copperplate Gothic Bold", "18"))
            canvas.create_text(394, 225 + (index * 50), text=count_text, anchor="w", fill="#000000", font= ("Copperplate Gothic Bold", "18"))
        
        
        # Scrollbar functionality
        canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(-1 * (event.delta // 120), "units"))
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    
    def year_win(self):
        
        if self.yearval == 'Select Year':
            self.select_error()
            
        else:
        
        
            # Use a different variable name for the Toplevel window
            self.year_win_toplevel = Toplevel()
            self.year_win_toplevel.iconbitmap(r"D:\\MostCommonScore\\Images\\football.ico")
            self.year_win_toplevel.geometry("700x1000")
            self.year_win_toplevel.title(f"{self.yearval} Score Counts")
            self.year_win_toplevel.resizable(width=False, height=False)
        
            # Centers the top level to the main screen
            x = self.main.winfo_x()
            y = self.main.winfo_y()
            self.year_win_toplevel.geometry("+%d+%d" % (x + 350, y + 0))
            self.year_win_toplevel.wm_transient(self.main)
        
            canvas = Canvas(self.year_win_toplevel, width=700, height=1000, bg='#7fadf5')
            canvas.pack(fill='both', expand=True)
            # Scrollbar Initialization and placement
            scrollbar = Scrollbar(canvas, orient=VERTICAL, command=canvas.yview)
            canvas.configure(yscrollcommand=scrollbar.set)
            scrollbar.pack(side=RIGHT, fill=Y)
        
            canvas.create_text(350, 50, text=f'All scores and counts from {self.yearval}', font= ("Copperplate Gothic Bold", "18"), fill="#000000")
            canvas.create_text(274, 125, text='Score', font= ("Copperplate Gothic Bold", "18"), fill="#000000")
            canvas.create_text(424, 125, text='Count', font= ("Copperplate Gothic Bold", "18"), fill="#000000")
        
            # Scrollbar functionality
            canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(-1 * (event.delta // 120), "units"))
            canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
            for index, row in self.sorted_value_counts.iterrows():
                score, count = row['Score'], row['Count']
                score_text = f"{score}"
                count_text = f"{count}"
                canvas.create_text(244, 175 + (index * 50), text=score_text, anchor="w", fill="#000000", font=("Copperplate Gothic Bold", "18"))
                canvas.create_text(424, 175 + (index * 50), text=count_text, anchor="w", fill="#000000", font=("Copperplate Gothic Bold", "18"))
            self.year_win_toplevel.protocol("WM_DELETE_WINDOW", self.on_close)

    def select_error(self):
        response = messagebox.showwarning("WARNING:", "You must select a year to view scores")
        if response == 'ok':
            pass
    
    def file_error(self):
        response = messagebox.showerror("File not found", f"The file '{self.yearval}_merged.csv' does not exist in the folder.")
        if response == 'ok':
            pass
    
    def on_close(self):
        self.year_win_toplevel.destroy()
    
    def get_year(self):
        global yearval
        self.yearval = self.seasons_combo.get()
        self.file_path = os.path.join(r'D:\\MostCommonScore\\Merged_CSVs', f"{self.yearval}_merged.csv")
        
        
            
            
        
        if os.path.isfile(self.file_path):
            self.file = pd.read_csv(self.file_path)
            self.file.drop(columns=['Week','Day','Date','Time','Winner/tie','Unnamed: 5','Loser/tie','Unnamed: 7','YdsW','TOW','YdsL','TOL'], inplace=True)
            self.value_counts = self.file['Combined_Pts'].value_counts().reset_index()
            self.value_counts.columns = ['Score', 'Count']
            self.sorted_value_counts = self.value_counts.sort_values(by='Count', ascending=False)
        
        else:
            print("Sorted value counts are empty. Check the DataFrame or file path.")

    
    def search_error(self):
        response = messagebox.showwarning("WARNING:", "You must enter a number in each search field to get scores data")
        if response == 'ok':
            pass

    def score_search(self):
        
        # Get the search input from the user
        self.search_input = self.score_search_pts.get().strip() + "-" + self.score_search_pts_1.get().strip()
        self.score_input = [self.search_input]
        
        # Read the CSV file
        self.combined_pts = pd.read_csv(r"D:\\MostCommonScore\\Merged_CSVs\\merge-csv.com__64cc71a569499.csv")
        self.combined_pts.drop(columns=['Week','Day','Date','Time','Winner/tie','Unnamed: 5','Loser/tie','Unnamed: 7','YdsW','TOW','YdsL','TOL'], inplace=True)
       
        if self.score_search_pts.get() == "" or self.score_search_pts_1.get() == "":
            self.search_error()
        
        
        # Use a different variable name for the Toplevel window
        else: 
            self.searched_toplevel = Toplevel()
            self.searched_toplevel.iconbitmap(r"D:\\MostCommonScore\\Images\\football.ico")
            self.searched_toplevel.geometry("700x250")
            self.searched_toplevel.title(f"Score Counts for {self.search_input}")
            self.searched_toplevel.resizable(width=False, height=False)
        
            # Centers the top level to the main screen
            self.x = self.main.winfo_x()
            self.y = self.main.winfo_y()
            self.searched_toplevel.geometry("+%d+%d" % (self.x + 300, self.y + 200))
            self.searched_toplevel.wm_transient(self.main)
        
            self.search_canvas = Canvas(self.searched_toplevel, width=700, height=250, bg='#7fadf5')
            self.search_canvas.pack(fill='both', expand=True)
            
            # Scrollbar Initialization and placement
            self.scrollbar = Scrollbar(self.search_canvas, orient=VERTICAL, command=self.search_canvas.yview)
            self.search_canvas.configure(yscrollcommand=self.scrollbar.set)
            self.scrollbar.pack(side=RIGHT, fill=Y)
            
            self.search_canvas.create_text(350, 50, text=f'The score of {self.search_input} has occurred', font= ("Copperplate Gothic Bold", "18"), fill="#000000")
            self.search_canvas.create_text(350, 100, text=f"{self.combined_pts['Combined_Pts'].str.lower().str.contains(self.search_input).sum()} times", font= ("Copperplate Gothic Bold", "20"), fill="#000000")
            
            
            
            # Scrollbar functionality
            self.search_canvas.bind("<MouseWheel>", lambda event: self.search_canvas.yview_scroll(-1 * (event.delta // 120), "units"))
            self.search_canvas.bind('<Configure>', lambda e: self.search_canvas.configure(scrollregion=self.search_canvas.bbox("all")))
             
         
             
             
            count = (self.combined_pts['Combined_Pts'].str.lower() == self.search_input.lower()).sum()
            print(f"The score {self.search_input} has occurred {count} times.")
            self.search_canvas.create_text(350, 100, text=f"{count} times", font=("Copperplate Gothic Bold", "20"), fill="#000000")
           
           
    
        
        
        
main = ScoreApp()
main.main_screen()