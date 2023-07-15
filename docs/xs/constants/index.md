---
hide:
#     - navigation
#     - toc
---

# Constant Reference

_Written by: Alian713_

## 1. Read/Write { #ReadWrite }

### 1.1. cOffsetString { #cOffsetString }

Value: `#!cpp int 0`

Used with the [`xsOffsetFilePosition()`](../functions/#xsOffsetFilePosition "Jump To: XS Scripting > Function Reference > xsOffsetFilePosition") function. Makes the offset function move the file position by the number of bytes it takes to store a string (4 bytes + a number of bytes that is determined by the integer that the first 4 bytes represent)

### 1.2. cOffsetInterger { #cOffsetInterger }

Value: `#!cpp int 1`

Used with the [`xsOffsetFilePosition()`](../functions/#xsOffsetFilePosition "Jump To: XS Scripting > Function Reference > xsOffsetFilePosition") function. Makes the offset function move the file position by the number of bytes it takes to store an integer (4 bytes)

### 1.3. cOffsetFloat { #cOffsetFloat }

Value: `#!cpp int 2`

Used with the [`xsOffsetFilePosition()`](../functions/#xsOffsetFilePosition "Jump To: XS Scripting > Function Reference > xsOffsetFilePosition") function. Makes the offset function move the file position by the number of bytes it takes to store a float (4 bytes)

### 1.4. cOffsetVector { #cOffsetVector }

Value: `#!cpp int 3`

Used with the [`xsOffsetFilePosition()`](../functions/#xsOffsetFilePosition "Jump To: XS Scripting > Function Reference > xsOffsetFilePosition") function. Makes the offset function move the file position by the number of bytes it takes to store a vector (12 bytes)

## 2. Age { #Age }

### 2.1. cDarkAge { #cDarkAge }

Value: `#!cpp int 0`

Value of the [Current Age](../../general/resources/#6 "Jump to: Game Mechanics > Player Resources > Current Age") resource when a player is in the Dark Age

### 2.2. cFeudalAge { #cFeudalAge }

Value: `#!cpp int 1`

Value of the [Current Age](../../general/resources/#6 "Jump to: Game Mechanics > Player Resources > Current Age") resource when a player is in the Feudal Age

### 2.3. cCastleAge { #cCastleAge }

Value: `#!cpp int 2`

Value of the [Current Age](../../general/resources/#6 "Jump to: Game Mechanics > Player Resources > Current Age") resource when a player is in the Castle Age

### 2.4. cImperialAge { #cImperialAge }

Value: `#!cpp int 3`

Value of the [Current Age](../../general/resources/#6 "Jump to: Game Mechanics > Player Resources > Current Age") resource when a player is in the Imperial Age

## 3. Value { #Value }

### 3.1. cActivationTime { #cActivationTime }

Value: `#!cpp int None`

This value is only defined inside the body of a rule. It holds the time of initial activation of that rule

### 3.2. cOriginVector { #cOriginVector }

Value: `#!cpp vector (0, 0, 0)`

The Origin Vector

### 3.3. cInvalidVector { #cInvalidVector }

Value: `#!cpp vector (-1, -1, -1)`

The Invalid Vector

## 4. Victory Conditions { #VictoryConditions }

### 4.1. cStandardVictory { #cStandardVictory }

Value: `#!cpp int 100`

one of the values returned by the [`xsGetVictoryCondition()`](../functions/#xsGetVictoryCondition "Jump To: XS Scripting > Function Reference > xsGetVictoryCondition") function

### 4.2. cWonderVictory { #cWonderVictory }

Value: `#!cpp int 101`

one of the values returned by the [`xsGetVictoryCondition()`](../functions/#xsGetVictoryCondition "Jump To: XS Scripting > Function Reference > xsGetVictoryCondition") function

### 4.3. cRelicVictory { #cRelicVictory }

Value: `#!cpp int 102`

one of the values returned by the [`xsGetVictoryCondition()`](../functions/#xsGetVictoryCondition "Jump To: XS Scripting > Function Reference > xsGetVictoryCondition") function

### 4.4. cKingOfTheHillVictory { #cKingOfTheHillVictory }

Value: `#!cpp int 103`

one of the values returned by the [`xsGetVictoryCondition()`](../functions/#xsGetVictoryCondition "Jump To: XS Scripting > Function Reference > xsGetVictoryCondition") function

## 5. Civs { #Civs }

### 5.1. cGaia { #cGaia }

Value: `#!cpp int 0`

This is the civilization ID of Gaia

### 5.2. cBritons { #cBritons }

Value: `#!cpp int 1`

This is the civilization ID of Britons

### 5.3. cFranks { #cFranks }

Value: `#!cpp int 2`

This is the civilization ID of Franks

### 5.4. cGoths { #cGoths }

Value: `#!cpp int 3`

This is the civilization ID of Goths

### 5.5. cTeutons { #cTeutons }

Value: `#!cpp int 4`

This is the civilization ID of Teutons

### 5.6. cJapanese { #cJapanese }

Value: `#!cpp int 5`

This is the civilization ID of Japanese

### 5.7. cChinese { #cChinese }

Value: `#!cpp int 6`

This is the civilization ID of Chinese

### 5.8. cByzantines { #cByzantines }

Value: `#!cpp int 7`

This is the civilization ID of Byzantines

### 5.9. cPersians { #cPersians }

Value: `#!cpp int 8`

This is the civilization ID of Persians

### 5.10. cSaracens { #cSaracens }

Value: `#!cpp int 9`

This is the civilization ID of Saracens

### 5.11. cTurks { #cTurks }

Value: `#!cpp int 10`

This is the civilization ID of Turks

### 5.12. cVikings { #cVikings }

Value: `#!cpp int 11`

This is the civilization ID of Vikings

### 5.13. cMongols { #cMongols }

Value: `#!cpp int 12`

This is the civilization ID of Mongols

### 5.14. cCelts { #cCelts }

Value: `#!cpp int 13`

This is the civilization ID of Celts

### 5.15. cSpanish { #cSpanish }

Value: `#!cpp int 14`

This is the civilization ID of Spanish

### 5.16. cAztecs { #cAztecs }

Value: `#!cpp int 15`

This is the civilization ID of Aztecs

### 5.17. cMayans { #cMayans }

Value: `#!cpp int 16`

This is the civilization ID of Mayans

### 5.18. cHuns { #cHuns }

Value: `#!cpp int 17`

This is the civilization ID of Huns

### 5.19. cKoreans { #cKoreans }

Value: `#!cpp int 18`

This is the civilization ID of Koreans

### 5.20. cItalians { #cItalians }

Value: `#!cpp int 19`

This is the civilization ID of Italians

### 5.21. cIndians { #cIndians }

Value: `#!cpp int 20`

This is the civilization ID of Indians

### 5.22. cIncas { #cIncas }

Value: `#!cpp int 21`

This is the civilization ID of Incas

### 5.23. cMagyars { #cMagyars }

Value: `#!cpp int 22`

This is the civilization ID of Magyars

### 5.24. cSlavs { #cSlavs }

Value: `#!cpp int 23`

This is the civilization ID of Slavs

### 5.25. cPortuguese { #cPortuguese }

Value: `#!cpp int 24`

This is the civilization ID of Portuguese

### 5.26. cEthiopians { #cEthiopians }

Value: `#!cpp int 25`

This is the civilization ID of Ethiopians

### 5.27. cMalians { #cMalians }

Value: `#!cpp int 26`

This is the civilization ID of Malians

### 5.28. cBerbers { #cBerbers }

Value: `#!cpp int 27`

This is the civilization ID of Berbers

### 5.29. cKhmer { #cKhmer }

Value: `#!cpp int 28`

This is the civilization ID of Khmer

### 5.30. cMalay { #cMalay }

Value: `#!cpp int 29`

This is the civilization ID of Malay

### 5.31. cBurmese { #cBurmese }

Value: `#!cpp int 30`

This is the civilization ID of Burmese

### 5.32. cVietnamese { #cVietnamese }

Value: `#!cpp int 31`

This is the civilization ID of Vietnamese

### 5.33. cBulgarians { #cBulgarians }

Value: `#!cpp int 32`

This is the civilization ID of Bulgarians

### 5.34. cTatars { #cTatars }

Value: `#!cpp int 33`

This is the civilization ID of Tatars

### 5.35. cCumans { #cCumans }

Value: `#!cpp int 34`

This is the civilization ID of Cumans

### 5.36. cLithuanians { #cLithuanians }

Value: `#!cpp int 35`

This is the civilization ID of Lithuanians

### 5.37. cBurgundians { #cBurgundians }

Value: `#!cpp int 36`

This is the civilization ID of Burgundians

### 5.38. cSicilians { #cSicilians }

Value: `#!cpp int 37`

This is the civilization ID of Sicilians

### 5.39. cPoles { #cPoles }

Value: `#!cpp int 38`

This is the civilization ID of Poles

### 5.40. cBohemians { #cBohemians }

Value: `#!cpp int 39`

This is the civilization ID of Bohemians

### 5.41. cDravidians { #cDravidians }

Value: `#!cpp int 40`

This is the civilization ID of Dravidians

### 5.42. cBengalis { #cBengalis }

Value: `#!cpp int 41`

This is the civilization ID of Bengalis

### 5.43. cGurjaras { #cGurjaras }

Value: `#!cpp int 42`

This is the civilization ID of Gurjaras

### 5.44. cRomans { #cRomans }

Value: `#!cpp int 43`

This is the civilization ID of Romans

## 6. EffectAmount Effect Type { #EffectAmountEffectType }

### 6.1. cSetAttribute { #cSetAttribute }

Value: `#!cpp int 0`

This is the ID of the `Set Attribute` effect of the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cSetAttribute, unitID, attributeID, value)`

Example: `#!cpp xsEffectAmount(cSetAttribute, 74, cHitpoints, 100)`

This sets the HP of unit 74 (militia) to 100 (the value). Alternatively, any of the [Unit Attribute Constants](./#7-effectamount-unit-attribute "Jump to: Unit Attribute Constants") may be used to modify the corresponding unit property

### 6.2. cModResource { #cModResource }

Value: `#!cpp int 1`

This is the ID of the `Modify Resource` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cModResource, resourceID, operation, value)`

Example: `#!cpp xsEffectAmount(cModResource, cAttributeFood, cAttributeAdd, 100)`

This adds 100 to the current food amount. Alternatively, `cAttributeSet` may be used to set the food amount to 100. Also, see the [Resource](./#9-resource "Jump to: Constant Reference > Resource")

### 6.3. cEnableObject { #cEnableObject }

Value: `#!cpp int 2`

This is the ID of the `Enable (or disable) Object` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cEnableObject, unitID, enableOrDisable, 0)`

Example: `#!cpp xsEffectAmount(cEnableObject, 74, cAttributeDisable, 0)`

This disables the unit 74 (militia). Alternatively, `cAttributeEnable` may be used to enable an object instead

### 6.4. cUpgradeUnit { #cUpgradeUnit }

Value: `#!cpp int 3`

This is the ID of the `Upgrade Unit` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cUpgradeUnit, oldUnitID, newUnitID, 0)`

Example: `#!cpp xsEffectAmount(cUpgradeUnit, 74, 75, 0)`

This copies all units attributes except ID and available from unit 75 (man at arms) to 74 (militia)

### 6.5. cAddAttribute { #cAddAttribute }

Value: `#!cpp int 4`

This is the ID of the `Add Attribute` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cAddAttribute, unitID, attributeID, value)`

Example: `#!cpp xsEffectAmount(cAddAttribute, 74, 0, 100)`

This adds 100 (the value) to the attribute 0 (HP) of unit 74 (militia)

### 6.6. cMulAttribute { #cMulAttribute }

Value: `#!cpp int 5`

This is the ID of the `Multiply Attribute` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cMulAttribute, unitID, attributeID, value)`

Example: `#!cpp xsEffectAmount(cMulAttribute, 74, 0, 100)`

This multiplies the attribute 0 (HP) of unit 74 (militia) by 100 (the value)

### 6.7. cMulResource { #cMulResource }

Value: `#!cpp int 6`

This is the ID of the `Multiply Resource` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cMulResource, resourceID, 0, value)`

Example: `#!cpp xsEffectAmount(cMulResource, cAttributeFood, 0, 10)`

This multiplies the food amount by 10 (the value)

### 6.8. cEnableTech { #cEnableTech }

Value: `#!cpp int 7`

This is the ID of the `Enable (or disable) Technology` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cEnableTech, techID, enableOrDisable, 0)`

Example: `#!cpp xsEffectAmount(cEnableTech, 6, cAttributeEnable, 0)`

This enables the tech 6 (Drill). Alternatively, `cAttributeDisable` may be used to disable the tech instead

### 6.9. cModifyTech { #cModifyTech }

Value: `#!cpp int 8`

This is the ID of the `Modify Technology` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cModifyTech, techID, techAttribute, value)`

Example: `#!cpp xsEffectAmount(cModifyTech, 22, cAttrSetTime, 10)`

This sets the research time of tech 22 (loom) to 10s (the value). Alternatively, any of the [Tech Attribute Constants](./#6-effectamount-technology-attribute "Jump to: Tech Attribute Constants") may be used to modify the corresponding tech property

### 6.10. cSetPlayerData { #cSetPlayerData }

Value: `#!cpp int 9`

This is the ID of the `Set Player Data` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cSetPlayerData, 0, cAttributeSet, value)`

Example: `#!cpp xsEffectAmount(cSetPlayerData, 0, cAttributeSet, 10230)`

This sets the player data 0 (Civilization Name ID) to 10230 (the value)

### 6.11. cSetTechCost { #cSetTechCost }

Value: `#!cpp int 100`

This is the ID of the `Set Technology Cost` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cSetTechCost, techID, resourceID, value)`

Example: `#!cpp xsEffectAmount(cSetTechCost, 22, cAttributeFood, 10)`

This sets the food cost of tech 22 (loom) to 10 (the value)

### 6.12. cAddTechCost { #cAddTechCost }

Value: `#!cpp int 101`

This is the ID of the `Add Technology Cost` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cAddTechCost, techID, resourceID, value)`

Example: `#!cpp xsEffectAmount(cAddTechCost, 22, cAttributeFood, 10)`

This adds 10 (the) to the current food cost of tech 22 (loom)

### 6.13. cDisableTech { #cDisableTech }

Value: `#!cpp int 102`

This is the ID of the `Disable Tech` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cDisableTech, techID, 0, 0)`

Example: `#!cpp xsEffectAmount(cDisableTech, 22, 0, 0)`

This disables the tech 22 (loom)

### 6.14. cModTechTime { #cModTechTime }

Value: `#!cpp int 103`

This is the ID of the `Modify Technology Time` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cModTechTime, techID, operation, value)`

Example: `#!cpp xsEffectAmount(cModTechTime, 22, cAttributeSet, 10)`

This sets the research time of tech 22 (loom) to 10s (the value). Alternatively, `cAttributeAdd` may be used to add to the current research time of the technology

### 6.15. cGaiaSetAttribute { #cGaiaSetAttribute }

Value: `#!cpp int -1`

This is the ID of the `Gaia Set Attribute` effect of the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cGaiaSetAttribute, unitID, attributeID, value)`

Example: `#!cpp xsEffectAmount(cGaiaSetAttribute, 74, 0, 100)`

