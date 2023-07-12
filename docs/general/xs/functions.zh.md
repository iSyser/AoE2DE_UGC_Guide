---
hide:
#     - navigation
#     - toc
---

_作者：Alian713_

## 1. 规则

### 1.1. xs 禁用规则

真实函数名: xsDisableRule

返回类型: `#!cpp void`

函数原型: `#!cpp void xsDisableRule(string ruleName);`

参数:

1.  `#!cpp string 规则名称`: 欲禁用规则的名称

禁用给定的规则。

### 1.2. xs 禁用规则组

真实函数名: xsDisableRuleGroup

返回类型: `#!cpp void`

函数原型: `#!cpp void xsDisableRuleGroup(string ruleGroupName);`

参数:

1.  `#!cpp string 规则组名`: 欲禁用规则组的名称

禁用给定规则组中的所有规则

### 1.3. xs 禁用自身

真实函数名: xsDisableSelf

返回类型: `#!cpp void`

函数原型: `#!cpp void xsDisableSelf();`

禁用该函数所处的规则。不能在规则主体之外使用！

### 1.4. xs 启用规则

真实函数名: xsEnableRule

返回类型: `#!cpp void`

函数原型: `#!cpp void xsEnableRule(string ruleName);`

参数:

1.  `#!cpp string 规则名称`: 欲启用规则的名称

启用给定的规则。

### 1.5. xs 启用规则组

真实函数名: xsEnableRuleGroup

返回类型: `#!cpp void`

函数原型: `#!cpp void xsEnableRuleGroup(string ruleGroupName);`

参数:

1.  `#!cpp string 规则组名`: 欲启用规则组的名称

启用给定规则组中的所有规则

### 1.6. xs 规则是否启用

真实函数名: xsIsRuleEnabled

返回类型: `#!cpp bool`

函数原型: `#!cpp bool xsIsRuleEnabled(string ruleName);`

参数:

1.  `#!cpp string 规则名称`: 欲检查规则的名称

如果规则启用则返回真，否则返回假。

### 1.7. xs 规则组是否启用

真实函数名: xsIsRuleGroupEnabled

返回类型: `#!cpp bool`

函数原型: `#!cpp bool xsIsRuleGroupEnabled(string ruleGroupName);`

参数:

1.  `#!cpp string 规则组名`: 欲检查规则组的名称

如果给定规则组中的所有规则均已启用，则返回真

### 1.8. xs 设置规则最大间隔

真实函数名: xsSetRuleMaxInterval

返回类型: `#!cpp void`

函数原型: `#!cpp void xsSetRuleMaxInterval(string ruleName, int interval);`

参数:

1.  `#!cpp string 规则名称`: 欲设置最大间隔规则的名称
2.  `#!cpp int 间隔`: 规则的新最大时间间隔

设置给定规则的在块必须再次执行之前可能经过的最大时间间隔

### 1.9. xs 设置自身规则最大间隔

真实函数名: xsSetRuleMaxIntervalSelf

返回类型: `#!cpp void`

函数原型: `#!cpp void xsSetRuleMaxIntervalSelf(int interval);`

参数:

1.  `#!cpp int 间隔`: 规则的新最大时间间隔

设置该函数所处规则的最大间隔。不能在规则主体之外使用！

### 1.10. xs 设置规则最小间隔

真实函数名: xsSetRuleMinInterval

返回类型: `#!cpp void`

函数原型: `#!cpp void xsSetRuleMinInterval(string ruleName, int interval);`

参数:

1.  `#!cpp string 规则名称`: 欲设置最小间隔规则的名称
2.  `#!cpp int 间隔`: 规则的新最小时间间隔

设置给定规则的再次执行块之前必须经过的最小时间间隔。

### 1.11. xs 设置自身规则最小间隔

真实函数名: xsSetRuleMinIntervalSelf

返回类型: `#!cpp void`

函数原型: `#!cpp void xsSetRuleMinIntervalSelf(int interval);`

参数:

1.  `#!cpp int 间隔`: 规则的新最小时间间隔

设置该函数所处规则的最小间隔。不能在规则主体之外使用！

### 1.12. xs 设置规则优先级

真实函数名: xsSetRulePriority

