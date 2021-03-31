"""
For pyinstaller
"""
from mido import MidiFile
import win32gui, win32api, win32con
import win32com.client as comclt
import time
import sys

filename = droppedFile = sys.argv[1]
mid = MidiFile(filename)
keymap = [None] * 100
#high
keymap[60] = 'q'
keymap[62] = 'w'
keymap[64] = 'e'
keymap[65] = 'r'
keymap[67] = 't'
keymap[69] = 'y'
keymap[71] = 'u'
#mid
keymap[72] = 'a'
keymap[74] = 's'
keymap[76] = 'd'
keymap[77] = 'f'
keymap[79] = 'g'
keymap[81] = 'h'
keymap[83] = 'j'
#low
keymap[82] = 'z'
keymap[84] = 'x'
keymap[86] = 'c'
keymap[87] = 'v'
keymap[89] = 'b'
keymap[91] = 'n'
keymap[93] = 'm'

hwnd=win32gui.FindWindow(None, "Genshin Impact")
win32gui.SetForegroundWindow(hwnd)
wsh = comclt.Dispatch("WScript.Shell")

for msg in mid.play():
    if win32api.GetAsyncKeyState(win32con.VK_CAPITAL):
        break
    if(msg.type == 'note_on'):
        note = msg.note
        if keymap[note] != None:
            wsh.SendKeys(keymap[note])