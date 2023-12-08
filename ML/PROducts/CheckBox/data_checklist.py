import sys
from PyQt6 import QtGui
from PyQt6.QtWidgets import (
    QApplication,
    QFileDialog,
    QWidget,
    QGridLayout,
    QLineEdit,
    QPushButton,
    QLabel,
    QCheckBox
)
from pathlib import Path


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # window settings
        self.setWindowTitle("Check_box")
        self.setWindowIcon(QtGui.QIcon(r'overall_decision_icon_149904.png'))
        self.setGeometry(100, 100, 400, 100)

        # layout setting
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # dir text
        self.filename_edit = QLineEdit()
        self.filename_edit.returnPressed.connect(self.construct_box)

        # dir selection
        direct_browse = QPushButton('Browse')
        direct_browse.clicked.connect(self.open_dir_dialog)

        # confirmation
        check_boxes_construct = QPushButton('OK')
        check_boxes_construct.clicked.connect(self.construct_box)

        # widget setup
        self.layout.addWidget(QLabel('File:'), 1, 0)
        self.layout.addWidget(self.filename_edit, 1, 1)
        self.layout.addWidget(direct_browse, 1, 2)
        self.layout.addWidget(check_boxes_construct, 2, 2)

        self.show()

        # dict for {file : button}
        self.filenames_buttons_dict = {}

    def construct_box(self):
        from os import listdir
        from os.path import exists
        self.catalogue = self.filename_edit.text()[self.filename_edit.text().rfind('\\') + 1:]
        if exists(f'{self.catalogue}.json'):
            ...
        else:
            self.content = {f for f in listdir(self.filename_edit.text())}
            for file in self.content:
                if file not in self.filenames_buttons_dict:
                    cbutton = QCheckBox(f"{file}")
                    self.filenames_buttons_dict[file] = cbutton
                    # cbutton.setChecked(True)
                    # cbutton.animal = "Cat"
                    # cbutton.toggled.connect(self.onClicked)
                    self.layout.addWidget(cbutton)
                else:
                    pass
            check_boxes_save = QPushButton('SAVE')
            check_boxes_save.clicked.connect(self.save_result)
            self.layout.addWidget(check_boxes_save, 2, 0)

    def open_dir_dialog(self):
        direct = str(QFileDialog.getExistingDirectory(self, "Select Directory", "Select directory"))
        if direct:
            path = Path(direct)
            self.filename_edit.setText(str(path))

    def save_result(self):
        import  json
        save_dict = {}
        for file in self.content:
            save_dict[file] = self.filenames_buttons_dict[file].checkState()
        with open(f'{self.catalogue}.json', 'w', encoding='utf-8') as file:
            json.dump(save_dict, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

# %%
