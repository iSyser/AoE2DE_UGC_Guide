# Hotkeys

_Written by: Alian713_

---

## 1. What is a hotkey?

A hotkey is a key or combination of keys that can be pressed to allow for quick execution of certain tasks. For example, pressing ++ctrl+1++ allows you to set a control group of units that you can then quickly select by pressing ++1++.

The standard way to bind hotkeys to units and actions is to assign them through the ingame menu. While this works great for the standard ingame units, what if you want to give hotkeys to a unit when you are making a custom scenario, a random map with custom units or a mod?

## 2. About Hotkey IDs

Every standard unit in the game has a "Hotkey ID" that tells the game which key is needed to be pressed for the hotkey. you can check A.G.E. to see what the value for the Hotkey ID for each unit is. If you do not know what A.G.E. is, refer to the [Data Mods]("Jump to: Data Mods NON EXISTENT") section of this guide.

Setting one unit's hotkey ID to the same value as another unit will make the hotkey for the first unit the same as the second unit. For example, if you set the hotkey ID for militia to the same value as villagers, then the hotkey for creating militia will become the same as the one used for creating villagers.

Similarly, if you set one building's hotkey ID to the same value as another building, it will make the hotkey for the first building the same as the second building. For example, if you set the hotkey ID for stables to the same value as houses, then the hotkey for creating stables will become the same as the one used for creating houses.

Note that the above hotkeys can be different for different players.

However, if you set a unit's hotkey ID to a building's hotkey ID (or vice versa) it won't actually assign the expected hotkey to the unit. In this case the hotkey assigned to the unit or building is a different, **fixed** key, **which does not change for different players**. For example, setting a villager's hotkey ID to the same as a house will **always** make the villager use ++q++ as its hotkeys.

How do we know which key this is going to be? This key is determined by the first character of the string (the text within quotes) corresponding to the hotkey ID in the file called `key-value-strings-utf8.txt` located in this directory:

```
PATH_TO_THE_FOLDER/AoE2DE/resources/en/strings/key-value/
```

If we search for the value `16344` in this file, which is the hotkey ID of the house, it can be seen that the string corresponding to it is `"Q"` and its first character is `Q` which is the hotkey that is used in this case.

In fact, we can actually use any number from this file as a hotkey ID and the hotkey set by it is determined by the first character of the corresponding string. For example, the value `15188` has the string `"Gold Score"` corresponding to it, and its first character is `G`. This means the value `15188` sets the key ++g++ as the hotkey.

Sometimes, the numbers in this file will have strings whoes starting characters are special characters. In this case, a different hotkey (this remains the same for a particular starting character) is used. The table below contains every unique starting character present in the strings file and the key that it corresponds to.

## 3. First Character of String ID to Hotkey Reference

| **String ID** | **Starting Character** |  **Hotkey Key**  |
| :-----------: | :--------------------: | :--------------: |
|     10101     |                        |    ++space++     |
|     15000     |           !            |   ++page-up++    |
|     2312      |           %            |  ++arrow-left++  |
|     19707     |           '            | ++arrow-right++  |
|     19731     |           (            |  ++arrow-down++  |
|     9025      |           -            |    ++insert++    |
|     19602     |           .            |    ++delete++    |
|      99       |           0            |      ++0++       |
|      98       |           1            |      ++1++       |
|     10360     |           2            |      ++2++       |
|     9786      |           3            |      ++3++       |
|     10362     |           4            |      ++4++       |
|     9785      |           5            |      ++5++       |
|      213      |           6            |      ++6++       |
|     8828      |           7            |      ++7++       |
|     9448      |           8            |      ++8++       |
|     9783      |           9            |      ++9++       |
|     1001      |           A            |      ++a++       |
|     1005      |           B            |      ++b++       |
|     1201      |           C            |      ++c++       |
|     1151      |           D            |      ++d++       |
|     1007      |           E            |      ++e++       |
|     4137      |           F            |      ++f++       |
|     2012      |           G            |      ++g++       |
|     2407      |           H            |      ++h++       |
|     1212      |           I            |      ++i++       |
|     1222      |           J            |      ++j++       |
|     4141      |           K            |      ++k++       |
|     1101      |           L            |      ++l++       |
|     1006      |           M            |      ++m++       |
|     3001      |           N            |      ++n++       |
|      214      |           O            |      ++o++       |
|     1210      |           P            |      ++p++       |
|     4169      |           Q            |      ++q++       |
|     1200      |           R            |      ++r++       |
|     1102      |           S            |      ++s++       |
|     2016      |           T            |      ++t++       |
|     1205      |           U            |      ++u++       |
|     1150      |           V            |      ++v++       |
|     1008      |           W            |      ++w++       |
|     1002      |           X            |      ++x++       |
|     2008      |           Y            |      ++y++       |
|     4174      |           Z            |      ++z++       |
|     19704     |           ]            | ++context-menu++ |
|     19721     |           `            |     ++num0++     |
|     4563      |           a            |     ++num1++     |
|     19499     |           d            |     ++num4++     |
|     5558      |           e            |     ++num5++     |
|     10069     |           g            |     ++num7++     |
|     1011      |           h            |     ++num8++     |
|     20123     |           n            |  ++num-delete++  |
|     9798      |           r            |      ++f3++      |
|     22019     |           s            |      ++f4++      |
|     9840      |           v            |      ++f7++      |
|     1152      |           w            |      ++f8++      |
|     10661     |           ~            |     ++f15++      |

## 4. Credits

Thanks to MrKirby and happy leaves happy life for helping in figuring out how these IDs work exactly!
