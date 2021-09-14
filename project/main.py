import deezer
import discord

api_key = "your api key here"

# Don't even mention the limitless jokes
deez_client = deezer.Client()
dis_client = discord.Client()

# Permissions Integer: 515396566016
# URL: https://discord.com/oauth2/authorize?client_id=887361112855678976&permissions=515396566016&scope=bot

# function called to use the deezer lib to grab artist info
def get_artist_info(artistname):
    # TODO: add deezer call here, and modify return statement accordingly
    return


# function called to grab the songs in an album
def get_album(albumname):
    # TODO: add deezer call here, and modify return statement accordingly
    return


# function called to play song preview. In progress.
def play_track_preview(track): 
    results = deez_client.duration('instant_crush')
    return results


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
                word = cmd.split('track ')[1]
                
                # TODO: change call to use array indexes as opposed to checking for the command in the
                # entire string. Right now, as user could type: $boombox artist album and the program would 
                # run the album loop.
                await message.channel.send(play_track_preview(word))

            elif ("album" in cmd):
                word = cmd.split('album ')[1]
                await message.channel.send('This command will return the songs in the album: '+word)

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
