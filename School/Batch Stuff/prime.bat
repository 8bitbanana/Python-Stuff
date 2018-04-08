pushd [redacted]\My Documents\Batch Projects
set denominator=0
set graphics=1
set colours=1
set lightning=0
set halfn=1
set write=0

@echo off
mode con lines=10000
setlocal ENABLEDELAYEDEXPANSION
setlocal ENABLEEXTENSIONS
rem echo on
:top
set count=0
color 0f
set /p n=limit: 
if %n%==more goto settings
set /a m=n/2
if %halfn%==0 set /a m=n
color 01
echo Wait...
for /L %%i in (1,1,%n%) do set crible.%%i=1
if %colours%==1 color a0
if %colours%==0 color 0f
cls
if %graphics%==0 echo Calculating...
for /L %%i in (2,1,%m%) do (
  set /a count+=1
  if !crible.%%i! EQU 1 (
    set /A w = %%i * 2
    if %colours%==1 (
      if %%i EQU 2 color 09
      if %%i EQU 3 color 0c
      if %%i EQU 5 color 0e
      if %%i EQU 7 color 0a
      if %%i EQU 97 color 0f
      if %lightning%==1 (
         if %%i GTR 200 (
            if %%i GTR 1000 (
               color c0
               color 0f
            ) else (
            color f0
            color 0f
            )
         )
      )
    )
    for /L %%j in (!w!,%%i,%n%) do (
       set crible.%%j=0
       if %graphics%==1 (
          if %denominator%==0 echo X-%%j %%i
          if %denominator%==1 echo X-%%j %%i/%m%
       )
       )
  )
)
cls
echo ===PRIMES===
if %write%==1 echo ===PRIMES===>primesoutput.txt
for /L %%i in (2,1,%n%) do (
  if !crible.%%i! EQU 1 (
  echo %%i 
  if %write%==1 echo %%i>>primesoutput.txt
)
)
if %write%==1 echo Up to %n%>>primesoutput.txt
color 0f
echo.
pause
cls
goto top

:settings
echo Settings
set /p denominator=(%denominator%) denominator 
set /p graphics=(%graphics%) graphics 
set /p colours=(%colours%) colours 
set /p lightning=(%lightning%) lightning 
set /p halfn=(%halfn%) half n 
set /p write=(%write%) write 
goto top