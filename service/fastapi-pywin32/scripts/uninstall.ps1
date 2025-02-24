Get-NetTCPConnection -LocalPort 8000 | Stop-Process -Force -Id {$_.OwningProcess}
./dist/service/service.exe remove
Remove-Item -Recurse .\build
Remove-Item -Recurse .\dist
Remove-Item .\service.spec