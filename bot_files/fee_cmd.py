import discord
from base.models import Fee  
from .processor import *

async def get_fee_command(interaction: discord.Interaction):
    fee_query = Fee.objects.all().order_by('-date_modified')
    if fee_query.exists():
        fee = fee_query[0].fee
        fee_text = f"Current fee: {fee}%"
        await interaction.response.send_message(fee_text, ephemeral=True)
    else:
        sorry_text = "Sorry, I can't provide you any Fee Structure right now."
        await interaction.response.send_message(sorry_text, ephemeral=True)

async def set_fee_command(interaction: discord.Interaction, fee:str):
    getted_number  = extract_number_from_string(fee)
    if getted_number == None:
        sorry_text = "Sorry, I can't change Fee Structure right now."
        await interaction.response.send_message(sorry_text, ephemeral=True)
    else:
        try:
            new_fee = Fee.objects.create(fee=getted_number)
            fee_query = Fee.objects.all().exclude(id=new_fee.id)
            fee_query.delete()
            new_fee_text = f"Fee Set to: {new_fee.fee}%"
            await interaction.response.send_message(new_fee_text, ephemeral=True)
        except:
            sorry_text = f"Sorry, Fee Structure can't be more than 100."
            await interaction.response.send_message(sorry_text, ephemeral=True)
