import functools

import ugcdoc

# As the number of languages increases,
# this section can be moved to the corresponding file
md_dict = {None: 'en'}

md_dict['en'] = {'head': """# Effects

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

""", "cfg": "The configurations for this effect are as follows", "trick": "Some useful tricks with this effect"}

md_dict['zh'] = {'head': """# 效果

_作者：Alian713_

---

## 1. 效果是什么？

效果是触发器的两个基本元素之一（另一个是条件）。从某种意义上说，它们本质上是“作弊”，允许您在玩游戏时更改有关游戏的信息。游戏中的所有技术都利用效果来完成它们应该做的事情。通常，一项技术几乎总是结合多种效果来实现其目的。当遇到适当的效果时，将给出技术及其使用效果的示例。可以在场景编辑器中使用的基本效果的一些示例包括：`创建单位`、`发送聊天`、`显示指南` 等。要使用效果，

1. 创建触发器
2. 为之添加效果。
3. 从效果列表中选择您想要使用的效果。
4. 根据需要配置效果的设置

让我们一一看看所有的效果及其配置：

## 2. 常用术语

如果您已经熟悉它们，请随意跳过它们

### 2.1. Bug

地图中任何未按预期工作的内容都是 Bug（错误）。

从历史上看，以原指昆虫的 “Bug” 一词代指错误，源于曾有真实的昆虫被卡在计算机中并导致计算机出现故障，当时计算机曾经有整个房间那么大。

在今天的背景下，任何事物中的 Bug 都意味着它发生故障并且无法按预期工作。

### 2.2. 调试

尝试找出故障原因并消除/修复该原因称为调试。

### 2.3. 执行

执行触发器意味着我们执行其效果。

## 3. 效果及其使用方法

""", "name": "英文原名", "cfg": "该效果的配置如下", "trick": "此效果的一些实用技巧"}


def build_doc(lang: str = None):
    def_lang = md_dict[None]
    lang = lang or def_lang
    effects = ugcdoc.load_json_dict("effects", def_lang, lang)
    effect_attrs = ugcdoc.load_json_dict("effects_attrs", def_lang, lang)

    if lang == def_lang:
        effects[def_lang] = dict(sorted(effects[def_lang].items(), key=lambda x: x[1]['name']))

    out = md_dict[lang]['head']
    for i, effect_id in enumerate(effects[def_lang], 1):
        k = functools.partial(ugcdoc.get_key, dict_set=effects, parent_key=effect_id, language=lang)

        out += f"### 3.{i}. {k('name')} {{ #{effect_id} }}\n\n"
        out += f"-   ID: {effect_id}\n\n"
        if lang != def_lang:
            out += f"-   {md_dict[lang]['name']}: {k('name', language=None)}\n\n"
        out += f"{k('desc')}\n\n"
        if attrs := k('attrs'):
            out += f"{md_dict[lang]['cfg']}:\n\n"

            j = 0
            for attr in attrs:
                k_attr = functools.partial(ugcdoc.get_key, dict_set=effect_attrs, parent_key=attr, language=lang)
                show = k_attr('show')
                if show is not None and not show:
                    continue
                j += 1
                out += f"{j}. {k_attr('display_name')}: {k_attr('desc')}\n"
            out += '\n'
        if tricks := k('tricks'):
            out += f"{md_dict[lang]['trick']}:\n\n"
            for j, trick in enumerate(tricks, 1):
                out += f"{j}. " + trick + "\n"
            out += '\n'

    out = out[:-1]
    ugcdoc.export_md_file("index", out, def_lang, lang)


build_doc()
build_doc('zh')
