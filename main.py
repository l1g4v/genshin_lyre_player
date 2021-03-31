from mido import MidiFile
import win32gui, win32api, win32con
import win32com.client as comclt
import time

filename = 'song.mid'

mid = MidiFile(filename)
keymap = [None] * 100
#high
keymap[60] = 'q'
#keymap[61] = 'wfn'#sharps and flats when?
keymap[62] = 'w'
#keymap[63] = 'egm'
keymap[64] = 'e'
keymap[65] = 'r'
#keymap[66] = 'egm'
keymap[67] = 't'
#keymap[68] = 'egm'
keymap[69] = 'y'
#keymap[70] = 'egm'
keymap[71] = 'u'

#mid
keymap[72] = 'a'
#keymap[73] = 'wfn'
keymap[74] = 's'
#keymap[75] = 'wfn'
keymap[76] = 'd'
keymap[77] = 'f'
#keymap[78] = 'wfn'
keymap[79] = 'g'
#keymap[80] = 'wfn'
keymap[81] = 'h'
#keymap[82] = 'wfn'
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
        #hahaha this wont work
        #or you transpose to C Major without sharps and flats or you don't
        """while note < 60:
            note += 12
        while note > 95:
            note -= 12"""
        if keymap[note] != None:
            wsh.SendKeys(keymap[note])
        print(note)
print("Done")