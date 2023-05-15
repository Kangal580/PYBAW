@echo off

echo Cleaning temporary files...

REM Delete temporary files in the user's temp folder
echo Deleting temporary files in the user's temp folder...
for %%F in ("%TEMP%\*.*") do (
    del "%%F" > nul 2>&1
    if not errorlevel 1 (
        echo Deleted file: %%F
    ) else (
        echo Unable to delete file: %%F
    )
)
echo Temporary files in the user's temp folder deleted.

REM Delete temporary files in the Windows temp folder
echo Deleting temporary files in the Windows temp folder...
for %%F in ("%windir%\Temp\*.*") do (
    del "%%F" > nul 2>&1
    if not errorlevel 1 (
        echo Deleted file: %%F
    ) else (
        echo Unable to delete file: %%F
    )
)
echo Temporary files in the Windows temp folder deleted.

echo Temporary files cleaned successfully.
pause
