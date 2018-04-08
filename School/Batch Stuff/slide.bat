@echo off
title Slide Puzzle
setlocal enabledelayedexpansion

set default= %
set pos=9
set loop=1

:reset
set slide1=1
set slide2=7
set slide3=3
set slide4=5
set slide5=8
set slide6=4
set slide7=2
set slide8=6
set slide9=%default%
set pos=9

:display
cls
echo  ____ ____ ____
echo ^|    ^|    ^|    ^|
echo ^|  %slide1% ^|  %slide2% ^|  %slide3% ^|
echo ^|____^|____^|____^|
echo ^|    ^|    ^|    ^|
echo ^|  %slide4% ^|  %slide5% ^|  %slide6% ^|
echo ^|____^|____^|____^|
echo ^|    ^|    ^|    ^|
echo ^|  %slide7% ^|  %slide8% ^|  %slide9% ^|
echo ^|____^|____^|____^|
choice /c wasdrq /n
if %errorlevel% == 1 goto movew
if %errorlevel% == 2 goto movea
if %errorlevel% == 3 goto moves
if %errorlevel% == 4 goto moved
if %errorlevel% == 5 goto reset
if %errorlevel% == 6 goto quit

:movew
if %pos% GEQ 7 goto display
set /a helper=%pos% + 3
set /a slide%pos%=!slide%helper%!
set slide%helper%=%default%
set /a pos=%pos% + 3
goto display

:movea
if %pos% == 3 goto display
if %pos% == 6 goto display
if %pos% == 9 goto display
set /a helper=%pos% + 1
set /a slide%pos%=!slide%helper%!
set slide%helper%=%default%
set /a pos=%pos% + 1
goto display

:moves
if %pos% LEQ 3 goto display
set /a helper=%pos% - 3
set /a slide%pos%=!slide%helper%!
set slide%helper%=%default%
set /a pos=%pos% - 3
goto display

:moved
if %pos% == 1 goto display
if %pos% == 4 goto display
if %pos% == 7 goto display
set /a helper=%pos% - 1
set /a slide%pos%=!slide%helper%!
set slide%helper%=%default%
set /a pos=%pos% - 1
goto display
:quit