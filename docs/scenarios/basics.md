Custom Scenarios allow you to define your own, custom game modes. Literally, they are different "scenarios" the game can be played in.

## The Scenario Editor

The Scenario Editor is the tool that every map maker uses to make and test scenarios.
To open a new scenario in the editor,

1. Click `Single Player` in the main menu
2. Click `Editors`
3. Click `Create Scenario`

To open a saved scenario in the editor,

1. Double-click the scenario from the list in the editors menu in step 3 above

When you load into a new scenario, it is a blank canvas for you to play with!

In the editor, there are quite a few tabs that you can see at the top, their functionalities are discussed below:

## 1. Map

Under the `Map` tab in the editor, there are several options to change the map, they are discussed below:

### 1.1. Map Style

1. `Blank Map`: This option generates a map of the same terrain throughout the map. The default map that is generated when a new scenario is loaded is a blank map with grass terrain.

2. `Random Map`: This option generates a map from an RMS. (RMS stands for Random Map Script, they are scripts that generate regular maps like Arabia)

3. `Seed Map`: This option generates a map from an RMS using a specified seed. 

What is a seed you ask?

Each generation of a particular RMS in the game has a number attached to it called its "seed" that uniquely identifies that particular generation of the RMS. Generating a map with the same RMS and seed twice will give you the exact same map!

### 1.2. AI Map Type

This option is used by AIs to figure out what kind of a map they are playing on. This is important if you have AIs in your map because you want them to go for water builds when you have water on your map. Lets say that the map is nomad themed, then setting the `AI Map Type` to `Nomad` would allow AI players to properly play in a nomad style.

### 1.3. Colour Mood

This setting changes the colour theme (lighting) of the map. By default it is set to `Empty` which means no colour theme. Colour themes are used for aesthetic reasons only and do not effect gameplay. For exmaple, if you are making a map set in the winter season, then using the winter colour theme could be an option.

### 1.4. Team Positions

This setting is for when you generate maps from an RMS. It determines if players **in the same team** are placed in order of their colour or if they are randomly distributed throughout the map

For example, The teams are currently set to Players 1,3,5,7 vs Players 2,4,6,8 and generating the map with team positions on gives this result:

![Team Positions On](imgs/team_pos_on.png "Team Positions On")

Notice that players 1,3,5,7 who are on the same team have, generated in that particular order (going counter clockwise in the image) and that players 2,4,6,8 have also generated in that order.

Generating the map with team positions off on the other hand, gives this result:

![Team Positions Off](imgs/team_pos_off.png "Team Positions Off")

Notice that now, players 1,3,5,7 who are on the same team, have generated in random positions. Similarly players 2,4,6,8 have generated in no particular order. Also note that even though the positions within the team are random, the players are still grouped on each side of the map by team.

To be more precise, this option generates players in each team in order of their player numbers. Players do not have to be in the specific teams used in the above exmaple for this to work.

### 1.5. Extend Map

This features is useful for expanding an already existing map if you need to use more space. To use it,

1. Click the checkbox called `Extend Map`.
2. This brings up two new options, `New Map Size` and a `Map Offset`.
3. `New Map Size`: the size of the new map that will be generated.
4. `Map Offset`: determines where to place the existing map on the new map.

For exmaple, Extending this 4 player map with a `New Map Size` of `8 players` and a `Map Offset` of `North`

![Before Extending](imgs/extend_before.png "Before Extending")

gives the following result:

![After Extending](imgs/extend_after.png "After Extending")

Remember, the top corner of the map is North!

![Map Directions](imgs/directions.png "Map Directions")

### 1.6. Script Filename

This is the place where you need to enter the name of any XS scripts that you are using in your map. XS scripts are covered in the `XS Scripts` segment of this guide

## 2. Global Victory

Under the `Global Victory` tab in the editor, there are options that allow you to define custom victory conditions for all players. They are all discussed below:

### 2.1. Standard

A player wins by either defeating all enemies, or capturing 5 relics and holding them for 200 years, or constructing and holding a wonder for 200 years

### 2.2. Conquest

A player can only win by defeating all enemy players

### 2.3. Score

The first player to reach the specified score wins

### 2.4. Time Limit

The game is played until the specified time limit. When the time limit is reached, the player with the highest score wins

### 2.5. Custom

This victory condition can be customised using the following options:

