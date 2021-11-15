#bot interface

import discord
import os

#command file that stores all the commands
import commands as cmd

#get the client for this computer
client = discord.Client()

#discord event
@client.event
async def on_ready():
  print('loggin as {0.user}'.format(client))

#discord event
@client.event
async def on_message(msg):

  cmd_msg = ""

  #if the message is from the bot or doesnt start with '!aoe' then ignore
  if msg.author == client.user or not msg.content.startswith('!aoe'):
    return
  #else break down the msg
  else:
    cmd_msg = msg.content.split(" ")
    try:
      cmd_msg[1] = cmd_msg[1].lower()
    except:
      await msg.channel.send("invalid syntax \n\n" + cmd.buildHelpMsg())
      return

  #dev testing block
  if cmd_msg[1] == "test":
    broken_msg = msg.content.split(" ")
    await msg.channel.send(broken_msg[2])

  #shuffle the teams!
  elif cmd_msg[1] == "shuffle":
    team_num=2
    try:
      # try to parse the second command as an int, if int is empty or unparsable default it to '2'
      try:
        team_num = int(cmd_msg[2])
        print(team_num)
      except:
        team_num = 2
      await msg.channel.send(cmd.shuffle(team_num))
    except Exception as e:
      await msg.channel.send("uh oh something went wrong! -->" + str(e))
    
  #add a new player!
  elif cmd_msg[1] == "add":
    await msg.channel.send(cmd.addPlayer(cmd_msg[2]))

  #remove a player!
  elif cmd_msg[1] == "remove":
    await msg.channel.send(cmd.removePlayer(cmd_msg[2]))

  #show all players!
  elif cmd_msg[1] == "all":
    await msg.channel.send(cmd.showPlayers())

  #reset the roster
  elif cmd_msg[1] == "reset":
    await msg.channel.send(cmd.resetPlayers())

  #save the roster
  elif cmd_msg[1] == "save":
    await msg.channel.send(cmd.savePlayers())

  #load the roster
  elif cmd_msg[1] == "load":
    await msg.channel.send(cmd.loadPlayers())

  #if the command was not recognized then send help msg
  else:
    await msg.channel.send(cmd.buildHelpMsg())

#main function
def main():
  client.run(os.getenv('TOKEN'))
  return

#python practice
if __name__ == "__main__":
  main()

  