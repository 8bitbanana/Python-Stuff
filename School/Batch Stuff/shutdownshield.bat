@echo off
title SHUTDOWN SHIELD
set blocked=0
:top
@shutdown /a
if not %errorlevel%==1116 set /a blocked=%blocked%+1
echo Shutdown prevention active
echo Blocked - %blocked%
@ping 0 \w 10
cls
goto top