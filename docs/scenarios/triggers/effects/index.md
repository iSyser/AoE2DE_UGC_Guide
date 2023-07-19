# Effects

_Written by: Alian713_

---

## 1. What are effects?

Effects are one of the two basic elements of triggers (the other one being Conditions). They are essentially "cheats" in some sense, that allow you to change information about the game as the game is being played. All technologies in the game utilise effects to do what they are meant to do. Usually, a technology almost always uses multiple effects in combination to achieve its purposes. Examples of technologies and the effects they use will be given when the appropriate effects for them are encountered. Some examples of basic effects that can be used in the scenario editor are: `Create Unit`, `Send Chat`, `Display Instructions` etc.. To use effects,

1. Create a trigger
2. Add an effect to it.
3. Pick the effect you wish to use from the effects list.
4. Configure the settings of the effect as desired

Lets look at all the effects and their configurations one by one:

## 2. Common Terminology

Feel free to skip these if you are already familiar with them

### 2.1. Bug

Anything in the map that is not working as intended is a bug.

Historically, the term "bug" comes from physical bugs getting stuck in computers and causing them to malfunction back in the day when computers used to be the size of entire rooms.

In today's context, a bug in anything just means that its malfunctioning and not working as intended.

### 2.2. Debugging

Attempting to find out the cause of the malfunction, and removing/fixing that cause is known as debugging.

### 2.3. Execution

Executing a trigger means that we carry out its effects.

## 3. Effects and How to Use Them

### 3.1. AI Script Goal { #10 }

-   ID: 10

This effect is used to communicate with the AI. An AI Trigger NUMBER set with this effect can be detected in an AI script using `event-detected trigger NUMBER`.

The configurations for this effect are as follows:

1. AI Script Goal: AI Trigger ID to set

### 3.2. Acknowledge AI Signal { #50 }

-   ID: 50

