
@echo off
cls
del /Q %LOCALAPPDATA%\Microsoft\Windows\INetCache\IE\*.* >nul 2>&1
del /Q "%SYSTEMROOT%\Downloaded Program Files\*.*" >nul 2>&1
rd /s /q %SYSTEMDRIVE%\$Recycle.bin >nul 2>&1
del /Q %TEMP%\*.* >nul 2>&1
del /Q %SYSTEMROOT%\Temp\*.* >nul 2>&1
del /Q %SYSTEMROOT%\Prefetch\*.* >nul 2>&1
cls