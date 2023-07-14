import functools

import ugcdoc

# As the number of languages increases,
# this section can be moved to the corresponding file
md_dict = {None: 'en'}

md_dict['en'] = {'head': """---
hide:
#     - navigation
#     - toc
---

# Functions Reference

_Written by: Alian713_

""", "return_type": "Returning Type", "prototype": "Prototype", "parameters": "Parameters", "optional": "(Optional)"}

md_dict['zh'] = {'head': """---
hide:
#     - navigation
#     - toc
---

# 函数参考

_作者：Alian713_

""", "return_type": "返回类型", "prototype": "函数原型", "parameters": "参数", "optional": "(可选)"}


def build_doc(lang: str = None):
    def_lang = md_dict[None]
    lang = lang or def_lang
    fun_set = ugcdoc.load_json_dict("functions", def_lang, lang, True)

    out = md_dict[lang]['head']
    for index, category in enumerate(fun_set[def_lang], 1):

        k = functools.partial(ugcdoc.get_key, dict_set=fun_set, parent_key=category, language=lang)

        # 'nickname' in other languages will not be used.
        if not (title := k('nickname', default_language=lang)):
            title = category

        title = title.title()
        anchor = ugcdoc.str2title(category.title())
        out += f"## {index}. {title} {{ #{anchor} }}\n\n"

        func_dict = {None: def_lang,
                     def_lang: ugcdoc.json_list_2_dict(sorted(k('functions', language=None), key=lambda x: x['name']))}
        if def_lang != lang:
            func_dict[lang] = ugcdoc.json_list_2_dict(k('functions', default_language=lang))

        for i_f, func_name in enumerate(func_dict[def_lang], 1):
            fun = ugcdoc.CXsFunction(func_name, func_dict, lang)

            out += f"### {index}.{i_f}. {fun.get_name()} {{ #{fun.get_real_name()} }}\n\n"

            out += f"{md_dict[lang]['return_type']}: `#!cpp {fun.get_type()}`\n\n"
            out += f"{md_dict[lang]['prototype']}: `#!cpp {fun}`\n\n"

            if fun.have_param():
                out += md_dict[lang]['parameters'] + ":\n\n"
                for i_p, param in enumerate(fun.get_params(), 1):
                    optional = "" if param.is_required() else " " + md_dict[lang]['optional']
                    out += f"{i_p}. {optional} `#!cpp {param}`"
                    if param.have_nickname():
                        out += f"({param.get_name()})"
                    out += f": {param.get_desc()}\n"

                out += "\n"

            out += f"{fun.get_desc()}\n\n"

    out = out[:-1]
    ugcdoc.export_md_file("index", out, def_lang, lang)


build_doc()
build_doc('zh')
