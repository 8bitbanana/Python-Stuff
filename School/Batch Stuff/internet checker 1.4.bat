set version=1.4
set features=q,c,restart,quit,cmd,rc,features,help,call

set snakerun=False
set usernameyear=%USERNAME:~-2%

::PRESETS
set psnake="\\[redacted]\14$\ecrooks14\My Documents\Batch Projects\snake.bat"
set pslide="\\[redacted]\14$\ecrooks14\My Documents\Batch Projects\slide.bat"
set pcmd="\\[redacted]\14$\ecrooks14\My Documents\Batch Projects\cmd.bat"
set pinternet="\\[redacted]\14$\ecrooks14\My Documents\Batch Projects\internet checker.bat"
set phomedir="\\[redacted]\14$\ecrooks14\My Documents\Batch Projects\"
set customhomedir="\\[redacted]\%usernameyear%$\%USERNAME%\My Documents\"
set pyahtzee="\\[redacted]\14$\ecrooks14\My Documents\Batch Projects\yahtzee.bat"
set ptime="\\[redacted]\14$\ecrooks14\My Documents\Batch Projects\time.bat"
set ptaskmgr="\\[redacted]\14$\ecrooks14\My Documents\Batch Projects\taskmgr.bat"

:startmain
@color 0a
@echo off
cls
:chooseip
if %snakerun%==True mode CON LINES=28
set ip=google.com
title WBIC %version%
echo Windows Batch Internet Checker v%version%
echo.
echo Choose the IP address to ping, type nothing to default
echo to google.com. Hit enter to continue.
echo You can also enter normal domains, like example.com or
echo www.example.com.
echo.
set /p ip=">>> "
if %ip%==q goto quit
if %ip%==c goto startmain
if %ip%==restart goto B
if %ip%==quit goto quit
if %ip%==easteregg goto egg
if %ip%==cmd goto cmd
if %ip%==rc goto rc
if %ip%==features goto fl
if %ip%==help goto fl
if %ip%==call goto callbatch
cls
:top
if %snakerun%==True mode CON LINES=40
title Pinging %ip%...
set delay=0
echo Windows Batch Internet Checker v%version%
echo User %USERNAME% on domain %USERDOMAIN%
echo Pinging %ip%...
ping %ip% -n 1 -w 1000
if errorlevel 1 goto no
echo.
echo Connected
title Connected
goto loop
:no
set delay=1
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
echo.
echo Hold C to restart or Q to quit
@timeout %delay%
@choice /C nqc /T 1 /D n /N /M ""
if errorlevel 3 goto repeat
if errorlevel 2 goto quit
cls
goto top
:repeat
cls
timeout 2 /NOBREAK
cls
goto chooseip
:egg
cls
color 0d
echo.
echo EASTER EGG!!!!!11
echo.
echo Windows Batch Internet Checker v%version%
echo By Ethan Crooks
echo.
timeout -1
color 0a
cls
goto chooseip
:cmd
@echo off
title WBIC %version% CMD
cls
:A
set /P the="%cd%>" 
if %the:~0,2%==cd goto justrunit
if %the:~0,2%==qu goto checkforcommand
if %the:~0,2%==ex goto checkforcommand
if %the:~0,2%==my goto checkforcommand
:justrunit
%the%
goto A
:checkforcommand
if "%the%"=="quit" goto B
if "%the%"=="exit" goto B
if "%the%"=="myhome" goto myhomecmd
if "%the%"=="cd" goto forcecdcmd
goto justrunit
:myhomecmd
pushd "\\[redacted]\%usernameyear%$\
cd %USERNAME%
cd "My Documents"
goto A
:forcecdcmd
set /p cdinput="> "
cd %cdinput%
goto a
:rc
set /p command="> "
%command%
cls
goto chooseip
:B
cls
goto chooseip
:fl
cls
echo WBIC V%version% FEATURES
echo %features%
echo.
timeout -1
cls
goto chooseip
timeout -1
:callbatch
cls
title Calling...
echo CALL
echo.
echo Type a file directory to call
echo.
set /p callinput="> "
cls
if "%callinput%"=="snake.bat" goto csnake
if "%callinput%"=="slide.bat" goto cslide
if "%callinput%"=="cmd.bat" goto ccmd
if "%callinput%"=="internet checker.bat" goto cinternet
if "%callinput%"=="ecrooks14" goto chomedir
if "%callinput%"=="myhome" goto customhome
if "%callinput%"=="yahtzee.bat" goto cyahtzee
if "%callinput%"=="time.bat" goto ctime
if "%callinput%"=="taskmgr.bat" goto ctaskmgr
call "%callinput%"
cls
goto chooseip
:ctaskmgr
set snakerun=True
call %ptaskmgr%
if errorlevel 1 set snakerun=False
cls
goto chooseip
:csnake
set snakerun=True
call %psnake%
if errorlevel 1 set snakerun=False
mode CON COLS=80 LINES=28
cls
goto chooseip
:cslide
call %pslide%
cls
goto chooseip
:cyahtzee
set snakerun=True
call %pyahtzee%
if errorlevel 1 set snakerun=False
color 0a
mode con cols=80 lines=28
cls
goto chooseip
:ccmd
call %pcmd%
cls
goto chooseip
:ctime
set snakerun=True
call %ptime%
goto chooseip
:cinternet
call %pinternet%
cls
goto chooseip
:chomedir
echo CALL ECROOKS14
echo.
echo Type a file name to call
echo.
set /p callinput="> "
cls
call "%phomedir%%callinput%"
cls
timeout -1
cls
goto chooseip
:customhome
echo CALL %USERNAME%, YEAR CREATED - 20%usernameyear%
echo.
echo Type a file name to call
echo.
set /p callinput="> "
cls
call %customhomedir%"%callinput%"
timeout -1
cls
goto chooseip
:quit
exit