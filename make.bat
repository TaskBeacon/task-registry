@ECHO OFF
pushd %~dp0

REM Command file for building Sphinx documentation on Windows

REM Set up defaults
IF "%SPHINXBUILD%"=="" SET SPHINXBUILD=sphinx-build
SET SOURCEDIR=source
SET BUILDDIR=docs

REM Check if sphinx-build exists
%SPHINXBUILD% >NUL 2>&1
IF ERRORLEVEL 9009 (
    ECHO.
    ECHO The 'sphinx-build' command was not found. Make sure you have Sphinx
    ECHO installed, then set the SPHINXBUILD environment variable to point
    ECHO to the full path of the 'sphinx-build' executable. Alternatively you
    ECHO may add the Sphinx directory to PATH.
    ECHO.
    ECHO If you don't have Sphinx installed, grab it from:
    ECHO https://www.sphinx-doc.org/
    EXIT /B 1
)

REM If no argument is given, show help
IF "%1"=="" GOTO help

REM Run the sphinx-build target
IF "%1"=="html" (
    %SPHINXBUILD% -b html %SOURCEDIR% %BUILDDIR%
    echo.> %BUILDDIR%\.nojekyll
) ELSE (
    %SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
)

GOTO end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
