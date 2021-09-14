import discord
import requests

api_key = "your api key here"

dis_client = discord.Client()

# Perm Int: 515396566016
# URL: https://discord.com/oauth2/authorize?client_id=887361112855678976&permissions=515396566016&scope=bot


# function called to use the deezer api to grab artist info
def get_artist_info(artistname):
    return


# function called to grab the songs in an album
def get_album(albumname):
    # send a GET request to deezer to get the album
    URL = 'https://api.deezer.com/search?q=album:"'+albumname+'"'

    # submit the request, and grab data
    r = requests.get(URL)
    results = r.json()

    # loop through results to get artists and songs
    artists = []
    songs = []
    for i in range(len(results['data'])):
        songs.append(results['data'][i]['title'])
        
        if (results['data'][i]['artist']['name'] in artists):
            pass
        else:
            artists.append(results['data'][i]['artist']['name'])

    # return the necessary data in array form
    res = [results['data'][0]['album']['cover'], albumname, artists, songs]
    return res


# function called to play song preview. In progress.
def play_track_preview(track): 
    # send a GET request to the Deezer API with the track as the user specified value
    URL = "https://api.deezer.com/search?"
    PARAM = {"q":'track:"'+track+'"'}

    # submit the request, and then grab the values returned.
    r = requests.get(url=URL, params = PARAM)
    results = r.json()

    # make a nice format for the output
    res = [results['data'][0]['album']['cover'], track, results['data'][0]['artist']['name'], results['data'][0]['preview']]
    return res


# setup and etc required to initialise Discord bot
def bot():
    @dis_client.event
    async def on_ready():
        print('Boombox logged in as: {0.user}'.format(dis_client))


    # simple listener to react to user messages
    @dis_client.event
    async def on_message(message):
        if message.author == dis_client.user:
            return

        # narrow message scope to only respond is the message starts with $boombox
        if message.content.startswith('$boombox'):
            # await message.channel.send('Boombox initiated!')
        
            cmd = message.content.split('$boombox ')[1]
            # check words after "$boombox" to see if the user wants to grab a specific track
            if ("track" in cmd):
                # try/catch to catch exceptions and alert the user of them
                try:

                    # TODO: change call to use array indexes as opposed to checking for the command in the
                    # entire string. Right now, as user could type: $boombox artist album and the program would 
                    # run the album loop.
                    word = cmd.split('track ')[1]
                    song_data = play_track_preview(word)

                    embedVar = discord.Embed(title=song_data[1], description="", color=discord.Color.blue())
                    embedVar.set_thumbnail(url=song_data[0])
                    embedVar.add_field(name="Artist: ", value=song_data[2], inline=False)
                    embedVar.add_field(name="Preview: ", value=song_data[3], inline=False)
                    await message.channel.send(embed=embedVar)
                    
                except:
                    await message.channel.send('❌ **An error occurred. Check the track spelling, and make sure the track is an actual song.** ❌')
                    
        
            elif ("album" in cmd):
                try:
                    word = cmd.split('album ')[1]

                    album_data = get_album(word)

                    embedVar = discord.Embed(title=album_data[1], description="", color=discord.Color.blue())
                    embedVar.set_thumbnail(url=album_data[0])
                    embedVar.add_field(name="Artist(s): ", value=', '.join(album_data[2]), inline=False)
                    embedVar.add_field(name="Tracks: ", value=', '.join(album_data[3]), inline=False)
                    await message.channel.send(embed=embedVar)

                except:
                    await message.channel.send('❌ **An error occurred. The specified album does not exist or was not found.** ❌')

            elif ("artist" in cmd):
                word = cmd.split('artist ')[1]
                await message.channel.send('This will return artist info for: '+ word)

            # catch unknown commands and return a generic error message.
            else: 
                await message.channel.send('Unknown command. Accepted strings are: $boombox artist artist name, $boombox album album name, and $boombox track song name')

# call the bot function for the bot to login
bot()

# required: discord run call to authorise bot perms
dis_client.run(api_key)
