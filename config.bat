@echo off

call %~dp0\venv\Scripts\activate

cd %~dp0

set API_ID=9905934
set API_HASH=1c37c89d67f3545a2aeb02cf941a382d

python main.py

pause