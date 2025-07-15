@echo off
echo Cleaning up old task files...
if exist source\Tasks rmdir /s /q source\Tasks
mkdir source\Tasks

echo.
echo Running fetch_tasks.py...
python fetch_tasks.py

echo.
echo Building documentation...
call make.bat html

echo.
echo Done.