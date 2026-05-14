@echo off
setlocal

REM Build the Pithos for Windows NSIS installer from a clean checkout.
REM Requirements:
REM   - NSIS installed and makensis.exe available in PATH
REM   - Run this script from anywhere; it will build windows\install.nsi

set "SCRIPT_DIR=%~dp0"
set "NSIS_SCRIPT=%SCRIPT_DIR%install.nsi"
set "OUTPUT=%SCRIPT_DIR%pithos_installer.exe"

where makensis >nul 2>nul
if errorlevel 1 (
    echo ERROR: makensis.exe was not found in PATH.
    echo Install NSIS from https://nsis.sourceforge.io/Download and try again.
    exit /b 1
)

if exist "%OUTPUT%" del "%OUTPUT%"

pushd "%SCRIPT_DIR%" || exit /b 1
makensis /V3 "%NSIS_SCRIPT%"
set "BUILD_RESULT=%ERRORLEVEL%"
popd

if not "%BUILD_RESULT%"=="0" (
    echo ERROR: Installer build failed.
    exit /b %BUILD_RESULT%
)

if not exist "%OUTPUT%" (
    echo ERROR: NSIS finished but %OUTPUT% was not created.
    exit /b 1
)

echo Built installer: %OUTPUT%
echo Reminder: do not bundle %%APPDATA%%\Pithos\pithos.ini or logs in public uploads.
exit /b 0
