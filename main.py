import nextcord,time,datetime
from nextcord import Interaction, SlashOption
from nextcord.ext import commands
from nextcord.ext import application_checks


bot = commands.Bot()



@bot.slash_command(name ="ping", description="myfirstcommand")  # this will apear on the slash command
@application_checks.has_permissions(send_messages=True) # you don't need to put this but i recommed
async def my_first_command(interaction: Interaction): # you can add more command like slash option!
        embed=nextcord.Embed(title="Pong!!" )  # this is the embed you can config
        embed.set_thumbnail(url="https://cliply.co/wp-content/uploads/2021/08/372108630_DISCORD_LOGO_BLACK_400.gif") # you can put gif or picture in here
     

        await interaction.send(embed=embed,  ephemeral=True ) # after you finish the embed you need to send message back !

        # ephemeral is the message that send and visible just only you but if you want it tovisible to everyone you can set it to false or delete it









@bot.event
async def on_ready():
    print(f"กำลังล็อกอินบอท : {bot.user}") # this just print bot name
    time.sleep(1.0)
    print("ล็อกอินสำเร็จ")
    await bot.change_presence(activity=nextcord.Streaming(name="putyourstatus",url="https://www.twitch.tv/Rawi1005")) # this is the status of the bot



bot.run("TOKEN")

# ⬆️ put your discord bot token here 
# https://www.writebots.com/discord-bot-token/  website if you need help