set chatdir="\\[redacted]\My Documents\Chat"
set snakedir="\\[redacted]\My Documents\Chat\programs\snake.bat"
set oldinput=0
set count=1
set maxcount=3
echo off
color 0a
cls
title Chat Sender
pushd %chatdir%
:top
echo Chat Sender
set /p input="> "
rem if %username==[redacted] exit
if "%input%"=="%oldinput%" goto spamstop
:bypass
set oldinput=%input%
if "%input%"=="snake" goto callsnake
if "%input%"=="rc" goto runcommand
if "%input%"=="rcs" goto runcommands
if "%input%"=="upupdowndownleftrightleftrightba" goto konami
if "%input%"=="about" goto displayhelp
rem if "%input%"=="ou" goto :onlineusers
if %username%==ecrooks14 goto admintag
if %username%==[redacted] goto supportertag
echo (%username%) - %input%>log.mp3
goto notag
:admintag
echo (%username% [A]) - %input%>log.mp3
goto notag
:supportertag
echo (%username% [S]) - %input%>log.mp3
:notag
waitfor /si CHATUPDATE>NUL
cls
goto top
:runcommand
if %username%==ecrooks14 goto runcommandagain
echo (%username%) - %input%>log.mp3
waitfor /si CHATUPDATE>NUL
cls
goto top
:runcommandagain
set /p commandinput="rc> "
echo rc%commandinput%>log.mp3
waitfor /si CHATUPDATE>NUL
cls
goto top
:onlineusers
echo ou>log.mp3
echo Online Users>usernames.dat
waitfor /si CHATUPDATE>NUL
timeout 1
waitfor /si CHATUPDATE>NUL
timeout 1
for /F "tokens=*" %%A in (usernames.dat) do (
echo %%A>log.mp3
waitfor /si CHATUPDATE>NUL
)
cls
goto top
:spamstop
if %username%==ecrooks14 goto bypass
if %username%==[redacted] goto bypass
echo SPAMMER! STRIKE %count% out of %maxcount%
set /a count+=1
timeout -1
if %count%==%maxcount% goto kick
goto bypass
:kick
echo %username% was kicked due to spam. Idiot.>log.mp3
waitfor /si CHATUPDATE>NUL
exit
:displayhelp
echo Just type anything into the sender to send it to the chat. Anyone viewing
echo the reader can see this too.
echo There is a spam filter installed - don't type the same thing twice - 3 strikes
echo and you're out! You will also kicked for being an arsehole.
if %username%==[redacted] echo Also Max don't spam numbers into the chat you tard. Only you can view this line of text.
if %username%==ecrooks14 echo Why the hell are you reading this? 'rc' to admin thingys!
if %username%==[redacted] echo Oi no spamming
echo Also don't type any speech marks, it will crash your sender (not anyone elses)
echo.
rem echo Also go to New Folder (3) for free memes!
echo.
goto top
:konami
echo 30 lives cheat activated!
echo %username% did a special!>log.mp3
waitfor /si CHATUPDATE>NUL
set maxcount=30
goto top
:runcommands
if %username%==ecrooks14 goto runcommandagains
echo (%username%) - %input%>log.mp3
waitfor /si CHATUPDATE>NUL
cls
goto top
:runcommandagains
set /p commandinput="rcs> "
set /p usernameinput="rcsuser> "
echo rsuser%username%>log.mp3
echo cs%commandinput%>log.mp3
waitfor /si CHATUPDATE>NUL
cls
goto top
:callsnake
echo %username% is now playing snake.>log.mp3
waitfor /si CHATUPDATE>NUL
call %snakedir%
cls
goto chattop
:logoff
echo %username% got trolled.>log.mp3
waitfor /si CHATUPDATE>NUL
shutdown -l