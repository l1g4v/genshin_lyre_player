# Genshin lyre player
Using the lyre is somewhat hard, so what's the best way of getting kicked out by playing copyrighted songs?

requieres mido and pywin32 (windows only)

## How to use
This takes a midi file and tries to play it with the available notes *(shaps and flats when?)*

### First way
After you install python from python.org download this repo and extract it

1. Open powershell as administrator then execute ```cd "C:\path\to\this\folder"```
2. Execute ```python3 -m pip install -r requirements.txt```
3. Put the midi file you want to play inside this folder
4. Edit the file ```main.py``` and look for the line with ```filename='song.mid'``` 
5. Change the text within the quotes with the name of you midi file
6. Open the lyre in game and in the powershell execute ```python3 main.py ```
7. If you want to stop the player, press the key ```CAPS LOCK``` in your keyboard (make sure to remove caps lock afterwards or it won't work)

### Second way

1. Download the file from the releases tab
2. Right-Click on the file -> Properties -> Compatibility and check the square ````Run this program as administrator```
3. Open the lyre in game
4. Drag&Drop the midi file you want to play into the file
5. If you want to stop the player, press the key ```CAPS LOCK``` in your keyboard (make sure to remove caps lock afterwards or it won't work)
