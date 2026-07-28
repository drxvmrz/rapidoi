####################################################

import os
import sys
import webbrowser

####################################################

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from settings import *
from download_checker import *
from gui_scripts.main_window import *

####################################################

class MainWin(QMainWindow):
    # Сигнал об открытии новой статьи, передается doi
    file_opened = Signal(str)

    def __init__(self, settings: Settings, settings_window: SettingsWin):
        super().__init__()

        self.current_doi_file_path = ""

        self.settings = settings
        self.settings_win = settings_window

        self.checked_thread = DownloadCheckerAndRenamer(self.settings.download_path)
        self.checked_thread.start()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setGeometry(100, 100, 500, 600)
        
        self.ui.act_open_settings.setMenuRole(QWidgetAction.MenuRole.NoRole)

        # Список для хранения DOI
        self.doi_list = []
        self.doi_buttons = []

        # Срабатывает сигнал, когда изменяются источники, нужен для обновления комбо-бокса
        self.settings_win.settings_changed.connect(self.new_srcs_added)
        self.ui.cmb_source.textActivated.connect(self.set_new_default_src)

        # Действие меню-бара
        self.ui.act_open_doi.triggered.connect(self.get_dois_from_file)
        self.ui.act_save_doi.triggered.connect(self.save_current_list_into_file)
        self.ui.act_open_settings.triggered.connect(self.open_settings_window)

        # Кнопки главного окна
        self.ui.btn_open_doi.clicked.connect(self.get_dois_from_file)
        self.ui.btn_save_doi.clicked.connect(self.save_current_list_into_file)

    def new_srcs_added(self):
        self.ui.cmb_source.clear()
        for src in self.settings.sources:
            self.ui.cmb_source.addItem(src)
        self.ui.cmb_source.setCurrentText(self.settings.default_source)

    def set_new_default_src(self, new_src):
        self.settings.set_default_source(new_src)
        self.settings.save_settings_into_file()

    def open_settings_window(self):
        self.settings_win.show()
        self.settings_win.draw_settings()

    def get_dois_from_file(self):
        meta = QFileDialog.getOpenFileName(caption="Open DOI list text file", filter="text (*.txt);;")
        path = meta[0]
        if path == "" or path is None: return

        self.current_doi_file_path = path
        with open(path, "r") as file:
            file_lines = file.readlines()
            for line in file_lines:
                doi = line.replace("\n", "")
                self.doi_list.append(doi)
                self.create_doi_button(doi)
    
    @staticmethod
    def transform_doi_to_good_name(doi):
        transformed = doi.replace(":", "@@").replace("/", "@").replace(";", "@@@")
        return transformed

    def on_doi_button_clicked(self, button: QPushButton):
        doi = button.property("doi")
        good_doi = MainWin.transform_doi_to_good_name(doi)
        self.checked_thread.set_current_name(good_doi)
        
        current_web_source = self.ui.cmb_source.currentText()
        webbrowser.open(f"https://{current_web_source}/{doi}")
        self.remove_button(button)
        self.save_current_list_into_file()

    def create_doi_button(self, doi):
        new_btn = QPushButton(doi)
        new_btn.setStyleSheet("""
            QPushButton {
                padding: 10px;
                margin: 3px;
                text-align: left;
                border: 1px solid #ccc;
                border-radius: 10px;
                background-color: #f0f0f0;
            }
            QPushButton:hover {
                background-color: #e0e0ff;
                border: 1px solid #8888ff;
            }""")
        new_btn.setProperty("doi", doi)
        new_btn.clicked.connect(lambda: self.on_doi_button_clicked(new_btn))
        self.doi_buttons.append(new_btn)

        self.ui.layout_dois_list.addWidget(new_btn)

    def remove_button(self, button: QPushButton):
        doi = button.property("doi")
        button.clicked.disconnect()
        self.ui.layout_dois_list.removeWidget(button)
        button.deleteLater()
        self.doi_buttons.remove(button)
        self.doi_list.remove(doi)
        
    def save_current_list_into_file(self):
        if not os.path.exists(self.current_doi_file_path): return
        
        with open(self.current_doi_file_path, "w") as file:
            for doi in self.doi_list:
                file.write(f"{doi}\n")
        
        print(f"**Saved {len(self.doi_list)} DOI entries into {self.current_doi_file_path} file")

    def closeEvent(self, event: QCloseEvent):
        print("**Stopping the checker thread!")
        self.checked_thread.stop()
        self.checked_thread.wait(1)
        print("**Saving current DOI-file!")
        self.save_current_list_into_file()
        print("**GOOD BYE!")

####################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Инициализация настроек (если требуется) и их загрузка
    settings = Settings()
    if not settings.is_settings_initialized(): settings.init_settings_file()
    settings.load_settings_from_file()

    # Создаем окно с настройками
    settings_window = SettingsWin(settings)

    # Теперь можно спокойно запускать главное окно с загруженными настройками
    main_window = MainWin(settings, settings_window)
    main_window.show()
    main_window.new_srcs_added()
    
    sys.exit(app.exec())