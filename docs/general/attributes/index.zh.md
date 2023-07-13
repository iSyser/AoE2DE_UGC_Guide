# 单位属性

_作者：Alian713, 别云_

---

此页面列出了可以在场景编辑器中修改的所有单位属性及其用途。如果您知道本页上未提及的任何属性，或者属性的描述有误，请告知本指南的作者！

## 0. 生命值 { #0 }

-   ID: 0

-   英文原名: Hit Points

-   该属性指的是单位的生命值

## 1. 视野 { #1 }

-   ID: 1

-   英文原名: Line of Sight

-   这是单位可以看到自身周围的距离

## 2. 驻扎容量 { #2 }

-   ID: 2

-   英文原名: Garrison Capacity

-   这是可以驻扎另一些单位的数量

## 3. 单位尺寸 X { #3 }

-   ID: 3

-   英文原名: Unit Size X

-   这决定了单位碰撞盒子的 x 尺寸（单位的宽度）

## 4. 单位尺寸 Y { #4 }

-   ID: 4

-   英文原名: Unit Size Y

-   这决定了单位碰撞盒子的 y 尺寸（单位的长度）

## 5. 移动速度 { #5 }

-   ID: 5

-   英文原名: Movement Speed

-   这是单位的移动速度，单位：格/秒

## 6. 旋转速度 { #6 }

-   ID: 6

-   英文原名: Rotation Speed

-   这是可以旋转的单位的旋转速率，单位：秒/帧（在对象可以切换到下一个旋转帧之前需要等待这么多秒）。例如，为了让投石机开始攻击与朝向相反方向的建筑物，它首先需要旋转朝向到那个方向

## 8. 护甲 { #8 }

-   ID: 8

-   英文原名: Armor

-   这是一个单位在其任何 `护甲类型` 上拥有的护甲值。如果您不知道什么是 `护甲类型`，请参阅本手册的[伤害计算](../damage_calculation "跳转至：游戏机制 > 伤害计算")部分。请注意，通过此选项更改护甲将显示其已添加到基础护甲值中（例如：4+4）。

## 9. 攻击力 { #9 }

-   ID: 9

-   英文原名: Attack

-   这是一个单位在其任何 `攻击类型` 上拥有的攻击力。如果您不知道什么是 `攻击类型`，请参阅本手册的[伤害计算](../damage_calculation "跳转至：游戏机制 > 伤害计算")部分。请注意，通过此选项更改攻击将显示其已添加到基本攻击力中（例如：6+2）。

## 10. 攻击间隔 { #10 }

-   ID: 10

-   英文原名: Attack Reload Time

-   这是单位能够再次射箭之前必须经过的最短时间。对于近战单位来说，这是他们可以进行的两次连续攻击之间的最短时间

## 11. 命中率 { #11 }

-   ID: 11

-   英文原名: Accuracy Percent

-   这决定了一个单位瞄准另一个单位的准确度

-   该命中率是单位向目标的正中心开火的命中率。如果发射的子弹不是瞄准目标的正中心，如果偏差不是太大，它仍然可能击中目标，因为它仍然可以落在目标的命中范围内，只是不是在正中心

    因此，更大的目标实际上更容易击中，这解释了为什么建筑物比小单位更容易被投石机击中

    ![视觉上较小](./imgs/visually_smaller.png "距离较远的目标视觉上较小")

    在此图中，您可以看到，在第二个情景中，红色区域散布的打偏的子弹，其实是能够击中像第一个情景中那样近的目标的。

    从技术上讲，距离较远的相同尺寸的物体的视角较小，因此在射击的角度范围方面，容错率更小

    单位被僧侣转换的几率也取决于其命中率

    如果您将投石车修改为具有较大的溅射半径并赋予其较小的命中率，然后攻击大量聚集在一起的单位，则命中率决定了受到投石车溅射伤害的单位百分比！同时这也是战狼号投石机设置 100% 命中率的原因，因为这样可以使得战狼号溅射范围内所有单位都受到伤害。还有一个有趣的用法是投石车的删除技巧。当投石车在抛射后被立即删除时，由于死亡的单位没有命中率，便默认为 100%，从而对溅射半径内的所有单位造成更多伤害

    注意：在确定被删除的投石车抛射砸中的伤害时，还有另外两个因素发挥作用

    1. 当从投石车溅射中心（目标点）向外移动时，其射击造成的伤害会随着距离的增加而降低。 然而，当投石车被删除时，这种随距离的衰减就不会发生，并且抛射物会对溅射半径内的所有单位造成 100% 的全额伤害！

    2. 由于高地存在伤害加减成，从较低高度发射的子弹通常只能造成正常伤害的 75%。在这种情况下删除投石车也会使伤害达到 100%，就好像没有高度差异一样

