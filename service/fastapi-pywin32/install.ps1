./dist/service/service.exe remove
Remove-Item -Recurse .\build
Remove-Item -Recurse .\dist
Remove-Item .\service.spec
python .venv/Scripts/pywin32_postinstall.py -install
pyinstaller --hidden-import=win32timezone service.py
./dist/service/service.exe install
./dist/service/service.exe start