@echo off
cd /d "%~dp0"
call npx astro dev stop
echo.
echo The local preview has stopped.
pause
