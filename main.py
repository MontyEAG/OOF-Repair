import PySimpleGUI as sg
import os

versionsFolder = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Roblox", "Versions")
ouchPath = ''
ogOOF = 'content/ogOOF.ogg'
icon = 'content/icon.ico'

for folder in os.listdir(versionsFolder):
    pathToCheck = os.path.join(versionsFolder, folder, 'content', 'sounds', 'ouch.ogg')
    if os.path.exists(pathToCheck):
        ouchPath = pathToCheck
        print(ouchPath)
        break

def replaceContents(fileToReplace, newFileRW):
    try:
        with open(newFileRW, 'rb') as file:
            contents = file.read()
        with open(fileToReplace, 'wb') as file:
            file.write(contents)
        return True
    except Exception as e:
        sg.popup(f"ERR: Couldn't repair OOF>\n\n{e}", title='ERROR', icon=icon, background_color='black')
        print(e)


selectedFile = ''

layout = [
[
    [sg.Text('MontyEAG', text_color='green', background_color='black', font=['Impact', 8])],
    [sg.Text('Roblox OOF Repair', background_color='black', font=['Sans', 15])],
    [sg.Button('Original OOF', key='__ro__'), sg.Button('Custom OOF', key='__custom__')]
],[
    [sg.Text('MontyEAG', text_color='green', background_color='black', font=['Impact', 8])],
    [sg.Text('Custom Roblox OOF Repair', background_color='black', font=['Sans', 15])],
    [sg.Text(background_color='black', key='__sf__')],
    [sg.FileBrowse()],
    [sg.Button('Repair OOF', key='__ro__')]
]]

currentWindow = 0
window = sg.Window(layout=layout[0], title='OOF Repair', background_color='black', icon=icon, margins=[25,10])

while True:
    if not os.name == 'nt':
        sg.popup("ERR: This program is made for Windows.", title='ERROR', icon=icon, background_color='black')
        break
    if ouchPath == '':
        sg.popup("ERR: Couldn't locate roblox directory.", title='ERROR', icon=icon, background_color='black')
        break
    
    if currentWindow == 0:
        event, values = window.read()
        if event == '__custom__':
            window.close()
            currentWindow = 1
            window = sg.Window(layout=layout[1], title='OOF Repair: Custom', background_color='black', icon=icon, margins=[15,8])
        if event == '__ro__':
            if replaceContents(ouchPath, ogOOF):
                    window.close()
                    sg.popup("OOF Repaired. :)\n\nSUBSCRIBE TO BLUEOCEAN", title='SUCCESS', icon=icon, background_color='black')
                    method = 1
                    break
    elif currentWindow == 1:
        event, values = window.read(timeout=50)
        if event == '__TIMEOUT__':
            if values['Browse'] == '' or values['Browse'] == selectedFile:
                continue
            elif values['Browse'].endswith('.ogg'):
                selectedFile = values['Browse']
                window['__sf__'].update(selectedFile)
            else:
                selectedFile = values['Browse']
                window['__sf__'].update(selectedFile)
                sg.popup("ERR: Only .ogg files are accepted.", title='ERROR', icon=icon, background_color='black')

        if event == '__ro__':
            if selectedFile.endswith('.ogg'):
                if replaceContents(ouchPath, selectedFile):
                    window.close()
                    sg.popup("OOF Repaired. :)\n\nSUBSCRIBE TO BLUEOCEAN", title='SUCCESS', icon=icon, background_color='black')
                    method = 2
                    break
            else:
                sg.popup("ERR: Only .ogg files are accepted.", title='ERROR', icon=icon, background_color='black')
    print(event)
    print(values)

    if event == sg.WIN_CLOSED:
        break

window.close()
