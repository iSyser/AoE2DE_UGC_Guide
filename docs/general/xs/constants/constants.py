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

# Constant Reference

_Written by: Alian713_

""", "value": "Value", "syntax": "Syntax", "example": "Example"}

md_dict['zh'] = {'head': """---
hide:
#     - navigation
#     - toc
---

# 常量参考

_作者：Alian713_

""", "name": "英文原名", "value": "值", "syntax": "句法", "example": "例程"}


def build_doc(lang: str = None):
    def_lang = md_dict[None]
    lang = lang or def_lang
    consts_set = ugcdoc.load_json_dict("constants", def_lang, lang, True)

    out = md_dict[lang]['head']
    for index, category in enumerate(consts_set[def_lang], 1):

        k = functools.partial(ugcdoc.get_key, dict_set=consts_set, parent_key=category, language=lang)

        # 'nickname' in other languages will not be used.
        if not (title := k('nickname', default_language=lang)):
            title = category
        out += f"## {index}. {title.title().replace('Effectamount', 'EffectAmount')} {{ #{category} }}\n\n"

        consts_def = ugcdoc.json_list_2_dict(k('constants', language=None))
        consts_local = {} if def_lang == lang else ugcdoc.json_list_2_dict(k('constants', default_language=lang))

        for i, (const_name, const_obj) in enumerate(consts_def.items(), 1):
            c = ugcdoc.CXsConstant(const_obj, consts_local.get(const_name))

            out += f"### {index}.{i}. {c.get_name()} {{ #{c.get_real_name()} }}\n\n"
            if c.have_nickname():
                out += f"{md_dict[lang]['name']}: {c.get_real_name()}\n\n"
            out += f"{md_dict[lang]['value']}: `#!cpp {c.get_type()} {c.get_value()}`\n\n"
            out += f"{c.get_desc()}\n\n"
            if usage := c.get_usage():
                out += f"{md_dict[lang]['syntax']}: `#!cpp {usage['syntax']}`\n\n"
                out += f"{md_dict[lang]['example']}: `#!cpp {usage['example']}`\n\n"
                out += usage['explanation'] + "\n\n"

    out = out[:-1]
    ugcdoc.export_md_file("index", out, def_lang, lang)


build_doc()
build_doc('zh')
