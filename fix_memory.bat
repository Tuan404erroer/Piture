@echo off
echo ========================================
echo GIAI PHONG RAM VA CHAY APP
echo ========================================
echo.
echo Dang giai phong RAM...
echo.

REM Giai phong RAM bang cach clear standby list
echo Clearing standby memory...
echo.|set /p="3" > memory.txt
type memory.txt > C:\Windows\System32\PurgeStandbyList.exe 2>nul
del memory.txt

echo.
echo Dang chay Kurzgesagt AI...
echo.
echo ========================================
echo.

py -3.11 web_app.py

pause
