import discord
from base.models import Task, Channel
from .processor import *
from django.db.models import Q

# Create a new task
# Create a new task
async def create_task(interaction: discord.Interaction, task_name: str):
    try:
        channel_id = interaction.channel.id
        channel = Channel.objects.get(channel_id=channel_id)
        task = Task.objects.create(channel_id=channel, task_name=task_name)
    except Exception as e:
        await interaction.response.send_message("Error creating task...", ephemeral=True)
    text_to_send =  f"{interaction.user.mention} created a new task: {task.task_name}"
    await interaction.response.send_message(text_to_send, ephemeral=True) 

# Read (Retrieve) all tasks for a specific channel
async def get_all_tasks(interaction: discord.Interaction):
    channel_id = interaction.channel.id
    channel = Channel.objects.get(channel_id=channel_id)
    tasks = Task.objects.filter(channel_id=channel)
    if tasks:
        task_text = "\n".join([str(f"{i+1}: {task}") for i, task in enumerate(tasks)])
        await interaction.response.send_message(task_text, ephemeral=True) 
    else:
        await interaction.response.send_message("No tasks found!", ephemeral=True)


# Update a task's agreement status or name
async def update_task(interaction: discord.Interaction, task_id: int, task_name: str = None, artist_agreed: bool = None, influencer_agreed: bool = None):
    try:
        task = Task.objects.get(id=task_id)
        if task_name is not None:
            task.task_name = task_name
        if artist_agreed is not None:
            task.artist_agreed = artist_agreed
        if influencer_agreed is not None:
            task.influencer_agreed = influencer_agreed
        task.save()
        return task
    except Task.DoesNotExist:
        return None

# Delete a task
async def delete_task(interaction: discord.Interaction, task: str):
    try:
        tasks = Task.objects.filter(Q(channel__channel_id=interaction.channel.id) & Q(task_name=task))
        tasks.delete()
        await interaction.response.send_message(f"You Deleted task: {task}", ephemeral=True) 
        await interaction.channel.send(f"{interaction.user.mention} deleted task: {task}") 
    except Task.DoesNotExist:
        await interaction.response.send_message("Unable to delete the task.", ephemeral=True) 
