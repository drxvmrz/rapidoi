####################################################

import os

####################################################

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

####################################################

class DownloadCheckerAndRenamer(QThread):
    def __init__(self, dir_to_check: str):
        super().__init__()
        self.running = True
        self.dir_to_check = dir_to_check
        self.indexed_files = set()
        self.new_name = ""

    def set_current_name(self, new_name):
        self.new_name = new_name

    def index_files(self):
        new_files_set = set()
        for root, dirs, files in os.walk(self.dir_to_check):
            if root != self.dir_to_check: break
            for file in files:
                if not file.endswith(".pdf"): continue
                new_files_set.add(file)
        return new_files_set

    def run(self):
        # первая индексация файлов
        self.indexed_files = self.index_files()
        while self.running:
            new_set = self.index_files()
            new_pdf_set = new_set.difference(self.indexed_files)
            if len(new_pdf_set) != 1: continue
            new_pdf_file = new_pdf_set.pop()
            new_file_old_path = os.path.join(self.dir_to_check, new_pdf_file)
            new_file_new_path = os.path.join(self.dir_to_check, f"{self.new_name}.pdf")
            os.rename(new_file_old_path, new_file_new_path)
            self.indexed_files = self.index_files()

    def stop(self):
        self.running = False
