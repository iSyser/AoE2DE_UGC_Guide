_作者: Alian713, 别云_

---

此页面列出了可以在场景编辑器中修改的所有单位属性及其用途。如果您知道本页上未提及的任何属性，或者属性的描述有误，请告知本指南的作者！

## 0. 生命值

-   英文原名: Hit Points

-   该属性指的是单位的生命值

## 1. 视野

-   英文原名: Line of Sight

-   这是单位可以看到自身周围的距离

## 2. 驻扎容量

-   英文原名: Garrison Capacity

-   这是可以驻扎另一些单位的数量

## 3. 单位尺寸 X

-   英文原名: Unit Size X

-   这决定了单位碰撞 hitbox 的 x 尺寸（单位的宽度）

## 4. 单位尺寸 Y

-   英文原名: Unit Size Y

-   这决定了单位碰撞 hitbox 的 y 尺寸（单位的长度）

## 5. 移动速度

-   英文原名: Movement Speed

-   这是单位的移动速度，单位：格/秒

## 6. 旋转速度

-   英文原名: Rotation Speed

-   这是可以旋转的单位的旋转速率，单位：秒/帧（在对象可以切换到下一个旋转帧之前需要等待这么多秒）。例如，为了让投石机开始攻击与朝向相反方向的建筑物，它首先需要旋转朝向到那个方向

## 8. 护甲

-   英文原名: Armor

-   这是一个单位在其任何 `护甲类型` 上拥有的护甲值。如果您不知道什么是 `护甲类型`，请参阅本指南的[伤害计算](../damage_calculation "跳转至：游戏机制 > 伤害计算")部分。请注意，通过此选项更改护甲将显示其已添加到基础护甲值中（例如：4+4）。

## 9. 

-   英文原名: Attack

-   

## 10. 

-   英文原名: Attack Reload Time

-   

## 11. 

-   英文原名: Accuracy Percent

-   

-   This accuracy is the accuracy of a unit to fire at the exact centre of its target. If the shot fired is not aimed at the exact centre of the target, it may still hit the target if its not off by too much since it can still land within the hitbox of the target, just not at the exact centre

    Thus, bigger targets are actually easier to hit, which explains why buildings are an easier target to hit for trebuchets than small units

    ![Visually Smaller](./imgs/visually_smaller.png "Targets that are farther away are visually smaller")

    In this image, you can see that shots that were fired in the red area in the 2nd scenario would've hit if the target had been closer like in the first scenario, but since the target is far away, they actually miss

    More technically, the visual angle of an object of the same size that is farther away is smaller, thus giving a smaller room for error for the shot in terms of the range of angles that will make the shot hit

    The chance of a unit getting converted by a monk is also determined by its accuracy

    If you modify an onager to have a big blast radius and give it a small accuracy, then attack a lot of units bunched together, the accuracy determines what percentage of units take damage from the blast of the onager! This is the reason why warwolf trebuchets get 100% accuracy because otherwise the blast wouldn't damage all of the units. Another interesting consequence of this is the delete trick with onagers and mangonels. This is where a mangonel is deleted immediately after it fires its shot and because a dead unit doesn't have an accuracy, it defaults to 100% and thus deals more damage to all the units in the blast radius

    Note: There are two other factors that play a role in determining the damage from the shot fired by the deleted mangonel

    1. The damage from a mangonel's shot is decreased over distance when moving outward from the centre of the blast (the targeted point). However, when the mangonel is deleted, this decrease over distance doesn't happen, and the projectile deals the full 100% damage to all the units in the blast radius!

    2. A shot that is fired from lower elevation would normally deal only 75% of its normal damage due to the elevation damage reduction. deleting a mangonel in this case also makes the damage the full 100% as if there was no elevation difference

## 12. 

-   英文原名: Max Range

-   

## 13. 

-   英文原名: Work Rate

-   

## 14. 

-   英文原名: Carry Capacity

-   

## 15. 

-   英文原名: Base Armor

