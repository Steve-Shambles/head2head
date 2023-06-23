""" Head2Head V0.82 - June 2023 by Steve Shambles.

    Historical data supplied by https://football-data.co.uk, with thanks.
    Current data covers Aug 1992 to June 24th 2023.

    logo photo attribution:
    By Bluejam - Self-photographed, CC BY-SA 4.0,
    https://commons.wikimedia.org/w/index.php?curid=78153606

V0.81: Added Luton to list of teams
V0.82: Updated results to end of season 22-2023, + some minor tinkering.

Requirements:
pip install Pillow
"""
import csv
from datetime import datetime
import os
import sys
import tkinter as tk
from tkinter import messagebox, Menu
from tkinter import ttk
import webbrowser as web

from PIL import Image, ImageTk


class Fs():
    """Variables, set at defaults for global use.
       Add Fs. to each var then its effectively global."""
    home_team = ''
    away_team = ''
    team_names = ''
    hits = ''
    home_wins = 0
    away_wins = 0
    draw = 0
    hg = 0
    ag = 0
    outcome = ""
    table = None
    home_goals = 0
    away_goals = 0
    home_avg_goals = 0
    away_avg_goals = 0
    home_win_percentage = 0
    away_win_percentage = 0
    draw_percentage = 0
    all_text = ''
    user_folder = 'user_saves'
    home_team_clean_sheets = 0
    away_team_clean_sheets = 0
    home_team_pts= 0
    away_team_pts = 0
    predicted_hg = 0
    predicted_ag = 0
    predict_match = ''
    total_results = 0


def load_fail(error_msg):
    """ file not found error message. """
    root.withdraw()
    tk.messagebox.showinfo("FileNotFoundError", error_msg)
    root.destroy()
    sys.exit(1)


def check_files():
    """
    Check if all required csv files exist.
    Call load_fail function if any file is missing.
    """
    if not os.path.exists('data'):
        load_fail(str('data folder not found'))

    try:
        with open(r'data\football.ico', 'rb') as f1, \
             open(r'data\plteams.txt', 'rb') as f2, \
             open(r'data\logo.jpg', 'rb') as f3,  \
             open(r'data\icons\help-16x16.ico', 'rb') as f4,  \
             open(r'data\icons\about-16x16.ico', 'rb') as f5,  \
             open(r'data\icons\exit-16x16.ico', 'rb') as f6,  \
             open(r'data\icons\donation-16x16.ico', 'rb') as f7,  \
             open(r'data\icons\github-16x16.ico', 'rb') as f8,  \
             open(r'data\h2h-help.txt', 'rb') as f9,  \
             open(r'data\icons\prg-fldr-16x16.ico', 'rb') as f10:
            pass

    except FileNotFoundError as file_error:
        load_fail(str(file_error))

    # Test csvs are present.
    missing_files = []
    for i in range(1, 32):
        filename = f'{i:02}.csv'
        filepath = os.path.join('data', filename)
        if not os.path.exists(filepath):
            missing_files.append(filename)
    if missing_files:
        error_msg = f'Missing files: {", ".join(str(f) for f in missing_files)}'
        load_fail(error_msg)

    root.withdraw()

    #  Check required folder exist in current dir If not,then create.
    check_folder = os.path.isdir(Fs.user_folder)
    if not check_folder:
        os.makedirs(Fs.user_folder)


root = tk.Tk()
check_files()
root.title('Head2Head V0.82')
root.iconbitmap(r'data\football.ico')

with open(r'data\plteams.txt', 'r') as f:
    Fs.team_names = f.read().splitlines()


def calc_avg_goals():
    """ Calculate the average goals scored by each team. """
    Fs.home_avg_goals = 0
    Fs.away_avg_goals = 0
    num_matches = Fs.home_wins + Fs.away_wins + Fs.draw
    Fs.home_avg_goals = round((Fs.home_goals / num_matches), 1)
    Fs.away_avg_goals = round((Fs.away_goals / num_matches), 1)


