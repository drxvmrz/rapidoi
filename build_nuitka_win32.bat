python -m nuitka ^
--mode=standalone ^
--enable-plugin=pyside6 ^
--include-package=PySide6.QtCore ^
--include-package=PySide6.QtWidgets ^
--include-package=PySide6.QtGui ^
--include-qt-plugins=platforms,styles,imageformats ^
--include-data-file=./icon.png=./icon.png ^
--output-dir=dist ^
--msvc=latest ^
--windows-icon-from-ico=./icon.png ^
--windows-disable-console ^
--output-filename=rapidoi.exe ^
main.py
pause