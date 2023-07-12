import functools

import ugcdoc

# As the number of languages increases,
# this section can be moved to the corresponding file
md_dict = {None: 'en'}

md_dict['en'] = {'head': """_Written by: Alian713, Syser_

---

This page is a list of all the unit attributes that can be modified in the scenario editor and their purposes.
If you know of any attributes that are not written on this page,
or if the descriptions of the attributes are wrong, please let the authors of this guide know!

""", "property": "Property", "flag_value": "Flag Value"}

md_dict['zh'] = {'head': """_作者：Alian713, 别云_

---

此页面列出了可以在场景编辑器中修改的所有单位属性及其用途。如果您知道本页上未提及的任何属性，或者属性的描述有误，请告知本指南的作者！

""", 'name': "英文原名", "property": "标识", "flag_value": "值"}


def build_doc(lang: str = None):
    def_lang = md_dict[None]
    lang = lang or def_lang
    attrs = ugcdoc.load_json_dict("attributes", def_lang, lang)

    out = md_dict[lang]['head']
    for attr_id in attrs[def_lang]:
        k = functools.partial(ugcdoc.get_key, dict_set=attrs, parent_key=attr_id, language=lang)

        out += f"## {attr_id}. {k('name')}\n\n"
        out += f"-   ID: {attr_id}\n\n"
        if lang != def_lang:
            out += f"-   {md_dict[lang]['name']}: {k('name', language=None)}\n\n"

        out += f"-   {k('desc')}\n\n"

        if extra := k('notes'):
            dnln = '\n\n'
            out += f"-   {f'{dnln}    '.join(extra)}\n\n"

        if extra := k('flags'):
            out += f"    | {md_dict[lang]['property']} | {md_dict[lang]['flag_value']} |\n"
            out += "    | :- | -: |\n"

            for value, desc in extra.items():
                out += f"    | {desc} | {value} | \n"
            out += "\n"

    out = out[:-1]
    ugcdoc.export_md_file("index", out, def_lang, lang)


build_doc()
build_doc('zh')
