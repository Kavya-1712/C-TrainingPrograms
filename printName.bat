@echo off
set /p name = Enter your name:
set /p n = Enter how many times to print:
for \L %%i in (1,1,%n%) do (
   echo %%i. %name%
)
