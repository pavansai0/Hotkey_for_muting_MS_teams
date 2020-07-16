from pywinauto.application import Application
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
temp = Application().start(r"C:\Windows\System32\SndVol.exe")
#print(app.windows())
app = temp['Volume Mixer - Speakers (Realtek High Definition Audio)']
app.child_window(title="Mute for Discord",class_name="ToolbarWindow32").click_input()
app.type_keys("%{F4}") # Alt-F4


