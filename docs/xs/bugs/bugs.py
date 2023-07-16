import functools
from datetime import date

import ugcdoc

info = {"version": "101.102.5558.0 (#71094) 9717890", "today": date.today(), "platform": "simple-steam: Steam",
        "os": ":simple-windows11: Windows 11"}

# As the number of languages increases,
# this section can be moved to the corresponding file
md_dict = {None: 'en'}

md_dict['en'] = {'head': f"""# Known Bugs And Quirks In XS Scripting

_Written by: Alian713_

---

This section is a list of known bugs, quirks and weird behaviour in XS Scripting. All the shown code can be directly copy pasted into any XS file to reproduce the bugs/effects documented.

Any new bugs discovered will be added to the list. This list will also be updated with each AoEII:DE update, removing any bugs that get fixed.

If you know of a bug that is not documented here, or if a bug listed here is actually fixed in the _indicated_ game version, reach out to the authors of this guide! Check the [About](/) page for relevant information about the authors.

The following is the author's environment at the time of writing this section.

Game Version: `{info['version']}`

Last Updated: `{info['today'].strftime('%d.%m.%Y')}`

Game Platform: {info['platform']}

OS: {info['os']}
""", "desc": "Description", "expected": "Expected Behaviour", "steps": "Reproduction Steps"}

md_dict['zh'] = {'head': f"""# 已知的 XS 脚本中的错误和怪异行为

_作者：Alian713_

---

本节列出了 XS 脚本中的已知错误、怪异行为和杂项。所有展示的代码都可以直接复制粘贴到任何 XS 文件中，以重现记录的错误/效果。

任何新发现的错误都将添加到列表中。此列表也将随着每次 AoEII:DE 更新而更新，消除任何已修复的错误。

如果您知道此处未记录的错误，或者此处列出的错误实际上已在*指定的*游戏版本中修复，请联系本指南的作者！查询[关于](/)页面以获取有关作者的相关信息。

以下是撰写本节时作者的环境。

游戏版本：`{info['version']}`

最后更新：`{info['today']}`

游戏平台：:{info['platform']}

操作系统：{info['os']}
""", "desc": "描述", "expected": "预期行为", "steps": "复现步骤"}


def build_doc(lang: str = None):
    def_lang = md_dict[None]
    lang = lang or def_lang
    ugcdoc.export_md_file("index", md_dict[lang]['head'], def_lang, lang)
    bug_set = ugcdoc.load_json_dict("bugs", def_lang, lang, True)

    for index, (category, bugs) in enumerate(bug_set[def_lang].items(), 1):
        local_category = bug_set[lang].get(category) or {}

        # 'nickname' in other languages will not be used.
        if not (title := local_category.get('nickname')):
            title = category
        title = title.title()
        out = f"# {title}\n\n"

        bug_dict: dict[dict] = {None: def_lang, def_lang: ugcdoc.json_list_2_dict((bugs['bugs']))}
        if def_lang != lang:
            bug_dict[lang] = ugcdoc.json_list_2_dict(local_category.get('bugs'))

        for i_bug, (bug_name, bug_info) in enumerate(bug_dict[def_lang].items(), 1):
            if (show := bug_info.get('show')) and not show:
                continue
            xs_code = ""
            if code_file := bug_info.get('Code File'):
                with open("./bugged/" + code_file) as file:
                    xs_code = "\n\n    ```cpp\n"
                    while code_line := file.readline():
                        if '\n' != code_line:
                            xs_code += '    ' + code_line
                    xs_code += "\n    ```\n"

            k = functools.partial(ugcdoc.get_key, dict_set=bug_dict, parent_key=bug_name, language=lang)
            if not (nick := k('nickname', default_language=lang)):
                nick = bug_name
            out += f"## {i_bug}. {nick} {{ #{i_bug} }}\n\n"
            out += f"{md_dict[lang]['desc']}: {k('desc')}\n\n"
            out += f"{md_dict[lang]['expected']}: {k('Expected Behaviour')}\n\n"
            out += f"{md_dict[lang]['steps']}:\n\n"

            all_step = ""
            for i_step, step in enumerate(k('Reproduction Steps'), 1):
                all_step += f'{i_step}. {step}\n'

            out += all_step.replace("GET_CODE", xs_code) + "\n"

        out = out[:-1]
        ugcdoc.export_md_file(ugcdoc.str2title(category), out, def_lang, lang)


build_doc()
build_doc('zh')
