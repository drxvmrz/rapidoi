import os

####################################################

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from gui_scripts.settings_window import *

####################################################

class Settings:
    def __init__(self):
        self.download_path = ""
        self.sources = []
        self.default_source = ""

    def set_default_source(self, new_source: str):
        self.default_source = new_source

    def set_download_path(self, new_path):
        self.download_path = new_path

    def add_source(self, source):
        self.sources.append(source)

    def delete_source(self, source):
        self.sources.remove(source)

    def init_settings_file(self):
        with open("settings", "w") as file:
            file.write("download_path=\n")
            file.write("sources=doi.org;\n")
            file.write("default=doi.org")

    def load_settings_from_file(self):
        try:
            with open("settings", "r") as file:
                lines = file.readlines()
                for line in lines:
                    line = line.replace("\n","")
                    splitted = line.split("=")

                    key = splitted[0]
                    val = splitted[1]
                    if key == "download_path":
                        self.download_path = val
                    if key == "sources":
                        splitted_list = val.split(";")
                        for src in splitted_list:
                            if src == "" or src is None: continue
                            self.add_source(src)
                    if key == "default":
                        self.default_source = val
            return True
        except:
            return False

    def save_settings_into_file(self):
        with open("settings", "w") as file:
            file.write(f"download_path={self.download_path}\n")

            file.write(f"sources=")
            for src in self.sources:
                file.write(f"{src};")
            file.write(f"\ndefault={self.default_source}")

    def is_settings_initialized(self):
        return os.path.exists("settings")
        
####################################################

class SettingsWin(QWidget):
    settings_changed = Signal()

    def __init__(self, settings: Settings):
        super().__init__()

        self.settings = settings

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.data_model = QStringListModel()
        self.ui.list_srcs.setModel(self.data_model)

        self.ui.btn_add_src.clicked.connect(self.add_new_src)
        self.ui.btn_rem_src.clicked.connect(self.remove_src)
        self.ui.list_srcs.doubleClicked.connect(self.edit_src)
        self.data_model.dataChanged.connect(self.update_sources)

        self.ui.btn_browse_path.clicked.connect(self.browse_path)
        self.ui.line_path.textChanged.connect(self.path_changed)

    def add_new_src(self):
        row = self.data_model.rowCount()
        self.data_model.insertRow(row)
        index = self.data_model.index(row)

        default_text = f"Введите новый источник!"
        self.data_model.setData(index, default_text)

        self.ui.list_srcs.edit(index)
        self.ui.list_srcs.scrollTo(index)

    def remove_src(self):
        indexes = self.ui.list_srcs.selectedIndexes()
        
        if not indexes:
            # Если ничего не выбрано, удаляем последний элемент
            row = self.data_model.rowCount() - 1
            if row >= 0:
                self.data_model.removeRow(row)
            return
        
        # Удаляем все выбранные элементы (с конца)
        rows_to_delete = sorted({idx.row() for idx in indexes}, reverse=True)
        for row in rows_to_delete:
            self.data_model.removeRow(row)

    def edit_src(self, index):
        self.ui.list_srcs.edit(index)
        self.settings.sources[index.row()] = index.data()

    def update_sources(self):
        current_sources = self.data_model.stringList()

        if current_sources != self.settings.sources:
            self.settings.sources = current_sources
            self.settings_changed.emit()
            self.settings.save_settings_into_file()
            print(f"Источники обновлены: {self.settings.sources}")

    def draw_settings(self):
        self.ui.line_path.setText(self.settings.download_path)
        self.data_model.setStringList(self.settings.sources)

    def browse_path(self):
        dir_path = QFileDialog.getExistingDirectory(caption="Directory for downloaded articles")
        self.ui.line_path.setText(dir_path)
        self.settings.save_settings_into_file()

    def path_changed(self):
        if os.path.exists(self.ui.line_path.text()):
            self.ui.line_path.setStyleSheet("color: #000000")
        else:
            self.ui.line_path.setStyleSheet("color: #ff4f00")
        self.settings.download_path = self.ui.line_path.text()
    