返回类型: `#!cpp void`

函数原型: `#!cpp void xsSetRulePriority(string ruleName, int priority);`

参数:

1.  `#!cpp string 规则名称`: 欲设置优先级规则的名称
2.  `#!cpp int 优先级`: 规则的新优先级

设置给定规则的优先级。

### 1.13. xs 设置自身规则优先级

真实函数名: xsSetRulePrioritySelf

返回类型: `#!cpp void`

函数原型: `#!cpp void xsSetRulePrioritySelf(int priority);`

参数:

1.  `#!cpp int 优先级`: 规则的新优先级

设置该函数所处规则的优先级。不能在规则主体之外使用！

## 2. 向量

### 2.1. xsVectorGetX

返回类型: `#!cpp float`

函数原型: `#!cpp float xsVectorGetX(vector v);`

参数:

1.  `#!cpp vector v`: The vector to get the X coordinate of

The X coordinate of the vector given.

### 2.2. xsVectorGetY

返回类型: `#!cpp float`

函数原型: `#!cpp float xsVectorGetY(vector v);`

参数:

1.  `#!cpp vector v`: The vector to get the Y coordinate of

The Y coordinate of the vector given.

### 2.3. xsVectorGetZ

返回类型: `#!cpp float`

函数原型: `#!cpp float xsVectorGetZ(vector v);`

参数:

1.  `#!cpp vector v`: The vector to get the Z coordinate of

The Z coordinate of the vector given.

### 2.4. xsVectorLength

返回类型: `#!cpp float`

函数原型: `#!cpp float xsVectorLength(vector v);`

参数:

1.  `#!cpp vector v`: The vector to calculate the length of

Returns the length of the given vector.

### 2.5. xsVectorNormalize

返回类型: `#!cpp vector`

函数原型: `#!cpp vector xsVectorNormalize(vector v);`

参数:

1.  `#!cpp vector v`: The vector to normalise

Returns the normalised vector in the direction of the given vector.

### 2.6. xsVectorSet

返回类型: `#!cpp vector`

函数原型: `#!cpp vector xsVectorSet(float x, float y, float z);`

参数:

1.  `#!cpp float x`: The value to set the X coordinate to
2.  `#!cpp float y`: The value to set the Y coordinate to
3.  `#!cpp float z`: The value to set the Z coordinate to

Returns a vector with the given X, Y and Z components.

### 2.7. xsVectorSetX

返回类型: `#!cpp vector`

函数原型: `#!cpp vector xsVectorSetX(vector v, float x);`

参数:

1.  `#!cpp vector v`: The vector to modify the X coordinate of
2.  `#!cpp float x`: The value to set the X coordinate to

Returns a new vector with the X component of the given vector changed to the given value. Note: This function DOES NOT modify the vector given as the parameter!

### 2.8. xsVectorSetY

返回类型: `#!cpp vector`

函数原型: `#!cpp vector xsVectorSetY(vector v, float y);`

参数:

1.  `#!cpp vector v`: The vector to modify the Y coordinate of
2.  `#!cpp float y`: The value to set the Y coordinate to

Returns a new vector with the Y component of the given vector changed to the given value. Note: This function DOES NOT modify the vector given as the parameter!

### 2.9. xsVectorSetZ

返回类型: `#!cpp vector`

函数原型: `#!cpp vector xsVectorSetZ(vector v, float z);`

参数:

1.  `#!cpp vector v`: The vector to modify the Z coordinate of
2.  `#!cpp float z`: The value to set the Z coordinate to

Returns a new vector with the Z component of the given vector changed to the given value. Note: This function DOES NOT modify the vector given as the parameter!

## 3. 数组

### 3.1. xsArrayCreateBool

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArrayCreateBool(int size, bool defaultValue, string uniqueName);`

参数:

1.  `#!cpp int size`: The length of the array to create
2.  `#!cpp bool defaultValue`: The default value to initialise all the values in the array to
3.  `#!cpp string uniqueName`: A unique name of the created array

Creates an array of type bool and returns its ID.

