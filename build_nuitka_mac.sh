#!/bin/bash
python3 -m nuitka \
--standalone \
-onedir \
--enable-plugin=pyside6 \
--macos-create-app-bundle \
--include-package=PySide6.QtCore \
--include-package=PySide6.QtWidgets \
--include-package=PySide6.QtGui \
--output-dir="./dist" \
--macos-app-icon="./icon.png" \
--macos-app-name="Rapidoi" \
--output-file="Rapidoi.app" \
./apexsymm_gui/main.py
echo "Done! Press ENTER to continue..."
read