def predict_outcome():
    """ Calculate the percentages of each outcome. """
    Fs.all_text = ''
    Fs.total_results = Fs.home_wins + Fs.away_wins + Fs.draw

    if Fs.total_results == 0:
        return

    calc_avg_goals()

    Fs.predicted_hg = round(Fs.home_avg_goals)
    Fs.predicted_ag = round(Fs.away_avg_goals)
    Fs.predicted_match = 'UNKNOWN'
    # print(Fs.predicted_hg, ' ' , Fs.predicted_ag)

    if Fs.predicted_hg == Fs.predicted_ag or Fs.predicted_ag == Fs.predicted_hg:
        Fs.predicted_match ='DRAW'
    if Fs.predicted_hg > Fs.predicted_ag:
        Fs.predicted_match ='HOME WIN'
    if Fs.predicted_ag > Fs.predicted_hg:
        Fs.predicted_match ='AWAY WIN'

    Fs.home_win_percentage = round((Fs.home_wins / Fs.total_results) * 100, 1)
    Fs.away_win_percentage = round((Fs.away_wins / Fs.total_results) * 100, 1)
    Fs.draw_percentage = round((Fs.draw / Fs.total_results) * 100, 1)

    msg_lab.config(bg='powderblue', text='Matches: ' + str(Fs.total_results) +
                   '  -  Home Wins: (' + str(Fs.home_wins)+') ' +
                   str(Fs.home_win_percentage) + '%' +
                   '  -  Away Wins: (' + str(Fs.away_wins)+') ' +
                   str(Fs.away_win_percentage) + '%' +
                   '  -  Draws: (' + str(Fs.draw) + ') ' +
                   str(Fs.draw_percentage) + '%\n'
                   'Home team points = ' + str(Fs.home_team_pts) +
                   ' - Away team points = ' + str(Fs.away_team_pts))

    msg_lab2.config(bg='white', text='Avg Home Goals: ' +
                    str(Fs.home_avg_goals) +
                    ' - Avg Away Goals: ' + str(Fs.away_avg_goals) +
                    '\nHome team clean sheets:' +str(Fs.home_team_clean_sheets) +
                    ' - Away team clean sheets:' +str(Fs.away_team_clean_sheets))
    # add 3\4 a goal for home team as home advantage
    home_adv = int(Fs.home_avg_goals) + 0.75
    # print(home_adv)  # testing
    predicted_hg = round(home_adv)
    predicted_ag = round(Fs.away_avg_goals)

    msg_lab3.config(bg='powderblue',
                    text='Prediction for this next fixture based on these PL results is :\n' +
                    str(Fs.predicted_match) + ' and the score could be ' +
                    str(Fs.predicted_hg) + ' - ' + str(Fs.predicted_ag))

    # create string for printing to csv and text file saves.
    Fs.all_text = 'Matches:' + str(Fs.total_results) + ' - ' +  \
    'Home Wins:(' + str(Fs.home_wins) + ') ' + str(Fs.home_win_percentage) + '%  - ' +  \
    'Away Wins:(' + str(Fs.away_wins) + ') ' + str(Fs.away_win_percentage) + '%  - ' +  \
    'Draws:(' + str(Fs.draw) + ') ' + str(Fs.draw_percentage) + '% \n' +  \
    'Home team points = ' + str(Fs.home_team_pts) +  \
    ' - Away team points = ' + str(Fs.away_team_pts) + '\n'\
    'Avg Home Goals:' + str(Fs.home_avg_goals) + ' - ' +  \
    'Avg Away Goals:' + str(Fs.away_avg_goals) + '\n'  \
    'Home team clean sheets:' +str(Fs.home_team_clean_sheets) +  \
    ' - Away team clean sheets:' +str(Fs.away_team_clean_sheets)+ '\n\n'  \
    'Prediction for this next fixture based on these PL results is :\n'  \
    + str(Fs.predicted_match) + ' and the score could be ' +  \
    str(Fs.predicted_hg) + ' - ' + str(Fs.predicted_ag)


def count_results_stats():
    """ Count home wins, away wins and draws. """
    if Fs.outcome == 'H':
        Fs.home_wins += 1
        Fs.home_goals += int(Fs.hg)
        Fs.home_team_pts += 3
    if Fs.outcome == 'A':
        Fs.away_wins += 1
        Fs.away_goals += int(Fs.ag)
        Fs.away_team_pts += 3
    if Fs.outcome == 'D':
        Fs.draw += 1
        Fs.home_goals += int(Fs.hg)
        Fs.away_goals += int(Fs.ag)
        Fs.home_team_pts += 1
        Fs.away_team_pts += 1


