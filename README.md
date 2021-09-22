### boombox
> A Rhythm-like music bot for discord, powered by Python and the Deezer API!


### Install (on Discord Server)
1. Navigate to https://discord.com/oauth2/authorize?client_id=887361112855678976&permissions=515396566016&scope=bot
2. In the window that opens, select the server you would like to add the bot to, and then click the "Continue" button
3. Login to your server. In the "Online" sidebar, you should see a new user called Boombox!


### Install (local bot copy)
1. 
```bash
cd project
```
2.
```bash
python3 main.py
```
_Make sure you add your API key inside the ``api_key = "your api key here"`` ``line in main.py``_


### Usage
At this time, boombox supports 5 different commands, and a game in-progress

**Check Artist Info**
```bash
$boombox artist Artist Name
```

**Check Album Info**
```bash
$boombox album Album Name
```

**Get Track Info, and Play Preview**
_Before doing command, please join a VC (Voice Channel)_
```bash
$boombox track Track Name
```
- select the "play" emoji reaction to play a track in the Voice Channel! (v2.0.0)
_The preview snippet of the song will play in the Voice Channel_

**Add Track to Queue**
- select the "queue" emoji to add the song to the queue! (v2.0.0)

**Play Queue**
```bash
$boombox play queue
```

**Play War**
```bash
$war drawcard
```


### License
```
Copyright 2021 Finn Lancaster and Aatmodhee Goswami

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES
OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT
OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```
