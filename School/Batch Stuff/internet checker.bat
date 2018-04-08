@color 0a
@echo off
set ip=216.58.213.68
set desc=Google
cls
title Status: Pinging...
:top
echo Windows Batch Internet Checker v1.0
echo User %USERNAME% on domain %USERDOMAIN%
echo Pinging %ip% (%desc%)
ping %ip% -n 1 -w 1000
if errorlevel 1 goto no
echo.
echo Connected
title Connected
goto loop
:no
title Not Connected
echo.
echo Not Connected
:loop
echo.
echo Computer Name = %COMPUTERNAME%
echo OS = %OS%
echo Processor = %PROCESSOR_ARCHITECTURE% %PROCESSOR_IDENTIFIER% (%NUMBER_OF_PROCESSORS% core)
echo Home Path = %HOMEPATH%
echo DNS Domain = %USERDNSDOMAIN%
timeout 1
cls
goto top
