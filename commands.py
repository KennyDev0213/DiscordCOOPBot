#command controller

import random
import json

#-----init-----
players = []

#------program utility (for the bot/scripts)------
#return true if player is found, false if not
def checkPlayers(player_name) -> bool:
  for player in players:
    if player == player_name:
      return True
  return False

#-----user utility (for commands)-----
def shuffle(team_num=2):
  
  #if the length of the player array is 0 then just return a prompt
  if len(players) == 0:
    return "roster is empty add players with '!aoe add [player]'"

  #initialize the teams list
  teams = []
  for _ in range(team_num):
    teams.append([])

  #copy the players list
  player_copy = players.copy()
  pointer = 0

  while len(player_copy) != 0:
    
    #select a random player and set it as a queued player
    queued_player = random.choice(player_copy)
    
    #removed the queued player from the list
    player_copy.remove(queued_player)

    #add the player to the team and tick the team pointer up
    team = teams[pointer]
    team.append(queued_player)

    #if the team pointer is going over, reset it to 0
    pointer += 1
    if pointer >= team_num:
      pointer = 0 

  #build the string
  team_str = '--------------------------------\n\n'
  for team in teams:
    for member in team:
      team_str += member + "\n"
    team_str += '\n--------------------------------\n\n'

  return team_str

#reset the playerlist to 0
def resetPlayers():
  try:
    players.clear()
    return "players have been reset!"
  except:
    return "there has been an issue reseting the players"

#builds a help msg to prompt users
def buildHelpMsg():
  help_msg = ""
  help_msg += "CO-OP gaming aoe team manager bot written by Kennon Dong\n\n"
  help_msg += "use '!aoe' as the prefix\n"
  help_msg += "type '!aoe shuffle [number of teams]' to generate teams\n"
  help_msg += "type '!aoe add [player]' to add a player to the roster \n"
  help_msg += "type '!aoe remove [player]' to remove a player from the roster\n"
  help_msg += "type '!aoe all' to view all current player in the roster\n"
  help_msg += "type '!aoe reset' to clear all current player in the roster\n"
  return help_msg

#-----player management-----

#add player, return msg of status
def addPlayer(player_name=""):
  if player_name == "":
    return "error: no player name found"
  elif checkPlayers(player_name):
    return player_name + " already in roster"
  else:
    players.append(player_name)
    return player_name + " added to roster"

#remove player, return msg of status
def removePlayer(player_name=""):
  if player_name == "":
    return "error: no player name found"
  elif checkPlayers(player_name):
    players.remove(player_name)
    return player_name + " was removed from roster"
  else:
    return player_name + " is not found in roster"

#show all the players in current roster
def showPlayers():

  #if player list is empty return the empty status
  if len(players) == 0:
    return "roster is empty"
  #else build the string
  else:
    all_players = ""
    count = 1
    for player in players:
      all_players += str(count) +". " + str(player) + "\n"
      count += 1
    return all_players

#save the players from queue into a json file
def savePlayers():
  #if player count in roster is 0, notify the player the players cannot be saved
  if len(players) == 0:
    return "No players in the roster to save"
  else:
    #convert the players list into a json string
    player_json = json.dumps(players)

    #open the json file, write the string then close
    with open("players.json", "w") as jFile:
      jFile.write(player_json)
      jFile.close()

    #notify the bot that is was successful
    return "SUCESS! all players have been saved"

def loadPlayers():

  #adding a try/catch incase the file doesn't exist yet and throws a FileNotFoundError
  try:

    #open the file, get its contents then parse the json string into a list then close the file
    with open("players.json", "r") as jFile:
      names = jFile.read()
      #assign the players varible with the new list
      players = json.loads(names)
      jFile.close()

    #notify that is has been loaded
    return "Roster has been loaded! Ready to game!"

  except FileNotFoundError:
    return "File was not found, did you save the last roster?"