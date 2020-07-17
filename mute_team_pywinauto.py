from pywinauto.application import Application
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
temp = Application().start(r"C:\Windows\System32\SndVol.exe")
#print(app.windows())
app = temp['Volume Mixer - Speakers (Realtek High Definition Audio)']
mb=app.child_window(title="Mute for Microsoft Teams", class_name="ToolbarWindow32")
mb.click_input()
app.type_keys("%{F4}") # Alt-F4