### 3.2. xsArrayCreateFloat

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArrayCreateFloat(int size, float defaultValue, string uniqueName);`

参数:

1.  `#!cpp int size`: The length of the array to create
2.  `#!cpp float defaultValue`: The default value to initialise all the values in the array to
3.  `#!cpp string uniqueName`: A unique name of the created array

Creates an array of type float and returns its ID.

### 3.3. xsArrayCreateInt

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArrayCreateInt(int size, int defaultValue, string uniqueName);`

参数:

1.  `#!cpp int size`: The length of the array to create
2.  `#!cpp int defaultValue`: The default value to initialise all the values in the array to
3.  `#!cpp string uniqueName`: A unique name of the created array

Creates an array of type int and returns its ID.

### 3.4. xsArrayCreateString

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArrayCreateString(int size, string defaultValue, string uniqueName);`

参数:

1.  `#!cpp int size`: The length of the array to create
2.  `#!cpp string defaultValue`: The default value to initialise all the values in the array to
3.  `#!cpp string uniqueName`: A unique name of the created array

Creates an array of type String and returns its ID.

### 3.5. xsArrayCreateVector

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArrayCreateVector(int size, vector defaultValue, string uniqueName);`

参数:

1.  `#!cpp int size`: The length of the array to create
2.  `#!cpp vector defaultValue`: The default value to initialise all the values in the array to
3.  `#!cpp string uniqueName`: A unique name of the created array

Creates an array of type Vector and returns its ID.

### 3.6. xsArrayGetBool

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArrayGetBool(int arrayID, int index);`

参数:

1.  `#!cpp int arrayID`: The ID of the array to get the value from
2.  `#!cpp int index`: The index to get the value of

Gets and returns the value of the given bool array at the specifed index.

### 3.7. xsArrayGetFloat

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArrayGetFloat(int arrayID, int index);`

参数:

1.  `#!cpp int arrayID`: The ID of the array to get the value from
2.  `#!cpp int index`: The index to get the value of

Gets and returns the value of the given float array at the specifed index.

### 3.8. xsArrayGetInt

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArrayGetInt(int arrayID, int index);`

参数:

1.  `#!cpp int arrayID`: The ID of the array to get the value from
2.  `#!cpp int index`: The index to get the value of

Gets and returns the value of the given int array at the specifed index.

### 3.9. xsArrayGetSize

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArrayGetSize(int arrayID);`

参数:

1.  `#!cpp int arrayID`: The ID of the array to get the length of

Returns the length of the given array.

### 3.10. xsArrayGetString

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArrayGetString(int arrayID, int index);`

参数:

1.  `#!cpp int arrayID`: The ID of the array to get the value from
2.  `#!cpp int index`: The index to get the value of

Gets and returns the value of the given String array at the specifed index.

### 3.11. xsArrayGetVector

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArrayGetVector(int arrayID, int index);`

参数:

1.  `#!cpp int arrayID`: The ID of the array to get the value from
2.  `#!cpp int index`: The index to get the value of

Gets and returns the value of the given Vector array at the specifed index.

### 3.12. xsArrayResizeBool

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArrayResizeBool(int arrayID, int newSize);`

参数:

1.  `#!cpp int arrayID`: The ID of the array to resize
2.  `#!cpp int newSize`: The new size of the array

Resizes the the given bool array to the specifed size and returns 1.

### 3.13. xsArrayResizeFloat

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArrayResizeFloat(int arrayID, int newSize);`

参数:

1.  `#!cpp int arrayID`: The ID of the array to resize
2.  `#!cpp int newSize`: The new size of the array

Resizes the the given float array to the specifed size and returns 1.

### 3.14. xsArrayResizeInt

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArrayResizeInt(int arrayID, int newSize);`

参数:

1.  `#!cpp int arrayID`: The ID of the array to resize
2.  `#!cpp int newSize`: The new size of the array

Resizes the the given int array to the specifed size and returns 1.

### 3.15. xsArrayResizeString

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArrayResizeString(int arrayID, int newSize);`

参数:

1.  `#!cpp int arrayID`: The ID of the array to resize
2.  `#!cpp int newSize`: The new size of the array

Resizes the the given String array to the specifed size and returns 1.