1. `Conquest` this is the same as the victory condition in point 2. above
2. `Exploration` the first player to reach the specified percentage of the map explored wins the game. (There is a text box infront of this option to specify percentage)
3. `Relics` the first player to capture the specified quantity of relics wins the game. Unlike Standard Victory, a playar wins as soon as they have gathered the relics and do not need to hold them for 200 years. (There is a text box infront of this option to specify quantity)
4. `Any One` a player can complete any one of the victory condition enabled above to win
5. `All` a player has to complete all of the victory conditions enabled above to win

## 3. Terrain

Under the `Terrain` tab in the editor, there are a lot of options to modify the terrain of the map. Each of them are discussed below:

### 3.1. Map

This option allows you to manually place down terrain on the map.

1. `Brush Size`: allows you to pick how large of an area you want to affect on the map at once
2. `Layering Mode`: allows you to blend and layer another type of terrain on top of the base terrain. Note that the terrain properties like buildings that can be placed on terrain are still determined by the base terrain. This means that you won't be able to build buildings on ice layered with grass but you will be able to build buildings on grass layered with ice
3. `Eye Candy`: determines if the terrain you place automatically spawns eye candy on top of it. Eye candy are plants and other units that are generated for aesthetic reasons only, hence the name "eye candy"
4. `No Waves on Shore`: disables waves on water throughout the map
5. `Water Definitions`: this option changes what water looks like throughout the map

Different water definitions are shown below:

`Preset_Main`:
![Preset_Main](imgs/preset_main.png "Preset_Main")

`Preset_FE1`:
![Preset_FE1](imgs/preset_fe1.png "Preset_FE1")

`Preset_FE2`:
![Preset_FE2](imgs/preset_fe2.png "Preset_FE2")

`Preset_WickedWitch`:
![Preset_WickedWitch](imgs/preset_wicked_witch.png "Preset_WickedWitch")


6. `Beach Type`: this option changes the type of beach terrain that is placed down when water terrain is placed. Exploring the different beach types has been left as an excersise for the reader.

### 3.2. Elevation

This option allows you to change the elevation of existing tiles on the map.

1. `Brush Size`: allows you to pick how large of an area you want to affect on the map at once

*Trick*: In the editor, there are 7 different levels of elevation to chose from, but the elevation can actually have higher or lower values. In the editor, there is no way to make water have elevation either, but it is actually possible to give water elevation as well. Both of these things requires use of external map editing tools and are covered under the `AoE2ScenarioParser` Segment of this guide.

### 3.3. Cliffs

This option allows you to place cliffs on your map. There are two types of cliffs to chose from, Granite and Sandstone. They function exactly the same, and differ only in their appearence.

*Trick*: a cliff is actually a gaia object that can be rotated, if you go to the `Units` tab, and enable the `Rotate` option, you will be able to click the cliff and rotate it (right click rotates it in the opposite direction). There are a few rotations of the cliff objects that actually do not have graphics for them and hence appear invisible. but since they are still present on the map, just not visible, they block units from going through them. This mechanic can be used to make invisible walls on the map!

### 3.4. Map Copy

This option allows you to copy a part of the map and paste it using a brush. There are options to rotate and flip the selected area as well.

**Current Bug**: When a selection that is rectangular is rotated, the highlighted area that shows the brush DOES NOT rotate accordingly to show this rotation, but the game still pastes a rotated as you would expect.

There is also another option called `Change Player`. This option allows you to change the player of the units in the selection to another player when pasting the selection.

### 3.5. Erase

This option allows you to selectively remove parts of the map in an area using a brush. The objects that can be selectively removed when using this feature are:

1. Buildings
2. Gaia Objects
3. Invisible Units
4. Layered Terrain
5. Trees
6. Units

Note: The layering mode option in this tab seems to have no effect on the way that elements are erased.

## 4. Options

Under the `Options` tab in the editor, there are options to:

### 4.1. Point of View
Set the specified player's starting PoV to your current view in the editor using the `set view` button. Once the view is set, check that it works by clicking `go to view`

### 4.2. Testing Difficulty 
Set the `Testing Difficulty`

### 4.3. Full Tech Tree
Enable `Full Tech Tree`. Note that this is a global option, and not specific to the player. Also note that this option does not disable civ bonuses unlike the full tech tree option in normal games!