## 12. Max Range { #12 }

-   ID: 12

-   英文原名: Max Range

-   This is the maximum range of a unit. Note that to be able to shoot at a target, it must be visible to the unit via its own line of sight or from another unit's line of sight

## 13. Work Rate { #13 }

-   ID: 13

-   英文原名: Work Rate

-   This is the work rate for any unit that can do work. Villagers, Fishing Ships, Serjeants

## 14. Carry Capacity { #14 }

-   ID: 14

-   英文原名: Carry Capacity

-   This is the carry capacity of Villagers

## 15. Base Armor { #15 }

-   ID: 15

-   英文原名: Base Armor

-   This is the quantity of base armour a unit has on any of its `Armour Classes`. If you do not know what an `Armour Class` is, refer to the [Damage Calculation](../damage_calculation "Jump to: Game Mechanics > Damage Calculation") section of this guide. Note that changing the armour through this option will show it as the base armour itself, and it will not be added to the regular amount

## 16. Projectile Unit { #16 }

-   ID: 16

-   英文原名: Projectile Unit

-   This is the ID of the projectile that a unit fires

## 17. Building Icon Override { #17 }

-   ID: 17

-   英文原名: Building Icon Override

-   The functionality of this attribute is unknown as it doesn't always behave certainly. If you know what this attribute does, please let the authors of this guide know!

## 18. Terrain Defense Bonus { #18 }

-   ID: 18

-   英文原名: Terrain Defense Bonus

-   Unknown... What does this attribute do?

## 19. Projectile Smart Mode { #19 }

-   ID: 19

-   英文原名: Projectile Smart Mode

-   This is a combinable bit field. Controls the following two behaviours for projectiles:

-   For example, if we set this property of the projectile used by an archer to `1`, it will have ballistics. (This is exactly what researching ballistics does in the first place). If we set this property to `2`, a missed projectile that hits another unit will deal its full damage instead of the 50% that it would normally do

    What if we want to enable both properties at once? This is achieved by adding the flag values for both of them together. Setting this property to `3` enables both effects

    | 标识                            |  值 |
    | :------------------------------ | --: |
    | No Ballistics                   |   0 |
    | Has Ballistics                  |   1 |
    | Deals full damage on missed hit |   2 |

## 20. Minimum Range { #20 }

-   ID: 20

-   英文原名: Minimum Range

-   The minimum distance a unit must be from an attacking unit for the attacking unit to be able to fire its projectile

## 21. Amount of 1st Resource Storage { #21 }

-   ID: 21

-   英文原名: Amount of 1st Resource Storage

-   This is the amount of 1st resource contained in any unit. Refer to A.G.E. to see which resource this is for each unit

## 22. Blast Width { #22 }

-   ID: 22

-   英文原名: Blast Width

-   All enemy units inside this radius take damage from an attacking unit. This is used by elephants, Druzhina Halberdiers, and Logistica Cataphracts

## 23. Search Radius { #23 }

-   ID: 23

-   英文原名: Search Radius

-   The maximum distance at which a unit can detect and auto attack enemy units

## 24. Bonus Damage Resistance { #24 }

-   ID: 24

-   英文原名: Bonus Damage Resistance

-   Used by Sicilians for the 50% bonus damage resistance. Set to 0.5 for all Sicilian land military units except siege

