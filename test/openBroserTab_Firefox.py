import webbrowser
import time
import os
import shutil
from pathlib import Path

data_folder = Path("/Users/kojayaku/Library/Application Support/Firefox/Profiles/zl6om7d6.default/")

a_website = "https://www.hotstar.com/sports/cricket/vivo-ipl-2019/kolkata-knight-riders-vs-kings-xi-punjab-m189957/live-streaming/2001710514?lang=tam"

#webbrowser.get('safari').open_new(a_website)



#run = raw_input("Start? > ")
mins = 0
# Only run if the user types in "start"
# Loop until we reach 20 minutes running
while mins != 30000:
    webbrowser.get('firefox').open_new_tab(a_website)
    print(">>>>>>>>>>>>>>>>>>>>>", mins)
    # Sleep for a minute
    time.sleep(240)
    # Increment the minute total
    mins += 1
    os.system("killall -9 'firefox'")
    if os.path.isfile(data_folder):
        shutil.rmtree(data_folder)
    #os.remove(data_folder)

# Bring up the dialog box here