def count_clean_sheets():
    """ Track how many clean sheets home and away teams aquired in matches found. """
    if int(Fs.ag) == 0:
        Fs.home_team_clean_sheets += 1
    if int(Fs.hg) == 0:
        Fs.away_team_clean_sheets += 1


def create_table():
    """ Create table in notebook. """
    # get the tab object for tab 1
    tab1 = tab_frame.winfo_children()[0]
    # create a table frame to hold the table and scrollbars
    table_frame = tk.Frame(tab1)
    table_frame.pack(fill=tk.BOTH, expand=True)
    # create a table to display the data
    Fs.table = ttk.Treeview(table_frame)
    Fs.table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    # create vertical scrollbar
    yscrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=Fs.table.yview)
    yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    # configure the table to use the scrollbars
    Fs.table.configure(yscrollcommand=yscrollbar.set)
    # define the columns
    Fs.table['columns'] = ('date', 'home_team', 'away_team', 'home_goals',
                           'away_goals', 'result')
    # format the columns
    Fs.table.column('#0', width=0, stretch=tk.NO)
    Fs.table.column('date', anchor=tk.CENTER, width=100)
    Fs.table.column('home_team', anchor=tk.W, width=100)
    Fs.table.column('away_team', anchor=tk.W, width=100)
    Fs.table.column('home_goals', anchor=tk.W, width=40)
    Fs.table.column('away_goals', anchor=tk.W, width=40)
    Fs.table.column('result', anchor=tk.W, width=40)
    # create the headings
    Fs.table.heading('#0', text='', anchor=tk.CENTER)
    Fs.table.heading('date', text='Date', anchor=tk.CENTER)
    Fs.table.heading('home_team', text='Home Team', anchor=tk.W)
    Fs.table.heading('away_team', text='Away Team', anchor=tk.W)
    Fs.table.heading('home_goals', text='HG', anchor=tk.W)
    Fs.table.heading('away_goals', text='AG', anchor=tk.W)
    Fs.table.heading('result', text='Result', anchor=tk.W)


def save_as_csv():
    """ Create time stamp for first part of unique csv filename. """
    time_stamp = (datetime.now().strftime
                  (r'%d' + ('-') + '%b' + ('-') +
                   '%Y' + ('-') + '%H' + ('.')
                   + '%M' + ('-') + '%S' + 's'))

    file_name = str(Fs.home_team)+' V '+str(Fs.away_team)+'-'+str(time_stamp)+'.csv'
    path = r'user_saves/' + str(file_name)

    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Home Team', 'Away Team', 'Home Goals',
                         'Away Goals', 'Result'])
        writer.writerows(Fs.hits)
        writer.writerow([''])  # add a blank row
        writer.writerow([''])
        writer.writerow([Fs.all_text])

    save_csv_btn.configure(state=tk.DISABLED)
    messagebox.showinfo('Head2Head Information',
                        'CSV file saved.\n'
                        'You can use the Open user saves folder menu item '
                        'from the drop-down menu, top left of program, '
                        'to view your saved files.')


def save_as_text():
    """ Create time stamp for first part of unique text filename. """
    time_stamp = (datetime.now().strftime
                  (r'%d' + ('-') + '%b' + ('-') +
                   '%Y' + ('-') + '%H' + ('.')
                   + '%M' + ('-') + '%S' + 's'))

    file_name = str(Fs.home_team)+' V '+str(Fs.away_team)+'-'+str(time_stamp)+'.txt'

    path = r'user_saves/' + str(file_name)

    with open(path, 'w') as f:
        for hit in Fs.hits:
            f.write(','.join(hit) + '\n')
        f.write('\n'+str(Fs.all_text))
        save_txt_btn.configure(state=tk.DISABLED)

    messagebox.showinfo('Head2Head Information',
                        'Text file saved.\n'
                        'You can use the Open user saves folder menu item '
                        'from the drop-down menu, top left of program, '
                        'to view your saved files.')


