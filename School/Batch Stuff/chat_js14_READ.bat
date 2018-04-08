pushd "\\[redacted]\My Documents\Chat"
cls
echo Wait...
@choice /c NL /d N /t 1 /n
if ERRORLEVEL==2 goto nowait
call chat_read.bat
exit
:nowait
call chat_read_nwf.bat
exit