### 3.16. xsArrayResizeVector

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArrayResizeVector(int arrayID, int newSize);`

参数:

1.  `#!cpp int arrayID`: The ID of the array to resize
2.  `#!cpp int newSize`: The new size of the array

Resizes the the given Vector array to the specifed size and returns 1.

### 3.17. xsArraySetBool

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArraySetBool(int arrayID, int index, bool value);`

参数:

1.  `#!cpp int arrayID`: The ID of the array to set the value in
2.  `#!cpp int index`: The index to set the value of
3.  `#!cpp bool value`: The new value to set

Sets the valuat the specified indedx e of the given bool arrindex to the provided value and returns 1.

### 3.18. xsArraySetFloat

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArraySetFloat(int arrayID, int index, float value);`

参数:

1.  `#!cpp int arrayID`: The ID of the array to set the value in
2.  `#!cpp int index`: The index to set the value of
3.  `#!cpp float value`: The new value to set

Sets the valueat the specified indedx of the given float array to the provided value and returns 1.

### 3.19. xsArraySetInt

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArraySetInt(int arrayID, int index, int value);`

参数:

1.  `#!cpp int arrayID`: The ID of the array to set the value in
2.  `#!cpp int index`: The index to set the value of
3.  `#!cpp int value`: The new value to set

Sets the valat the specified indedx ue of the given int arrindex to the provided value and returns 1.

### 3.20. xsArraySetString

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArraySetString(int arrayID, int index, string value);`

参数:

1.  `#!cpp int arrayID`: The ID of the array to set the value in
2.  `#!cpp int index`: The index to set the value of
3.  `#!cpp string value`: The new value to set

Sets the value at the specified indedx of the given String array to the provided value and returns 1.

### 3.21. xsArraySetVector

返回类型: `#!cpp int`

函数原型: `#!cpp int xsArraySetVector(int arrayID, int index, vector value);`

参数:

1.  `#!cpp int arrayID`: The ID of the array to set the value in
2.  `#!cpp int index`: The index to set the value of
3.  `#!cpp vector value`: The new value to set

Sets the value at the specified indedx of the given Vector array to the provided value and returns 1.

## 4. 数学

### 4.1. abs

返回类型: `#!cpp float`

函数原型: `#!cpp float abs(float x);`

参数:

1.  `#!cpp float x`: The number to find the absolute value of

Returns the absolute value (magnitude) of the given number.

### 4.2. acos

返回类型: `#!cpp float`

函数原型: `#!cpp float acos(float x);`

参数:

1.  `#!cpp float x`: The value to find the inverse cosine of

Returns the inverse cosine (arccos) of the given value

### 4.3. asin

返回类型: `#!cpp float`

函数原型: `#!cpp float asin(float x);`

参数:

1.  `#!cpp float x`: The value to find the inverse sine of

Returns the inverse sine (arcsin) of the given value

### 4.4. atan

返回类型: `#!cpp float`

函数原型: `#!cpp float atan(float x);`

参数:

1.  `#!cpp float x`: The value to find the inverse tangent of

Returns the inverse tangent (arctan) of the given value

### 4.5. atan2

返回类型: `#!cpp float`

函数原型: `#!cpp float atan2(float x);`

参数:

1.  `#!cpp float x`: The X coordinate of the point to find the amplitude of

This is supposed to be the atan2(y, x) function but apparently it only takes one input. ThxDE

### 4.6. cos

返回类型: `#!cpp float`

函数原型: `#!cpp float cos(float x);`

参数:

1.  `#!cpp float x`: The angle (in radians) to find the cosine of

Returns the cosine of the angle in radians

### 4.7. pow

返回类型: `#!cpp float`

函数原型: `#!cpp float pow(float x, float y);`

参数:

1.  `#!cpp float x`: The base value
2.  `#!cpp float y`: The exponenet to raise the base value to

Returns x raised to the power y (x\*\*y).

### 4.8. sin

返回类型: `#!cpp float`

函数原型: `#!cpp float sin(float x);`

参数:

1.  `#!cpp float x`: The angle (in radians) to find the sine of

Returns the sine of the angle in radians.

### 4.9. sqrt

返回类型: `#!cpp float`

函数原型: `#!cpp float sqrt(float x);`

参数:

