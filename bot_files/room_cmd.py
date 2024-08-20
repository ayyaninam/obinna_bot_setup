import discord
from .processor import get_room_creation_title_description, create_channel_in_db

async def create_room_command(interaction: discord.Interaction, artist: discord.Member, influencer: discord.Member):
    # Create the new channel name
    new_channel_name = f"{artist.display_name}-x-{influencer.display_name}"

    # Create the channel in the server
    guild = interaction.guild
    new_channel = await guild.create_text_channel(new_channel_name)

    # Create the embed with the "banner" content
    title, desc = get_room_creation_title_description()
    embed = discord.Embed(
        title=title,
        description=desc, color=0x3498db)
    
    embed.add_field(name="Artist", value=artist.mention, inline=True)
    embed.add_field(name="Influencer", value=influencer.mention, inline=True)
    embed.add_field(name="Status", value=":hourglass: Pending", inline=True)
    embed.add_field(name="Fee", value="8.00%", inline=False)
    embed.set_footer(text="Need Assistance? Tag admins for help")
    create_channel_in_db(channel_id=new_channel.id, artist=artist.display_name, influencer=influencer.display_name, artist_id=artist.id, influencer_id=influencer.id)

    await new_channel.send(embed=embed)
