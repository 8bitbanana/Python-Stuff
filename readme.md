# My Programming Stuff

This is an archive of all the files I could find of all the stuff I wrote in Python, from me learning to program to me making useful scripts for fun. A bunch of windows batch scripts and a couple Autohotkey scripts thrown in for fun.

I am putting these up here for 3 reasons

1. To prove to unis, employers etc that I was programming for fun since I was about 12
2. To have another online backup of all this just in case
3. Some of the later scripts may actually be useful for some people

I am going to try to document all these to the best of my ability, explain what each script does and provide context if needed.

I have sorted them into 3 folders based off where they came from

 - Rpi - From my Raspberry Pi. 12-14 year old me trying to learn Python.
 - School - From my middle and high school documents. 13-15 year old me messing about on the school computers.
 - Laptop - From my current laptop which I use for personal use and college. 16 year old me tinkering and making tools to make my life easier

I have replaced some text with "[redacted]" to replace personal info, api keys, friends full names and the like.

So, here goes.

# Laptop

## AutoBrowser
Me using selenium.

### Aternos.py
A bot that logs into the aternos minecraft servers and starts an old server of mine up after waiting in the queue. Possibly broken now.

### [redacted]_login.py
A bot that logs into my colleges wifi network

### bin
A folder of stuff for selenium to work, like phantom_js (a headless browser)

## GoogleLocation
A script that takes your Google location history (which you can download from <https://takeout.google.com/settings/takeout>) and plots it all on a map using MatPlotLib.

### main.py
The main script

### main_multi.py
Like the main script, but outputs multiple maps in chronological order so you can make a nice gif of it

## newgrounds_dl.py
Downloads all the music that a specified newgrounds artist made. I wrote this because I was annoyed that some of Waterflame's music that I liked wasn't on Spotify, but as soon as I finished it he announced a new album so I never actually used it :P

### main.py
The main script

### main - specific.py
Like main.py, but you can search for and download a specific list of songs.

## SpotifyLogging
I was going to use this with tasker to log what I am listening to on Spotify, but I couldn't get python to run on my Android (without buying paid apps). I resorted to coding this algorithm directly into tasker instead.

## timelapse
I wanted to create a timelapse from a bunch of stills (from my Rpi camera which I set up overnight).

### filename_sorter.py
Adds zeros to the still filename so they sorted correctly. (from 0.jpg 1.jpg 2.jpg to 0000.jpg 0001.jpg 0002.jpg)

### timelapse_sync.py
Ran while the pi was taking the photos to pull them off the pi and onto my laptop via a local SAMBA share. The pi didn't have enough space to store all the photos so I had to pull them all on the fly. (which worked suprisingly)

## The rest

### artists.py
Gets details about a specific artist on spotify

### AutoRemote.py
Sends an AutoRemote message to my phone

### blender_terminal.py
A cyberpunky terminal which I used in a 3D model in my Games Design A-Level

### cpu_test.py
Logs when my cpu clock speed changes. Doesn't work.

### csvmania.py
Speedfan logs are .csv files, but seperates the values using tabs and not commas. This fixes that

### EJC.ahk
My main AutoHotkey script which I have running all the time on my laptop. Remaps the capslock to a bunch of media controls, as well as a bunch of other stuff like opening rainmeter when spotify opens.

### invoice.py
Creates invoice pdfs for my dads work

### music_link_convert.py
Scrapes songlink.io to get spotify, dezzer and other links from a youtube music link. Doesn't work as far as I remember.

### Nuclear Tracker.py
Displays details about your Nuclear Throne game using the stream key feature.

### nuclear_switch.py
Switches my Nuclear Throne exe file with the Nuclear Throne Together exe file, so I can swap between modded and vanilla.

### pyQtTest.py
Me learning pyQt

### reddit_dl.py
Downloads all images from a specified reddit user. Was going to work with imgur links but I had troubles with imgurs api before and couldn't be bothered to go through it again.

### r-tldr-feed.py
A nice terminal view of the most recent post on /r/tldr

### sendAR.py
Similar to AutoRemote.py

### shutdown_timer.py
Type in a date, and your computer will shut down on that date. For when I was downloading the witcher but was going on holiday.

### startup.pyw
Used to run instead of all the programs that ran on startup so I could pick which ones to run.

### steamgrid.py
Gets all your games from steam and displays it in a nice table. Scroll bar doesn't work.

### textures_freebie.pyw
Downloads the current freebie of the day from textures.com. They stopped doing freebies of the day because of arseholes like me, so this no longer works.

### unload.pyw
Adds all my nuclear throne mods to a text file so I can unload them all at the same time easily.

### wiki_console.py
A terminal viewer for wikipedia.

# RPi

### Calculator*.py
A calculator

### cards.py
Creates a deck of cards

### explore_bot.py
Type a starting website, it gets all the links, follows a random one, and goes on a little adventure.

### FindPrime (1.0).py
Finds primes. Doesn't work

### Hangman*.py
A game of hangman from the python book I was reading. I just kept adding and adding and adding.

### html_wip.py
Tries to get all text (all p tags) from a website. Almost works but I couldn't get rid of the whitespace.

### pyrate_game*.py
A game we used to play in high school maths which I adapted into a terminal/tkinter game. 25KB of really, really bad code. Some of my favorites include using multiple variables instead of arrays and only using classes because thats the only was I knew how to use tkinter.

### slots (1.0).py
A slot machine.

### TicTacToe *.py
A game of TicTacToe against an AI. From the programming book I was reading.

### YuGiOh LP Counter.py
A Life Point counter for YuGiOh. Can't remember if I ever finished this.

# School

## Batch stuff

### Chat scripts and folders
I made a chat system in my computing class. It worked by editing a shared text file and using the waitfor command to ping every script on the network. Worked, was fun, I screwed about with people by logging off their computers, and I got into a lot of trouble. You could type snake and play snake in it, with your score being announced to the chat. Good times.

### All of the games
All games like snake, totalwar, yahtzee etc I got off the internet.

### internet checker
Constantly pings google to check if the internet was working as our schools library computers would frequently go offline. Used title so the internet status was always in the windows dock.

### prime.bat
Finds primes. Doesn't work.

### time.bat
Displays the time.

### shutdownshield.bat
Someone worked out how to use cmd to shutdown peoples computers remotely. This script constantly calls shutdown -a so your computer never shut down.

### taskmgr
Task manager was blocked, so this constantly calls tasklist so you can see the stuff that was running (and kill processes)

### cmd
Cmd was blocked, but batch was not!

## GCSE
All my GCSE work. This is was I was suppost to do in computing, everything else here is me screwing about

## The rest

### ayheichkay.ahk
Replaces all letters with photetic spellings of them, so A = AY, B = BEE, W = DOUBLEYOU. Funny funny stuff.

### backspacetest.py
I thought that using \b to call a backspace in python was pretty neat. This script is me testing it.

### Everything with "inject"
Copies troll scripts from my memory stick to the first writeable folder it can find, so I can plug in my memory stick, run the script and run away by the time the script actually executes. One opens eelslap.com, one logs off your computer and one opens notepad a thousand times.

### openall_noUI.pyw
Runs through my schools shared folder and opens everything it can, often freezing your computer.