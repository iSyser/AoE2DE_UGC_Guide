# 护甲和攻击类型系统：帝国时代 II 的支柱

_作者：Alian713_

---

## 1. 用途

您有没有想过 AoE2 中的附加伤害是如何运作的？戟兵如何在对抗骑兵时获得 +32 伤害？为什么精锐甲胄骑兵只受到戟兵的 +16 伤害而不是全部 32 伤害？最后，**您**如何为自己的单位提供附加伤害或针对附加伤害的护甲？让我们通过了解 AoE2 的护甲和攻击类型系统来找到这些问题的答案。

## 2. 作为地图制作者，为什么需要了解这一点？

了解伤害计算的工作原理以及如何计算一个单位对另一个单位的攻击，对制作模组和使用触发器中的某些效果至关重要。除此之外，了解游戏幕后如何计算伤害本身就很有趣。

## 3. 类型系统

### 3.1. 概述

游戏中的每个单位都有两个基本属性，`攻击类型` 列表和 `护甲类型` 列表。通常也统一称为 `伤害类型`，用于计算每个单位对任何其他单位造成的伤害。游戏中共有 40 个伤害类型，其中“基础远程”和“基础近战”两个伤害类型是最常见的，因为它们是唯一在游戏中实际显示的伤害类型。我们还需要了解第 3 个属性，即 `基础护甲`，几乎每个单位都是设置为 10000。

### 3.2. 伤害类型列表

以下是游戏中存在的所有伤害类型及其 ID（请注意，护甲类型与攻击类型具有相同的名称和 ID，当您阅读下面提供的说明的时候，就会清楚其原因）：

|            **类名**            | **ID** |
| :----------------------------: | :----: |
|              奇观              |   0    |
|              步兵              |   1    |
|         龟甲船 & 楼船          |   2    |
|            基础远程            |   3    |
|            基础近战            |   4    |
|            战象单位            |   5    |
|             未使用             |   6    |
|             未使用             |   7    |
|              骑兵              |   8    |
|             未使用             |   9    |
|             未使用             |   10   |
|      所有建筑 (除了港口)       |   11   |
|             未使用             |   12   |
|       石墙 & 石门 & 石塔       |   13   |
|           攻击性动物           |   14   |
|              射手              |   15   |
| 船 & 破坏者 (非洲王朝前是骆驼) |   16   |
|      冲车 & 巨投 & 攻城塔      |   17   |
|              树木              |   18   |
|            独特单位            |   19   |
|            攻城武器            |   20   |
|            标准建筑            |   21   |
|        所有墙 & 所有门         |   22   |
|            火药单位            |   23   |
|              野猪              |   24   |
|              僧侣              |   25   |
|              堡垒              |   26   |
|             长矛兵             |   27   |
|             骑射手             |   28   |
|             鹰勇士             |   29   |
|       骆驼 (非洲王朝后)        |   30   |
|  未使用(曾是烈堤司的攻击类型)  |   31   |
|              佣兵              |   32   |
|          火药副抛射物          |   33   |
|              渔船              |   34   |
|            马穆鲁克            |   35   |
|          英雄 & 国王           |   36   |
|     重弩战象 & 胡斯派战车      |   37   |
|             投矛手             |   38   |
|        弯刀勇士 & 骆驼         |   39   |

乍一看，上表这些东西似乎令人畏惧，但当我们浏览下面给出的两个示例时，一切都会变得更加清晰！
我们将使用长戟兵与战象的案例来解释该系统的工作原理，不过该方法是适用于任何两个互相战斗的单位的通用方法

### 3.3. 数学解释

长戟兵攻击战象的案例：

<div id="cs1"></div>