1.  `#!cpp float x`: The number to find the square root of

Returns the square root of the given number.

### 4.10. tan

返回类型: `#!cpp float`

函数原型: `#!cpp float tan(float x);`

参数:

1.  `#!cpp float x`: The angle (in radians) to find the tangent of

Returns the tangent of the angle in radians

## 5. 通用

### 5.1. xsChatData

返回类型: `#!cpp void`

函数原型: `#!cpp void xsChatData(string message, int value);`

参数:

1.  `#!cpp string message`: The message to display in chat
2.  (可选) `#!cpp int value`: This value is inserted in place of any `%d` used in the message of the function

Shows the given message in the game chat

### 5.2. xsEffectAmount

返回类型: `#!cpp void`

函数原型: `#!cpp void xsEffectAmount(int effectID, int unitOrTechnologyID, int attributeOrOperation, float value, int playerNumber);`

参数:

1.  `#!cpp int effectID`: The ID of the effect to use
2.  `#!cpp int unitOrTechnologyID`: The ID of the unit or technology to effect
3.  `#!cpp int attributeOrOperation`: The attribute to modify or the operation to perform
4.  `#!cpp float value`: The value of the effect
5.  (可选) `#!cpp int playerNumber`: The player to apply the effect to. If unspecified, applies to all players except Gaia.

Change the specified attribute of the specified unit or technology by the value for the specified player. For more information on this, check the [UserPatch]("Jump to: UserPatch NON EXISTENT") section of the guide

### 5.3. xsGetGameTime

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetGameTime();`

Returns the current game time in seconds

### 5.4. xsGetMapHeight

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetMapHeight();`

Returns the Height of the map.

### 5.5. xsGetMapID

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetMapID();`

Returns the AI map type.

### 5.6. xsGetMapName

返回类型: `#!cpp string`

函数原型: `#!cpp string xsGetMapName(bool showFileExtension);`

参数:

1.  `#!cpp bool showFileExtension`: If this is set to true, then the returned name also contains the file extension

Returns the name of the map currently being played.

### 5.7. xsGetMapWidth

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetMapWidth();`

Returns the Width of the map.

### 5.8. xsGetNumPlayers

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetNumPlayers();`

Returns the number of players in the game

### 5.9. xsGetObjectCount

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetObjectCount(int playerId, int id);`

参数:

1.  `#!cpp int playerId`: The player to get the object count for
2.  `#!cpp int id`: The ID of the object to get the count for

Returns the number of currently alive objects of with the given ID of the specified player. The behaviours of these two functions is identical, the same descriptions are not a mistake.

### 5.10. xsGetObjectCountTotal

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetObjectCountTotal(int playerId, int id);`

参数:

1.  `#!cpp int playerId`: The player to get the object count for
2.  `#!cpp int id`: The ID of the object to get the count for

Returns the number of currently alive objects of with the given ID of the specified player. The behaviours of these two functions is identical, the same descriptions are not a mistake.

### 5.11. xsGetPlayerCivilization

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetPlayerCivilization(int playerNumber);`

参数:

1.  `#!cpp int playerNumber`: The player to get the civilization of