When `set-signal` is used in an AI file, this effect is used to unset it so it can be reused. This only works in Single Player games. Refer to the [Acknowledge Multiplayer AI Signal](./#69 "Jump to: Acknowledge Multiplayer AI Signal") effect for the multiplayer version of this effect.

The configurations for this effect are as follows:

1. AI Signal Value: The AI Signal ID to acknowledge

### 3.3. Acknowledge Multiplayer AI Signal { #69 }

-   ID: 69

When `set-signal` is used in an AI file, this effect is used to unset it so it can be reused. This only works in Multiplayer games. Refer to the [Acknowledge AI Signal](./#50 "Jump to: Acknowledge AI Signal") effect for the single player version of this effect.

The configurations for this effect are as follows:

1. AI Signal Value: The AI Signal ID to acknowledge

### 3.4. Activate Trigger { #8 }

-   ID: 8

This effect can be used to activate a trigger.

The configurations for this effect are as follows:

1. Trigger List: The trigger to activate/deactivate

### 3.5. Attack Move { #30 }

-   ID: 30

This effect can be used to command units of a given player to attack move to a location. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Location: The location to create the unit on, or task a unit to
4. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
5. Object Group: This is the class of units to effect
6. Object Type: This is the type of the unit to effect

### 3.6. Change Civilization Name { #48 }

-   ID: 48

This effect can be used to change the name of the civilization of a player to any desired name.

The configurations for this effect are as follows:

1. Source Player: The player that is affected by the effect
2. String Id: This is the same as the `Name String ID`. Refer to [Name String ID](../../#38-name-string-id "Jump to: Custom Scenarios > Scenario Basics > #3.8 Name String ID") section of the guide
3. Message: The name/message/instruction to show on screen or the script call to execute

### 3.7. Change Color Mood { #72 }

-   ID: 72

This effect can change the colour mood of the map.

The configurations for this effect are as follows:

1. Color Mood: This is the new colour mood to set
2. Quantity: The amount to modify by or a timer

### 3.8. Change Diplomacy { #1 }

-   ID: 1

This effect can be used to change the diplomacy stance of the soruce players with the target player.

The configurations for this effect are as follows:

1. Diplomacy Stance: The new diplomacy state
2. Source Player: The player that is affected by the effect
3. Target Player: This is the second player that is affected by the effect

### 3.9. Change Object Armor { #31 }

-   ID: 31

This effect can be used to change the armour of existing units of a given player to the specified value. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Quantity: The amount to modify by
2. Armour or Attack Class: The Armour/Attack Class to Modify
3. Unit List 1: This is the unit to affect
4. Source Player: The player that is affected by the effect
5. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
6. Object Group: This is the class of units to effect
7. Object Type: This is the type of the unit to effect
8. Operation: Add, Subtract, Multiply or Divide the given quantity

Some useful tricks with this effect:

1. The quantity field on this effect has a maximum limit of 255, use multiple of these effects/addition or multiplication operations to get a higher value

### 3.10. Change Object Attack { #28 }

-   ID: 28

This effect can be used to change the attack of existing units of a given player to the specified value. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Quantity: The amount to modify by
2. Armour or Attack Class: The Armour/Attack Class to Modify
3. Unit List 1: This is the unit to affect
4. Source Player: The player that is affected by the effect
5. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
6. Object Group: This is the class of units to effect
7. Object Type: This is the type of the unit to effect
8. Operation: Add, Subtract, Multiply or Divide the given quantity

Some useful tricks with this effect:

1. The quantity field on this effect has a maximum limit of 255, use multiple of these effects/addition or multiplication operations to get a higher value

### 3.11. Change Object Civilization Name { #59 }

-   ID: 59

This effect can be used to change the civilization name of specified objects of a given player. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. String Id: This is the same as the `Name String ID`. Refer to [Name String ID](../../#38-name-string-id "Jump to: Custom Scenarios > Scenario Basics > #3.8 Name String ID") section of the guide
2. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.

### 3.12. Change Object Cost { #40 }

-   ID: 40

This effect can be used to change the cost of a specifed unit for a particular player.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Food: The new food cost of the unit/technology
4. Wood: The new wood cost of the unit/technology
5. Stone: The new stone cost of the unit/technology
6. Gold: The new Gold cost of the unit/technology

Some useful tricks with this effect:

1. Due to a current bug in the game, to properly set costs, you need to first set all the different wood, food, stone and gold costs of the unit to -1. Now using a 2nd effect you can set them to anything you like.
2. Units in the game can only have a maximum of 2 different resource of costs.

### 3.13. Change Object Description { #44 }

-   ID: 44

This effect can be used to change the description of a specifed unit for a particular player.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. String Id: This is the same as the `Name String ID`. Refer to [Name String ID](../../#38-name-string-id "Jump to: Custom Scenarios > Scenario Basics > #3.8 Name String ID") section of the guide
4. Message: The name/message/instruction to show on screen or the script call to execute

Some useful tricks with this effect:

1. There are special keywords that are used to display certain information about an object in its description
2. This is illustrated with the following example:

    ```
    Build Trade Workshop (<Cost>)
    Allows you to buy special perks

    <hp> <attack> <armor> <piercearmor> <garrison> LoS: 4
    ```

3. Here, all the words in the angle brackets are replaced by those relevant statistics for the unit.

### 3.14. Change Object HP { #27 }

-   ID: 27

This effect can be used to change the max HP of existing units of a given player to the specified value. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Quantity: The amount to modify by or a timer
2. Unit List 1: This is the unit to affect
3. Source Player: The player that is affected by the effect
4. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
5. Object Group: This is the class of units to effect
6. Object Type: This is the type of the unit to effect
7. Operation: Add, Subtract, Multiply or Divide the given quantity

Some useful tricks with this effect:

1. Unit Max HP is capped at 32768. If you try to set it to a value above 32768, the unit will die because of an overflow.

### 3.15. Change Object Icon { #42 }

-   ID: 42

This effect can be used to change the icon of existing units of a given player to the 2nd unit's icon. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
4. Object Group: This is the class of units to effect
5. Object Type: This is the type of the unit to effect
6. Unit List 2: This is the second unit to affect

### 3.16. Change Object Name { #26 }

-   ID: 26

This effect can be used to change the names of existing units of a given player to the specified name. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. String Id: This is the same as the `Name String ID`. Refer to [Name String ID](../../#38-name-string-id "Jump to: Custom Scenarios > Scenario Basics > #3.8 Name String ID") section of the guide
4. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
5. Message: The name/message/instruction to show on screen or the script call to execute

Some useful tricks with this effect:

1. This effect is mostly used to make markers, signs and waypoints which the player can select and read using units on the map

### 3.17. Change Object Player Color { #58 }

-   ID: 58

This effect can be used to change the colour of specified objects of a given player. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
4. Player Color: The new colour of the unit

### 3.18. Change Object Player Name { #60 }

-   ID: 60

This effect can be used to change the player name of specified objects of a given player. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. String Id: This is the same as the `Name String ID`. Refer to [Name String ID](../../#38-name-string-id "Jump to: Custom Scenarios > Scenario Basics > #3.8 Name String ID") section of the guide
4. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.

### 3.19. Change Object Range { #32 }

-   ID: 32

This effect can be used to change the range of existing units of a given player to the specified value. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Quantity: The amount to modify by or a timer
2. Unit List 1: This is the unit to affect
3. Source Player: The player that is affected by the effect
4. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
5. Object Group: This is the class of units to effect
6. Object Type: This is the type of the unit to effect
7. Operation: Add, Subtract, Multiply or Divide the given quantity

### 3.20. Change Object Speed { #33 }

-   ID: 33

This effect can be used to change the speed of existing units of a given player to the specified value. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Quantity: The amount to modify by or a timer
2. Unit List 1: This is the unit to affect
3. Source Player: The player that is affected by the effect
4. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
5. Object Group: This is the class of units to effect
6. Object Type: This is the type of the unit to effect

### 3.21. Change Object Stance { #36 }

-   ID: 36

This effect can be used to change the stance of units of a given player to the given stance. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
4. Object Group: This is the class of units to effect
5. Object Type: This is the type of the unit to effect
6. Attack Stance: Set the new stance of the unit, aggressive, defensive, stand ground or no attack

### 3.22. Change Ownership { #18 }

-   ID: 18

This effect can be used to convert units of the source player to the target player. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Target Player: This is the second player that is affected by the effect
4. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
5. Object Group: This is the class of units to effect
6. Object Type: This is the type of the unit to effect
7. Flash Object: When this is enabled if the source and target players are the same, the selected object(s) will be flashed

Some useful tricks with this effect:

1. This effect can be used to make unconvertable gaia units. If a unit is originally owned by a different player, but is then converted to gaia using this effect, then that unit can no longer be converted by other players

### 3.23. Change Player Name { #45 }

-   ID: 45

This effect can be used to change the name of a player to any desired name.

The configurations for this effect are as follows:

1. Source Player: The player that is affected by the effect
2. String Id: This is the same as the `Name String ID`. Refer to [Name String ID](../../#38-name-string-id "Jump to: Custom Scenarios > Scenario Basics > #3.8 Name String ID") section of the guide
3. Message: The name/message/instruction to show on screen or the script call to execute

### 3.24. Change Technology Cost { #63 }

-   ID: 63

This effect can be used to change a technology's cost for a particular player.

The configurations for this effect are as follows:

1. Source Player: The player that is affected by the effect
2. Technology: The technology to affect
3. Food: The new food cost of the unit/technology
4. Wood: The new wood cost of the unit/technology
5. Stone: The new stone cost of the unit/technology
6. Gold: The new Gold cost of the unit/technology

Some useful tricks with this effect:

1. Due to a current bug in the game, this effect changes the cost of the tech for all players
2. Due to a current bug in the game, to properly set costs, you need to first set all the different wood, food, stone and gold costs of the tech to -1. Now using a 2nd effect you can set them to anything you like.
3. Techs in the game can only have a maximum of 3 different resource of costs.

### 3.25. Change Technology Description { #66 }

-   ID: 66

This effect can be used to change a technology's Description for a particular player.

The configurations for this effect are as follows:

1. Source Player: The player that is affected by the effect
2. Technology: The technology to affect
3. String Id: This is the same as the `Name String ID`. Refer to [Name String ID](../../#38-name-string-id "Jump to: Custom Scenarios > Scenario Basics > #3.8 Name String ID") section of the guide
4. Message: The name/message/instruction to show on screen or the script call to execute

### 3.26. Change Technology Location { #47 }

-   ID: 47

This effect can be used to change the research location of a specifed technology for a particular player to another unit. The research location of Loom is the Town Centre.

The configurations for this effect are as follows:

1. Source Player: The player that is affected by the effect
2. Technology: The technology to affect
3. Unit List 2: This is the second unit to affect
4. Button Location: The location of the button for a unit or technology. This number is given by $(row-1)\times5+column$. For example, the button location for the man at arms **research** in the barracks, which is in the 2nd row and 1st column, is given by $(2-1)\times5+1 = 6$

### 3.27. Change Technology Name { #65 }

-   ID: 65

This effect can be used to change a technology's name for a particular player.

The configurations for this effect are as follows:

1. Source Player: The player that is affected by the effect
2. Technology: The technology to affect
3. String Id: This is the same as the `Name String ID`. Refer to [Name String ID](../../#38-name-string-id "Jump to: Custom Scenarios > Scenario Basics > #3.8 Name String ID") section of the guide
4. Message: The name/message/instruction to show on screen or the script call to execute

### 3.28. Change Technology Research Time { #64 }

-   ID: 64

This effect can be used to change a technology's research time for a particular player.

The configurations for this effect are as follows:

1. Quantity: The amount to modify by or a timer
2. Source Player: The player that is affected by the effect
3. Technology: The technology to affect

### 3.29. Change Train Location { #46 }

-   ID: 46

This effect can be used to change the train location of a specifed unit for a particular player to another unit. The train location of Archers is Archery Range.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Unit List 2: This is the second unit to affect
4. Button Location: The location of the button for a unit or technology. This number is given by $(row-1)\times5+column$. For example, the button location for the man at arms **research** in the barracks, which is in the 2nd row and 1st column, is given by $(2-1)\times5+1 = 6$

### 3.30. Change Variable { #56 }

-   ID: 56

This effect can be used to change the value of a variable.

The configurations for this effect are as follows:

1. Quantity: The amount to modify by or a timer
2. Operation: Add, Subtract, Multiply or Divide the given quantity
3. Variable: The variable to modify
4. Message: The name/message/instruction to show on screen or the script call to execute

### 3.31. Change View { #16 }

-   ID: 16

This effect can be used to move the camera of the player to a specified location.

The configurations for this effect are as follows:

1. Source Player: The player that is affected by the effect
2. Location: The location to create the unit on, or task a unit to
3. Scroll: If this is enabled, changing the camera to a new position shows a scrolling animation from the position the player was previously on. If not enabled, the camera cuts to the new position wihout any animations.

Some useful tricks with this effect:

1. This effect can be used to bring attention of the player to a certain part of the map

### 3.32. Clear Instructions { #21 }

-   ID: 21

This effect can be used to clear instructions on the screen before the timer for that instruction is up.

The configurations for this effect are as follows:

1. Panel Position: Position 0 displays the instruction at the top, Position 1 displays the instruction in the middle of the top half of the screen and Position 2 displays the instruction at the bottom of the top half of the screen

Some useful tricks with this effect:

1. This effect is not used very often, since mostly you want your display instruction effects to display an instruction for the full length of time you specify

### 3.33. Clear Timer { #57 }

-   ID: 57

This effect can be used to remove a displayed timer from the screen.

The configurations for this effect are as follows:

1. Timer: The time to display the message for

### 3.34. Create Garrisoned Object { #49 }

-   ID: 49

This effect creates the unit chosen in the 2nd list inside the selected object or the unit chosen in the 1st list. The unit that the created unit is garrisoned inside does not need to be of the same player.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
4. Unit List 2: This is the second unit to affect

Some useful tricks with this effect:

1. The object you are creating garrisoned objects inside must have at least 1 garrison capacity and it must have the garrison ability

### 3.35. Create Object { #11 }

-   ID: 11

This effect can be used to create a unit or building for the specified player.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Location: The location to create the unit on, or task a unit to
4. Facet: The rotation of the created unit

### 3.36. Damage Object { #24 }

-   ID: 24

This effect can be used to deal damage to units of a given player. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Quantity: The amount to modify by or a timer
2. Unit List 1: This is the unit to affect
3. Source Player: The player that is affected by the effect
4. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
5. Object Group: This is the class of units to effect
6. Object Type: This is the type of the unit to effect

Some useful tricks with this effect:

1. Dealing negative damage to an object will actually increase their HP beyond their max HP. Using this, a unit's HP can go over 32768.
2. This is used in Tower Defence maps like ATD where units have over a million HP, since directly setting an object's HP to over 32768 using the change object HP effect would kill the object.

### 3.37. Deactivate Trigger { #9 }

-   ID: 9

This effect can be used to deactivate a trigger.

The configurations for this effect are as follows:

1. Trigger List: The trigger to activate/deactivate

### 3.38. Declare Victory { #13 }

-   ID: 13

This effect can be used to grant victory or defeat to a specifed player.

The configurations for this effect are as follows:

1. Source Player: The player that is affected by the effect
2. Victory: If this is selected, the chosen player will win the game. If it is not selected, then the chosen player is defeated

### 3.39. Disable Object Deletion { #74 }

-   ID: 74

This effect makes specified units of the given player unable to be removed by the player themselves. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.

### 3.40. Disable Object Selection { #70 }

-   ID: 70

This effect makes specified units of the given player unselectable. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.

### 3.41. Disable Technology Stacking { #68 }

-   ID: 68

This effect disables 256x tech mode for the specified technology and player. Refer to the [Enable Technology Stacking](./#67 "Jump to: Enable Technology Stacking") effect.

The configurations for this effect are as follows:

1. Source Player: The player that is affected by the effect
2. Technology: The technology to affect

### 3.42. Disable Unit Targeting { #61 }

-   ID: 61

This effect makes it so that the specified units of the given player cannot be targeted (basically, you can't perform any right click actions from another unit on these units anymore) by other units. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.

### 3.43. Display Instructions { #20 }

-   ID: 20

This effect can be used to display instructions on the screen. An icon of a unit may also be displayed along with the instructions.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. String Id: This is the same as the `Name String ID`. Refer to [Name String ID](../../#38-name-string-id "Jump to: Custom Scenarios > Scenario Basics > #3.8 Name String ID") section of the guide
4. Display Time: The amount of time to display the instruction for
5. Panel Position: Position 0 displays the instruction at the top, Position 1 displays the instruction in the middle of the top half of the screen and Position 2 displays the instruction at the bottom of the top half of the screen
6. Play Sound: The sound to play
7. Message: The name/message/instruction to show on screen or the script call to execute
8. Sound Name: The name of the sound to play

Some useful tricks with this effect:

1. This effect is useful for making dialogue sequences
2. When you do multiple display instruction effects on the same panel position at the same time, only the last instruction is shown. One panel position can only show one instruction at a time
3. Adding a colour prefix to a messages will colour the message in chat. The message must begin with the colour prefix for it to work, and the colour prefix is not shown in the real message shown in chat. The following colour prefixes may be used:
    1. <span style="color: blue"><BLUE\></span>
    2. <span style="color: red"><RED\></span>
    3. <span style="color: green"><GREEN\></span>
    4. <span style="color: yellow"><YELLOW\></span>
    5. <span style="color: aqua"><AQUA\></span>
    6. <span style="color: purple"><PURPLE\></span>
    7. <span style="color: grey"><GREY\></span>
    8. <span style="color: orange"><ORANGE\></span>

### 3.44. Display Timer { #37 }

-   ID: 37

This effect can be used to display a timer on screen.

The configurations for this effect are as follows:

1. String Id: This is the same as the `Name String ID`. Refer to [Name String ID](../../#38-name-string-id "Jump to: Custom Scenarios > Scenario Basics > #3.8 Name String ID") section of the guide
2. Display Time: The amount of time to display the instruction for
3. Time Unit: This specifies the unit of time used in the timer trigger. This can be seconds, minutes or years
4. Timer: The time to display the message for
5. Message: The name/message/instruction to show on screen or the script call to execute

Some useful tricks with this effect:

1. Adding a colour prefix to a messages will colour the message in chat. The message must begin with the colour prefix for it to work, and the colour prefix is not shown in the real message shown in chat. The following colour prefixes may be used:
    1. <span style="color: blue"><BLUE\></span>
    2. <span style="color: red"><RED\></span>
    3. <span style="color: green"><GREEN\></span>
    4. <span style="color: yellow"><YELLOW\></span>
    5. <span style="color: aqua"><AQUA\></span>
    6. <span style="color: purple"><PURPLE\></span>
    7. <span style="color: grey"><GREY\></span>
    8. <span style="color: orange"><ORANGE\></span>

### 3.45. Enable Object Deletion { #73 }

-   ID: 73

This effect makes specified units of the given player deleteable by the player themselves. Refer to the [Disable Object Deletion](./#74 "Jump to: Disable Object Deletion") effect. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.

### 3.46. Enable Object Selection { #71 }

-   ID: 71

This effect makes specified units of the given player selectable. Refer to the [Disable Object Selection](./#70 "Jump to: Disable Object Selection") effect. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.

### 3.47. Enable Technology Stacking { #67 }

-   ID: 67

This effect enables 256x tech mode for the specified technology and player.

The configurations for this effect are as follows:

1. Source Player: The player that is affected by the effect
2. Technology: The technology to affect

### 3.48. Enable Unit Targeting { #62 }

-   ID: 62

This effect makes it so that the specified units of the given player can be targeted by other units. Refer to the [Disable Unit Targeting](./#61 "Jump to: Disable Unit Targeting") effect. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.

### 3.49. Enable/Disable Object { #38 }

-   ID: 38

This effect can be used to enable/disable any unit for a specific player. Note that sometimes, simply enabling a unit wont allow you to train them, because if it is not a default unit, the game doesn't know which building to train the unit in. Thus, A train location and a train button ([Change Train Location](./#46 "Jump to: Change Train Location")), a cost ([Change Object Cost](./#40 "Jump to: Change Object Cost")), and optionally a discription ([Change Object Description](./#44 "Jump to: Change Object Description")), of the unit are needed to also be set using additional effects to allow training the enabled unit.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Enabled: If this is selected, the units/technology is enabled if it is not already enabled

### 3.50. Enable/Disable Technology { #39 }

-   ID: 39

This effect can be used to enable/disable any technology for a specific player. Similar to units, when a non default technology is enabled, its train location and button ([Change Technology Location](./#47 "Jump to: Change Technology Location")), costs ([Change Technology Cost](./#63 "Jump to: Change Technology Cost")), and optionally a description ([Change Technology Description](./#66 "Jump to: Change Technology Description")), must be set using additional effects for someone to research it.

The configurations for this effect are as follows:

1. Source Player: The player that is affected by the effect
2. Technology: The technology to affect
3. Enabled: If this is selected, the units/technology is enabled if it is not already enabled

### 3.51. Freeze Object { #22 }

-   ID: 22

This effect can be used to stop units of a specific player. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
4. Object Group: This is the class of units to effect
5. Object Type: This is the type of the unit to effect

### 3.52. Heal Object { #34 }

-   ID: 34

This effect can be used to heal existing units of a given player by the specifed HP amount. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Quantity: The amount to modify by or a timer
2. Unit List 1: This is the unit to affect
3. Source Player: The player that is affected by the effect
4. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
5. Object Group: This is the class of units to effect
6. Object Type: This is the type of the unit to effect

Some useful tricks with this effect:

1. This effect should not be used to simulate regeneration of HP of a unit similar to heroes, because there is another effect ([Modify Attribute](./#51 "Jump to: Modify Attribute"), change attribute [regeneration rate](../../../general/attributes/#109 "Jump to: Game Mechanics > Attributes > Regeneration Rate") to the desired quantity), that does exactly this

### 3.53. Kill Object { #14 }

-   ID: 14

This effect can be used to kill certain units of the specified player. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
4. Object Group: This is the class of units to effect
5. Object Type: This is the type of the unit to effect

### 3.54. Lock Gate { #7 }

-   ID: 7

This effect can be used to lock an unlocked gate.

The configurations for this effect are as follows:

1. Selected Objects: The units to apply the effect to

### 3.55. Modify Attribute { #51 }

-   ID: 51

This effect can be used to modify any attribute of a specified unit. Note that this effects the unit itself, not just existing units. This means that even new units created will have the modified attribute. Refer to the [Attributes](../../../general/attributes "Jump to: Game Mechanics > Attributes") section of the guide to see a list of modifiable attributes and what each of them does.

The configurations for this effect are as follows:

1. Quantity: The amount to modify by or a timer
2. Unit List 1: This is the unit to affect
3. Source Player: The player that is affected by the effect
4. Operation: Add, Subtract, Multiply or Divide the given quantity
5. Attribute List: The attribute of a unit to modify

Some useful tricks with this effect:

1. Changing the Amount of 1st Resource of a unit changes its population requirement
2. Since the quantity field cannot take in fractional values, to modify an attribute by a fractional amount, use the division operation to your advantage. for example setting a value to `0.1` is the same as first setting it to 1 and then dividing by 10. Similarly, adding a value of 0.5 is the same as first multiplying the initial value by 10, adding 5 and then dividing by 10.

### 3.56. Modify Resource { #52 }

-   ID: 52

This effect can be used to modify the resource amounts of a particular player by specified amounts. Refer to the [Resources](../../../general/resources "Jump to: Game Mechanics > Resources") section of the guide to see all the resources that can be modified and their purposes.

The configurations for this effect are as follows:

1. Quantity: The amount to modify by or a timer
2. Tribute List: The resource to tribute
3. Source Player: The player that is affected by the effect
4. Operation: Add, Subtract, Multiply or Divide the given quantity

### 3.57. Modify Resource By Variable { #53 }

-   ID: 53

This effect can be used to modify the resource amounts of a particular player by the value of another variable. Refer to the [Resources](../../../general/resources "Jump to: Game Mechanics > Resources") section of the guide to see all the resources that can be modified and their purposes.

The configurations for this effect are as follows:

1. Tribute List: The resource to tribute
2. Source Player: The player that is affected by the effect
3. Operation: Add, Subtract, Multiply or Divide the given quantity
4. Variable: The variable to modify

### 3.58. Patrol { #19 }

-   ID: 19

This effect can be used to make units of a specified player patrol from one location to another. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Location: The location to create the unit on, or task a unit to
4. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
5. Object Group: This is the class of units to effect
6. Object Type: This is the type of the unit to effect

### 3.59. Place Foundation { #25 }

-   ID: 25

This effect can be used to automatically place down a building foundation for a specific player.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Location: The location to create the unit on, or task a unit to

### 3.60. Play Sound { #4 }

-   ID: 4

This effect can be used to play a specified sound.

The configurations for this effect are as follows:

1. Source Player: The player that is affected by the effect
2. Location: The location to create the unit on, or task a unit to
3. Sound Name: The name of the sound to play

Some useful tricks with this effect:

1. This effect is useful for playing a notification sound

### 3.61. Remove Object { #15 }

-   ID: 15

This effect can be used to remove certain units of the specified player from the map. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
4. Object Group: This is the class of units to effect
5. Object Type: This is the type of the unit to effect

### 3.62. Replace Object { #43 }

-   ID: 43

This effect can be used to replace existing units of a given player with another unit. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Target Player: This is the second player that is affected by the effect
4. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
5. Object Group: This is the class of units to effect
6. Object Type: This is the type of the unit to effect
7. Unit List 2: This is the second unit to affect

Some useful tricks with this effect:

1. This effect is widely used by unit upgrade technologies.
2. Researching Man at Arms replaces all Militia with Man at Arms on the map
3. Researching Crossbowman replaces all Archers with Crossbowmen on the map

### 3.63. Research Technology { #2 }

-   ID: 2

This effect can automatically research a technology for the specified player.

The configurations for this effect are as follows:

1. Source Player: The player that is affected by the effect
2. Technology: The technology to affect
3. Force: If this is enabled, then the technology is researched even if the player's civilization does not have access to it

### 3.64. Script Call { #55 }

-   ID: 55

This effect allows us to write or call functions from an XS Script. While the script call effect can be used to both call functions and write small scripts, it is advised to always use a function call and never use this effect for writing scripts. Refer to the [XS Scripting](../../../xs/beginner "Jump to: XS Scripting: A Beginner's Guide").

The configurations for this effect are as follows:

1. String Id: This is the same as the `Name String ID`. Refer to [Name String ID](../../#38-name-string-id "Jump to: Custom Scenarios > Scenario Basics > #3.8 Name String ID") section of the guide
2. Message: The name/message/instruction to show on screen or the script call to execute

### 3.65. Send Chat { #3 }

-   ID: 3

This effect can be used to display messages in chat.

The configurations for this effect are as follows:

1. Source Player: The player that is affected by the effect
2. String Id: This is the same as the `Name String ID`. Refer to [Name String ID](../../#38-name-string-id "Jump to: Custom Scenarios > Scenario Basics > #3.8 Name String ID") section of the guide
3. Message: The name/message/instruction to show on screen or the script call to execute
4. Sound Name: The name of the sound to play

Some useful tricks with this effect:

1. This effect is super useful for debugging. When you're unsure of which triggers in your map are executed at which point, adding one of these to that trigger will display a message on screen when it gets executed
2. This effect can also be used to simulate chat between two players
3. This effect should NOT be used to display instructions to players, because there is an effect that can be used specifically for that
4. Duplicate messages are not shown
5. Adding a colour prefix to a messages will colour the message in chat. The message must begin with the colour prefix for it to work, and the colour prefix is not shown in the real message shown in chat. The following colour prefixes may be used:
    1. <span style="color: blue"><BLUE\></span>
    2. <span style="color: red"><RED\></span>
    3. <span style="color: green"><GREEN\></span>
    4. <span style="color: yellow"><YELLOW\></span>
    5. <span style="color: aqua"><AQUA\></span>
    6. <span style="color: purple"><PURPLE\></span>
    7. <span style="color: grey"><GREY\></span>
    8. <span style="color: orange"><ORANGE\></span>

### 3.66. Set Building Gather Point { #54 }

-   ID: 54

This effect can be used to set a gather point for specified buildings of a given player. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Location: The location to create the unit on, or task a unit to
4. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.

### 3.67. Set Player Visibility { #41 }

-   ID: 41

This trigger sets the visibility of the target player for the source player.

The configurations for this effect are as follows:

1. Source Player: The player that is affected by the effect
2. Target Player: This is the second player that is affected by the effect
3. Visibility State: The new visibility state

### 3.68. Stop Object { #29 }

-   ID: 29

This effect can be used to stop units of a given player. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
4. Object Group: This is the class of units to effect
5. Object Type: This is the type of the unit to effect

### 3.69. Task Object { #12 }

-   ID: 12

This effect can be used to task certain units of the specified player to (it basically simulates a right click at the specified location or unit) move to a specified locaiton, or perform an action on another unit. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Location: The location to create the unit on, or task a unit to
4. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
5. Object Group: This is the class of units to effect
6. Object Type: This is the type of the unit to effect

### 3.70. Teleport Object { #35 }

-   ID: 35

This effect can be used to teleport units of a player from one area of the map to another location on the map. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Location: The location to create the unit on, or task a unit to
4. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
5. Object Group: This is the class of units to effect
6. Object Type: This is the type of the unit to effect

### 3.71. Train Unit { #75 }

-   ID: 75

This effect can be used to automatically queue a specified number of units for training and set gather point for a specific player. If no building or area is specified, training queues will be allocated as evenly as possible across all buildings where the unit can be trained.

The configurations for this effect are as follows:

1. Quantity: The amount to modify by or a timer
2. Unit List 1: This is the unit to affect
3. Source Player: The player that is affected by the effect
4. Location: The location to create the unit on, or task a unit to
5. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.

### 3.72. Tribute { #5 }

-   ID: 5

This effect can be used to tribute resources from one player to another.

The configurations for this effect are as follows:

1. Quantity: The amount to modify by or a timer
2. Tribute List: The resource to tribute
3. Source Player: The player that is affected by the effect
4. Target Player: This is the second player that is affected by the effect

Some useful tricks with this effect:

1. Tributing negative resources actually gives the source player the resource and deducts that amount from the target player
2. Tributing negative resources from a player to gaia is a way to make silent resource trickles that do not make the tribute sound.

### 3.73. Unload { #17 }

-   ID: 17

This effect can be used to ungarisson objects from a unit or building. The units affected by this effect are determined by the configurations of the effect.

The configurations for this effect are as follows:

1. Unit List 1: This is the unit to affect
2. Source Player: The player that is affected by the effect
3. Location: The location to create the unit on, or task a unit to
4. Area: Only units on this selected area will be affected by the effect. If not set, units on the entire map are affected.
5. Object Group: This is the class of units to effect
6. Object Type: This is the type of the unit to effect

### 3.74. Unlock Gate { #6 }

-   ID: 6

This effect can be used to unlock a locked gate.

The configurations for this effect are as follows:

1. Selected Objects: The units to apply the effect to

### 3.75. Use Advanced Buttons { #23 }

-   ID: 23

Enables Advanced Buttons.

Some useful tricks with this effect:

1. If you can't see the buttons for aggressive stance, and unit groups use this effect to enable them for yourself. That is all that this effect does, its useless otherwise
