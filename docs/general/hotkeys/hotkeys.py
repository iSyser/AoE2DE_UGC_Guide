import functools
import json
from sys import winver

import ugcdoc

# As the number of languages increases,
# this section can be moved to the corresponding file
md_dict = {None: 'en'}

md_dict['en'] = {'head': """# Hotkeys

_Written by: Alian713_

---

## 1. What is a hotkey?

A hotkey is a key or combination of keys that can be pressed to allow for quick execution of certain tasks. For example, pressing `Ctrl + 1` allows you to set a control group of units that you can then quickly select by pressing `1`.

The standard way to bind hotkeys to units and actions is to assign them through the ingame menu. While this works great for the standard ingame units, what if you want to give hotkeys to a unit when you are making a custom scenario, a random map with custom units or a mod?

## 2. About Hotkey IDs

Every standard unit in the game has a "Hotkey ID" that tells the game which key is needed to be pressed for the hotkey. you can check A.G.E. to see what the value for the Hotkey ID for each unit is. If you do not know what A.G.E. is, refer to the [Data Mods]("Jump to: Data Mods NON EXISTENT") section of this guide.

Setting one unit's hotkey ID to the same value as another unit will make the hotkey for the first unit the same as the second unit. For example, if you set the hotkey ID for militia to the same value as villagers, then the hotkey for creating militia will become the same as the one used for creating villagers.

Similarly, if you set one building's hotkey ID to the same value as another building, it will make the hotkey for the first building the same as the second building. For example, if you set the hotkey ID for stables to the same value as houses, then the hotkey for creating stables will become the same as the one used for creating houses.

Note that the above hotkeys can be different for different players.

However, if you set a unit's hotkey ID to a building's hotkey ID (or vice versa) it won't actually assign the expected hotkey to the unit. In this case the hotkey assigned to the unit or building is a different, **fixed** key, **which does not change for different players**. For example, setting a villager's hotkey ID to the same as a house will **always** make the villager use `Q` as its hotkeys.

How do we know which key this is going to be? This key is determined by the first character of the string (the text within quotes) corresponding to the hotkey ID in the file called `key-value-strings-utf8.txt` located in this directory:

```
PATH_TO_THE_FOLDER/AoE2DE/resources/en/strings/key-value/
```

If we search for the value `16344` in this file, which is the hotkey ID of the house, it can be seen that the string corresponding to it is `"Q"` and its first character is `Q` which is the hotkey that is used in this case.

In fact, we can actually use any number from this file as a hotkey ID and the hotkey set by it is determined by the first character of the corresponding string. For example, the value `15188` has the string `"Gold Score"` corresponding to it, and its first character is `G`. This means the value `15188` sets the key `G` as the hotkey.

Sometimes, the numbers in this file will have strings whoes starting characters are special characters. In this case, a different hotkey (this remains the same for a particular starting character) is used. The table below contains every unique starting character present in the strings file and the key that it corresponds to.

## 3. First Character of String ID to Hotkey Reference

| **String ID** | **Starting Character** | **Hotkey Key** |
| :-----------: | :--------------------: | :------------: |
""", "rear": """
## 4. Credits

Thanks to MrKirby and happy leaves happy life for helping in figuring out how these IDs work exactly!
"""}

md_dict['zh'] = {'head': """# 热键

_作者：Alian713_

---

## 1. 热键是什么？

热键是一个按键或按键组合，按下后可以快速执行某些任务。例如，按 `Ctrl + 1` 可以为当前选中单位编队，此后可以通过按 `1` 快速选择这些单位。

将热键绑定到单位和操作的标准方法是通过游戏内菜单进行分配。虽然这对标准游戏内单位有用，但如果您想在制作自定义场景、带有自定义单位的随机地图或模组时为某个单位提供热键，应该怎么做呢？

## 2. 关于热键 ID

游戏中的每个标准单位都有一个“热键 ID”，它告诉游戏激活热键需要按下哪个键。你可以通过 A.G.E. 查询每个单位的热键 ID 的值是多少。如果您不知道 A.G.E. 是什么，请参阅本手册的[数据模组]("跳转至：数据模组 NON EXISTENT")部分。

将一个单位的热键 ID 设置为与另一个单位相同的值将使两者的热键相同。例如，将民兵的热键 ID 设置为与村民相同的值，则创建民兵的热键将与创建村民的相同。

同样地，将一个建筑物的热键 ID 设置为与另一个建筑物相同的值，则第一个建筑物的热键将与第二个建筑物的相同。例如，将马厩的热键 ID 设置为与房屋相同的值，则创建马厩的热键将与创建房屋的相同。

请注意，上述热键对于不同的玩家可能有所不同。

然而，如果您将单位的热键 ID 设置为建筑物的热键 ID（反之亦然），则实际上不会将预期的热键分配给该单位。在这种情况下，分配给单位或建筑物的热键是不同的**固定**键，**不会因不同的玩家而改变**。例如，将村民的热键 ID 设置为与房屋相同将**始终**使村民使用 `Q` 作为其热键。

我们如何知道这些是什么键？在文件 `key-value-strings-utf8.txt` 中，与热键 ID 对应的（引号内的）字符串的第一个字符决定了该键，该文件位于以下目录：

```
文件夹路径/AoE2DE/resources/zh/strings/key-value/
```

如果我们在这个文件中查找值 `16344`，即房屋的热键 ID，可以看到它对应的字符串是 `"Q"`，其中的第一个字符 `Q` 是本例中所使用的热键。

其实，我们可以使用该文件中的任何数字作为热键 ID，并且它设置的热键由对应字符串的第一个字符决定。例如，值 `15228` 有对应的字符串 `AI 玩家击杀村民数`，其第一个字符是 `A`。这意味着值 `15228` 将键 `A` 设置为热键。

有时，该文件中的数字对应的字符串会以特殊字符开头。在这种情况下，将使用不同的热键（但相同的首字符仍然对应相同的键）。下表包含字符串（英文版）文件中存在的每个唯一起始字符及其对应的键。

## 3. 字符串 ID 首字符转热键参考

| **字符串 ID** | **首字符** | **热键** |
| :----------: | :-------: | :-----: |
""", "rear": """
## 4. 致谢

感谢 MrKirby 和 happy leaves happy life 帮助我们弄清楚这些 ID 的确切工作方式！
"""}


def build_doc(lang: str = None):
    def_lang = md_dict[None]
    lang = lang or def_lang

    # Hotkeys don't need to be translated yet
    keys = ugcdoc.load_json_dict("hotkeys", def_lang, def_lang)

    out = md_dict[lang]['head']

    for key in keys[def_lang]:
        k = functools.partial(ugcdoc.get_key, dict_set=keys, parent_key=key, lang=lang)
        if not k('char'):
            continue

        out += f"""|{f"{k('string_id')}":15s}|"""
        out += f"{key:24s}"
        out += f"|{k('char').upper().replace('_', ' '):16s}|\n"

    out += md_dict[lang]['rear']
    output_file = "index"
    output_file = f"{output_file}.md" if lang == def_lang else f"{output_file}.{lang}.md"
    with open(output_file, "w") as file:
        file.write(out)


build_doc()
build_doc('zh')