## 25. Icon ID { #25 }

-   ID: 25

-   英文原名: Icon ID

-   The ID of the icon that you want a unit to show

## 26. Amount of 2nd Resource Storage { #26 }

-   ID: 26

-   英文原名: Amount of 2nd Resource Storage

-   This is the amount of 2nd resource contained in any unit. Refer to A.G.E. to see which resource this is for each unit

## 27. Amount of 3rd Resource Storage { #27 }

-   ID: 27

-   英文原名: Amount of 3rd Resource Storage

-   This is the amount of 3rd resource contained in any unit. Refer to A.G.E. to see which resource this is for each unit

## 28. Fog Visibility { #28 }

-   ID: 28

-   英文原名: Fog Visibility

-   Controls visibility of a unit through the fog of war

    | 标识                |  值 |
    | :------------------ | --: |
    | Not Visible         |   0 |
    | Always Visible      |   1 |
    | Visible If Alive    |   2 |
    | Inverted Visibility |   3 |
    | Check Doppelganger  |   4 |

## 29. Occlusion Mode { #29 }

-   ID: 29

-   英文原名: Occlusion Mode

-   This is a combinable bit field. Controls the outlines of units as seen through other units

    | 标识                                                                               |  值 |
    | :--------------------------------------------------------------------------------- | --: |
    | No outline                                                                         |   0 |
    | Display outline when behind other units that have flag 2                           |   1 |
    | Other units' outlines are rendered when they are behind this unit                  |   2 |
    | Display outline on this unit's foundation when behind other units that have flag 2 |   4 |

## 30. Garrison Type { #30 }

-   ID: 30

-   英文原名: Garrison Type

-   This is a combinable bit field. Controls which units are able to garrison in a building. A unit needs to have the garrison in building task to be able to garrison in a building to begin with

    | 标识      |  值 |
    | :-------- | --: |
    | Villagers |   1 |
    | Infantry  |   2 |
    | Cavalry   |   4 |
    | Monks     |   8 |
    | Herdables |  16 |
    | Siege     |  32 |
    | Ships     |  64 |

## 32. Unit Size Z { #32 }

-   ID: 32

-   英文原名: Unit Size Z

-   This determines the z-size of the unit's collision hitbox (height of the unit)

## 40. Hero Status { #40 }

-   ID: 40

-   英文原名: Hero Status

-   This is a combinable bit field. Controls the following properties:

-   For example, if we set the hero status of a knight to 2, a monk will not be able to convert it. If we set the hero status of a militia to 4, it will regenerate HP automatically

    What if we want to enable multiple properties at once? This is achieved by adding the flag values for those properties together and setting the hero status to that value. For example, if we want to make a paladin both unconvertable and regenerate HP automatically, we can set its hero status to 2+4 = 6. This means that the hero status of a unit can take on any values in the range 1-63. If you set it to any other value, it does not have any effect on the unit

    This works because notice that there is one and only one way to add different flag values together to obtain a particular value for the hero status! For example, if we have a value of 20 for the hero status of a unit, the only way to make 20 from the above flag values is to add 4 and 16. Thus, we know that the properties corresponding to the flag values 4 (self regeneration) and 16 (protected formation by default) must be enabled for that unit

    This is a consequence of the fact that every number can be represented as a unique sum of powers of two (binary numbers)

    | 标识                             |  值 |
    | :------------------------------- | --: |
    | Full Hero Status                 |   1 |
    | Cannot be Converted              |   2 |
    | Self Regeneration (30 HP/min)    |   4 |
    | Defensive Stance by Default      |   8 |
    | Protected Formation by Default   |  16 |
    | Safe Delete Confirmation         |  32 |
    | Hero Glow                        |  64 |
    | Invert All Flags (except flag 1) | 128 |

## 41. Frame Delay { #41 }

-   ID: 41

-   英文原名: Frame Delay

-   The amount of delay between the point when the attacking animation starts and the actual hit happening for military units. This is what makes Cavalry Archers annoying to micro

