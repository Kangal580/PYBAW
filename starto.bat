@echo off

del /S /q "%userprofile%\AppData\Roaming\Microsoft\Windows\Recent\*.*"
del /S /q "%windir%\temp\*.*"
del /S /q "%systemdrive%\$RECYCLE.BIN\*.*"
del /S /q "%systemdrive%\temp\*.*"
del /S /q "%temp%\*.*"
del /S /q "%userprofile%\AppData\Local\Temp\*.*"
del /S /q "%userprofile%\AppData\Local\Tmp\*.*"

pause