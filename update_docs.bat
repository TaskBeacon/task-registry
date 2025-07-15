@REM @echo off
@REM echo Cleaning up old task files...
@REM if exist source\Tasks rmdir /s /q source\Tasks
@REM mkdir source\Tasks

echo.
echo Running fetch_tasks.py...
python fetch_tasks.py

echo.
echo Building documentation...
call make.bat html

echo.
echo Done.