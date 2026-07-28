@echo off
cd /d "%~dp0"

if not exist "%USERPROFILE%\.ssh\2026blog_github_ed25519.pub" (
  echo The blog connection key was not found. Please take a screenshot of this window and send it to me.
  pause
  exit /b 1
)

type "%USERPROFILE%\.ssh\2026blog_github_ed25519.pub" | clip
start "" "https://github.com/settings/ssh/new"
echo.
echo GitHub has opened and the public key is already copied.
echo On the GitHub page:
echo 1. Title: 2026blog laptop
echo 2. Keep Key type as Authentication Key
echo 3. Click the Key box and press Ctrl+V
echo 4. Click Add SSH key
echo.
echo Then return to the 2026blog folder and double click the file beginning with 3.
pause
