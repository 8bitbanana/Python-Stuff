@echo off
title loop
mode con lines=10000
set count=50

:loop

for /l %%x in (0,1,10) do (
for /l %%y in (0,1,10) do (
for /l %%z in (0,1,10) do echo %%x %%y %%z
))

echo end
pause