## 42. Train Location { #42 }

-   ID: 42

-   英文原名: Train Location

-   The ID of the unit that trains any given unit. Barracks train Militia, so the train location of a Militia is the ID of the Barracks

## 43. Train Button { #43 }

-   ID: 43

-   英文原名: Train Button

-   The button used for training any given unit. For example, Militia are trained by using the first button, hence the Button Location of Militia is 1. This number ranges from 0-15

## 44. Blast Attack Level { #44 }

-   ID: 44

-   英文原名: Blast Attack Level

-   A unit deals blast damage to **_other_** units with **_equal or higher_** [Blast Defense Level](./#45 "Jump to: Blast Defense Level") that are in its blast radius. For example, while mangonels (blast attack: 2) can damage your own units (blast defense of all player owned units is always 2), scorpions (blast attack: 3) cannot do the same

-   One of the flags 0-3 can be combined with one of the flags from 4-64 by adding the two values

    | 标识                                                                                               |  值 |
    | :------------------------------------------------------------------------------------------------- | --: |
    | damage resources, nearby allied units and tress                                                    |   0 |
    | damage trees, nearby allied units                                                                  |   1 |
    | damage nearby allied units                                                                         |   2 |
    | damage targeted unit only                                                                          |   3 |
    | Deal a fixed 5 HP of damage to nearby units                                                        |   4 |
    | Deal 50% of unit's own damage to nearby units                                                      |   8 |
    | Deal 25% of unit's own damage to nearby units                                                      |  16 |
    | Deal 33% of unit's own damage to nearby units                                                      |  32 |
    | Attenuate damage as distance from the centre of attack increases (infantry only)                   |  64 |
    | Blast damage is dealt along the direction the unit is facing only. This area is a very narrow cone | 128 |

## 45. Blast Defense Level { #45 }

-   ID: 45

-   英文原名: Blast Defense Level

-   A unit feels the blast damage from **_other_** units with **_equal or lower_** [Blast Attack Level](./#44 "Jump to: Blast Attack Level") and if it is inside the attacker's blast radius. For example, while onagers (blast attack: 1) can cut trees (blast defense 1), mangonels (blast attack: 2) cannot do the same

    | 标识                                            |  值 |
    | :---------------------------------------------- | --: |
    | damage resources, nearby allied units and tress |   0 |
    | damage trees, nearby allied units               |   1 |
    | damage nearby allied units                      |   2 |
    | damage targeted unit only                       |   3 |

## 46. Shown Attack { #46 }

-   ID: 46

-   英文原名: Shown Attack

-   The amount of attack that is displayed as a unit's attack (may not actually be the true attack)

## 47. Shown Range { #47 }

-   ID: 47

-   英文原名: Shown Range

-   The quantity that is displayed as a unit's attack ingame (may not actually be the true attack)

## 48. Shown Melee Armor { #48 }

-   ID: 48

-   英文原名: Shown Melee Armor

-   The quantity that is displayed as a unit's melee armour ingame (may not actually be the true armour)

## 49. Shown Pierce Armor { #49 }

-   ID: 49

-   英文原名: Shown Pierce Armor

-   The quantity that is displayed as a unit's pierce armour ingame (may not actually be the true armour)

## 50. Object Name ID { #50 }

-   ID: 50

-   英文原名: Object Name ID

-   The string ID to use for the name of an object. A string ID is used for refering to strings that the game recognises by default. It can be used to automatically set names by using a value that the game recognises. Trying out the value 1 on a unit and seeing what happens is left as an excersise for the reader

## 51. Short Description ID { #51 }

-   ID: 51

-   英文原名: Short Description ID

-   The string ID for the Short Description of an object. A string ID is used for refering to strings that the game recognises by default. It can be used to automatically set a Short Description by using a value that the game recognises. Trying out the value 1 on a unit and seeing what happens is left as an excersise for the reader

## 53. Terrain Restriction ID { #53 }

-   ID: 53

-   英文原名: Terrain Restriction ID

-   This number determines how a unit interacts with terrains and which terrains it can walk on

    | 标识                              |  值 |
    | :-------------------------------- | --: |
    | All                               |   0 |
    | Land And Shallows                 |   1 |
    | Beach                             |   2 |
    | Water Small Trail                 |   3 |
    | Land                              |   4 |
    | Nothing                           |   5 |
    | Water No Trail                    |   6 |
    | All Except Water                  |   7 |
    | Land Except Farm                  |   8 |
    | Nothing 2                         |   9 |
    | Land And Beach                    |  10 |
    | Land Except Farm 2                |  11 |
    | All Except Water Bridge Cannon    |  12 |
    | Water Medium Trail                |  13 |
    | All Except Water Bridge Arrow     |  14 |
    | Water Large Trail                 |  15 |
    | Grass And Beach                   |  16 |
    | Water And Bridge Except Beach     |  17 |
    | All Except Water Bridge Spear     |  18 |
    | Only Water And Ice                |  19 |
    | All Except Water Wheel            |  20 |
    | Shallow Water                     |  21 |
    | All Dart                          |  22 |
    | All Arrow Fire                    |  23 |
    | All Cannon Fire                   |  24 |
    | All Spear Fire                    |  25 |
    | All Dart Fire                     |  26 |
    | All Laser                         |  27 |
    | All Except Water Cavalry          |  28 |
    | All Except Water Packet Trebuchet |  29 |
    | Water Smallest Trail              |  30 |

## 54. Unit Trait { #54 }

-   ID: 54

-   英文原名: Unit Trait

-   This is a combinable bit field. Controls the following properties:

-   See Also:

    [Trait Piece](./#56)

    | 标识                                |  值 |
    | :---------------------------------- | --: |
    | Garrison Unit                       |   1 |
    | Ship Unit                           |   2 |
    | Build Another Building (Serjeants)  |   4 |
    | Transform Into Another Unit (Ratha) |   8 |
    | Auto Scout Unit                     |  16 |

## 56. Trait Piece { #56 }

-   ID: 56

-   英文原名: Trait Piece

-   This can be set to the ID of a unit that is used along with some of the Unit Traits

-   See Also:

    [Unit Trait](./#54)

    | 标识           |  值 |
    | :------------- | --: |
    | Unused         |   1 |
    | Unused         |   2 |
    | Build Unit     |   4 |
    | Transform Unit |   8 |
    | Unused         |  16 |

## 57. Dead Unit ID { #57 }

-   ID: 57

-   英文原名: Dead Unit ID

-   This is the ID of the unit to spawn after the current unit dies. This is whats used to make the dismounted konniks possible

## 58. Hotkey ID { #58 }

-   ID: 58

-   英文原名: Hotkey ID

-   This number determines which hotkey is assigned to a unit

## 59. Maximum Charge { #59 }

-   ID: 59

-   英文原名: Maximum Charge

-   The maximum amount of charge that a unit can hold

## 60. Recharge Rate { #60 }

-   ID: 60

-   英文原名: Recharge Rate

-   The rate of charge regeneration per second

## 61. Charge Event { #61 }

-   ID: 61

-   英文原名: Charge Event

-   This action depletes the unit's charge

    | 标识                                                                   |  值 |
    | :--------------------------------------------------------------------- | --: |
    | If charge type is set to `1`, `2` or `3`, depletes charge on attacking |   1 |

## 62. Charge Type { #62 }

-   ID: 62

-   英文原名: Charge Type

-   The type of charge that a unit holds

    | 标识               |  值 |
    | :----------------- | --: |
    | Attack charge      |   1 |
    | ??? charge         |   2 |
    | Area attack charge |   3 |
    | Agility charge     |   4 |

## 63. Combat Ability { #63 }

-   ID: 63

-   英文原名: Combat Ability

-   Combinable bit field. Controls several attacking behaviours for units

    | 标识                                                 |  值 |
    | :--------------------------------------------------- | --: |
    | Ignore melee and pierce armours of the targeted unit |   1 |
    | Resist armour-ignoring attacks                       |   2 |
    | Damage the targeted unit's armor (Obuch)             |   4 |
    | Attack ground ability                                |   8 |
    | Bulk volley release (kipchak/siege weapons)          |  16 |

## 64. Attack Dispersion { #64 }

-   ID: 64

-   英文原名: Attack Dispersion

-   Half of the radius from the target unit in which missed projectiles fired by this unit can land in

## 65. Secondary Projectile Unit { #65 }

-   ID: 65

-   英文原名: Secondary Projectile Unit

-   This is the ID of the secondary projectile that a unit fires (Chu Ko Nu)

## 66. Blood Unit { #66 }

-   ID: 66

-   英文原名: Blood Unit

-   This is the ID of a secondary unit to spawn after the current unit dies. This could potentially be used along with dead unit ID to spawn two units after a single unit dies

## 67. Projectile Hit Mode { #67 }

-   ID: 67

-   英文原名: Projectile Hit Mode

-   Controls how a projectile collides with units in the path of its target. Currently changing this through XS has no effect

    | 标识                                                                 |  值 |
    | :------------------------------------------------------------------- | --: |
    | Collide only with the targeted unit                                  |   0 |
    | Collide with any damage-able units in the path to the targetted unit |   1 |
    | Collide with any unit in the path to the targetted unit              |   2 |

## 68. Projectile Vanish Mode { #68 }

-   ID: 68

-   英文原名: Projectile Vanish Mode

-   Controls if a projectile passes through or disappears on impact. Currently changing this through XS has no effect

    | 标识                      |  值 |
    | :------------------------ | --: |
    | Disappear on first impact |   0 |
    | Pass through              |   1 |

## 69. Projectile Arc { #69 }

-   ID: 69

-   英文原名: Projectile Arc

-   Controls the maximum height of the fired projectile

## 100. Resource Costs { #100 }

-   ID: 100

-   英文原名: Resource Costs

-   Refers to the first resource cost of a unit. Refer to A.G.E. to see which resource cost that is

## 101. Train Time { #101 }

-   ID: 101

-   英文原名: Train Time

-   This is the amount of time it takes to create a unit

## 102. Total Missiles { #102 }

-   ID: 102

-   英文原名: Total Missiles

-   This is the number of projectiles a unit fires. The Chu Ko Nu fires 3 and the Elite Chu Ko Nu fires 5

## 103. Food Costs { #103 }

-   ID: 103

-   英文原名: Food Costs

-   The food cost of a unit

## 104. Wood Costs { #104 }

-   ID: 104

-   英文原名: Wood Costs

-   The wood cost of a unit

## 105. Gold Costs { #105 }

-   ID: 105

-   英文原名: Gold Costs

-   The gold cost of a unit

## 106. Stone Costs { #106 }

-   ID: 106

-   英文原名: Stone Costs

-   The stone cost of a unit

## 107. Max Total Missiles { #107 }

-   ID: 107

-   英文原名: Max Total Missiles

-   The maximum number of projectiles a unit can fire when other units are garrisoned inside of it. A castle fires 5 projectiles by default but can fire more if units are garrisoned inside it. This attribute controls the maximum number of those

## 108. Garrison Heal Rate { #108 }

-   ID: 108

-   英文原名: Garrison Heal Rate

-   The rate measured in HP/s at which garissoned units are healed inside a given building

## 109. Regeneration Rate { #109 }

-   ID: 109

-   英文原名: Regeneration Rate

-   The rate measured in HP/minute at which units heal themselves. This value is overridden to 30 HP/minute if the flag for Self Regeneration is set in the [Hero Status](./#40 "Jump to: 26. Hero Status") of a unit

## 110. Population { #110 }

-   ID: 110

-   英文原名: Population

-   Modifies the population headroom storage of a unit. Negative values = require population (units), positive values = give population (houses). This is not a real attribute that exists in A.G.E., just seems like a way to edit the population heardroom provided by a unit