def scan_csv_files(home_team, away_team):
    """ Read in data from csv files. """
    Fs.hits = []
    Fs.hg = 0
    Fs.ag = 0
    Fs.draw = 0
    Fs.outcome = ''
    Fs.home_wins = 0
    Fs.away_wins = 0
    Fs.home_goals = 0
    Fs.away_goals = 0
    Fs.home_avg_goals = 0
    Fs.away_avg_goals = 0
    Fs.home_win_percentage = 0
    Fs.away_win_percentage = 0
    Fs.draw_percentage = 0
    Fs.home_team_clean_sheets = 0
    Fs.away_team_clean_sheets = 0
    Fs.home_team_pts = 0
    Fs.away_team_pts = 0

    save_txt_btn.configure(state=tk.NORMAL)
    save_csv_btn.configure(state=tk.NORMAL)

    # loop over all CSV files in the directory
    for i in range(1, 32):
        filename = f"{i:02}.csv"
        filepath = os.path.join("data", filename)

        # open the CSV file and read its rows
        with open(filepath, "r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                # check if this row matches the home and away team names
                if row[1] == Fs.home_team and row[2] == Fs.away_team:
                    # if it matches, add it to the list of matches
                    Fs.hits.append((row[0], row[1], row[2], row[3], row[4], row[5]))
                    Fs.hg = row[3]
                    Fs.ag = row[4]
                    Fs.outcome = row[5]

                    count_clean_sheets()
                    count_results_stats()
    # add the rows
    for hit in Fs.hits:
        Fs.table.insert('', tk.END, text='', values=hit)

    if Fs.hits:
        predict_outcome()
    else:
        paddy = " " * 140
        msg_lab.config(bg='powderblue', text=paddy)
        msg_lab2.config(bg='powderblue', text='These two teams have not played this fixture in the EPL')
        msg_lab3.config(bg='powderblue', text=paddy)
        messagebox.showinfo('Sorry',
                            'No matches found!')
        save_txt_btn.configure(state=tk.DISABLED)
        save_csv_btn.configure(state=tk.DISABLED)
        return


def get_team_selections():
    """ Get home and away teams from combo boxes. """
    Fs.home_team = home_team_combo.get()
    Fs.away_team = away_team_combo.get()


def get_stats():
    """ Gather stats from home v away teams results. """
    get_team_selections()
    if Fs.away_team == Fs.home_team:
        messagebox.showinfo('Doh!',
                            'Please choose two different teams...')
        return

    for i in Fs.table.get_children():
        Fs.table.delete(i)
        root.update()

    Fs.home_wins = 0
    Fs.away_wins = 0
    Fs.draw = 0

    scan_csv_files(Fs.home_team, Fs.away_team)


def help_text():
    """Show help msg box."""
    web.open(r'data\h2h-help.txt')


def donate_me():
    """User splashes the cash here!"""
    web.open('https:\\paypal.me/photocolourizer')


def visit_github():
    """View source code and my other Python projects at GitHub."""
    web.open('https://github.com/Steve-Shambles/head2head')


def about_menu():
    """About program msgbox."""
    messagebox.showinfo('Head2Head Program Information',
                        'V0.82\n\n'
                        'Freeware by Steve Shambles\n'
                        '(c) June 2023\n\n'
                        'Historical data supplied by\n'
                        'football-data.co.uk\n\n'
                        'Current data covers Aug 1992\n'
                        'to June 24th 2023\n\n'
                        'logo photo By Bluejam\n\n'
                        'See help file for more details.')


def open_prg_dir():
    """File browser to view contents of program folder."""
    cwd = os.getcwd()
    cwd = cwd + r'\user_saves'
    web.open(cwd)


def exit_h2h():
    """Yes-no requestor to exit program."""
    ask_yn = messagebox.askyesno('Question',
                                 'Quit Head2Head?')
    if ask_yn is False:
        return
    root.destroy()
    sys.exit()


def view_epl_table():
    """ Open web page of current EPL table from links menu. """
    web.open('https://www.premierleague.com/tables')

def current_form():
    """ Open web page of current form from links menu. """
    web.open('https://thefishy.co.uk/formtable.php?table=1')
    

def view_epl_odds():
    """ Open web page of up-coming EPL matches from links menu. """
    web.open('https://www.oddschecker.com/football/english/premier-league')


# Insert logo.
logo_frame = tk.LabelFrame(root)
logo_image = Image.open(r'data/logo.jpg')
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = tk.Label(logo_frame, image=logo_photo)
logo_label.logo_image = logo_photo
logo_label.grid(padx=2, pady=2)
logo_frame.grid(row=0, column=0, padx=8, pady=8)

# Create and populate combo boxes.
combo_frame = tk.LabelFrame(root)
home_team_label = ttk.Label(combo_frame, text='Home Team')
away_team_label = ttk.Label(combo_frame, text='Away Team')
home_team_label.grid(row=0, column=0, padx=10, pady=10)
away_team_label.grid(row=0, column=2, padx=10, pady=10)
home_team_combo = ttk.Combobox(combo_frame, values=Fs.team_names)
away_team_combo = ttk.Combobox(combo_frame, values=Fs.team_names)
home_team_combo.grid(row=1, column=0, padx=45, pady=(0, 25))
away_team_combo.grid(row=1, column=2, padx=20, pady=(0, 25))

# Set initial teams in combo boxes
home_team_combo.current(44)  # spurs.
away_team_combo.current(0)   # arse.

get_team_selections()
combo_frame.grid(row=2, column=0, padx=8, pady=8, sticky='ew')

# Create get stats button.
btn_frame = tk.Frame(root)
get_stats_btn = tk.Button(btn_frame, bg='lime', text='Get Results',
                          command=get_stats)
get_stats_btn.grid(padx=4, pady=(8, 8))
save_csv_btn = tk.Button(btn_frame, bg='steelblue', text='Save  CSV',
                         command=save_as_csv)
save_csv_btn.grid(row=0, column=1, padx=4)
save_txt_btn = tk.Button(btn_frame, bg='indianred', text='SaveText',
                         command=save_as_text)
save_txt_btn.grid(row=0, column=2, padx=4)
btn_frame.grid(row=3, column=0, padx=8, pady=6)

# create the frame with tab
tab_frame = ttk.Notebook(root)
tab1 = ttk.Frame(tab_frame)
tab_frame.add(tab1, text='Head2Head')

# tab2 = ttk.Frame(tab_frame)
# tab_frame.add(tab2, text="Future expansion")

tab_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

# configure the grid layout
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

create_table()

# Labels to output processed data
msg_frame = tk.LabelFrame(root, bg='powderblue')
msg_lab = tk.Label(msg_frame, text='')
msg_lab.grid()
msg_frame.grid(row=5, column=0, pady=8)

msg_lab2 = tk.Label(msg_frame, text='')
msg_lab2.grid(row=1, column=0)

msg_lab3 = tk.Label(msg_frame, text='')
msg_lab3.grid(row=2, column=0)

# Drop-down menu.
# Pre-load icons for drop-down menu.
help_icon = ImageTk.PhotoImage(file=r'data/icons/help-16x16.ico')
about_icon = ImageTk.PhotoImage(file=r'data/icons/about-16x16.ico')
exit_icon = ImageTk.PhotoImage(file=r'data/icons/exit-16x16.ico')
donation_icon = ImageTk.PhotoImage(file=r'data/icons/donation-16x16.ico')
github_icon = ImageTk.PhotoImage(file=r'data/icons/github-16x16.ico')
prg_fldr_icon = ImageTk.PhotoImage(file=r'data/icons/prg-fldr-16x16.ico')

# File menu
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Menu', menu=file_menu)

file_menu.add_command(label='Help', compound='left',
                      image=help_icon, command=help_text)
file_menu.add_command(label='About', compound='left',
                      image=about_icon, command=about_menu)
file_menu.add_separator()
file_menu.add_command(label='Open user saves folder', command=open_prg_dir,
                      compound='left',
                      image=prg_fldr_icon)
file_menu.add_separator()
file_menu.add_command(label='Python source code on GitHub', compound='left',
                      image=github_icon, command=visit_github)
file_menu.add_command(label='Make a small donation via PayPal',
                      compound='left',
                      image=donation_icon, command=donate_me)
file_menu.add_separator()
file_menu.add_command(label='Exit', compound='left',
                      image=exit_icon, command=exit_h2h)
root.config(menu=menu_bar)

# Links menu.
links_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Links', menu=links_menu)
links_menu.add_command(
    label='Current EPL Table',
    command=view_epl_table)
links_menu.add_command(
    label='Current teams form',
    command=current_form)
links_menu.add_command(
    label='Betting odds for up-coming matches',
    command=view_epl_odds)
root.config(menu=menu_bar)

get_stats()

root.eval('tk::PlaceWindow . Center')
root.protocol('WM_DELETE_WINDOW', exit_h2h)


root.mainloop()