This sets the attribute 0 (HP) of unit 74 (militia) to 100 (the value)

### 6.16. cGaiaModResource { #cGaiaModResource }

Value: `#!cpp int -2`

This is the ID of the `Gaia Modify Resource` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cGaiaModResource, resourceID, operation, value)`

Example: `#!cpp xsEffectAmount(cGaiaModResource, cAttributeFood, cAttributeAdd, 100)`

This adds 100 to the current food amount. Alternatively, `cAttributeSet` may be used to set the food amount to 100

### 6.17. cGaiaEnableObject { #cGaiaEnableObject }

Value: `#!cpp int -3`

This is the ID of the `Gaia Enable (or disable) Object` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cGaiaEnableObject, unitID, enableOrDisable, 0)`

Example: `#!cpp xsEffectAmount(cGaiaEnableObject, 74, cAttributeDisable, 0)`

This disables the unit 74 (militia). Alternatively, `cAttributeEnable` may be used to enable an object instead

### 6.18. cGaiaUpgradeUnit { #cGaiaUpgradeUnit }

Value: `#!cpp int -4`

This is the ID of the `Gaia Upgrade Unit` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cGaiaUpgradeUnit, oldUnitID, newUnitID, 0)`

Example: `#!cpp xsEffectAmount(cGaiaUpgradeUnit, 74, 75, 0)`

This replaces all units 74 (militia) with 75 (man at arms) on the map and also disables unit 74 and enables unit 75

### 6.19. cGaiaAddAttribute { #cGaiaAddAttribute }

Value: `#!cpp int -5`

This is the ID of the `Gaia Add Attribute` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cGaiaAddAttribute, unitID, attributeID, value)`

Example: `#!cpp xsEffectAmount(cGaiaAddAttribute, 74, 0, 100)`

This adds 100 (the value) to the attribute 0 (HP) of unit 74 (militia)

### 6.20. cGaiaMulAttribute { #cGaiaMulAttribute }

Value: `#!cpp int -6`

This is the ID of the `Gaia Multiply Attribute` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cGaiaMulAttribute, unitID, attributeID, value)`

Example: `#!cpp xsEffectAmount(cGaiaMulAttribute, 74, 0, 100)`

This multiplies the attribute 0 (HP) of unit 74 (militia) by 100 (the value)

### 6.21. cGaiaMulResource { #cGaiaMulResource }

Value: `#!cpp int -7`

This is the ID of the `Gaia Multiply Resource` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cGaiaMulResource, resourceID, 0, value)`

Example: `#!cpp xsEffectAmount(cGaiaMulResource, cAttributeFood, 0, 10)`

This multiplies the food amount by 10 (the value)

### 6.22. cGaiaEnableTech { #cGaiaEnableTech }

Value: `#!cpp int -8`

This is the ID of the `Gaia Enable (or disable) Technology` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cGaiaEnableTech, techID, enableOrDisable, 0)`

Example: `#!cpp xsEffectAmount(cGaiaEnableTech, 6, cAttributeEnable, 0)`

This enables the tech 6 (Drill). Alternatively, `cAttributeDisable` may be used to disable the tech instead

### 6.23. cGaiaModifyTech { #cGaiaModifyTech }

Value: `#!cpp int -9`

This is the ID of the `Gaia Modify Technology` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cGaiaModifyTech, techID, techAttribute, value)`

Example: `#!cpp xsEffectAmount(cGaiaModifyTech, 22, cAttrSetTime, 10)`

This sets the research time of tech 22 (loom) to 10s (the value). Alternatively, any of the [Tech Attribute Constants](./6-effectamount-technology-attribute "Jump to: Tech Attribute Constants") may be used to modify the corresponding tech property

### 6.24. cGaiaSetPlayerData { #cGaiaSetPlayerData }

Value: `#!cpp int -10`

This is the ID of the `Gaia Set Player Data` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cGaiaSetPlayerData, 0, cAttributeSet, value)`

Example: `#!cpp xsEffectAmount(cGaiaSetPlayerData, 0, cAttributeSet, 10230)`

This sets the player data 0 (Civilization Name ID) to 10230 (the value)

### 6.25. cGaiaSetTechCost { #cGaiaSetTechCost }

Value: `#!cpp int -101`

This is the ID of the `Gaia Set Technology Cost` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cGaiaSetTechCost, techID, resourceID, value)`

Example: `#!cpp xsEffectAmount(cGaiaSetTechCost, 22, cAttributeFood, 10)`

This sets the food cost of tech 22 (loom) to 10 (the value)

### 6.26. cGaiaAddTechCost { #cGaiaAddTechCost }

Value: `#!cpp int -102`

This is the ID of the `Gaia Add Technology Cost` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cGaiaAddTechCost, techID, resourceID, value)`

Example: `#!cpp xsEffectAmount(cGaiaAddTechCost, 22, cAttributeFood, 10)`

This adds 10 (the) to the current food cost of tech 22 (loom)

### 6.27. cGaiaDisableTech { #cGaiaDisableTech }

Value: `#!cpp int -103`

This is the ID of the `Gaia Disable Tech` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cGaiaDisableTech, techID, 0, 0)`

Example: `#!cpp xsEffectAmount(cGaiaDisableTech, 22, 0, 0)`

This disables the tech 22 (loom)

### 6.28. cGaiaModTechTime { #cGaiaModTechTime }

Value: `#!cpp int -104`

This is the ID of the `Gaia Modify Technology Time` effect for the xsEffectAmount function

Syntax: `#!cpp xsEffectAmount(cGaiaModTechTime, techID, operation, value)`

Example: `#!cpp xsEffectAmount(cGaiaModTechTime, 22, cAttributeSet, 10)`

This sets the research time of tech 22 (loom) to 10s (the value). Alternatively, `cAttributeAdd` may be used to add to the current research time of the technology

## 7. EffectAmount Effect Operations { #EffectAmountEffectOperations }

### 7.1. cAttributeDisable { #cAttributeDisable }

Value: `#!cpp int 0`

This is the ID of the `Attribute Disbale` modifier for the xsEffectAmount function

### 7.2. cAttributeEnable { #cAttributeEnable }

Value: `#!cpp int 1`

This is the ID of the `Attribute Enable` modifier for the xsEffectAmount function

### 7.3. cAttributeForce { #cAttributeForce }

Value: `#!cpp int 2`

This is the ID of the `Attribute Force` modifier for the xsEffectAmount function

### 7.4. cAttributeSet { #cAttributeSet }

Value: `#!cpp int 0`

This is the ID of the `Attribute Set` modifier for the xsEffectAmount function

### 7.5. cAttributeAdd { #cAttributeAdd }

Value: `#!cpp int 1`

This is the ID of the `Attribute Add` modifier for the xsEffectAmount function

## 8. EffectAmount Technology Attribute { #EffectAmountTechnologyAttribute }

### 8.1. cAttrSetTime { #cAttrSetTime }

Value: `#!cpp int -1`

This is the ID of the `Attribute Set Time` modifier for the xsEffectAmount function

### 8.2. cAttrAddTime { #cAttrAddTime }

Value: `#!cpp int -2`

This is the ID of the `Attribute Add Time` modifier for the xsEffectAmount function

### 8.3. cAttrSetFoodCost { #cAttrSetFoodCost }

Value: `#!cpp int 0`

This is the ID of the `Attribute Set Food Cost` modifier for the xsEffectAmount function

### 8.4. cAttrSetWoodCost { #cAttrSetWoodCost }

Value: `#!cpp int 1`

This is the ID of the `Attribute Set Wood Cost` modifier for the xsEffectAmount function

### 8.5. cAttrSetStoneCost { #cAttrSetStoneCost }

Value: `#!cpp int 2`

This is the ID of the `Attribute Set Stone Cost` modifier for the xsEffectAmount function

### 8.6. cAttrSetGoldCost { #cAttrSetGoldCost }

Value: `#!cpp int 3`

This is the ID of the `Attribute Set Gold Cost` modifier for the xsEffectAmount function

### 8.7. cAttrAddFoodCost { #cAttrAddFoodCost }

Value: `#!cpp int 16384`

This is the ID of the `Attribute Add Food Cost` modifier for the xsEffectAmount function

### 8.8. cAttrAddWoodCost { #cAttrAddWoodCost }

Value: `#!cpp int 16385`

This is the ID of the `Attribute Add Wood Cost` modifier for the xsEffectAmount function

### 8.9. cAttrAddStoneCost { #cAttrAddStoneCost }

Value: `#!cpp int 16386`

This is the ID of the `Attribute Add Stone Cost` modifier for the xsEffectAmount function

### 8.10. cAttrAddGoldCost { #cAttrAddGoldCost }

Value: `#!cpp int 16387`

This is the ID of the `Attribute Add Gold Cost` modifier for the xsEffectAmount function

### 8.11. cAttrSetLocation { #cAttrSetLocation }

Value: `#!cpp int 4`

This is the ID of the `Attribute Set Tech Location` modifier for the xsEffectAmount function

### 8.12. cAttrSetButton { #cAttrSetButton }

Value: `#!cpp int 5`

This is the ID of the `Attribute Set Tech Button` modifier for the xsEffectAmount function

### 8.13. cAttrSetIcon { #cAttrSetIcon }

Value: `#!cpp int 6`

This is the ID of the `Attribute Set Tech Icon` modifier for the xsEffectAmount function

### 8.14. cAttrSetName { #cAttrSetName }

Value: `#!cpp int 7`

This is the ID of the `Attribute Set Tech Name` modifier for the xsEffectAmount function

### 8.15. cAttrSetDescription { #cAttrSetDescription }

Value: `#!cpp int 8`

This is the ID of the `Attribute Set Tech Description` modifier for the xsEffectAmount function

### 8.16. cAttrSetStacking { #cAttrSetStacking }

Value: `#!cpp int 9`

This is the ID of the `Attribute Set Tech Stacking` modifier for the xsEffectAmount function

### 8.17. cAttrSetStackingResearchCap { #cAttrSetStackingResearchCap }

Value: `#!cpp int 10`

This is the ID of the `Attribute Set Stacking Research Cap` modifier for the xsEffectAmount function

### 8.18. cAttrSetHotkey { #cAttrSetHotkey }

Value: `#!cpp int 11`

This is the ID of the `Attribute Set Hotkey` modifier for the xsEffectAmount function

## 9. EffectAmount Unit Attribute { #EffectAmountUnitAttribute }

### 9.1. cHitpoints { #cHitpoints }

Value: `#!cpp int 0`