-   

## 16. 

-   英文原名: Projectile Unit

-   

## 17. 

-   英文原名: Building Icon Override

-   

## 18. 

-   英文原名: Terrain Defense Bonus

-   

## 19. Projectile Smart Mode

-   英文原名: Projectile Smart Mode

-   This is a combinable bit field. Controls the following two behaviours for projectiles:

-   For example, if we set this property of the projectile used by an archer to `1`, it will have ballistics. (This is exactly what researching ballistics does in the first place). If we set this property to `2`, a missed projectile that hits another unit will deal its full damage instead of the 50% that it would normally do

    What if we want to enable both properties at once? This is achieved by adding the flag values for both of them together. Setting this property to `3` enables both effects

    | 标识 | 值 |
    | :- | -: |
    | No Ballistics | 0 | 
    | Has Ballistics | 1 | 
    | Deals full damage on missed hit | 2 | 

## 20. 

-   英文原名: Minimum Range

-   

## 21. 

-   英文原名: Amount of 1st Resource Storage

-   

## 22. 

-   英文原名: Blast Width

-   

## 23. 

-   英文原名: Search Radius

-   

## 24. 

-   英文原名: Bonus Damage Resistance

-   

## 25. 

-   英文原名: Icon ID

-   

## 26. 

-   英文原名: Amount of 2nd Resource Storage

-   

## 27. 

-   英文原名: Amount of 3rd Resource Storage

-   

## 28. Fog Visibility

-   英文原名: Fog Visibility

-   Controls visibility of a unit through the fog of war

    | 标识 | 值 |
    | :- | -: |
    | Not Visible | 0 | 
    | Always Visible | 1 | 
    | Visible If Alive | 2 | 
    | Inverted Visibility | 3 | 
    | Check Doppelganger | 4 | 

## 29. Occlusion Mode

-   英文原名: Occlusion Mode

-   This is a combinable bit field. Controls the outlines of units as seen through other units

    | 标识 | 值 |
    | :- | -: |
    | No outline | 0 | 
    | Display outline when behind other units that have flag 2 | 1 | 
    | Other units' outlines are rendered when they are behind this unit | 2 | 
    | Display outline on this unit's foundation when behind other units that have flag 2 | 4 | 

## 30. Garrison Type

-   英文原名: Garrison Type

-   This is a combinable bit field. Controls which units are able to garrison in a building. A unit needs to have the garrison in building task to be able to garrison in a building to begin with

    | 标识 | 值 |
    | :- | -: |
    | Villagers | 1 | 
    | Infantry | 2 | 
    | Cavalry | 4 | 
    | Monks | 8 | 
    | Herdables | 16 | 
    | Siege | 32 | 
    | Ships | 64 | 

## 32. 

-   英文原名: Unit Size Z

-   

## 40. Hero Status

-   英文原名: Hero Status

-   This is a combinable bit field. Controls the following properties:

-   For example, if we set the hero status of a knight to 2, a monk will not be able to convert it. If we set the hero status of a militia to 4, it will regenerate HP automatically

    What if we want to enable multiple properties at once? This is achieved by adding the flag values for those properties together and setting the hero status to that value. For example, if we want to make a paladin both unconvertable and regenerate HP automatically, we can set its hero status to 2+4 = 6. This means that the hero status of a unit can take on any values in the range 1-63. If you set it to any other value, it does not have any effect on the unit

    This works because notice that there is one and only one way to add different flag values together to obtain a particular value for the hero status! For example, if we have a value of 20 for the hero status of a unit, the only way to make 20 from the above flag values is to add 4 and 16. Thus, we know that the properties corresponding to the flag values 4 (self regeneration) and 16 (protected formation by default) must be enabled for that unit

    This is a consequence of the fact that every number can be represented as a unique sum of powers of two (binary numbers)

    | 标识 | 值 |
    | :- | -: |
    | Full Hero Status | 1 | 
    | Cannot be Converted | 2 | 
    | Self Regeneration (30 HP/min) | 4 | 
    | Defensive Stance by Default | 8 | 
    | Protected Formation by Default | 16 | 
    | Safe Delete Confirmation | 32 | 
    | Hero Glow | 64 | 
    | Invert All Flags (except flag 1) | 128 | 