Returns the civilization ID of the given player. Refer to the [Constant Reference](../constants/#3-civs "Jump to: XS Scriptin > Constant Reference > #3. Civs") for all the different civ IDs

### 5.12. xsGetPlayerInGame

返回类型: `#!cpp bool`

函数原型: `#!cpp bool xsGetPlayerInGame(int playerNumber);`

参数:

1.  `#!cpp int playerNumber`: Check if this player is still alive

Returns true if the player given is still alive, and false otherwise.

### 5.13. xsGetPlayerNumberOfTechs

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetPlayerNumberOfTechs(int playerNumber);`

参数:

1.  `#!cpp int playerNumber`: The player whoes technology count is being requested.

Returns the number of technologies available to the player in the entire game.

### 5.14. xsGetRandomNumber

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetRandomNumber();`

Returns a random number between 0 and 32766.

### 5.15. xsGetRandomNumberLH

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetRandomNumberLH(int low, int high);`

参数:

1.  `#!cpp int low`: The lower bound for the range for the random number returned (included)
2.  `#!cpp int high`: The upper bound for the range for the random number returned (excluded)

Returns a random number between `low` and `high`

### 5.16. xsGetRandomNumberMax

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetRandomNumberMax(int max);`

参数:

1.  `#!cpp int max`: The upper bound for the range for the random number returned (excluded)

Returns a random number between 0 and `max`.

### 5.17. xsGetTime

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetTime();`

Returns the current game time - 1 in seconds

### 5.18. xsGetVictoryCondition

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetVictoryCondition();`

Returns one of these constants: `cStandardVictory` `cWonderVictory` `cRelicVictory` `cKingOfTheHillVictory`

### 5.19. xsGetVictoryConditionForSecondaryGameMode

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetVictoryConditionForSecondaryGameMode();`

Returns one of these constants: `cStandardVictory` `cWonderVictory` `cRelicVictory` `cKingOfTheHillVictory`

### 5.20. xsGetVictoryPlayer

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetVictoryPlayer();`

Returns the number of the player with the highest score in a normal game. Returns the number of the player who owns 5 relics or has a wonder if standard victory is enabled. In a game like KoTH, returns the number of the player who owns the monument.

### 5.21. xsGetVictoryPlayerForSecondaryGameMode

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetVictoryPlayerForSecondaryGameMode();`

Returns `1` when no secondary game mode is set. Returns the number of the player who owns the monument in game modes like KotH

### 5.22. xsGetVictoryTime

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetVictoryTime();`

For game modes like KoTH and other game modes where there is a timer on the screen, it returns the amount of time left in half seconds. meaning if the value returned is 799, it means there are 399.5s remaining. Returns `-1` otherwise

### 5.23. xsGetVictoryTimeForSecondaryGameMode

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetVictoryTimeForSecondaryGameMode();`

For game modes like KoTH and other game modes where there is a timer on the screen, it returns the amount of time left in half seconds. meaning if the value returned is 799, it means there are 399.5s remaining. Returns `-1` otherwise

### 5.24. xsGetVictoryType

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetVictoryType();`

Returns an integer corresponding to different victory settings ingame. These are:

0: Standard

1: Conquest

2: Time Limit

3: Score

4: Custom (scenarios only).

Last Man Standing returns 0 as well.

### 5.25. xsPlayerAttribute

返回类型: `#!cpp float`

函数原型: `#!cpp float xsPlayerAttribute(int playerNumber, int resourceID);`

参数:

1.  `#!cpp int playerNumber`: The player to get the resource of (0 for Gaia)
2.  `#!cpp int resourceID`: The ID of the resource to get the amount of

Returns the amount the specified resource of the given player.

### 5.26. xsResearchTechnology

返回类型: `#!cpp bool`

函数原型: `#!cpp bool xsResearchTechnology(int techID, bool force, bool techAvailable, int playerNumber);`

参数:

1.  `#!cpp int techID`: The technology ID to research.
2.  `#!cpp bool force`: Force researching the tech even if it is not enabled. To force an unavailable tech, the argument `techAvailable` must be set to false
3.  `#!cpp bool techAvailable`: This flag determines if it is required to check if a tech is available before researching it
4.  `#!cpp int playerNumber`: The player to research the technology for

Returns a boolean based on whether the technology was researched or not.

### 5.27. xsSetPlayerAttribute

返回类型: `#!cpp void`

函数原型: `#!cpp void xsSetPlayerAttribute(int playerNumber, int resourceID, float value);`

参数:

1.  `#!cpp int playerNumber`: The player to set the resource of (0 for Gaia)
2.  `#!cpp int resourceID`: The ID of the resource to set the amount of
3.  `#!cpp float value`: The amount to set the resource to

Sets the amount of the specified resource of the given player to the provided value.

### 5.28. xsSetTriggerVariable

返回类型: `#!cpp void`

函数原型: `#!cpp void xsSetTriggerVariable(int variableID, int value);`

参数:

1.  `#!cpp int variableID`: The ID of the variable to set the value of
2.  `#!cpp int value`: The value to set the variable to

Sets the value of the variable of the given variable ID to the provided value.

### 5.29. xsTriggerVariable

返回类型: `#!cpp int`

函数原型: `#!cpp int xsTriggerVariable(int variableID);`

参数:

1.  `#!cpp int variableID`: The ID of the variable to get the value of

Returns the value of the variable of the given variable ID.

## 6. 文件读写

### 6.1. xsCloseFile

返回类型: `#!cpp bool`

函数原型: `#!cpp bool xsCloseFile();`

Close the currently opened or created file. Returns `#!cpp true` if the file was successfully closed

### 6.2. xsCreateFile

返回类型: `#!cpp bool`

函数原型: `#!cpp bool xsCreateFile(bool append);`

参数:

1.  (可选) `#!cpp bool append`: Default: `#!cpp true`. If set to `#!cpp false`, this will overwrite any existing file with the same name.

Creates a new (or appends to an existing) `.xsdat` file with the same name as the RMS/scenario being played. After invoking this function, the writing functions can be used to write data to the file. Returns `#!cpp true` if the file was successfully created

### 6.3. xsGetDataTypeSize

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetDataTypeSize(int type);`

参数:

1.  `#!cpp int type`: One of the `cOffsetXXX` constants may be used as a parameter

Returns the number of bytes used to store a given type value.

### 6.4. xsGetFilePosition

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetFilePosition();`

Gets the byte (0-indexed) of the file that the next read function will start reading from.

### 6.5. xsGetFileSize

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetFileSize();`

Gets the size (in bytes) of the currently open file

### 6.6. xsOffsetFilePosition

返回类型: `#!cpp bool`

函数原型: `#!cpp bool xsOffsetFilePosition(int dataType, bool forward);`

参数:

1.  `#!cpp int dataType`: The [cOffset constants](../constants/#1-readwrite "Jump To: XS > Constant Reference > Read/Write Constants") can be used to specify the datatype used for the offset. Integers and floats are 4 bytes long, vectors are 12 bytes long and strings can be of variable length (specified by the 32 bit int preceeding the chars of the string)
2.  (可选) `#!cpp bool forward`: Default: `#!cpp true`. Setting this to `#!cpp false` will make the file position move back

Moves the file position forward (or backward) relative to the current file position, and by an amount of bytes equivalent to reading the given data type

### 6.7. xsOpenFile

返回类型: `#!cpp bool`

函数原型: `#!cpp bool xsOpenFile(string filename);`

参数:

1.  `#!cpp string filename`: The name of the file to open, without the `.xsdat` extension

Opens an existing `.xsdat`file in read only mode. After invoking this function, the reading functions can be used to read data from the file. Returns `#!cpp true` if the file was successfully opened

### 6.8. xsReadFloat

返回类型: `#!cpp float`

函数原型: `#!cpp float xsReadFloat();`

Reads and returns a float from the previously opened `.xsdat` file. Note that this function does not check if the value being read is actually meant to be a float, which means the value being read is bit casted into a float regardless of what it originally was. This function also moves the file position forward by 4 bytes

### 6.9. xsReadInt

返回类型: `#!cpp int`

函数原型: `#!cpp int xsReadInt();`

Reads and returns an integer from the previously opened `.xsdat` file. Note that this function does not check if the value being read is actually meant to be an integer, which means the value being read is bit casted into an integer regardless of what it originally was. This function also moves the file position forward by 4 bytes

### 6.10. xsReadString

返回类型: `#!cpp string`

函数原型: `#!cpp string xsReadString();`

Reads and returns a string from the previously opened `.xsdat` file. Note that this function does not check if the value being read is actually meant to be a string, which means the value being read is bit casted into a string regardless of what it originally was. This function also moves the file position forward by 4 bytes + the amount of bytes in the length of the string

### 6.11. xsReadVector

返回类型: `#!cpp vector`

函数原型: `#!cpp vector xsReadVector();`

Reads and returns a vector from the previously opened `.xsdat` file. Note that this function does not check if the value being read is actually meant to be a vector, which means the value being read is bit casted into a vector regardless of what it originally was. This function also moves the file position forward by 12 bytes

### 6.12. xsSetFilePosition

返回类型: `#!cpp bool`

函数原型: `#!cpp bool xsSetFilePosition(int byteOffset);`

参数:

1.  `#!cpp int byteOffset`: 0 indexed byte offset to determine which byte to read and return from the file

Sets the byte (0-indexed) of the file that the next read function will start reading from.

### 6.13. xsWriteFloat

返回类型: `#!cpp bool`

函数原型: `#!cpp bool xsWriteFloat(float data);`

参数:

1.  `#!cpp float data`: The float value to write

Writes a floating point number to the previously created `.xsdat` file. Causes an error if a file hasn't been opened before using. Returns `#!cpp true` if the floating point number was successfully written. Floats are written in the 32 bit IEEE 754 format

### 6.14. xsWriteInt

返回类型: `#!cpp bool`

函数原型: `#!cpp bool xsWriteInt(int data);`

参数:

1.  `#!cpp int data`: The integer to write

Writes an integer to the previously created `.xsdat` file. Causes an error if a file hasn't been opened before using. Returns `#!cpp true` if the integer was successfully written. Integers are written as signed 32 bit numbers

### 6.15. xsWriteString

返回类型: `#!cpp bool`

函数原型: `#!cpp bool xsWriteString(string data);`

参数:

1.  `#!cpp string data`: The string to write

Writes a string to the previously created `.xsdat` file. Causes an error if a file hasn't been opened before using. Returns `#!cpp true` if the string was successfully written. A string is written to the file in two parts, an unsigned 32 bit integer (indicates the length of the string) followed by that many bytes making up the actual characters of the string

### 6.16. xsWriteVector

返回类型: `#!cpp bool`

函数原型: `#!cpp bool xsWriteVector(vector data);`

参数:

1.  `#!cpp vector data`: The vector to write

Writes a vector to the previously created `.xsdat` file. Causes an error if a file hasn't been opened before using. Returns `#!cpp true` if the vector was successfully written. Vectors are written as 3 consecutive floating point numbers, one for each coordinate.

## 7. Functions With Seemingly No Practical Use

### 7.1. xsAddRuntimeEvent

返回类型: `#!cpp bool`

函数原型: `#!cpp bool xsAddRuntimeEvent(string runtimeName, string functionName, int functionArgument);`

参数:

1.  `#!cpp string runtimeName`: This is the name of the runtime to create the event in. This should be `"Random Map"` for RMS and `"Scenario Triggers"` for scenarios. Find which one to use in a general script by using the `#!cpp xsGetMapName(true)` [function](./#56-xsgetmapname "Jump To: Function Reference > xsGetMapName") and checking the extension.
2.  `#!cpp string functionName`: This is the name of a user defined function that takes a single integer argument
3.  `#!cpp int functionArgument`: This is an integer argument that is passed to the function given to the argument `functionName` when this event runs.

A runtime event is called after all the XS code has finished executing but before rules start executing. It calls the function `functionName` given to it with the `functionArgument` passed to it as a parameter. For programmers familiar with the terminology, this is basically a way to set a callback. It also returns true if the function name given to it exists, otherwise it returns false. Does not work with built-ins

### 7.2. xsBreakPoint

返回类型: `#!cpp void`

函数原型: `#!cpp void xsBreakPoint();`

This function adds a break point to the execution of code. Do not use this function and beware, if you do, it will likely cause a crash!

### 7.3. xsDumpArrays

返回类型: `#!cpp void`

函数原型: `#!cpp void xsDumpArrays();`

This function is supposed to blogs out all XS arrays. Currently, it does absolutely nothing.

### 7.4. xsGetContextPlayer

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetContextPlayer();`

Returns the current context player ID.

### 7.5. xsGetFunctionID

返回类型: `#!cpp int`

函数原型: `#!cpp int xsGetFunctionID(string functionName);`

参数:

1.  `#!cpp string functionName`: The name of the function to get the hash of

Returns the hash of a given function. This function has no practical application and is probably for internal usage only.

### 7.6. xsSetContextPlayer

返回类型: `#!cpp void`

函数原型: `#!cpp void xsSetContextPlayer(int playerNumber);`

参数:

1.  `#!cpp int playerNumber`: The player to set the context player to

In other functions involving a `playerNumber` argument, the value of the context player is used if `-1` is passed as `playerNumber` to them. `xsEffectAmount` will use the value of the context player as its player if `-2` is passed to it as the player argument.