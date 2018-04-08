title Starting...
@echo off
color 0a
mode con lines=3 cols=16
:top
title %time:~0,8%
echo.
echo     %time:~0,8%
choice /c SQ /n /t 1 /d S
if errorlevel 2 goto quit
if errorlevel 1 goto top
:quit