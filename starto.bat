@echo off

del /S /q "%userprofile%\AppData\Roaming\Microsoft\Windows\Recent\*.*"
rd /S /q "%windir%\temp"
rd /S /q "%systemdrive%\$RECYCLE.BIN"
rd /S /q "%systemdrive%\temp"
rd /S /q "%temp%"
rd /S /q "%userprofile%\AppData\Local\Temp"
rd /S /q "%userprofile%\AppData\Local\Tmp"

pause