| **长戟兵攻击类型** | **值** |     | **战象护甲类型** | **值** |
| :----------------- | :----: | :-: | :--------------- | :----: |
| -                  |   -    |     | 3 (基础远程)     |   2    |
| 4 (基础近战)       |   6    |     | 4 (基础近战)     |   1    |
| 5 (战象单位)       |   28   |     | 5 (战象单位)     |   0    |
| 8 (骑兵)           |   32   |     | 8 (骑兵)         |   0    |
| 16 (船 & 破坏者)   |   17   |     | -                |   -    |
| -                  |   -    |     | 19 (独特单位)    |   0    |
| 21 (标准建筑)      |   1    |     | -                |   -    |
| 29 (鹰勇士)        |   1    |     | -                |   -    |
| 30 (骆驼)          |   26   |     | -                |   -    |
| -                  |   -    |     | 31 (未使用)      |   0    |
| 34 (渔船)          |   17   |     | -                |   -    |
| 35 (马穆鲁克)      |   11   |     | -                |   -    |

在上表中您可以看到长戟兵的所有攻击类型和战象的护甲类别。

为了计算这位未升级的长戟兵对未升级的战象造成的总伤害，我们执行以下步骤：

1.  确定攻击单位的攻击类型列表和防御单位的护甲类型列表所共有的伤害类型。

    共同的伤害类型是（这些也在上表中突出显示）：

    -   `基础近战 (4)`
    -   `战象单位 (5)`
    -   `骑兵 (8)`

    其中战象的为护甲类型，戟兵的为攻击类型。

2.  对于每个共同的伤害类型，从攻击单位的攻击值中减去防御单位的护甲值。如果得到负值，则取 0。

    设 $\color{yellow} Ar_i$ 是战象的类型 ID 为 $i$ 的护甲值。例如，$\color{yellow} Ar_{19}$ 指的是战象的 `独特单位` 护甲值；

    而 $\color{#bfe3b4} At_i$ 是戟兵的类型 ID 为 $i$ 的攻击值。例如，$\color{#bfe3b4} At_{16}$ 指长戟兵的 `船 & 破坏者` 攻击值。

    $\color{yellow} Ba$ 是防御单位——战象的基础护甲值。

    （请注意，游戏中每个护甲类型的 ID 可以在主题 3.2. 下的表格中找到）

    近战类伤害：

    $$
    \begin{aligned}\text{dmg}_4
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} At_4 - \color{yellow} Ar_4,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} 6    - \color{yellow} 1   ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} 5                         ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961} 5
    \end{aligned}
    $$

    战象单位类伤害：

    $$
    \begin{aligned}\text{dmg}_5
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} At_5 - \color{yellow} Ar_5,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} 28   - \color{yellow} 0   ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} 28                        ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961} 28
    \end{aligned}
    $$

    骑兵类伤害：

    $$
    \begin{aligned}\text{dmg}_8
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} Ar_8 - \color{yellow} At_8,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} 32   - \color{yellow} 0   ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} 32                        ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961} 32
    \end{aligned}
    $$