This is the attribute [Hit Points](./../../attributes/attributes/#0-hit-points)

### 9.2. cLineOfSight { #cLineOfSight }

Value: `#!cpp int 1`

This is the attribute [Line of Sight](./../../attributes/attributes/#1-line-of-sight)

### 9.3. cGarrisonCapacity { #cGarrisonCapacity }

Value: `#!cpp int 2`

This is the attribute [Garrison Capacity](./../../attributes/attributes/#2-garrison-capacity)

### 9.4. cUnitSizeX { #cUnitSizeX }

Value: `#!cpp int 3`

This is the attribute [Unit Size X](./../../attributes/attributes/#3-unit-size-x)

### 9.5. cUnitSizeY { #cUnitSizeY }

Value: `#!cpp int 4`

This is the attribute [Unit Size Y](./../../attributes/attributes/#4-unit-size-y)

### 9.6. cMovementSpeed { #cMovementSpeed }

Value: `#!cpp int 5`

This is the attribute [Movement Speed](./../../attributes/attributes/#5-movement-speed)

### 9.7. cRotationSpeed { #cRotationSpeed }

Value: `#!cpp int 6`

This is the attribute [Rotation Speed](./../../attributes/attributes/#6-rotation-speed)

### 9.8. cArmor { #cArmor }

Value: `#!cpp int 8`

This is the attribute [Armor](./../../attributes/attributes/#8-armor)

### 9.9. cAttack { #cAttack }

Value: `#!cpp int 9`

This is the attribute [Attack](./../../attributes/attributes/#9-attack)

### 9.10. cAttackReloadTime { #cAttackReloadTime }

Value: `#!cpp int 10`

This is the attribute [Attack Reload Time](./../../attributes/attributes/#10-attack-reload-time)

### 9.11. cAccuracyPercent { #cAccuracyPercent }

Value: `#!cpp int 11`

This is the attribute [Accuracy Percent](./../../attributes/attributes/#11-accuracy-percent)

### 9.12. cMaxRange { #cMaxRange }

Value: `#!cpp int 12`

This is the attribute [Max Range](./../../attributes/attributes/#12-max-range)

### 9.13. cWorkRate { #cWorkRate }

Value: `#!cpp int 13`

This is the attribute [Work Rate](./../../attributes/attributes/#13-work-rate)

### 9.14. cCarryCapacity { #cCarryCapacity }

Value: `#!cpp int 14`

This is the attribute [Carry Capacity](./../../attributes/attributes/#14-carry-capacity)

### 9.15. cBaseArmor { #cBaseArmor }

Value: `#!cpp int 15`

This is the attribute [Base Armor](./../../attributes/attributes/#15-base-armor)

### 9.16. cProjectileUnit { #cProjectileUnit }

Value: `#!cpp int 16`

This is the attribute [Projectile Unit](./../../attributes/attributes/#16-projectile-unit)

### 9.17. cIconGraphicsAngle { #cIconGraphicsAngle }

Value: `#!cpp int 17`

This is the attribute [Building Icon Override](./../../attributes/attributes/#17-building-icon-override)

### 9.18. cTerrainDefenseBonus { #cTerrainDefenseBonus }

Value: `#!cpp int 18`

This is the attribute [Terrain Defense Bonus](./../../attributes/attributes/#18-terrain-defense-bonus)

### 9.19. cEnableSmartProjectile { #cEnableSmartProjectile }

Value: `#!cpp int 19`

This is the attribute [Projectile Smart Mode](./../../attributes/attributes/#19-projectile-smart-mode)

### 9.20. cMinimumRange { #cMinimumRange }

Value: `#!cpp int 20`

This is the attribute [Minimum Range](./../../attributes/attributes/#20-minimum-range)

### 9.21. cAmountFirstStorage { #cAmountFirstStorage }

Value: `#!cpp int 21`

This is the attribute [Amount of 1st Resource Storage](./../../attributes/attributes/#21-amount-of-1st-resource-storage)

### 9.22. cBlastWidth { #cBlastWidth }

Value: `#!cpp int 22`

This is the attribute [Blast Width](./../../attributes/attributes/#22-blast-width)

### 9.23. cSearchRadius { #cSearchRadius }

Value: `#!cpp int 23`

This is the attribute [Search Radius](./../../attributes/attributes/#23-search-radius)

### 9.24. cBonusResistance { #cBonusResistance }

Value: `#!cpp int 24`

This is the attribute [Bonus Damage Resistance](./../../attributes/attributes/#24-bonus-damage-resistance)

### 9.25. cIconId { #cIconId }

Value: `#!cpp int 25`

This is the attribute [Icon ID](./../../attributes/attributes/#25-icon-id)

### 9.26. cAmountSecondStorage { #cAmountSecondStorage }

Value: `#!cpp int 26`

This is the attribute [Amount of 2nd Resource Storage](./../../attributes/attributes/#26-amount-of-2nd-resource-storage)

### 9.27. cAmountThirdStorage { #cAmountThirdStorage }

Value: `#!cpp int 27`

This is the attribute [Amount of 3rd Resource Storage](./../../attributes/attributes/#27-amount-of-3rd-resource-storage)

### 9.28. cFogFlag { #cFogFlag }

Value: `#!cpp int 28`

This is the attribute [Fog Visibility](./../../attributes/attributes/#28-fog-visibility)

### 9.29. cOcclusionMode { #cOcclusionMode }

Value: `#!cpp int 29`

This is the attribute [Occlusion Mode](./../../attributes/attributes/#29-occlusion-mode)

### 9.30. cGarrisonType { #cGarrisonType }

Value: `#!cpp int 30`

This is the attribute [Garrison Type](./../../attributes/attributes/#30-garrison-type)

### 9.31. cUnitSizeZ { #cUnitSizeZ }

Value: `#!cpp int 32`

This is the attribute [Unit Size Z](./../../attributes/attributes/#32-unit-size-z)

### 9.32. cHeroStatus { #cHeroStatus }

Value: `#!cpp int 40`

This is the attribute [Hero Status](./../../attributes/attributes/#40-hero-status)

### 9.33. cAttackDelay { #cAttackDelay }

Value: `#!cpp int 41`

This is the attribute [Frame Delay](./../../attributes/attributes/#41-frame-delay)

### 9.34. cTrainLocation { #cTrainLocation }

Value: `#!cpp int 42`

This is the attribute [Train Location](./../../attributes/attributes/#42-train-location)

### 9.35. cTrainButton { #cTrainButton }

Value: `#!cpp int 43`

This is the attribute [Train Button](./../../attributes/attributes/#43-train-button)

### 9.36. cBlastAttackLevel { #cBlastAttackLevel }

Value: `#!cpp int 44`

This is the attribute [Blast Attack Level](./../../attributes/attributes/#44-blast-attack-level)

### 9.37. cBlastDefenseLevel { #cBlastDefenseLevel }

Value: `#!cpp int 45`

This is the attribute [Blast Defense Level](./../../attributes/attributes/#45-blast-defense-level)

### 9.38. cShownAttack { #cShownAttack }

Value: `#!cpp int 46`

This is the attribute [Shown Attack](./../../attributes/attributes/#46-shown-attack)

### 9.39. cShownRange { #cShownRange }

Value: `#!cpp int 47`

This is the attribute [Shown Range](./../../attributes/attributes/#47-shown-range)

### 9.40. cShownMeleeArmor { #cShownMeleeArmor }

Value: `#!cpp int 48`

This is the attribute [Shown Melee Armor](./../../attributes/attributes/#48-shown-melee-armor)

### 9.41. cShownPierceArmor { #cShownPierceArmor }

Value: `#!cpp int 49`

This is the attribute [Shown Pierce Armor](./../../attributes/attributes/#49-shown-pierce-armor)

### 9.42. cNameId { #cNameId }

Value: `#!cpp int 50`

This is the attribute [Object Name ID](./../../attributes/attributes/#50-object-name-id)

### 9.43. cDescriptionId { #cDescriptionId }

Value: `#!cpp int 51`

This is the attribute [Short Description ID](./../../attributes/attributes/#51-short-description-id)

### 9.44. cTerrainTable { #cTerrainTable }

Value: `#!cpp int 53`

This is the attribute [Terrain Restriction ID](./../../attributes/attributes/#53-terrain-restriction-id)

### 9.45. cTraits { #cTraits }

Value: `#!cpp int 54`

This is the attribute [Unit Trait](./../../attributes/attributes/#54-unit-trait)

### 9.46. cTraitPiece { #cTraitPiece }

Value: `#!cpp int 56`

This is the attribute [Trait Piece](./../../attributes/attributes/#56-trait-piece)

### 9.47. cDeadUnitId { #cDeadUnitId }

Value: `#!cpp int 57`

This is the attribute [Dead Unit ID](./../../attributes/attributes/#57-dead-unit-id)

### 9.48. cHotkeyId { #cHotkeyId }

Value: `#!cpp int 58`

This is the attribute [Hotkey ID](./../../attributes/attributes/#58-hotkey-id)

### 9.49. cMaxCharge { #cMaxCharge }

Value: `#!cpp int 59`

This is the attribute [Maximum Charge](./../../attributes/attributes/#59-maximum-charge)

### 9.50. cRechargeRate { #cRechargeRate }

Value: `#!cpp int 60`

This is the attribute [Recharge Rate](./../../attributes/attributes/#60-recharge-rate)

### 9.51. cChargeEvent { #cChargeEvent }

Value: `#!cpp int 61`

This is the attribute [Charge Event](./../../attributes/attributes/#61-charge-event)

### 9.52. cChargeType { #cChargeType }

Value: `#!cpp int 62`

This is the attribute [Charge Type](./../../attributes/attributes/#62-charge-type)

### 9.53. cCombatAbility { #cCombatAbility }

Value: `#!cpp int 63`

This is the attribute [Combat Ability](./../../attributes/attributes/#63-combat-ability)

### 9.54. cAttackDispersion { #cAttackDispersion }

Value: `#!cpp int 64`

This is the attribute [Attack Dispersion](./../../attributes/attributes/#64-attack-dispersion)

### 9.55. cSecondaryProjectileUnit { #cSecondaryProjectileUnit }

Value: `#!cpp int 65`

This is the attribute [Secondary Projectile Unit](./../../attributes/attributes/#65-secondary-projectile-unit)

### 9.56. cBloodUnitId { #cBloodUnitId }

Value: `#!cpp int 66`

This is the attribute [Blood Unit](./../../attributes/attributes/#66-blood-unit)

### 9.57. cHitMode { #cHitMode }

Value: `#!cpp int 67`

This is the attribute [Projectile Hit Mode](./../../attributes/attributes/#67-projectile-hit-mode)

### 9.58. cVanishMode { #cVanishMode }

Value: `#!cpp int 68`

This is the attribute [Projectile Vanish Mode](./../../attributes/attributes/#68-projectile-vanish-mode)

### 9.59. cProjectileArc { #cProjectileArc }

Value: `#!cpp int 69`

This is the attribute [Projectile Arc](./../../attributes/attributes/#69-projectile-arc)

### 9.60. cResourceCost { #cResourceCost }

Value: `#!cpp int 100`

This is the attribute [Resource Costs](./../../attributes/attributes/#100-resource-costs)

### 9.61. cTrainTime { #cTrainTime }

Value: `#!cpp int 101`

This is the attribute [Train Time](./../../attributes/attributes/#101-train-time)

### 9.62. cTotalProjectiles { #cTotalProjectiles }

Value: `#!cpp int 102`

This is the attribute [Total Missiles](./../../attributes/attributes/#102-total-missiles)

### 9.63. cFoodCost { #cFoodCost }

Value: `#!cpp int 103`

This is the attribute [Food Costs](./../../attributes/attributes/#103-food-costs)

### 9.64. cWoodCost { #cWoodCost }

Value: `#!cpp int 104`

This is the attribute [Wood Costs](./../../attributes/attributes/#104-wood-costs)

### 9.65. cGoldCost { #cGoldCost }

Value: `#!cpp int 105`

This is the attribute [Gold Costs](./../../attributes/attributes/#105-gold-costs)

### 9.66. cStoneCost { #cStoneCost }

Value: `#!cpp int 106`

This is the attribute [Stone Costs](./../../attributes/attributes/#106-stone-costs)

### 9.67. cMaxTotalProjectiles { #cMaxTotalProjectiles }

Value: `#!cpp int 107`

This is the attribute [Max Total Missiles](./../../attributes/attributes/#107-max-total-missiles)

### 9.68. cGarrisonHealRate { #cGarrisonHealRate }

Value: `#!cpp int 108`

This is the attribute [Garrison Heal Rate](./../../attributes/attributes/#108-garrison-heal-rate)

### 9.69. cRegenerationRate { #cRegenerationRate }

Value: `#!cpp int 109`

This is the attribute [Regeneration Rate](./../../attributes/attributes/#109-regeneration-rate)

### 9.70. cPopulation { #cPopulation }

Value: `#!cpp int 110`

This is the attribute [Population](./../../attributes/attributes/#110-population)

## 10. EffectAmount Object Class { #EffectAmountObjectClass }

### 10.1. cArcherClass { #cArcherClass }

Value: `#!cpp int 900`

This is the ID used to target the Archer Class

### 10.2. cArtifactClass { #cArtifactClass }

Value: `#!cpp int 901`

This is the ID used to target the Artifact Class

### 10.3. cTradeBoatClass { #cTradeBoatClass }

Value: `#!cpp int 902`

This is the ID used to target the Trade Boat Class

### 10.4. cBuildingClass { #cBuildingClass }

Value: `#!cpp int 903`

This is the ID used to target the Building Class

### 10.5. cVillagerClass { #cVillagerClass }

Value: `#!cpp int 904`

This is the ID used to target the Villager Class

### 10.6. cSeaFishClass { #cSeaFishClass }

Value: `#!cpp int 905`

This is the ID used to target the Sea Fish Class

### 10.7. cInfantryClass { #cInfantryClass }

Value: `#!cpp int 906`

This is the ID used to target the Infantry Class

### 10.8. cForageBushClass { #cForageBushClass }

Value: `#!cpp int 907`

This is the ID used to target the Forage Bush Class

### 10.9. cStoneMineClass { #cStoneMineClass }

Value: `#!cpp int 908`

This is the ID used to target the Stone Mine Class

### 10.10. cPreyAnimalClass { #cPreyAnimalClass }

Value: `#!cpp int 909`

This is the ID used to target the Prey Animal Class

### 10.11. cPredatorAnimalClass { #cPredatorAnimalClass }

Value: `#!cpp int 910`

This is the ID used to target the Predator Animal Class

### 10.12. cMiscellaneousClass { #cMiscellaneousClass }

Value: `#!cpp int 911`

This is the ID used to target the Miscellaneous Class

### 10.13. cCavalryClass { #cCavalryClass }

Value: `#!cpp int 912`

This is the ID used to target the Cavalry Class

### 10.14. cSiegeWeaponClass { #cSiegeWeaponClass }

Value: `#!cpp int 913`

This is the ID used to target the Siege Weapon Class

### 10.15. cTerrainClass { #cTerrainClass }

Value: `#!cpp int 914`

This is the ID used to target the Terrain Class

### 10.16. cTreeClass { #cTreeClass }

Value: `#!cpp int 915`

This is the ID used to target the Tree Class

### 10.17. cTreeStumpClass { #cTreeStumpClass }

Value: `#!cpp int 916`

This is the ID used to target the Tree Stump Class

### 10.18. cHealerClass { #cHealerClass }

Value: `#!cpp int 917`

This is the ID used to target the Healer Class

### 10.19. cMonkClass { #cMonkClass }

Value: `#!cpp int 918`

This is the ID used to target the Monk Class

### 10.20. cTradeCartClass { #cTradeCartClass }

Value: `#!cpp int 919`

This is the ID used to target the Trade Cart Class

### 10.21. cTransportShipClass { #cTransportShipClass }

Value: `#!cpp int 920`

This is the ID used to target the Transport Ship Class

### 10.22. cFishingBoatClass { #cFishingBoatClass }

Value: `#!cpp int 921`

This is the ID used to target the Fishing Boat Class

### 10.23. cWarshipClass { #cWarshipClass }

Value: `#!cpp int 922`

This is the ID used to target the Warship Class

### 10.24. cConquistadorClass { #cConquistadorClass }

Value: `#!cpp int 923`

This is the ID used to target the Conquistador Class

### 10.25. cWarElephantClass { #cWarElephantClass }

Value: `#!cpp int 924`

This is the ID used to target the War Elephant Class

### 10.26. cHeroClass { #cHeroClass }

Value: `#!cpp int 925`

This is the ID used to target the Hero Class

### 10.27. cElephantArcherClass { #cElephantArcherClass }

Value: `#!cpp int 926`

This is the ID used to target the Elephant Archer Class

### 10.28. cWallClass { #cWallClass }

Value: `#!cpp int 927`

This is the ID used to target the Wall Class

### 10.29. cPhalanxClass { #cPhalanxClass }

Value: `#!cpp int 928`

This is the ID used to target the Phalanx Class

### 10.30. cDomesticAnimalClass { #cDomesticAnimalClass }

Value: `#!cpp int 929`

This is the ID used to target the Domestic Animal Class

### 10.31. cFlagClass { #cFlagClass }

Value: `#!cpp int 930`

This is the ID used to target the Flag Class

### 10.32. cDeepSeaFishClass { #cDeepSeaFishClass }

Value: `#!cpp int 931`

This is the ID used to target the Deep Sea Fish Class

### 10.33. cGoldMine { #cGoldMine }

Value: `#!cpp int 932`

This is the ID used to target the Gold Mine

### 10.34. cShoreFish { #cShoreFish }

Value: `#!cpp int 933`

This is the ID used to target the Shore Fish

### 10.35. cCliffClass { #cCliffClass }

Value: `#!cpp int 934`

This is the ID used to target the Cliff Class

### 10.36. cPetardClass { #cPetardClass }

Value: `#!cpp int 935`

This is the ID used to target the Petard Class

### 10.37. cCavalryArcherClass { #cCavalryArcherClass }

Value: `#!cpp int 936`

This is the ID used to target the Cavalry Archer Class

### 10.38. cDoppelgangerClass { #cDoppelgangerClass }

Value: `#!cpp int 937`

This is the ID used to target the Doppelganger Class

### 10.39. cBirdClass { #cBirdClass }

Value: `#!cpp int 938`

This is the ID used to target the Bird Class

### 10.40. cGateClass { #cGateClass }

Value: `#!cpp int 939`

This is the ID used to target the Gate Class

### 10.41. cSalvagePileClass { #cSalvagePileClass }

Value: `#!cpp int 940`

This is the ID used to target the Salvage Pile Class

### 10.42. cResourcePileClass { #cResourcePileClass }

Value: `#!cpp int 941`

This is the ID used to target the Resource Pile Class

### 10.43. cRelicClass { #cRelicClass }

Value: `#!cpp int 942`

This is the ID used to target the Relic Class

### 10.44. cMonkWithRelicClass { #cMonkWithRelicClass }

Value: `#!cpp int 943`

This is the ID used to target the Monk With Relic Class

### 10.45. cHandCannoneerClass { #cHandCannoneerClass }

Value: `#!cpp int 944`

This is the ID used to target the Hand Cannoneer Class

### 10.46. cTwoHandedSwordsmanClass { #cTwoHandedSwordsmanClass }

Value: `#!cpp int 945`

This is the ID used to target the Two Handed Swordsman Class

### 10.47. cPikemanClass { #cPikemanClass }

Value: `#!cpp int 946`

This is the ID used to target the Pikeman Class

### 10.48. cScoutCavalryClass { #cScoutCavalryClass }

Value: `#!cpp int 947`

This is the ID used to target the Scout Cavalry Class

### 10.49. cOreMineClass { #cOreMineClass }

Value: `#!cpp int 948`

This is the ID used to target the Ore Mine Class

### 10.50. cFarmClass { #cFarmClass }

Value: `#!cpp int 949`

This is the ID used to target the Farm Class

### 10.51. cSpearmanClass { #cSpearmanClass }

Value: `#!cpp int 950`

This is the ID used to target the Spearman Class

### 10.52. cPackedUnitClass { #cPackedUnitClass }

Value: `#!cpp int 951`

This is the ID used to target the Packed Unit Class

### 10.53. cTowerClass { #cTowerClass }

Value: `#!cpp int 952`

This is the ID used to target the Tower Class

### 10.54. cBoardingShipClass { #cBoardingShipClass }

Value: `#!cpp int 953`

This is the ID used to target the Boarding Ship Class

### 10.55. cUnpackedSiegeUnitClass { #cUnpackedSiegeUnitClass }

Value: `#!cpp int 954`

This is the ID used to target the Unpacked Siege Unit Class

### 10.56. cScorpionClass { #cScorpionClass }

Value: `#!cpp int 955`

This is the ID used to target the Scorpion Class

### 10.57. cRaiderClass { #cRaiderClass }

Value: `#!cpp int 956`

This is the ID used to target the Raider Class

### 10.58. cCavalryRaiderClass { #cCavalryRaiderClass }

Value: `#!cpp int 957`

This is the ID used to target the Cavalry Raider Class

### 10.59. cLivestockClass { #cLivestockClass }

Value: `#!cpp int 958`

This is the ID used to target the Livestock Class

### 10.60. cKingClass { #cKingClass }

Value: `#!cpp int 959`

This is the ID used to target the King Class

### 10.61. cMiscBuildingClass { #cMiscBuildingClass }

Value: `#!cpp int 960`

This is the ID used to target the Misc Building Class

### 10.62. cControlledAnimalClass { #cControlledAnimalClass }

Value: `#!cpp int 961`

This is the ID used to target the Controlled Animal Class

## 11. Resource { #Resource }

### 11.1. cAttributeFood { #cAttributeFood }

Value: `#!cpp int 0`

ID of the player resource Food. Check [here](../../resources/resources/#0 "Jump to: Game Mecahnicsc > Resources > #0") for more info about what this resource does.

### 11.2. cAttributeWood { #cAttributeWood }

Value: `#!cpp int 1`

ID of the player resource Wood. Check [here](../../resources/resources/#1 "Jump to: Game Mecahnicsc > Resources > #1") for more info about what this resource does.

### 11.3. cAttributeStone { #cAttributeStone }

Value: `#!cpp int 2`

ID of the player resource Stone. Check [here](../../resources/resources/#2 "Jump to: Game Mecahnicsc > Resources > #2") for more info about what this resource does.

### 11.4. cAttributeGold { #cAttributeGold }

Value: `#!cpp int 3`

ID of the player resource Gold. Check [here](../../resources/resources/#3 "Jump to: Game Mecahnicsc > Resources > #3") for more info about what this resource does.

### 11.5. cAttributePopulationCap { #cAttributePopulationCap }

Value: `#!cpp int 4`

ID of the player resource Population Cap. Check [here](../../resources/resources/#4 "Jump to: Game Mecahnicsc > Resources > #4") for more info about what this resource does.

### 11.6. cAttributeReligion { #cAttributeReligion }

Value: `#!cpp int 5`

ID of the player resource Religion. Check [here](../../resources/resources/#5 "Jump to: Game Mecahnicsc > Resources > #5") for more info about what this resource does.

### 11.7. cAttributeCurrentAge { #cAttributeCurrentAge }

Value: `#!cpp int 6`

ID of the player resource Current Age. Check [here](../../resources/resources/#6 "Jump to: Game Mecahnicsc > Resources > #6") for more info about what this resource does.

### 11.8. cAttributeRelics { #cAttributeRelics }

Value: `#!cpp int 7`

ID of the player resource Relics. Check [here](../../resources/resources/#7 "Jump to: Game Mecahnicsc > Resources > #7") for more info about what this resource does.

### 11.9. cAttributeTrageBonus { #cAttributeTrageBonus }

Value: `#!cpp int 8`

ID of the player resource Trage Bonus. Click [here](../../resources/resources/#8 "Jump to: Game Mecahnicsc > Resources > #8"). The name is mispelled in the `Constants.xs` Check so thats how it needs to be used for more info about what this resource does.

### 11.10. cAttributeTradeGoods { #cAttributeTradeGoods }

Value: `#!cpp int 9`

ID of the player resource Trade Goods. Check [here](../../resources/resources/#9 "Jump to: Game Mecahnicsc > Resources > #9") for more info about what this resource does.

### 11.11. cAttributeTradeProducation { #cAttributeTradeProducation }

Value: `#!cpp int 10`

ID of the player resource Trade Producation. Check [here](../../resources/resources/#10 "Jump to: Game Mecahnicsc > Resources > #10") for more info about what this resource does.

### 11.12. cAttributePopulation { #cAttributePopulation }

Value: `#!cpp int 11`

ID of the player resource Population. Check [here](../../resources/resources/#11 "Jump to: Game Mecahnicsc > Resources > #11") for more info about what this resource does.

### 11.13. cAttributeDecay { #cAttributeDecay }

Value: `#!cpp int 12`

ID of the player resource Decay. Check [here](../../resources/resources/#12 "Jump to: Game Mecahnicsc > Resources > #12") for more info about what this resource does.

### 11.14. cAttributeDiscovery { #cAttributeDiscovery }

Value: `#!cpp int 13`

ID of the player resource Discovery. Check [here](../../resources/resources/#13 "Jump to: Game Mecahnicsc > Resources > #13") for more info about what this resource does.

### 11.15. cAttributeRuins { #cAttributeRuins }

Value: `#!cpp int 14`

ID of the player resource Ruins. Check [here](../../resources/resources/#14 "Jump to: Game Mecahnicsc > Resources > #14") for more info about what this resource does.

### 11.16. cAttributeMeat { #cAttributeMeat }

Value: `#!cpp int 15`

ID of the player resource Meat. Check [here](../../resources/resources/#15 "Jump to: Game Mecahnicsc > Resources > #15") for more info about what this resource does.

### 11.17. cAttributeBerries { #cAttributeBerries }

Value: `#!cpp int 16`

ID of the player resource Berries. Check [here](../../resources/resources/#16 "Jump to: Game Mecahnicsc > Resources > #16") for more info about what this resource does.

### 11.18. cAttributeFish { #cAttributeFish }

Value: `#!cpp int 17`

ID of the player resource Fish. Check [here](../../resources/resources/#17 "Jump to: Game Mecahnicsc > Resources > #17") for more info about what this resource does.

### 11.19. cAttributeKills { #cAttributeKills }

Value: `#!cpp int 20`

ID of the player resource Kills. Check [here](../../resources/resources/#20 "Jump to: Game Mecahnicsc > Resources > #20") for more info about what this resource does.

### 11.20. cAttributeResearchCount { #cAttributeResearchCount }

Value: `#!cpp int 21`

ID of the player resource Research Count. Check [here](../../resources/resources/#21 "Jump to: Game Mecahnicsc > Resources > #21") for more info about what this resource does.

### 11.21. cAttributeExploration { #cAttributeExploration }

Value: `#!cpp int 22`

ID of the player resource Exploration. Check [here](../../resources/resources/#22 "Jump to: Game Mecahnicsc > Resources > #22") for more info about what this resource does.

### 11.22. cAttributeConvertPriest { #cAttributeConvertPriest }

Value: `#!cpp int 27`

ID of the player resource Convert Priest. Check [here](../../resources/resources/#27 "Jump to: Game Mecahnicsc > Resources > #27") for more info about what this resource does.

### 11.23. cAttributeConvertBuilding { #cAttributeConvertBuilding }

Value: `#!cpp int 28`

ID of the player resource Convert Building. Check [here](../../resources/resources/#28 "Jump to: Game Mecahnicsc > Resources > #28") for more info about what this resource does.

### 11.24. cAttributeBuildingLimit { #cAttributeBuildingLimit }

Value: `#!cpp int 30`

ID of the player resource Building Limit. Check [here](../../resources/resources/#30 "Jump to: Game Mecahnicsc > Resources > #30") for more info about what this resource does.

### 11.25. cAttributeFoodLimit { #cAttributeFoodLimit }

Value: `#!cpp int 31`

ID of the player resource Food Limit. Check [here](../../resources/resources/#31 "Jump to: Game Mecahnicsc > Resources > #31") for more info about what this resource does.

### 11.26. cAttributeUnitLimit { #cAttributeUnitLimit }

Value: `#!cpp int 32`

ID of the player resource Unit Limit. Check [here](../../resources/resources/#32 "Jump to: Game Mecahnicsc > Resources > #32") for more info about what this resource does.

### 11.27. cAttributeMaintenance { #cAttributeMaintenance }

Value: `#!cpp int 33`

ID of the player resource Maintenance. Check [here](../../resources/resources/#33 "Jump to: Game Mecahnicsc > Resources > #33") for more info about what this resource does.

### 11.28. cAttributeFaith { #cAttributeFaith }

Value: `#!cpp int 34`

ID of the player resource Faith. Check [here](../../resources/resources/#34 "Jump to: Game Mecahnicsc > Resources > #34") for more info about what this resource does.

### 11.29. cAttributeFaithRechargeRate { #cAttributeFaithRechargeRate }

Value: `#!cpp int 35`

ID of the player resource Faith Recharge Rate. Check [here](../../resources/resources/#35 "Jump to: Game Mecahnicsc > Resources > #35") for more info about what this resource does.

### 11.30. cAttributeFarmFood { #cAttributeFarmFood }

Value: `#!cpp int 36`

ID of the player resource Farm Food. Check [here](../../resources/resources/#36 "Jump to: Game Mecahnicsc > Resources > #36") for more info about what this resource does.

### 11.31. cAttributeCivilianPopulation { #cAttributeCivilianPopulation }

Value: `#!cpp int 37`

ID of the player resource Civilian Population. Check [here](../../resources/resources/#37 "Jump to: Game Mecahnicsc > Resources > #37") for more info about what this resource does.

### 11.32. cAttributeAllTechsAchieved { #cAttributeAllTechsAchieved }

Value: `#!cpp int 39`

ID of the player resource All Techs Achieved. Check [here](../../resources/resources/#39 "Jump to: Game Mecahnicsc > Resources > #39") for more info about what this resource does.

### 11.33. cAttributeMilitaryPopulation { #cAttributeMilitaryPopulation }

Value: `#!cpp int 40`

ID of the player resource Military Population. Check [here](../../resources/resources/#40 "Jump to: Game Mecahnicsc > Resources > #40") for more info about what this resource does.

### 11.34. cAttributeConversions { #cAttributeConversions }

Value: `#!cpp int 41`

ID of the player resource Conversions. Check [here](../../resources/resources/#41 "Jump to: Game Mecahnicsc > Resources > #41") for more info about what this resource does.

### 11.35. cAttributeWonder { #cAttributeWonder }

Value: `#!cpp int 42`

ID of the player resource Wonder. Check [here](../../resources/resources/#42 "Jump to: Game Mecahnicsc > Resources > #42") for more info about what this resource does.

### 11.36. cAttributeRazings { #cAttributeRazings }

Value: `#!cpp int 43`

ID of the player resource Razings. Check [here](../../resources/resources/#43 "Jump to: Game Mecahnicsc > Resources > #43") for more info about what this resource does.

### 11.37. cAttributeKillRatio { #cAttributeKillRatio }

Value: `#!cpp int 44`

ID of the player resource Kill Ratio. Check [here](../../resources/resources/#44 "Jump to: Game Mecahnicsc > Resources > #44") for more info about what this resource does.

### 11.38. cAttributePlayerKilled { #cAttributePlayerKilled }

Value: `#!cpp int 45`

ID of the player resource Player Killed. Check [here](../../resources/resources/#45 "Jump to: Game Mecahnicsc > Resources > #45") for more info about what this resource does.

### 11.39. cAttributeTributeInefficency { #cAttributeTributeInefficency }

Value: `#!cpp int 46`

ID of the player resource Tribute Inefficency. Check [here](../../resources/resources/#46 "Jump to: Game Mecahnicsc > Resources > #46") for more info about what this resource does.

### 11.40. cAttributeGoldBonus { #cAttributeGoldBonus }

Value: `#!cpp int 47`

ID of the player resource Gold Bonus. Check [here](../../resources/resources/#47 "Jump to: Game Mecahnicsc > Resources > #47") for more info about what this resource does.

### 11.41. cAttributeTownCenterUnavailable { #cAttributeTownCenterUnavailable }

Value: `#!cpp int 48`

ID of the player resource Town Center Unavailable. Check [here](../../resources/resources/#48 "Jump to: Game Mecahnicsc > Resources > #48") for more info about what this resource does.

### 11.42. cAttributeGoldCounter { #cAttributeGoldCounter }

Value: `#!cpp int 49`

ID of the player resource Gold Counter. Check [here](../../resources/resources/#49 "Jump to: Game Mecahnicsc > Resources > #49") for more info about what this resource does.

### 11.43. cAttributeWriting { #cAttributeWriting }

Value: `#!cpp int 50`

ID of the player resource Writing. Check [here](../../resources/resources/#50 "Jump to: Game Mecahnicsc > Resources > #50") for more info about what this resource does.

### 11.44. cAttributeMonasteries { #cAttributeMonasteries }

Value: `#!cpp int 52`

ID of the player resource Monasteries. Check [here](../../resources/resources/#52 "Jump to: Game Mecahnicsc > Resources > #52") for more info about what this resource does.

### 11.45. cAttributeTribute { #cAttributeTribute }

Value: `#!cpp int 53`

ID of the player resource Tribute. Check [here](../../resources/resources/#53 "Jump to: Game Mecahnicsc > Resources > #53") for more info about what this resource does.

### 11.46. cAttributeHoldRuins { #cAttributeHoldRuins }

Value: `#!cpp int 54`

ID of the player resource Hold Ruins. Check [here](../../resources/resources/#54 "Jump to: Game Mecahnicsc > Resources > #54") for more info about what this resource does.

### 11.47. cAttributeHoldRelics { #cAttributeHoldRelics }

Value: `#!cpp int 55`

ID of the player resource Hold Relics. Check [here](../../resources/resources/#55 "Jump to: Game Mecahnicsc > Resources > #55") for more info about what this resource does.

### 11.48. cAttributeOre { #cAttributeOre }

Value: `#!cpp int 56`

ID of the player resource Ore. Check [here](../../resources/resources/#56 "Jump to: Game Mecahnicsc > Resources > #56") for more info about what this resource does.

### 11.49. cAttributeCapturedUnit { #cAttributeCapturedUnit }

Value: `#!cpp int 57`

ID of the player resource Captured Unit. Check [here](../../resources/resources/#57 "Jump to: Game Mecahnicsc > Resources > #57") for more info about what this resource does.

### 11.50. cAttributeTradeGoodQuality { #cAttributeTradeGoodQuality }

Value: `#!cpp int 59`

ID of the player resource Trade Good Quality. Check [here](../../resources/resources/#59 "Jump to: Game Mecahnicsc > Resources > #59") for more info about what this resource does.

### 11.51. cAttributeTradeMarketLevel { #cAttributeTradeMarketLevel }

Value: `#!cpp int 60`

ID of the player resource Trade Market Level. Check [here](../../resources/resources/#60 "Jump to: Game Mecahnicsc > Resources > #60") for more info about what this resource does.

### 11.52. cAttributeFormations { #cAttributeFormations }

Value: `#!cpp int 61`

ID of the player resource Formations. Check [here](../../resources/resources/#61 "Jump to: Game Mecahnicsc > Resources > #61") for more info about what this resource does.

### 11.53. cAttributeBuildingHouseRate { #cAttributeBuildingHouseRate }

Value: `#!cpp int 62`

ID of the player resource Building House Rate. Check [here](../../resources/resources/#62 "Jump to: Game Mecahnicsc > Resources > #62") for more info about what this resource does.

### 11.54. cAttributeGatherTaxRate { #cAttributeGatherTaxRate }

Value: `#!cpp int 63`

ID of the player resource Gather Tax Rate. Check [here](../../resources/resources/#63 "Jump to: Game Mecahnicsc > Resources > #63") for more info about what this resource does.

### 11.55. cAttributeGatherAccumalation { #cAttributeGatherAccumalation }

Value: `#!cpp int 64`

ID of the player resource Gather Accumalation. Check [here](../../resources/resources/#64 "Jump to: Game Mecahnicsc > Resources > #64") for more info about what this resource does.

### 11.56. cAttributeSalvageDecayRate { #cAttributeSalvageDecayRate }

Value: `#!cpp int 65`

ID of the player resource Salvage Decay Rate. Check [here](../../resources/resources/#65 "Jump to: Game Mecahnicsc > Resources > #65") for more info about what this resource does.

### 11.57. cAttributeAllowFormations { #cAttributeAllowFormations }

Value: `#!cpp int 66`

ID of the player resource Allow Formations. Check [here](../../resources/resources/#66 "Jump to: Game Mecahnicsc > Resources > #66") for more info about what this resource does.

### 11.58. cAttributeCanConvert { #cAttributeCanConvert }

Value: `#!cpp int 67`

ID of the player resource Can Convert. Check [here](../../resources/resources/#67 "Jump to: Game Mecahnicsc > Resources > #67") for more info about what this resource does.

### 11.59. cAttributePlayer1Kills { #cAttributePlayer1Kills }

Value: `#!cpp int 69`

ID of the player resource Player1 Kills. Check [here](../../resources/resources/#69 "Jump to: Game Mecahnicsc > Resources > #69") for more info about what this resource does.

### 11.60. cAttributePlayer2Kills { #cAttributePlayer2Kills }

Value: `#!cpp int 70`

ID of the player resource Player2 Kills. Check [here](../../resources/resources/#70 "Jump to: Game Mecahnicsc > Resources > #70") for more info about what this resource does.

### 11.61. cAttributePlayer3Kills { #cAttributePlayer3Kills }

Value: `#!cpp int 71`

ID of the player resource Player3 Kills. Check [here](../../resources/resources/#71 "Jump to: Game Mecahnicsc > Resources > #71") for more info about what this resource does.

### 11.62. cAttributePlayer4Kills { #cAttributePlayer4Kills }

Value: `#!cpp int 72`

ID of the player resource Player4 Kills. Check [here](../../resources/resources/#72 "Jump to: Game Mecahnicsc > Resources > #72") for more info about what this resource does.

### 11.63. cAttributePlayer5Kills { #cAttributePlayer5Kills }

Value: `#!cpp int 73`

ID of the player resource Player5 Kills. Check [here](../../resources/resources/#73 "Jump to: Game Mecahnicsc > Resources > #73") for more info about what this resource does.

### 11.64. cAttributePlayer6Kills { #cAttributePlayer6Kills }

Value: `#!cpp int 74`

ID of the player resource Player6 Kills. Check [here](../../resources/resources/#74 "Jump to: Game Mecahnicsc > Resources > #74") for more info about what this resource does.

### 11.65. cAttributePlayer7Kills { #cAttributePlayer7Kills }

Value: `#!cpp int 75`

ID of the player resource Player7 Kills. Check [here](../../resources/resources/#75 "Jump to: Game Mecahnicsc > Resources > #75") for more info about what this resource does.

### 11.66. cAttributePlayer8Kills { #cAttributePlayer8Kills }

Value: `#!cpp int 76`

ID of the player resource Player8 Kills. Check [here](../../resources/resources/#76 "Jump to: Game Mecahnicsc > Resources > #76") for more info about what this resource does.

### 11.67. cAttributeConvertResistance { #cAttributeConvertResistance }

Value: `#!cpp int 77`

ID of the player resource Convert Resistance. Check [here](../../resources/resources/#77 "Jump to: Game Mecahnicsc > Resources > #77") for more info about what this resource does.

### 11.68. cAttributeTradeVigRate { #cAttributeTradeVigRate }

Value: `#!cpp int 78`

ID of the player resource Trade Vig Rate. Check [here](../../resources/resources/#78 "Jump to: Game Mecahnicsc > Resources > #78") for more info about what this resource does.

### 11.69. cAttributeStoneBonus { #cAttributeStoneBonus }

Value: `#!cpp int 79`

ID of the player resource Stone Bonus. Check [here](../../resources/resources/#79 "Jump to: Game Mecahnicsc > Resources > #79") for more info about what this resource does.

### 11.70. cAttributeQueuedCount { #cAttributeQueuedCount }

Value: `#!cpp int 80`

ID of the player resource Queued Count. Check [here](../../resources/resources/#80 "Jump to: Game Mecahnicsc > Resources > #80") for more info about what this resource does.

### 11.71. cAttributeTrainingCount { #cAttributeTrainingCount }

Value: `#!cpp int 81`

ID of the player resource Training Count. Check [here](../../resources/resources/#81 "Jump to: Game Mecahnicsc > Resources > #81") for more info about what this resource does.

### 11.72. cAttributeRaider { #cAttributeRaider }

Value: `#!cpp int 82`

ID of the player resource Raider. Check [here](../../resources/resources/#82 "Jump to: Game Mecahnicsc > Resources > #82") for more info about what this resource does.

### 11.73. cAttributeBoardingRechargeRate { #cAttributeBoardingRechargeRate }

Value: `#!cpp int 83`

ID of the player resource Boarding Recharge Rate. Check [here](../../resources/resources/#83 "Jump to: Game Mecahnicsc > Resources > #83") for more info about what this resource does.

### 11.74. cAttributeStartingVillagers { #cAttributeStartingVillagers }

Value: `#!cpp int 84`

ID of the player resource Starting Villagers. Check [here](../../resources/resources/#84 "Jump to: Game Mecahnicsc > Resources > #84") for more info about what this resource does.

### 11.75. cAttributeResearchCostMod { #cAttributeResearchCostMod }

Value: `#!cpp int 85`

ID of the player resource Research Cost Mod. Check [here](../../resources/resources/#85 "Jump to: Game Mecahnicsc > Resources > #85") for more info about what this resource does.

### 11.76. cAttributeResearchTimeMod { #cAttributeResearchTimeMod }

Value: `#!cpp int 86`

ID of the player resource Research Time Mod. Check [here](../../resources/resources/#86 "Jump to: Game Mecahnicsc > Resources > #86") for more info about what this resource does.

### 11.77. cAttributeConvertBoats { #cAttributeConvertBoats }

Value: `#!cpp int 87`

ID of the player resource Convert Boats. Check [here](../../resources/resources/#87 "Jump to: Game Mecahnicsc > Resources > #87") for more info about what this resource does.

### 11.78. cAttributeFishTrapFood { #cAttributeFishTrapFood }

Value: `#!cpp int 88`

ID of the player resource Fish Trap Food. Check [here](../../resources/resources/#88 "Jump to: Game Mecahnicsc > Resources > #88") for more info about what this resource does.

### 11.79. cAttributeHealRateModifer { #cAttributeHealRateModifer }

Value: `#!cpp int 89`

ID of the player resource Heal Rate Modifer. Check [here](../../resources/resources/#89 "Jump to: Game Mecahnicsc > Resources > #89") for more info about what this resource does.

### 11.80. cAttributeHealRange { #cAttributeHealRange }

Value: `#!cpp int 90`

ID of the player resource Heal Range. Check [here](../../resources/resources/#90 "Jump to: Game Mecahnicsc > Resources > #90") for more info about what this resource does.

### 11.81. cAttributeStartingFood { #cAttributeStartingFood }

Value: `#!cpp int 91`

ID of the player resource Starting Food. Check [here](../../resources/resources/#91 "Jump to: Game Mecahnicsc > Resources > #91") for more info about what this resource does.

### 11.82. cAttributeStartingWood { #cAttributeStartingWood }

Value: `#!cpp int 92`

ID of the player resource Starting Wood. Check [here](../../resources/resources/#92 "Jump to: Game Mecahnicsc > Resources > #92") for more info about what this resource does.

### 11.83. cAttributeStartingStone { #cAttributeStartingStone }

Value: `#!cpp int 93`

ID of the player resource Starting Stone. Check [here](../../resources/resources/#93 "Jump to: Game Mecahnicsc > Resources > #93") for more info about what this resource does.

### 11.84. cAttributeStartingGold { #cAttributeStartingGold }

Value: `#!cpp int 94`

ID of the player resource Starting Gold. Check [here](../../resources/resources/#94 "Jump to: Game Mecahnicsc > Resources > #94") for more info about what this resource does.

### 11.85. cAttributeRaiderAbility { #cAttributeRaiderAbility }

Value: `#!cpp int 95`

ID of the player resource Raider Ability. Check [here](../../resources/resources/#95 "Jump to: Game Mecahnicsc > Resources > #95") for more info about what this resource does.

### 11.86. cAttributeNoDropsiteFarmers { #cAttributeNoDropsiteFarmers }

Value: `#!cpp int 96`

ID of the player resource No Dropsite Farmers. Check [here](../../resources/resources/#96 "Jump to: Game Mecahnicsc > Resources > #96") for more info about what this resource does.

### 11.87. cAttributeDominantSheepControl { #cAttributeDominantSheepControl }

Value: `#!cpp int 97`

ID of the player resource Dominant Sheep Control. Check [here](../../resources/resources/#97 "Jump to: Game Mecahnicsc > Resources > #97") for more info about what this resource does.

### 11.88. cAttributeObjectCostSummation { #cAttributeObjectCostSummation }

Value: `#!cpp int 98`

ID of the player resource Object Cost Summation. Check [here](../../resources/resources/#98 "Jump to: Game Mecahnicsc > Resources > #98") for more info about what this resource does.

### 11.89. cAttributeResearchCostSummation { #cAttributeResearchCostSummation }

Value: `#!cpp int 99`

ID of the player resource Research Cost Summation. Check [here](../../resources/resources/#99 "Jump to: Game Mecahnicsc > Resources > #99") for more info about what this resource does.

### 11.90. cAttributeRelicIncomeSummation { #cAttributeRelicIncomeSummation }

Value: `#!cpp int 100`

ID of the player resource Relic Income Summation. Check [here](../../resources/resources/#100 "Jump to: Game Mecahnicsc > Resources > #100") for more info about what this resource does.

### 11.91. cAttributeTradeIncomeSummation { #cAttributeTradeIncomeSummation }

Value: `#!cpp int 101`

ID of the player resource Trade Income Summation. Check [here](../../resources/resources/#101 "Jump to: Game Mecahnicsc > Resources > #101") for more info about what this resource does.

### 11.92. cAttributePlayer1Tribute { #cAttributePlayer1Tribute }

Value: `#!cpp int 102`

ID of the player resource Player1 Tribute. Check [here](../../resources/resources/#102 "Jump to: Game Mecahnicsc > Resources > #102") for more info about what this resource does.

### 11.93. cAttributePlayer2Tribute { #cAttributePlayer2Tribute }

Value: `#!cpp int 103`

ID of the player resource Player2 Tribute. Check [here](../../resources/resources/#103 "Jump to: Game Mecahnicsc > Resources > #103") for more info about what this resource does.

### 11.94. cAttributePlayer3Tribute { #cAttributePlayer3Tribute }

Value: `#!cpp int 104`

ID of the player resource Player3 Tribute. Check [here](../../resources/resources/#104 "Jump to: Game Mecahnicsc > Resources > #104") for more info about what this resource does.

### 11.95. cAttributePlayer4Tribute { #cAttributePlayer4Tribute }

Value: `#!cpp int 105`

ID of the player resource Player4 Tribute. Check [here](../../resources/resources/#105 "Jump to: Game Mecahnicsc > Resources > #105") for more info about what this resource does.

### 11.96. cAttributePlayer5Tribute { #cAttributePlayer5Tribute }

Value: `#!cpp int 106`

ID of the player resource Player5 Tribute. Check [here](../../resources/resources/#106 "Jump to: Game Mecahnicsc > Resources > #106") for more info about what this resource does.

### 11.97. cAttributePlayer6Tribute { #cAttributePlayer6Tribute }

Value: `#!cpp int 107`

ID of the player resource Player6 Tribute. Check [here](../../resources/resources/#107 "Jump to: Game Mecahnicsc > Resources > #107") for more info about what this resource does.

### 11.98. cAttributePlayer7Tribute { #cAttributePlayer7Tribute }

Value: `#!cpp int 108`

ID of the player resource Player7 Tribute. Check [here](../../resources/resources/#108 "Jump to: Game Mecahnicsc > Resources > #108") for more info about what this resource does.

### 11.99. cAttributePlayer8Tribute { #cAttributePlayer8Tribute }

Value: `#!cpp int 109`

ID of the player resource Player8 Tribute. Check [here](../../resources/resources/#109 "Jump to: Game Mecahnicsc > Resources > #109") for more info about what this resource does.

### 11.100. cAttributePlayer1KillValue { #cAttributePlayer1KillValue }

Value: `#!cpp int 110`

ID of the player resource Player1 Kill Value. Check [here](../../resources/resources/#110 "Jump to: Game Mecahnicsc > Resources > #110") for more info about what this resource does.

### 11.101. cAttributePlayer2KillValue { #cAttributePlayer2KillValue }

Value: `#!cpp int 111`

ID of the player resource Player2 Kill Value. Check [here](../../resources/resources/#111 "Jump to: Game Mecahnicsc > Resources > #111") for more info about what this resource does.

### 11.102. cAttributePlayer3KillValue { #cAttributePlayer3KillValue }

Value: `#!cpp int 112`

ID of the player resource Player3 Kill Value. Check [here](../../resources/resources/#112 "Jump to: Game Mecahnicsc > Resources > #112") for more info about what this resource does.

### 11.103. cAttributePlayer4KillValue { #cAttributePlayer4KillValue }

Value: `#!cpp int 113`

ID of the player resource Player4 Kill Value. Check [here](../../resources/resources/#113 "Jump to: Game Mecahnicsc > Resources > #113") for more info about what this resource does.

### 11.104. cAttributePlayer5KillValue { #cAttributePlayer5KillValue }

Value: `#!cpp int 114`

ID of the player resource Player5 Kill Value. Check [here](../../resources/resources/#114 "Jump to: Game Mecahnicsc > Resources > #114") for more info about what this resource does.

### 11.105. cAttributePlayer6KillValue { #cAttributePlayer6KillValue }

Value: `#!cpp int 115`

ID of the player resource Player6 Kill Value. Check [here](../../resources/resources/#115 "Jump to: Game Mecahnicsc > Resources > #115") for more info about what this resource does.

### 11.106. cAttributePlayer7KillValue { #cAttributePlayer7KillValue }

Value: `#!cpp int 116`

ID of the player resource Player7 Kill Value. Check [here](../../resources/resources/#116 "Jump to: Game Mecahnicsc > Resources > #116") for more info about what this resource does.

### 11.107. cAttributePlayer8KillValue { #cAttributePlayer8KillValue }

Value: `#!cpp int 117`

ID of the player resource Player8 Kill Value. Check [here](../../resources/resources/#117 "Jump to: Game Mecahnicsc > Resources > #117") for more info about what this resource does.

### 11.108. cAttributePlayer1Razings { #cAttributePlayer1Razings }

Value: `#!cpp int 118`

ID of the player resource Player1 Razings. Check [here](../../resources/resources/#118 "Jump to: Game Mecahnicsc > Resources > #118") for more info about what this resource does.

### 11.109. cAttributePlayer2Razings { #cAttributePlayer2Razings }

Value: `#!cpp int 119`

ID of the player resource Player2 Razings. Check [here](../../resources/resources/#119 "Jump to: Game Mecahnicsc > Resources > #119") for more info about what this resource does.

### 11.110. cAttributePlayer3Razings { #cAttributePlayer3Razings }

Value: `#!cpp int 120`

ID of the player resource Player3 Razings. Check [here](../../resources/resources/#120 "Jump to: Game Mecahnicsc > Resources > #120") for more info about what this resource does.

### 11.111. cAttributePlayer4Razings { #cAttributePlayer4Razings }

Value: `#!cpp int 121`

ID of the player resource Player4 Razings. Check [here](../../resources/resources/#121 "Jump to: Game Mecahnicsc > Resources > #121") for more info about what this resource does.

### 11.112. cAttributePlayer5Razings { #cAttributePlayer5Razings }

Value: `#!cpp int 122`

ID of the player resource Player5 Razings. Check [here](../../resources/resources/#122 "Jump to: Game Mecahnicsc > Resources > #122") for more info about what this resource does.

### 11.113. cAttributePlayer6Razings { #cAttributePlayer6Razings }

Value: `#!cpp int 123`

ID of the player resource Player6 Razings. Check [here](../../resources/resources/#123 "Jump to: Game Mecahnicsc > Resources > #123") for more info about what this resource does.

### 11.114. cAttributePlayer7Razings { #cAttributePlayer7Razings }

Value: `#!cpp int 124`

ID of the player resource Player7 Razings. Check [here](../../resources/resources/#124 "Jump to: Game Mecahnicsc > Resources > #124") for more info about what this resource does.

### 11.115. cAttributePlayer8Razings { #cAttributePlayer8Razings }

Value: `#!cpp int 125`

ID of the player resource Player8 Razings. Check [here](../../resources/resources/#125 "Jump to: Game Mecahnicsc > Resources > #125") for more info about what this resource does.

### 11.116. cAttributePlayer1RazingValue { #cAttributePlayer1RazingValue }

Value: `#!cpp int 126`

ID of the player resource Player1 Razing Value. Check [here](../../resources/resources/#126 "Jump to: Game Mecahnicsc > Resources > #126") for more info about what this resource does.

### 11.117. cAttributePlayer2RazingValue { #cAttributePlayer2RazingValue }

Value: `#!cpp int 127`

ID of the player resource Player2 Razing Value. Check [here](../../resources/resources/#127 "Jump to: Game Mecahnicsc > Resources > #127") for more info about what this resource does.

### 11.118. cAttributePlayer3RazingValue { #cAttributePlayer3RazingValue }

Value: `#!cpp int 128`

ID of the player resource Player3 Razing Value. Check [here](../../resources/resources/#128 "Jump to: Game Mecahnicsc > Resources > #128") for more info about what this resource does.

### 11.119. cAttributePlayer4RazingValue { #cAttributePlayer4RazingValue }

Value: `#!cpp int 129`

ID of the player resource Player4 Razing Value. Check [here](../../resources/resources/#129 "Jump to: Game Mecahnicsc > Resources > #129") for more info about what this resource does.

### 11.120. cAttributePlayer5RazingValue { #cAttributePlayer5RazingValue }

Value: `#!cpp int 130`

ID of the player resource Player5 Razing Value. Check [here](../../resources/resources/#130 "Jump to: Game Mecahnicsc > Resources > #130") for more info about what this resource does.

### 11.121. cAttributePlayer6RazingValue { #cAttributePlayer6RazingValue }

Value: `#!cpp int 131`

ID of the player resource Player6 Razing Value. Check [here](../../resources/resources/#131 "Jump to: Game Mecahnicsc > Resources > #131") for more info about what this resource does.

### 11.122. cAttributePlayer7RazingValue { #cAttributePlayer7RazingValue }

Value: `#!cpp int 132`

ID of the player resource Player7 Razing Value. Check [here](../../resources/resources/#132 "Jump to: Game Mecahnicsc > Resources > #132") for more info about what this resource does.

### 11.123. cAttributePlayer8RazingValue { #cAttributePlayer8RazingValue }

Value: `#!cpp int 133`

ID of the player resource Player8 Razing Value. Check [here](../../resources/resources/#133 "Jump to: Game Mecahnicsc > Resources > #133") for more info about what this resource does.

### 11.124. cAttributeCastle { #cAttributeCastle }

Value: `#!cpp int 134`

ID of the player resource Castle. Check [here](../../resources/resources/#134 "Jump to: Game Mecahnicsc > Resources > #134") for more info about what this resource does.

### 11.125. cAttributeHitPointRazings { #cAttributeHitPointRazings }

Value: `#!cpp int 135`

ID of the player resource Hit Point Razings. Check [here](../../resources/resources/#135 "Jump to: Game Mecahnicsc > Resources > #135") for more info about what this resource does.

### 11.126. cAttributeKillsByPlayer1 { #cAttributeKillsByPlayer1 }

Value: `#!cpp int 136`

ID of the player resource Kills By Player1. Check [here](../../resources/resources/#136 "Jump to: Game Mecahnicsc > Resources > #136") for more info about what this resource does.

### 11.127. cAttributeKillsByPlayer2 { #cAttributeKillsByPlayer2 }

Value: `#!cpp int 137`

ID of the player resource Kills By Player2. Check [here](../../resources/resources/#137 "Jump to: Game Mecahnicsc > Resources > #137") for more info about what this resource does.

### 11.128. cAttributeKillsByPlayer3 { #cAttributeKillsByPlayer3 }

Value: `#!cpp int 138`

ID of the player resource Kills By Player3. Check [here](../../resources/resources/#138 "Jump to: Game Mecahnicsc > Resources > #138") for more info about what this resource does.

### 11.129. cAttributeKillsByPlayer4 { #cAttributeKillsByPlayer4 }

Value: `#!cpp int 139`

ID of the player resource Kills By Player4. Check [here](../../resources/resources/#139 "Jump to: Game Mecahnicsc > Resources > #139") for more info about what this resource does.

### 11.130. cAttributeKillsByPlayer5 { #cAttributeKillsByPlayer5 }

Value: `#!cpp int 140`

ID of the player resource Kills By Player5. Check [here](../../resources/resources/#140 "Jump to: Game Mecahnicsc > Resources > #140") for more info about what this resource does.

### 11.131. cAttributeKillsByPlayer6 { #cAttributeKillsByPlayer6 }

Value: `#!cpp int 141`

ID of the player resource Kills By Player6. Check [here](../../resources/resources/#141 "Jump to: Game Mecahnicsc > Resources > #141") for more info about what this resource does.

### 11.132. cAttributeKillsByPlayer7 { #cAttributeKillsByPlayer7 }

Value: `#!cpp int 142`

ID of the player resource Kills By Player7. Check [here](../../resources/resources/#142 "Jump to: Game Mecahnicsc > Resources > #142") for more info about what this resource does.

### 11.133. cAttributeKillsByPlayer8 { #cAttributeKillsByPlayer8 }

Value: `#!cpp int 143`

ID of the player resource Kills By Player8. Check [here](../../resources/resources/#143 "Jump to: Game Mecahnicsc > Resources > #143") for more info about what this resource does.

### 11.134. cAttributeRazingsByPlayer1 { #cAttributeRazingsByPlayer1 }

Value: `#!cpp int 144`

ID of the player resource Razings By Player1. Check [here](../../resources/resources/#144 "Jump to: Game Mecahnicsc > Resources > #144") for more info about what this resource does.

### 11.135. cAttributeRazingsByPlayer2 { #cAttributeRazingsByPlayer2 }

Value: `#!cpp int 145`

ID of the player resource Razings By Player2. Check [here](../../resources/resources/#145 "Jump to: Game Mecahnicsc > Resources > #145") for more info about what this resource does.

### 11.136. cAttributeRazingsByPlayer3 { #cAttributeRazingsByPlayer3 }

Value: `#!cpp int 146`

ID of the player resource Razings By Player3. Check [here](../../resources/resources/#146 "Jump to: Game Mecahnicsc > Resources > #146") for more info about what this resource does.

### 11.137. cAttributeRazingsByPlayer4 { #cAttributeRazingsByPlayer4 }

Value: `#!cpp int 147`

ID of the player resource Razings By Player4. Check [here](../../resources/resources/#147 "Jump to: Game Mecahnicsc > Resources > #147") for more info about what this resource does.

### 11.138. cAttributeRazingsByPlayer5 { #cAttributeRazingsByPlayer5 }

Value: `#!cpp int 148`

ID of the player resource Razings By Player5. Check [here](../../resources/resources/#148 "Jump to: Game Mecahnicsc > Resources > #148") for more info about what this resource does.

### 11.139. cAttributeRazingsByPlayer6 { #cAttributeRazingsByPlayer6 }

Value: `#!cpp int 149`

ID of the player resource Razings By Player6. Check [here](../../resources/resources/#149 "Jump to: Game Mecahnicsc > Resources > #149") for more info about what this resource does.

### 11.140. cAttributeRazingsByPlayer7 { #cAttributeRazingsByPlayer7 }

Value: `#!cpp int 150`

ID of the player resource Razings By Player7. Check [here](../../resources/resources/#150 "Jump to: Game Mecahnicsc > Resources > #150") for more info about what this resource does.

### 11.141. cAttributeRazingsByPlayer8 { #cAttributeRazingsByPlayer8 }

Value: `#!cpp int 151`

ID of the player resource Razings By Player8. Check [here](../../resources/resources/#151 "Jump to: Game Mecahnicsc > Resources > #151") for more info about what this resource does.

### 11.142. cAttributeValueKilledByOthers { #cAttributeValueKilledByOthers }

Value: `#!cpp int 152`

ID of the player resource Value Killed By Others. Check [here](../../resources/resources/#152 "Jump to: Game Mecahnicsc > Resources > #152") for more info about what this resource does.

### 11.143. cAttributeValueRazedByOthers { #cAttributeValueRazedByOthers }

Value: `#!cpp int 153`

ID of the player resource Value Razed By Others. Check [here](../../resources/resources/#153 "Jump to: Game Mecahnicsc > Resources > #153") for more info about what this resource does.

### 11.144. cAttributeKilledByOthers { #cAttributeKilledByOthers }

Value: `#!cpp int 154`

ID of the player resource Killed By Others. Check [here](../../resources/resources/#154 "Jump to: Game Mecahnicsc > Resources > #154") for more info about what this resource does.

### 11.145. cAttributeRazedByOthers { #cAttributeRazedByOthers }

Value: `#!cpp int 155`

ID of the player resource Razed By Others. Check [here](../../resources/resources/#155 "Jump to: Game Mecahnicsc > Resources > #155") for more info about what this resource does.

### 11.146. cAttributeTributeFromPlayer1 { #cAttributeTributeFromPlayer1 }

Value: `#!cpp int 156`

ID of the player resource Tribute From Player1. Check [here](../../resources/resources/#156 "Jump to: Game Mecahnicsc > Resources > #156") for more info about what this resource does.

### 11.147. cAttributeTributeFromPlayer2 { #cAttributeTributeFromPlayer2 }

Value: `#!cpp int 157`

ID of the player resource Tribute From Player2. Check [here](../../resources/resources/#157 "Jump to: Game Mecahnicsc > Resources > #157") for more info about what this resource does.

### 11.148. cAttributeTributeFromPlayer3 { #cAttributeTributeFromPlayer3 }

Value: `#!cpp int 158`

ID of the player resource Tribute From Player3. Check [here](../../resources/resources/#158 "Jump to: Game Mecahnicsc > Resources > #158") for more info about what this resource does.

### 11.149. cAttributeTributeFromPlayer4 { #cAttributeTributeFromPlayer4 }

Value: `#!cpp int 159`

ID of the player resource Tribute From Player4. Check [here](../../resources/resources/#159 "Jump to: Game Mecahnicsc > Resources > #159") for more info about what this resource does.

### 11.150. cAttributeTributeFromPlayer5 { #cAttributeTributeFromPlayer5 }

Value: `#!cpp int 160`

ID of the player resource Tribute From Player5. Check [here](../../resources/resources/#160 "Jump to: Game Mecahnicsc > Resources > #160") for more info about what this resource does.

### 11.151. cAttributeTributeFromPlayer6 { #cAttributeTributeFromPlayer6 }

Value: `#!cpp int 161`

ID of the player resource Tribute From Player6. Check [here](../../resources/resources/#161 "Jump to: Game Mecahnicsc > Resources > #161") for more info about what this resource does.

### 11.152. cAttributeTributeFromPlayer7 { #cAttributeTributeFromPlayer7 }

Value: `#!cpp int 162`

ID of the player resource Tribute From Player7. Check [here](../../resources/resources/#162 "Jump to: Game Mecahnicsc > Resources > #162") for more info about what this resource does.

### 11.153. cAttributeTributeFromPlayer8 { #cAttributeTributeFromPlayer8 }

Value: `#!cpp int 163`

ID of the player resource Tribute From Player8. Check [here](../../resources/resources/#163 "Jump to: Game Mecahnicsc > Resources > #163") for more info about what this resource does.

### 11.154. cAttributeValueCurrentUnits { #cAttributeValueCurrentUnits }

Value: `#!cpp int 164`

ID of the player resource Value Current Units. Check [here](../../resources/resources/#164 "Jump to: Game Mecahnicsc > Resources > #164") for more info about what this resource does.

### 11.155. cAttributeValueCurrentBuildings { #cAttributeValueCurrentBuildings }

Value: `#!cpp int 165`

ID of the player resource Value Current Buildings. Check [here](../../resources/resources/#165 "Jump to: Game Mecahnicsc > Resources > #165") for more info about what this resource does.

### 11.156. cAttributeFoodTotal { #cAttributeFoodTotal }

Value: `#!cpp int 166`

ID of the player resource Food Total. Check [here](../../resources/resources/#166 "Jump to: Game Mecahnicsc > Resources > #166") for more info about what this resource does.

### 11.157. cAttributeWoodTotal { #cAttributeWoodTotal }

Value: `#!cpp int 167`

ID of the player resource Wood Total. Check [here](../../resources/resources/#167 "Jump to: Game Mecahnicsc > Resources > #167") for more info about what this resource does.

### 11.158. cAttributeStoneTotal { #cAttributeStoneTotal }

Value: `#!cpp int 168`

ID of the player resource Stone Total. Check [here](../../resources/resources/#168 "Jump to: Game Mecahnicsc > Resources > #168") for more info about what this resource does.

### 11.159. cAttributeGoldTotal { #cAttributeGoldTotal }

Value: `#!cpp int 169`

ID of the player resource Gold Total. Check [here](../../resources/resources/#169 "Jump to: Game Mecahnicsc > Resources > #169") for more info about what this resource does.

### 11.160. cAttributeTotalValueOfKills { #cAttributeTotalValueOfKills }

Value: `#!cpp int 170`

ID of the player resource Total Value Of Kills. Check [here](../../resources/resources/#170 "Jump to: Game Mecahnicsc > Resources > #170") for more info about what this resource does.

### 11.161. cAttributeTotalTributeReceived { #cAttributeTotalTributeReceived }

Value: `#!cpp int 171`

ID of the player resource Total Tribute Received. Check [here](../../resources/resources/#171 "Jump to: Game Mecahnicsc > Resources > #171") for more info about what this resource does.

### 11.162. cAttributeTotalValueOfRazings { #cAttributeTotalValueOfRazings }

Value: `#!cpp int 172`

ID of the player resource Total Value Of Razings. Check [here](../../resources/resources/#172 "Jump to: Game Mecahnicsc > Resources > #172") for more info about what this resource does.

### 11.163. cAttributeTotalCastlesBuilt { #cAttributeTotalCastlesBuilt }

Value: `#!cpp int 173`

ID of the player resource Total Castles Built. Check [here](../../resources/resources/#173 "Jump to: Game Mecahnicsc > Resources > #173") for more info about what this resource does.

### 11.164. cAttributeTotalWondersBuilt { #cAttributeTotalWondersBuilt }

Value: `#!cpp int 174`

ID of the player resource Total Wonders Built. Check [here](../../resources/resources/#174 "Jump to: Game Mecahnicsc > Resources > #174") for more info about what this resource does.

### 11.165. cAttributeTributeScore { #cAttributeTributeScore }

Value: `#!cpp int 175`

ID of the player resource Tribute Score. Check [here](../../resources/resources/#175 "Jump to: Game Mecahnicsc > Resources > #175") for more info about what this resource does.

### 11.166. cAttributeConvertMinAdj { #cAttributeConvertMinAdj }

Value: `#!cpp int 176`

ID of the player resource Convert Min Adj. Check [here](../../resources/resources/#176 "Jump to: Game Mecahnicsc > Resources > #176") for more info about what this resource does.

### 11.167. cAttributeConvertMaxAdj { #cAttributeConvertMaxAdj }

Value: `#!cpp int 177`

ID of the player resource Convert Max Adj. Check [here](../../resources/resources/#177 "Jump to: Game Mecahnicsc > Resources > #177") for more info about what this resource does.

### 11.168. cAttributeConvertResistMinAdj { #cAttributeConvertResistMinAdj }

Value: `#!cpp int 178`

ID of the player resource Convert Resist Min Adj. Check [here](../../resources/resources/#178 "Jump to: Game Mecahnicsc > Resources > #178") for more info about what this resource does.

### 11.169. cAttributeConvertResistMaxAdj { #cAttributeConvertResistMaxAdj }

Value: `#!cpp int 179`

ID of the player resource Convert Resist Max Adj. Check [here](../../resources/resources/#179 "Jump to: Game Mecahnicsc > Resources > #179") for more info about what this resource does.

### 11.170. cAttributeConvertBuildingMin { #cAttributeConvertBuildingMin }

Value: `#!cpp int 180`

ID of the player resource Convert Building Min. Check [here](../../resources/resources/#180 "Jump to: Game Mecahnicsc > Resources > #180") for more info about what this resource does.

### 11.171. cAttributeConvertBuildingMax { #cAttributeConvertBuildingMax }

Value: `#!cpp int 181`

ID of the player resource Convert Building Max. Check [here](../../resources/resources/#181 "Jump to: Game Mecahnicsc > Resources > #181") for more info about what this resource does.

### 11.172. cAttributeConvertBuildingChance { #cAttributeConvertBuildingChance }

Value: `#!cpp int 182`

ID of the player resource Convert Building Chance. Check [here](../../resources/resources/#182 "Jump to: Game Mecahnicsc > Resources > #182") for more info about what this resource does.

### 11.173. cAttributeSpies { #cAttributeSpies }

Value: `#!cpp int 183`

ID of the player resource Spies. Check [here](../../resources/resources/#183 "Jump to: Game Mecahnicsc > Resources > #183") for more info about what this resource does.

### 11.174. cAttributeValueWondersCastles { #cAttributeValueWondersCastles }

Value: `#!cpp int 184`

ID of the player resource Value Wonders Castles. Check [here](../../resources/resources/#184 "Jump to: Game Mecahnicsc > Resources > #184") for more info about what this resource does.

### 11.175. cAttributeFoodScore { #cAttributeFoodScore }

Value: `#!cpp int 185`

ID of the player resource Food Score. Check [here](../../resources/resources/#185 "Jump to: Game Mecahnicsc > Resources > #185") for more info about what this resource does.

### 11.176. cAttributeWoodScore { #cAttributeWoodScore }

Value: `#!cpp int 186`

ID of the player resource Wood Score. Check [here](../../resources/resources/#186 "Jump to: Game Mecahnicsc > Resources > #186") for more info about what this resource does.

### 11.177. cAttributeStoneScore { #cAttributeStoneScore }

Value: `#!cpp int 187`

ID of the player resource Stone Score. Check [here](../../resources/resources/#187 "Jump to: Game Mecahnicsc > Resources > #187") for more info about what this resource does.

### 11.178. cAttributeGoldScore { #cAttributeGoldScore }

Value: `#!cpp int 188`

ID of the player resource Gold Score. Check [here](../../resources/resources/#188 "Jump to: Game Mecahnicsc > Resources > #188") for more info about what this resource does.

### 11.179. cAttributeWoodBonus { #cAttributeWoodBonus }

Value: `#!cpp int 189`

ID of the player resource Wood Bonus. Check [here](../../resources/resources/#189 "Jump to: Game Mecahnicsc > Resources > #189") for more info about what this resource does.

### 11.180. cAttributeFoodBonus { #cAttributeFoodBonus }

Value: `#!cpp int 190`

ID of the player resource Food Bonus. Check [here](../../resources/resources/#190 "Jump to: Game Mecahnicsc > Resources > #190") for more info about what this resource does.

### 11.181. cAttributeRelicRate { #cAttributeRelicRate }

Value: `#!cpp int 191`

ID of the player resource Relic Rate. Check [here](../../resources/resources/#191 "Jump to: Game Mecahnicsc > Resources > #191") for more info about what this resource does.

### 11.182. cAttributeHeresy { #cAttributeHeresy }

Value: `#!cpp int 192`

ID of the player resource Heresy. Check [here](../../resources/resources/#192 "Jump to: Game Mecahnicsc > Resources > #192") for more info about what this resource does.

### 11.183. cAttributeTheocracy { #cAttributeTheocracy }

Value: `#!cpp int 193`

ID of the player resource Theocracy. Check [here](../../resources/resources/#193 "Jump to: Game Mecahnicsc > Resources > #193") for more info about what this resource does.

### 11.184. cAttributeCrenellations { #cAttributeCrenellations }

Value: `#!cpp int 194`

ID of the player resource Crenellations. Check [here](../../resources/resources/#194 "Jump to: Game Mecahnicsc > Resources > #194") for more info about what this resource does.

### 11.185. cAttributeConstructionRateMod { #cAttributeConstructionRateMod }

Value: `#!cpp int 195`

ID of the player resource Construction Rate Mod. Check [here](../../resources/resources/#195 "Jump to: Game Mecahnicsc > Resources > #195") for more info about what this resource does.

### 11.186. cAttributeHunWonderBonus { #cAttributeHunWonderBonus }

Value: `#!cpp int 196`

ID of the player resource Hun Wonder Bonus. Check [here](../../resources/resources/#196 "Jump to: Game Mecahnicsc > Resources > #196") for more info about what this resource does.

### 11.187. cAttributeSpiesDiscount { #cAttributeSpiesDiscount }

Value: `#!cpp int 197`

ID of the player resource Spies Discount. Check [here](../../resources/resources/#197 "Jump to: Game Mecahnicsc > Resources > #197") for more info about what this resource does.

### 11.188. cAttributeTemporaryMapReveal { #cAttributeTemporaryMapReveal }

Value: `#!cpp int 209`

ID of the player resource Temporary Map Reveal. Check [here](../../resources/resources/#209 "Jump to: Game Mecahnicsc > Resources > #209") for more info about what this resource does.

### 11.189. cAttributeRevealInitialType { #cAttributeRevealInitialType }

Value: `#!cpp int 210`

ID of the player resource Reveal Initial Type. Check [here](../../resources/resources/#210 "Jump to: Game Mecahnicsc > Resources > #210") for more info about what this resource does.

### 11.190. cAttributeElevationBonusHigher { #cAttributeElevationBonusHigher }

Value: `#!cpp int 211`

ID of the player resource Elevation Bonus Higher. Check [here](../../resources/resources/#211 "Jump to: Game Mecahnicsc > Resources > #211") for more info about what this resource does.

### 11.191. cAttributeElevationBonusLoweer { #cAttributeElevationBonusLoweer }

Value: `#!cpp int 212`

ID of the player resource Elevation Bonus Loweer. Check [here](../../resources/resources/#212 "Jump to: Game Mecahnicsc > Resources > #212") for more info about what this resource does.

### 11.192. cAttributeTriggerSharedLOS { #cAttributeTriggerSharedLOS }

Value: `#!cpp int 217`

ID of the player resource Trigger Shared L O S. Check [here](../../resources/resources/#217 "Jump to: Game Mecahnicsc > Resources > #217") for more info about what this resource does.

### 11.193. cAttributeFeudalTownCenterLimit { #cAttributeFeudalTownCenterLimit }

Value: `#!cpp int 218`

ID of the player resource Feudal Town Center Limit. Check [here](../../resources/resources/#218 "Jump to: Game Mecahnicsc > Resources > #218") for more info about what this resource does.

### 11.194. cAttributeUnused1 { #cAttributeUnused1 }

Value: `#!cpp int 219`

ID of the player resource Unused1. Check [here](../../resources/resources/#219 "Jump to: Game Mecahnicsc > Resources > #219") for more info about what this resource does.

### 11.195. cAttributeUnused2 { #cAttributeUnused2 }

Value: `#!cpp int 220`

ID of the player resource Unused2. Check [here](../../resources/resources/#220 "Jump to: Game Mecahnicsc > Resources > #220") for more info about what this resource does.

### 11.196. cAttributeMonumentFoodTrickle { #cAttributeMonumentFoodTrickle }

Value: `#!cpp int 221`

ID of the player resource Monument Food Trickle. Check [here](../../resources/resources/#221 "Jump to: Game Mecahnicsc > Resources > #221") for more info about what this resource does.

### 11.197. cAttributeMonumentWoodTrickle { #cAttributeMonumentWoodTrickle }

Value: `#!cpp int 222`

ID of the player resource Monument Wood Trickle. Check [here](../../resources/resources/#222 "Jump to: Game Mecahnicsc > Resources > #222") for more info about what this resource does.

### 11.198. cAttributeMonumentStoneTrickle { #cAttributeMonumentStoneTrickle }

Value: `#!cpp int 223`

ID of the player resource Monument Stone Trickle. Check [here](../../resources/resources/#223 "Jump to: Game Mecahnicsc > Resources > #223") for more info about what this resource does.

### 11.199. cAttributeMonumentGoldTrickle { #cAttributeMonumentGoldTrickle }

Value: `#!cpp int 224`

ID of the player resource Monument Gold Trickle. Check [here](../../resources/resources/#224 "Jump to: Game Mecahnicsc > Resources > #224") for more info about what this resource does.

### 11.200. cAttributeRelicFoodRate { #cAttributeRelicFoodRate }

Value: `#!cpp int 225`

ID of the player resource Relic Food Rate. Check [here](../../resources/resources/#225 "Jump to: Game Mecahnicsc > Resources > #225") for more info about what this resource does.

### 11.201. cAttributeVillagersKilledByGaia { #cAttributeVillagersKilledByGaia }

Value: `#!cpp int 226`

ID of the player resource Villagers Killed By Gaia. Check [here](../../resources/resources/#226 "Jump to: Game Mecahnicsc > Resources > #226") for more info about what this resource does.

### 11.202. cAttributeVillgaersKilledByAnimal { #cAttributeVillgaersKilledByAnimal }

Value: `#!cpp int 227`

ID of the player resource Villgaers Killed By Animal. Check [here](../../resources/resources/#227 "Jump to: Game Mecahnicsc > Resources > #227") for more info about what this resource does.

### 11.203. cAttributeVillagersKilledByAIPlayer { #cAttributeVillagersKilledByAIPlayer }

Value: `#!cpp int 228`

ID of the player resource Villagers Killed By A I Player. Check [here](../../resources/resources/#228 "Jump to: Game Mecahnicsc > Resources > #228") for more info about what this resource does.

### 11.204. cAttributeVillagersKilledByHumanPlayer { #cAttributeVillagersKilledByHumanPlayer }

Value: `#!cpp int 229`

ID of the player resource Villagers Killed By Human Player. Check [here](../../resources/resources/#229 "Jump to: Game Mecahnicsc > Resources > #229") for more info about what this resource does.

### 11.205. cAttributeFoodGeneration { #cAttributeFoodGeneration }

Value: `#!cpp int 230`

ID of the player resource Food Generation. Check [here](../../resources/resources/#230 "Jump to: Game Mecahnicsc > Resources > #230") for more info about what this resource does.

### 11.206. cAttributeWoodGeneration { #cAttributeWoodGeneration }

Value: `#!cpp int 231`

ID of the player resource Wood Generation. Check [here](../../resources/resources/#231 "Jump to: Game Mecahnicsc > Resources > #231") for more info about what this resource does.

### 11.207. cAttributeStoneGeneration { #cAttributeStoneGeneration }

Value: `#!cpp int 232`

ID of the player resource Stone Generation. Check [here](../../resources/resources/#232 "Jump to: Game Mecahnicsc > Resources > #232") for more info about what this resource does.

### 11.208. cAttributeGoldGeneration { #cAttributeGoldGeneration }

Value: `#!cpp int 233`

ID of the player resource Gold Generation. Check [here](../../resources/resources/#233 "Jump to: Game Mecahnicsc > Resources > #233") for more info about what this resource does.

### 11.209. cAttributeSpawnCap { #cAttributeSpawnCap }

Value: `#!cpp int 234`

ID of the player resource Spawn Cap. Check [here](../../resources/resources/#234 "Jump to: Game Mecahnicsc > Resources > #234") for more info about what this resource does.

### 11.210. cAttributeFlemishMilitiaPop { #cAttributeFlemishMilitiaPop }

Value: `#!cpp int 235`

ID of the player resource Flemish Militia Pop. Check [here](../../resources/resources/#235 "Jump to: Game Mecahnicsc > Resources > #235") for more info about what this resource does.

### 11.211. cAttributeGoldFarmingProductivity { #cAttributeGoldFarmingProductivity }

Value: `#!cpp int 236`

ID of the player resource Gold Farming Productivity. Check [here](../../resources/resources/#236 "Jump to: Game Mecahnicsc > Resources > #236") for more info about what this resource does.

### 11.212. cAttributeFolwarkCollectionAmount { #cAttributeFolwarkCollectionAmount }

Value: `#!cpp int 237`

ID of the player resource Folwark Collection Amount. Check [here](../../resources/resources/#237 "Jump to: Game Mecahnicsc > Resources > #237") for more info about what this resource does.

### 11.213. cAttributeFolwarkCollectionType { #cAttributeFolwarkCollectionType }

Value: `#!cpp int 238`

ID of the player resource Folwark Collection Type. Check [here](../../resources/resources/#238 "Jump to: Game Mecahnicsc > Resources > #238") for more info about what this resource does.

### 11.214. cAttributeBuildingId { #cAttributeBuildingId }

Value: `#!cpp int 239`

ID of the player resource Building Id. Check [here](../../resources/resources/#239 "Jump to: Game Mecahnicsc > Resources > #239") for more info about what this resource does.

### 11.215. cAttributeUnitsConverted { #cAttributeUnitsConverted }

Value: `#!cpp int 240`

ID of the player resource Units Converted. Check [here](../../resources/resources/#240 "Jump to: Game Mecahnicsc > Resources > #240") for more info about what this resource does.

### 11.216. cAttributeStoneGoldMiningProductivity { #cAttributeStoneGoldMiningProductivity }

Value: `#!cpp int 241`

ID of the player resource Stone Gold Mining Productivity. Check [here](../../resources/resources/#241 "Jump to: Game Mecahnicsc > Resources > #241") for more info about what this resource does.

### 11.217. cAttributeWorkshopFoodTrickle { #cAttributeWorkshopFoodTrickle }

Value: `#!cpp int 242`

ID of the player resource Workshop Food Trickle. Check [here](../../resources/resources/#242 "Jump to: Game Mecahnicsc > Resources > #242") for more info about what this resource does.

### 11.218. cAttributeWorkshopWoodTrickle { #cAttributeWorkshopWoodTrickle }

Value: `#!cpp int 243`

ID of the player resource Workshop Wood Trickle. Check [here](../../resources/resources/#243 "Jump to: Game Mecahnicsc > Resources > #243") for more info about what this resource does.

### 11.219. cAttributeWorkshopStoneTrickle { #cAttributeWorkshopStoneTrickle }

Value: `#!cpp int 244`

ID of the player resource Workshop Stone Trickle. Check [here](../../resources/resources/#244 "Jump to: Game Mecahnicsc > Resources > #244") for more info about what this resource does.

### 11.220. cAttributeWorkshopGoldTrickle { #cAttributeWorkshopGoldTrickle }

Value: `#!cpp int 245`

ID of the player resource Workshop Gold Trickle. Check [here](../../resources/resources/#245 "Jump to: Game Mecahnicsc > Resources > #245") for more info about what this resource does.

### 11.221. cAttributeUnitsValueTotal { #cAttributeUnitsValueTotal }

Value: `#!cpp int 246`

ID of the player resource Units Value Total. Check [here](../../resources/resources/#246 "Jump to: Game Mecahnicsc > Resources > #246") for more info about what this resource does.

### 11.222. cAttributeBuildingsValueTotal { #cAttributeBuildingsValueTotal }

Value: `#!cpp int 247`

ID of the player resource Buildings Value Total. Check [here](../../resources/resources/#247 "Jump to: Game Mecahnicsc > Resources > #247") for more info about what this resource does.

### 11.223. cAttributeVillagersCreatedTotal { #cAttributeVillagersCreatedTotal }

Value: `#!cpp int 248`

ID of the player resource Villagers Created Total. Check [here](../../resources/resources/#248 "Jump to: Game Mecahnicsc > Resources > #248") for more info about what this resource does.

### 11.224. cAttributeVillagersIdlePeriodsTotal { #cAttributeVillagersIdlePeriodsTotal }

Value: `#!cpp int 249`

ID of the player resource Villagers Idle Periods Total. Check [here](../../resources/resources/#249 "Jump to: Game Mecahnicsc > Resources > #249") for more info about what this resource does.

### 11.225. cAttributeVillagersIdleSecondsTotal { #cAttributeVillagersIdleSecondsTotal }

Value: `#!cpp int 250`

ID of the player resource Villagers Idle Seconds Total. Check [here](../../resources/resources/#250 "Jump to: Game Mecahnicsc > Resources > #250") for more info about what this resource does.

### 11.226. cAttributeTradeFoodPercent { #cAttributeTradeFoodPercent }

Value: `#!cpp int 251`

ID of the player resource Trade Food Percent. Check [here](../../resources/resources/#251 "Jump to: Game Mecahnicsc > Resources > #251") for more info about what this resource does.

### 11.227. cAttributeTradeWoodPercent { #cAttributeTradeWoodPercent }

Value: `#!cpp int 252`

ID of the player resource Trade Wood Percent. Check [here](../../resources/resources/#252 "Jump to: Game Mecahnicsc > Resources > #252") for more info about what this resource does.

### 11.228. cAttributeTradeStonePercent { #cAttributeTradeStonePercent }

Value: `#!cpp int 253`

ID of the player resource Trade Stone Percent. Check [here](../../resources/resources/#253 "Jump to: Game Mecahnicsc > Resources > #253") for more info about what this resource does.

### 11.229. cAttributeLivestockFoodProductivity { #cAttributeLivestockFoodProductivity }

Value: `#!cpp int 254`

ID of the player resource Livestock Food Productivity. Check [here](../../resources/resources/#254 "Jump to: Game Mecahnicsc > Resources > #254") for more info about what this resource does.

### 11.230. cAttributeSpeedUpBuildingType { #cAttributeSpeedUpBuildingType }

Value: `#!cpp int 255`

ID of the player resource Speed Up Building Type. Check [here](../../resources/resources/#255 "Jump to: Game Mecahnicsc > Resources > #255") for more info about what this resource does.

### 11.231. cAttributeSpeedUpBuildingRange { #cAttributeSpeedUpBuildingRange }

Value: `#!cpp int 256`

ID of the player resource Speed Up Building Range. Check [here](../../resources/resources/#256 "Jump to: Game Mecahnicsc > Resources > #256") for more info about what this resource does.

### 11.232. cAttributeSpeedUpPercentage { #cAttributeSpeedUpPercentage }

Value: `#!cpp int 257`

ID of the player resource Speed Up Percentage. Check [here](../../resources/resources/#257 "Jump to: Game Mecahnicsc > Resources > #257") for more info about what this resource does.

### 11.233. cAttributeSpeedUpObjectType { #cAttributeSpeedUpObjectType }

Value: `#!cpp int 258`

ID of the player resource Speed Up Object Type. Check [here](../../resources/resources/#258 "Jump to: Game Mecahnicsc > Resources > #258") for more info about what this resource does.

### 11.234. cAttributeSpeedUpEffectType { #cAttributeSpeedUpEffectType }

Value: `#!cpp int 259`

ID of the player resource Speed Up Effect Type. Check [here](../../resources/resources/#259 "Jump to: Game Mecahnicsc > Resources > #259") for more info about what this resource does.

### 11.235. cAttributeSpeedUpSecondaryEffectType { #cAttributeSpeedUpSecondaryEffectType }

Value: `#!cpp int 260`

ID of the player resource Speed Up Secondary Effect Type. Check [here](../../resources/resources/#260 "Jump to: Game Mecahnicsc > Resources > #260") for more info about what this resource does.

### 11.236. cAttributeSpeedUpSecondaryPercentage { #cAttributeSpeedUpSecondaryPercentage }

Value: `#!cpp int 261`

ID of the player resource Speed Up Secondary Percentage. Check [here](../../resources/resources/#261 "Jump to: Game Mecahnicsc > Resources > #261") for more info about what this resource does.

### 11.237. cAttributeExtraElephantConvertResist { #cAttributeExtraElephantConvertResist }

Value: `#!cpp int 262`

ID of the player resource Extra Elephant Convert Resist. Check [here](../../resources/resources/#262 "Jump to: Game Mecahnicsc > Resources > #262") for more info about what this resource does.

### 11.238. cAttributeStartingScoutID { #cAttributeStartingScoutID }

Value: `#!cpp int 263`

ID of the player resource Starting Scout I D. Check [here](../../resources/resources/#263 "Jump to: Game Mecahnicsc > Resources > #263") for more info about what this resource does.

### 11.239. cAttributeRelicWoodRate { #cAttributeRelicWoodRate }

Value: `#!cpp int 264`

ID of the player resource Relic Wood Rate. Check [here](../../resources/resources/#264 "Jump to: Game Mecahnicsc > Resources > #264") for more info about what this resource does.

### 11.240. cAttributeRelicStoneRate { #cAttributeRelicStoneRate }

Value: `#!cpp int 265`

ID of the player resource Relic Stone Rate. Check [here](../../resources/resources/#265 "Jump to: Game Mecahnicsc > Resources > #265") for more info about what this resource does.
