# Head2Head V0.80.02 (updated June 24th 2023)
-------------------------------------------
A database of every English Premier League football match with head2head stats and tentative match prediction.

Historical data supplied by https://football-data.co.uk, with thanks. Current data covers Aug 1992 to June 24th 2023.

logo photo attribution: Thank you to Bluejam - Self-photographed, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=78153606

This program is Freeware and the source code comes under the MIT Licence, but the program as a whole remains (c) Steve Shambles.


V0.81: Added Luton to list of teams.

V0.82: Updated results to end of season 22-2023, + updated help file + some minor tinkering.

![Alt Text](https://github.com/Steve-Shambles/head2head/blob/main/data/h2h_v0802_screenshot.png)


Head2Head is a desktop app written for Windows PC's but the Python source code should work on MAC and Linux too (not tested),
it contains every single English Premier league result from the day of the league's inception back in August 1992 to June 24th 2023.

No cup fixtures are included at all, strictly EPL only.

You can choose a home team and an away team (all 51 teams that have ever played in the EPL are selectable) and after clicking on
"Get Stats" H2H will show a table of all the matches played (if any) for that exact fixture. 

Note the exact fixture, which means if you select say, Tottenham V West Ham you will not be given West Ham V Tottenham results like
almost all other sites on the web do, that discolours the data in my opinion because home advantage really does count for the majority of teams,
with the rare exception.

Cup matches mixed in would also make the data worthless. As we all know cup matches are totally different to EPL matches as a lot of the time
weakened teams are played in the cups, especially in the early rounds. 

At the bottom of the program you will see some statistics gleaned from the displayed results and a tentative prediction for the next time 
that fixture is to be played.

Of course, this prediction is based solely on history and does not take into account current form, injuries, manager etc. so take the predictions
with a pinch of salt on its own and use the history as part of your prediction strategy, not your whole prediction strategy.

To help you quickly look up current EPL form I have provided links (see the links menu top left of the program window)to reliable websites
with the EPL table, current form table and bookmaker odds for forth-coming matches
which can all give good indicators of current form.

If you wish you can save the resultant H2H data as a CSV file (you can open a csv file in a spreadsheet) or just plain text by
clicking the appropriate button.

You can quickly view, edit or delete those saved files in your file browser, if you go to the drop-down menu, top left of the program window,
you can select "open user saves folder" to achieve this quickly.



The Python source code.

Though I am fully aware my programming leaves a lot to be desired (from a professional point of view,
I am a hobbyist, not a pro, I do this for fun and probably only I can understand the spaghetti code I have created here. 
I have an ADHD brain and it works different to most other people, you will be scratching your heads with my code I assure you :-)


Unapologetically, Steve Shambles June 2023.




Make your own executable:
(note: Windows defender usually deletes any python executable it can get its hands on, so be prepared for that nonsense.)

If you want to create your own executable file with pyinstaller (pip install pyinstaller) first and in your python CLI copy and paste this:

pyinstaller head2head_v0802.py -n head2head_v0802 --windowed --onefile


to run, the exe will need the complete data folder in same dir as the exe.

If you prefer you can take a chance and download a zip of my executable and all files required, just unzip and run the exe (27Mb)

https://drive.google.com/file/d/1c7clon3EHvLmY9rmoPO2qdsyAB6ZuRot/view?usp=sharing




