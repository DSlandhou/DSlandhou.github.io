@echo off
cd /d "%~dp0"

git rev-parse --is-inside-work-tree >nul 2>nul
if errorlevel 1 (
  git init
  git config user.name "DSlandhou"
  git config user.email "DSlandhou@users.noreply.github.com"
)

git remote get-url origin >nul 2>nul
if errorlevel 1 (
  git remote add origin https://github.com/DSlandhou/DSlandhou.github.io.git
)

git add -A
git diff --cached --quiet
if %errorlevel% equ 0 (
  echo.
  echo No new local files. Trying to upload the last saved version.
  goto :push
)

git commit -m "update my blog"
if errorlevel 1 (
  echo.
  echo The commit did not finish. Take a screenshot of this window and send it to me.
  pause
  exit /b 1
)

:push
git branch -M main
git push -u origin main
if errorlevel 1 (
  echo.
  echo The upload did not finish. Sign in to GitHub if a browser window opens, then double click this file again.
  pause
  exit /b 1
)

echo.
echo Upload complete. Your website will update in about one minute.
pause
