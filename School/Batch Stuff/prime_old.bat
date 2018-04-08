@echo off
mode con lines=10000
setlocal ENABLEDELAYEDEXPANSION
setlocal ENABLEEXTENSIONS
rem echo on
:top
set /p n=limit: 
for /L %%i in (1,1,%n%) do set crible.%%i=1
for /L %%i in (2,1,%n%) do (
  if !crible.%%i! EQU 1 (
    set /A w = %%i * 2
    for /L %%j in (!w!,%%i,%n%) do (
       set crible.%%j=0
       echo X-%%j
       )
    )
  )
)
cls
for /L %%i in (2,1,%n%) do (
  if !crible.%%i! EQU 1 echo %%i 
)
pause
cls
goto top