## 41. 

-   英文原名: Frame Delay

-   

## 42. 

-   英文原名: Train Location

-   

## 43. 

-   英文原名: Train Button

-   

## 44. Blast Attack Level

-   英文原名: Blast Attack Level

-   A unit deals blast damage to ***other*** units with ***equal or higher*** [Blast Defense Level](./#45-blast-defense-level "Jump to: Blast Defense Level") that are in its blast radius. For example, while mangonels (blast attack: 2) can damage your own units (blast defense of all player owned units is always 2), scorpions (blast attack: 3) cannot do the same

-   One of the flags 0-3 can be combined with one of the flags from 4-64 by adding the two values

    | 标识 | 值 |
    | :- | -: |
    | damage resources, nearby allied units and tress | 0 | 
    | damage trees, nearby allied units | 1 | 
    | damage nearby allied units | 2 | 
    | damage targeted unit only | 3 | 
    | Deal a fixed 5 HP of damage to nearby units | 4 | 
    | Deal 50% of unit's own damage to nearby units | 8 | 
    | Deal 25% of unit's own damage to nearby units | 16 | 
    | Deal 33% of unit's own damage to nearby units | 32 | 
    | Attenuate damage as distance from the centre of attack increases (infantry only) | 64 | 
    | Blast damage is dealt along the direction the unit is facing only. This area is a very narrow cone | 128 | 

## 45. Blast Defense Level

-   英文原名: Blast Defense Level

-   A unit feels the blast damage from ***other*** units with ***equal or lower*** [Blast Attack Level](./#44-blast-attack-level "Jump to: Blast Attack Level") and if it is inside the attacker's blast radius. For example, while onagers (blast attack: 1) can cut trees (blast defense 1), mangonels (blast attack: 2) cannot do the same

    | 标识 | 值 |
    | :- | -: |
    | damage resources, nearby allied units and tress | 0 | 
    | damage trees, nearby allied units | 1 | 
    | damage nearby allied units | 2 | 
    | damage targeted unit only | 3 | 

## 46. 

-   英文原名: Shown Attack

-   

## 47. 

-   英文原名: Shown Range

-   

## 48. 

-   英文原名: Shown Melee Armor

-   

## 49. 

-   英文原名: Shown Pierce Armor

-   

## 50. 

-   英文原名: Object Name ID

-   

## 51. 

-   英文原名: Short Description ID

-   

## 53. Terrain Restriction ID

-   英文原名: Terrain Restriction ID

-   This number determines how a unit interacts with terrains and which terrains it can walk on

    | 标识 | 值 |
    | :- | -: |
    | All | 0 | 
    | Land And Shallows | 1 | 
    | Beach | 2 | 
    | Water Small Trail | 3 | 
    | Land | 4 | 
    | Nothing | 5 | 
    | Water No Trail | 6 | 
    | All Except Water | 7 | 
    | Land Except Farm | 8 | 
    | Nothing 2 | 9 | 
    | Land And Beach | 10 | 
    | Land Except Farm 2 | 11 | 
    | All Except Water Bridge Cannon | 12 | 
    | Water Medium Trail | 13 | 
    | All Except Water Bridge Arrow | 14 | 
    | Water Large Trail | 15 | 
    | Grass And Beach | 16 | 
    | Water And Bridge Except Beach | 17 | 
    | All Except Water Bridge Spear | 18 | 
    | Only Water And Ice | 19 | 
    | All Except Water Wheel | 20 | 
    | Shallow Water | 21 | 
    | All Dart | 22 | 
    | All Arrow Fire | 23 | 
    | All Cannon Fire | 24 | 
    | All Spear Fire | 25 | 
    | All Dart Fire | 26 | 
    | All Laser | 27 | 
    | All Except Water Cavalry | 28 | 
    | All Except Water Packet Trebuchet | 29 | 
    | Water Smallest Trail | 30 | 

## 54. Unit Trait

-   英文原名: Unit Trait

-   This is a combinable bit field. Controls the following properties:

-   See Also:

    [Trait Piece](./#56-trait-piece)

    | 标识 | 值 |
    | :- | -: |
    | Garrison Unit | 1 | 
    | Ship Unit | 2 | 
    | Build Another Building (Serjeants) | 4 | 
    | Transform Into Another Unit (Ratha) | 8 | 
    | Auto Scout Unit | 16 | 

## 56. Trait Piece

-   英文原名: Trait Piece

-   This can be set to the ID of a unit that is used along with some of the Unit Traits

-   See Also:

    [Unit Trait](./#54-unit-trait)

    | 标识 | 值 |
    | :- | -: |
    | Unused | 1 | 
    | Unused | 2 | 
    | Build Unit | 4 | 
    | Transform Unit | 8 | 
    | Unused | 16 | 

## 57. 

-   英文原名: Dead Unit ID

-   

## 58. 

-   英文原名: Hotkey ID

-   

## 59. 

-   英文原名: Maximum Charge

-   

## 60. 

-   英文原名: Recharge Rate

-   

## 61. Charge Event

-   英文原名: Charge Event

-   This action depletes the unit's charge

    | 标识 | 值 |
    | :- | -: |
    | If charge type is set to `1`, `2` or `3`, depletes charge on attacking | 1 | 

## 62. Charge Type

-   英文原名: Charge Type

-   The type of charge that a unit holds

    | 标识 | 值 |
    | :- | -: |
    | Attack charge | 1 | 
    | ??? charge | 2 | 
    | Area attack charge | 3 | 
    | Agility charge | 4 | 

## 63. Combat Ability

-   英文原名: Combat Ability

-   Combinable bit field. Controls several attacking behaviours for units

    | 标识 | 值 |
    | :- | -: |
    | Ignore melee and pierce armours of the targeted unit | 1 | 
    | Resist armour-ignoring attacks | 2 | 
    | Damage the targeted unit's armor (Obuch) | 4 | 
    | Attack ground ability | 8 | 
    | Bulk volley release (kipchak/siege weapons) | 16 | 

## 64. 

-   英文原名: Attack Dispersion

-   

## 65. 

-   英文原名: Secondary Projectile Unit

-   

## 66. 

-   英文原名: Blood Unit

-   

## 67. Projectile Hit Mode

-   英文原名: Projectile Hit Mode

-   Controls how a projectile collides with units in the path of its target. Currently changing this through XS has no effect

    | 标识 | 值 |
    | :- | -: |
    | Collide only with the targeted unit | 0 | 
    | Collide with any damage-able units in the path to the targetted unit | 1 | 
    | Collide with any unit in the path to the targetted unit | 2 | 

## 68. Projectile Vanish Mode

-   英文原名: Projectile Vanish Mode

-   Controls if a projectile passes through or disappears on impact. Currently changing this through XS has no effect

    | 标识 | 值 |
    | :- | -: |
    | Disappear on first impact | 0 | 
    | Pass through | 1 | 

## 69. 

-   英文原名: Projectile Arc

-   

## 100. 

-   英文原名: Resource Costs

-   

## 101. 

-   英文原名: Train Time

-   

## 102. 

-   英文原名: Total Missiles

-   

## 103. 

-   英文原名: Food Costs

-   

## 104. 

-   英文原名: Wood Costs

-   

## 105. 

-   英文原名: Gold Costs

-   

## 106. 

-   英文原名: Stone Costs

-   

## 107. 

-   英文原名: Max Total Missiles

-   

## 108. 

-   英文原名: Garrison Heal Rate

-   

## 109. 

-   英文原名: Regeneration Rate

-   

## 110. 

-   英文原名: Population

-   