### 4.4. Disable Objects
Disable Buildings, Units or Techs by moving them from the `Full List` to the `Disabled List` by clicking the `<` arrow. remove an object from the disabled list by clicking `>`. The `<<` and `>>` move all items at once  
Note: Using this option to disable objects is not recommended as there is a better way to do it via triggers which will be covered in the triggers segment of this guide.

### 4.5. Collide & Correcting
Enabling this option makes stationary units move out the way to let moving units pass through. 

### 4.6. Villager Force Drop
Makes villagers instantly lose their resources when their tasks are switched instead of losing when they actually start working on the other task. This mimics FE behaviour, i.e. if villagers are switched from hunters to sheep, they don't lose any food.

### 4.7. Block Humanity Team Change
Lock Teams ONLY for human players.

## 5. Players

Under the `Players` tab in the editor, there are several properties that can be changed about the players

### 5.1. Number of Players
The total number of players you have in your scenario
### 5.2. Starting Age
Specify the starting age for the currently selected player
### 5.3. Colour
Specify the colour of the currently selected player
### 5.4. Starting Resources
`Food`, `Wood`, `Stone`, `Gold` determine the starting amount of the currently selected player's resources
### 5.5. Pop Limit
Determine the maximum population limit allowed for the currently selected player. This value is capped at 500
### 5.6. Base Priority
This option seems to have no effect on the game.  
(Note: If you are aware of what this does, please reach out to one of the authors of this guide and let them know!)
### 5.7. Tribe Name
Sets the name for the currently selected player **if** they are an AI. Does not effect human players
### 5.8. Name String ID
This field is used for refering to names that the game recognises by default. It can be used to automatically set a `Tribe name` by using a value that the game recognises. Trying out the value `1` in this field on an AI and seeing what happens is left as an excersise for the reader.
### 5.9. Personality
The AI to use for this player if they are not a human player. Pick `E3-p2.ai` to simulate an afk player
### 5.10. Player Type
This setting doesn't make a difference to gameplay. The only difference between the two options is that setting this to `Either` wont auto fill lobby slots with AIs. Setting it to `AI` will automatically set that player up for you in a lobby game
### 5.11. Civilization
Set the currently selected player's civilization
### 5.12. Lock Civ
Prevent the currently selected player from changing their civilization in a lobby
### 5.13. Architecture
Change the currently selected player's architecture set to another civilization's.
### 5.14. Swap Players
Swap the settings for the currently selected player with the specified player.

## 6. Messages

Under the `Messages` tab, there are different options for displaying text in the scenario.

### 6.1. Scenario Instructions
This 

## Useful Hotkeys

1. Scrolling up and down on a dropdown list makes the values go up and down the lists as well
2. Pressing or holding a letter in any object selection menu will cycle through the list of objects
3. If you are on a tab where a player can be selected (except triggers) then pressing numbers 1-8 will switch to that player
4. When testing a scenario (this also works in SP games, and is counted as a cheat) pressing `Ctrl+Shift+F#` where `#` is the number of a player, will let you control that player. For example, pressing `Ctrl+Shift+F4` will shift your control to player 4
5. Scrolling when placing objects will rotate them. Some gaia buildings and units have entirely different graphics for different rotations!
6. Pressing `Ctrl+G` once allows for off grid placement of units. Pressing it again allows for stacking units and off grid placement together. Pressing a 3rd time allows for on grid unit placement with stacking enabled. Pressing a 4th time makes it go back to default! Even Buildings can be stacked using this option!
7. `Ctrl+Q` Quit the scenario editor
8. `Ctrl+A` Toggle hitboxes on every unit on the map
9. `Ctrl+S` Save the scenario
10. `Ctrl+L` Load a scenario
11. `Ctrl+N` Create a new scenario
12. Tabs
    1. `F1`-`F10` selects a tab in the scenario editor. `F1` - Map, `F2` - Terrain, and so on
    2. `Ctrl+W` Switch to the `Messages` tab
    3. `Ctrl+R` Switch to the `Triggers` tab
    4. `Ctrl+T` Switch to the `Terrain` tab
    5. `Ctrl+U` Switch to the `Units` tab
    6. `Ctrl+O` Switch to the `Options` tab
    7. `Ctrl+P` Switch to the `Players` tab
    8. `Ctrl+D` Switch to the `Diplomacy` tab
    9. `Ctrl+C` Switch to the `Cinematics` tab
    10. `Ctrl+V` Switch to the `Global Victory` tab
    11. `Ctrl+M` Switch to the `Map` tab