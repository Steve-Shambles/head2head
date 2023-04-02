# Head2Head V0.80 (updated 17th March 2023)
-------------------------------------------
A database of every English Premier League football match with head2head stats and tentative match prediction.

Historical data supplied by https://football-data.co.uk, with thanks. Current data covers Aug 1992 to March 14th 2023.

logo photo attribution: Thank you to Bluejam - Self-photographed, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=78153606

This program is Freeware and the source code comes under the MIT Licence, but the program as a whole remains (c) Steve Shambles.


Changes since last version (0.74)
V0.75. Added clean sheets statitics.

V0.76. Added 0.75 of a goal for home advantage in prediction formula.

V0.77. Added home and away pts stat.

V0.78. Added match outcome prediction to correct score prediction for clarity.
       Resized logo img as running out of vertical screen space.
       
V0.79: Added white bg to break up stats text ands make more readable.+ code tidy up.

V0.80: Added links menu to quickly see EPL table and odds of up-coming matches.
       Added when a fixture that has never been played before
       clear stats box and show relevent message.
       Redone logo img for better quality.

![Alt Text](https://github.com/Steve-Shambles/head2head/blob/main/h2h-0.74-screenshot1.png)

Head2Head is a desktop app written for Windows PC's but should work on MAC and Linux too (not tested)
it contains every single English Premier league result from the day of the league's inception back in August 1992
to march 14th 2023.

You can choose a home team and an away team (all 50 teams that have ever played in the EPL are selectable) 
and H2H will show a table of all the matches played for that exact fixture.

At the bottom of the program you will see some statistics gleaned from the displayed results and a tentative prediction
for the next time that fixture is to be played.

Of course this prediction is based solely on history and cannot take into account current form, injuries, manager etc.
so take the predictions with a pinch of salt.

You can save the resultant data as CSV or plain text by clicking the appropriate button.

You can quickly view edit or delete those saved files in your file browser, if you go to the drop-down menu,
top left of the program, you can select "open user saves folder".

Though I am fully aware my programming leaves a lot to be desired (from a professional point of view, I am a hobbyist not a pro)
and probably only I can work with the spaghetti that I have created here as I have an ADHD brain and it works 
different to most other peoples!

Anyway:

If you want to create your own executable file with pyinstaller (pip install pyinstaller) first:

pyinstaller head2head_v074.py -n head2head_v074 --windowed --onefile

to run, the exe will need the complete data folder in same dir as the exe.


or download pre-made Windows exe 25Mb:  https://drive.google.com/file/d/1LR6ft0LdTS0tmDOIm5fm3nQhQI9bavSp/view?usp=share_link

download includes all required files, just unzip it and double click the exe file.



Steve Shambles.
