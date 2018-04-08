#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir C:\Users\8bitb\Desktop\AHK Data
#InstallKeybdHook
#SingleInstance, Force

RainmeterPath := "C:\Program Files\Rainmeter\rainmeter.exe"

SendRainmeterCommand(Command) {
  global RainmeterPath
  Run, %RainmeterPath% %Command%
}

capsToggle := false

^!p::Reload

#!Q::
{
    WinGet, ProcessID, PID, A
    Process, Close, %ProcessID%
}

SetTimer, RainmeterLoop, 1000
spotify_active := False
NTT_active := False
Joystick_active := False
Discord_active := False
RainmeterLoop:
{
    If WinExist("ahk_exe Spotify.exe") and !spotify_active 
    {
        spotify_active := True
        Run, "C:\Program Files\Rainmeter\Rainmeter.exe"
    }
    If !WinExist("ahk_exe Spotify.exe") and spotify_active 
    {
        spotify_active := False
        Process, Close, Rainmeter.exe
    }
    If WinExist("Nuclear Throne Together") and !NTT_active
    {
       NTT_active := True
       Run, "C:\Users\8bitb\Desktop\AHK Data\unload.pyw"
    }
    If !WinExist("Nuclear Throne Together") and NTT_active
    {
        NTT_active := False
    }
    If capsToggle
	{
		SetCapsLockState, AlwaysOn
	}
	else
	{
		SetCapsLockState, AlwaysOff
	}
    return
}
; No longer needed due to the loop above
;DetectHiddenWindows, On
;SetTitleMatchMode, 2
;IfWinNotExist, rainmeter.ahk
;{
;	Run, rainmeter.ahk
;	Return
;}
;SetTitleMatchMode, 1
;DetectHiddenWindows, Off

^CapsLock::
{
	capsToggle := !capsToggle
    If capsToggle
	{
		SetCapsLockState, AlwaysOn
	}
	else
	{
		SetCapsLockState, AlwaysOff
	}
    return
}



^+c::
{
	Send, ^c
	Sleep 100
	Run, http://www.google.com/search?q=%clipboard%
	Return
}

CapsLock::Shift

CapsLock & Shift::
+CapsLock::
{
	Send, {Media_Play_Pause}
    FirefoxId := WinExist("ahk_class MozillaWindowClass")
    If FirefoxId
    {
        toSend := [1,2,3,4,5,6,7,8]
        for v, key in toSend
        {
            ControlSend, , {LCtrl down}{%key%}{LCtrl up}, ahk_id %FirefoxId%
            Sleep, 50
            WinGetTitle, FirefoxTitle, ahk_id %FirefoxId%
            Sleep, 50
            IfInString, FirefoxTitle, YouTube
            {
                IfNotInString, FirefoxTitle, Subscriptions
                {
                    ControlSend, , k, ahk_id %FirefoxId%
                    break
                }
            }
        }
        SetCapsLockState, AlwaysOff
    }
	return
}

CapsLock & a::
{
    Send, {Volume_Down}
    Return
}

CapsLock & s::
{
	Send, {Volume_Up}
	Return
}
CapsLock & q::
{
	Send, {Media_Prev}
	Return
}
CapsLock & w::
{
	Send, {Media_Next}
	Return
}
CapsLock & Tab::
{
	Send, {Volume_Mute}
	Return
}

CapsLock & z::
{
	FormatTime, TimeString,, Time
	SplashTextOn, 100, 30, Time, %TimeString%
	WinMove, Time, , 0, 0
	Loop,
	{
		GetKeyState, capsstate, CapsLock, P
		GetKeyState, zstate, z, P
		if capsstate = U
		{
		break
		}
		if zstate = U
		{
		break
		}
		Sleep, 10
	}
	SplashTextOff
	return
}

CapsLock & x::
{
	RunWait, battery.pyw
	Sleep, 10
	FileRead, BatteryString, battery_data.txt
	SplashTextOn, 200, 30, Battery, %BatteryString%
	WinMove, Battery, , 0, 0
	Loop,
	{
		GetKeyState, capsstate, CapsLock, P
		GetKeyState, zstate, x, P
		if capsstate = U
		{
		break
		}
		if zstate = U
		{
		break
		}
		Sleep, 10
	}
	SplashTextOff
	return
}

CapsLock & c::
{
	
	Run, "C:\Users\8bitb\Desktop\AHK Data\sendAR.pyw" "%clipboard%"
	ToolTip, Sent clipboard to Samsung S8
	SetTimer, RemoveToolTip, 1000
	return
}

CapsLock & v::
{
    If WinActive("ahk_exe Overwatch.exe")
    {
        SendMode, Event
        CoordMode, Mouse, Screen
        Click, 1012, 765
        Sleep, 50
        Send, [redacted]
        Sleep, 50
        Click, 1012, 872
        CoordMode, Mouse, Client
        Sleep, 50
        Send, [redacted]
        Sleep, 50
        Send, {Return}
        SendMode, Input
        return
    }
	Process, Exist, Rainmeter.exe
	If errorlevel
	{
		SendRainmeterCommand("!ToggleConfig ""Fountain of Colors\SettingsWindow"" ""SettingsWindow.ini""")
        return
    }
}

CapsLock & `::
{
	Send, {Volume_Mute}
	Send, {Volume_Mute}
	return
} 

#+z::
{
	WinGet, activeprocess, ProcessName, A
	Process, Exist, %activeprocess%
	If errorlevel
	{
		Process, Close, %errorlevel%
	}
	Return
}

CapsLock & d::
{
	If WinActive("ahk_exe explorer.exe")
	{
		MouseGetPos, xpos, ypos
		Click 0,0
		Send +{F10}
		Send n
		Click %xpos%, %ypos%, 0
	}
	return
}

CapsLock & b::
{
	block := !block
	if block
	{
		BlockInput, MouseMove
		ToolTip, Blocked Mouse Input
		SetTimer, RemoveToolTip, 1000
	}
	else
	{
		BlockInput, MouseMoveOff
		ToolTip, Unblocked Mouse Input
		SetTimer, RemoveToolTip, 1000
	}
	return
}

randtoggle := False
CapsLock & y::
{
    if randtoggle
    {
        SendMode, Input
        SetTimer, MouseMoveRandom, Off
        randtoggle := False
    }
    else
    {
        SendMode, Event
        SetTimer, MouseMoveRandom, 1000
        randtoggle := True
    }
    return
}

MoveMod := 50
MouseMoveRandom:
{
    SendMode, Event
    ;Random, RandX, 100, %ScreenW%
    ;Random, RandY, 100, %ScreenH%
    ;MouseMove, RandX, RandY, 15
    
    MouseMove, 100+%MoveMod%, 500, 15
    Movemod := %Movemod% / -1
    return
}

RemoveToolTip:
{
	SetTimer, RemoveToolTip, Off
	ToolTip
	return
}

CapsLock & i::
{
	RegRead, ScreenS, HKEY_CURRENT_USER,Control Panel\Desktop\,SCRNSAVE.EXE
	Sleep, 1000
	Run,%ScreenS% /S
    return
}

CapsLock & LWin::
{
    Run, "C:\Program Files\Everything\Everything.exe"
    return
}

CapsLock & .::
{
    Sleep, 500
	Run, "C:\Users\8bitb\Desktop\Turn Off LCD.exe"
    return
}

CapsLock & ,::
{
    Run, "C:\WINDOWS\system32\rundll32.exe" shell32.dll`,Control_RunDLL mmsys.cpl`,`,playback
    Sleep, 500
    WinActivate, Sound ahk_exe rundll32.exe
    return
}