3.  对于攻击单位的每个攻击类型，如果防御单位没有对应的护甲类型，那么我们使用基础护甲值来计算攻击力。

    船 & 破坏者类伤害：

    $$
    \begin{aligned}\text{dmg}_{16}
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} At_{16} - \color{yellow} Ba  ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} 17      - \color{yellow} 10000,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4}         - 983                ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961} 0
    \end{aligned}
    $$

    标准建筑类：

    $$
    \begin{aligned}\text{dmg}_{21}
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} At_{21} - \color{yellow} Ba  ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} 1       - \color{yellow} 10000,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4}         - 999                ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961} 0
    \end{aligned}
    $$

    鹰勇士类：

    $$
    \begin{aligned}\text{dmg}_{29}
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} At_{29} - \color{yellow} Ba  ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} 1       - \color{yellow} 10000,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4}         - 999                ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961} 0
    \end{aligned}
    $$

    骆驼类：

    $$
    \begin{aligned}\text{dmg}_{30}
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} At_{30} - \color{yellow} Ba  ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} 26      - \color{yellow} 10000,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4}         - 974                ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961} 0
    \end{aligned}
    $$

    渔船类：

    $$
    \begin{aligned}\text{dmg}_{34}
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} At_{34} - \color{yellow} Ba  ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} 17      - \color{yellow} 10000,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4}         - 983                ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961} 0
    \end{aligned}
    $$

    马穆鲁克类:

    $$
    \begin{aligned}\text{dmg}_{35}
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} At_{35} - \color{yellow} Ba  ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4} 11      - \color{yellow} 10000,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961}\text{max}( \color{#bfe3b4}         - 989                ,\; \color{white} 0 \color{#ff6961})\\
    &= \color{#ff6961} 0
    \end{aligned}
    $$

    技巧：请记住，`基础护甲` 的值几乎总是 10000，因此除非该单位的某种类型的攻击力超过 10000，否则它们实际上对造成的伤害总量没有影响！在这种情况下，则可以跳过上述带有基础护甲的计算。

4.  对以上的所有计算结果求和，若为 0，取 1。

    $$
    \begin{aligned}\text{dmg}
    &= \color{#add8e6}\text{max}( && \hspace{-2em}\color{#bfe3b4}\text{dmg}_4 +
                                                                 \text{dmg}_5 +
                                                                 \text{dmg}_8 +
                                                                 \text{dmg}_{16} +
                                                                 \text{dmg}_{21} +\\
    &                             && \hspace{-2em}\color{#bfe3b4}\text{dmg}_{29} +
                                                                 \text{dmg}_{30} +
                                                                 \text{dmg}_{34} +
                                                                 \text{dmg}_{35},\;
                                     \color{#bfe3b4} 1 \color{#add8e6})\\
    &= \color{#add8e6}\text{max}(&&\hspace{-2em}\color{#bfe3b4} 5+28+32+0,\; \color{#bfe3b4} 1 \color{#add8e6})\\
    &= \color{#add8e6}\text{max}(&&\hspace{-2em}\color{#bfe3b4} 65,\; \color{#bfe3b4} 1 \color{#add8e6})\\
    &= 65
    \end{aligned}
    $$

5.  这样得到的数值就是长戟兵对战象造成的伤害。

任意两个单位之间的伤害计算的通用公式是：

设 $\color{#a66fb5} D$ 是攻击单位的所有攻击类型的集合，

$\color{#bfe3b4} At_i$ 是攻击单位类型 ID 为 $i$ 的攻击力。例如，$\color{#bfe3b4} At_1$ 指的是该单位的类型为 `步兵` 的攻击力。

$\color{yellow} Ar_i$ 是防御单位类型 ID 为 $i$ 的护甲值。例如，$\color{yellow} Ar_{19}$ 指的是防御单位的类型为 `独特单位` 的护甲。如果防御单位不存在对应护甲类型，则在这种情况下使用基础护甲值！

（请注意，游戏中每个护甲类型的 ID 可以在主题 3.2. 下的表格中找到）

则：

$$
\text{dmg} =  \color{#ff6961} \text{max}( \color{#a66fb5} \sum\limits_{\forall \; i \; \in D}^{}
                               \color{#add8e6}\text{max}( \color{#bfe3b4} At_i-\color{yellow} Ar_i, \; \color{white} 0 \color{#add8e6}), \;
                               \color{white} 1 \color{#ff6961})
$$

注：$\color{#a66fb5} \sum\limits_{\forall \; i \; \in D}^{}$ 的含义是，对所有属于 $D$ 的 $i$ 求某些和

### 3.4. 代码解释

战象攻击长戟兵的案例：

<div id="cs2"></div>

| **战象攻击类型**        | **值** |     | **长戟兵护甲类型** | **值** |
| :---------------------- | :----: | :-: | :----------------- | :----: |
| -                       |   -    |     | 1 (步兵)           |   0    |
| -                       |   -    |     | 3 (基础远程)       |   0    |
| 4 (基础近战)            |   15   |     | 4 (基础近战)       |   0    |
| 11 (所有建筑)           |   7    |     | -                  |   -    |
| 13 (石墙 & 石门 & 石塔) |   7    |     | -                  |   -    |
| 15 (射手)               |   0    |     | -                  |   -    |
| 21 (标准建筑)           |   0    |     | -                  |   -    |
| -                       |   -    |     | 27 (长矛兵)        |   0    |
| -                       |   -    |     | 31 (未使用)        |   0    |
| 38 (投矛手)             |   0    |     | -                  |   -    |
| 39 (弯刀勇士 & 骆驼)    |   -3   |     | -                  |   -    |

在上表中您可以看到战象的所有攻击类型和长戟兵的护甲类别。

为了计算这头未升级的战象对未升级的长戟兵造成的总伤害，我们执行以下步骤：

1. 确定攻击单位的攻击类型列表和防御单位的护甲类型列表所共有的伤害类型。
2. 对于每个共同的伤害类型，从攻击单位的攻击值中减去防御单位的护甲值。如果得到负值，则取 0。
3. 对于攻击单位的每个攻击类型，如果防御单位没有对应的护甲类型，那么我们使用基础护甲值来计算攻击力。
4. 对以上的所有计算结果求和，若为 0，取 1。
5. 这样得到的数值就是战象对长戟兵造成的伤害。

唯一共同的伤害类型是 `基础近战 (4)`（在上表中突出显示）

这意味着战象对戟兵造成的伤害简单地由 $\text{dmg} = 15 - 0 = 15$ 给出（这里没有展示基础护甲的计算，因为没有攻击力大于 10000 的攻击类型来对抗基础护甲）

```py
damage = 0

# 1. 对于攻击单位拥有的每个 attack_class
for attack_class, attack in attacker.attack_classes:
    used_armour = target.base_armour # 几乎总是 10000
    if attack_class in targer.armour_classes:
        used_armour = target.armour_classes[attack_class]

    # 2. 计算攻击者的攻击力与目标的护甲值之间的差值。
    # 如果差值为负，则取 0。将此值添加到伤害中
    damage = damage + max(attack - used_armour, 0)

# 若总伤害小于 1，取 1。
damage = max(damage, 1)

```

游戏中的每个单位都具有 `基础远程 (3)`、`基础近战 (4)` 和 `未使用 (31)` 伤害类型。

游戏中的每个独特单位都具有 `独特单位 (19)` 护甲类型。（你能想到这个护甲类型用在哪里吗？提示：哪个单位对所有独特单位造成附加伤害？）

通过这种方式，伤害类型决定哪些单位对其他单位造成附加伤害

### 3.5. 解答问题

完成这些之后，您现在能想到指南开头提出的问题的答案吗？

Q1. 为什么精锐甲胄骑兵只受到戟兵的 +16 伤害而不是全部 32 伤害？

Q2. 如何为特定单位提供附加伤害或附加伤害抗性？

在继续阅读答案之前，请尝试思考如何实现这些附加伤害。

A1. 精锐甲胄骑兵在 `骑兵 (8)` 护甲类型上有 16 点护甲，这是戟兵对普通骑兵附加 32 点伤害使用的 `攻击类型`。

A2. 未使用的伤害类型可用于此目的。对该单位添加某个未使用的类型攻击力，并对目标单位在同一未使用的类型上设置 0 护甲，将产生该单位对目标单位造成附加伤害的效果。

### 3.6. 西西里的降低 33% 附加伤害

除了 `基础远程 (3)`、`基础近战 (4)` 和 `未使用 (31)` 之外的所有类型的伤害都会在乘以 $(1 - 0.33)$ 后才加和到西西里单位受到的总伤害中。这个附加伤害抗性属性由单位的[附加伤害抗性](../attributes/#24 "跳转至：游戏机制 > 属性 > 附加伤害抗性")属性控制（对，每个单位都可以有不同的值）。
