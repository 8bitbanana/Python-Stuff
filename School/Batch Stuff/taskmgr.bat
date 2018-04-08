@echo off 
color 0a
mode con lines=10000
:top
cls
tasklist
choice /c sqk /t 1 /n /d s
if %errorlevel%==3 goto kill
if %errorlevel%==2 goto quit
goto top
:kill
set /p killedtask="taskkill /f /pid "
taskkill /f /pid %killedtask%
pause
goto top
:quit