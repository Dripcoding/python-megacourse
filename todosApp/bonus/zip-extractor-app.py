import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme('Black')

# row 1
label1 = sg.Text('Select archive:')
input1 = sg.Input()
choose_button1 = sg.FileBrowse('Choose', key='archive')

# row2
label2 = sg.Text('Select dest dir:')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose', key='folder')

# row3
extract_button = sg.Button('Extract')
output_label = sg.Text(key='output', text_color='green')

# window
window = sg.Window('Archive Extractor',
                  layout=[[label1, input1, choose_button1],
                          [label2, input2, choose_button2],
                          [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    archivepath = values['archive']
    dest_dir = values['folder']
    extract_archive(archivepath, dest_dir)
    window['output'].update(value='Extraction completed')

window.read()
window.close()