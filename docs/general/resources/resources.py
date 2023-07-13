import functools

import ugcdoc

# As the number of languages increases,
# this section can be moved to the corresponding file
md_dict = {None: 'en'}

md_dict['en'] = {'head': r"""# Player Resources

_Written by: Alian713, Bradical, Syser_

---

This page is a list of all the player resources in the scenario editor and their purposes.
If you know of any resources that are not written on this page,
or if the descriptions of the resources are wrong, please let the authors of this guide know!

There are some resources named start with **\[invalid\]**,
whose real names do not contain this flag.
This flag indicates that reading and writing to this resource
has (so far) not affected the game in any way.

""", "invalid": r"**\[INVALID\]**", "purpose": "Purpose", "property": "Property", "default_values": "Default Values",
                 "note": "Note"}

md_dict['zh'] = {'head': r"""# 玩家资源

_作者：Alian713, Bradical, 别云_

---

此页面列出了场景编辑器中所有的玩家资源及其用途。如果您知道本页上未写的任何资源，或者如果资源描述有误，请告知本指南的作者！

请注意，下文中名称以 **\[无效\]** 开头的资源，其真实名称并不包含该标识，
该标识表明目前为止读写这个资源不会对游戏造成任何影响。

""", 'name': "英文原名", "invalid": r"**\[无效\]**", "purpose": "用途", "default_values": "默认值", "note": "注意"}


def build_doc(lang: str = None):
    def_lang = md_dict[None]
    lang = lang or def_lang
    reses = ugcdoc.load_json_dict("resources", def_lang, lang)

    out = md_dict[lang]['head']
    for res_id in reses[def_lang]:
        k = functools.partial(ugcdoc.get_key, dict_set=reses, parent_key=res_id, language=lang)

        name = k('name')
        if k('valid') is not None and not k('valid'):
            name = f"{md_dict[lang]['invalid']} {name}"
        out += f"## {res_id}. {name} {{ #{res_id} }}\n\n"
        out += f"-   ID: {res_id}\n\n"
        if lang != def_lang:
            out += f"-   {md_dict[lang]['name']}: {k('name', language=None)}\n\n"

        out += "-   " + md_dict[lang]['purpose'] + f": {k('desc')}\n\n"

        if extra := k('defaults'):
            out += f"-   {md_dict[lang]['default_values']}:\n\n"
            for v, n in extra.items():
                out += f"    -   {v}: {n}\n"
            out += '\n'

        if extra := k('note'):
            out += f"-   {md_dict[lang]['note']}: {extra}\n\n"

    out = out[:-1]
    out = ugcdoc.f2math(out)
    ugcdoc.export_md_file("index", out, def_lang, lang)


build_doc()
build_doc('zh')
