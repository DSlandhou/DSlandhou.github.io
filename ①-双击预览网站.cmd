@echo off
cd /d "%~dp0"
echo Starting your local preview. Please wait a few seconds...
call npx astro dev --background
if errorlevel 1 goto :error
timeout /t 3 /nobreak >nul
start "" "http://localhost:4321"
echo.
echo Your browser should now show the blog.
echo Keep this black window open while you are using the preview.
echo To stop later, double click the file beginning with 2.
pause
exit /b 0

:error
echo.
echo The preview did not start. Please take a screenshot of this window and send it to me.
pause
