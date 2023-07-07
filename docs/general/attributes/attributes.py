import functools
import regex
import json

# As the number of languages increases,
# this section can be moved to the corresponding file
out_dict = {'default': 'en'}

out_dict['en'] = {'head': """_Written by: Alian713, Syser_

---

This page is a list of all the unit attributes that can be modified in the scenario editor and their purposes.   
If you know of any attributes that are not written on this page,
or if the descriptions of the attributes are wrong, please let the authors of this guide know!

""", "property": "Property", "flag_value": "Flag Value"}

out_dict['zh'] = {'head': """_作者: Alian713, 别云_

---

此页面列出了可以在场景编辑器中修改的所有单位属性及其用途。如果您知道本页上未提及的任何属性，或者属性的描述有误，请告知本指南的作者！

""", 'name': "英文原名", "property": "标识", "flag_value": "值"}


def validify(name: str) -> str:
    name = name.upper()
    name = name.replace(" ", "_")
    name = name.replace("(", "_")
    name = name.replace("%", "_PERCENT")
    name = name.replace("/", "_")
    name = name.replace(")", "_")
    name = name.replace("-", "_")
    name = name.replace("!", "")
    name = name.replace(".", "_")
    name = name.replace(",", "_")
    name = name.replace("'", "_")
    name = name.replace("+", "AND")
    name = name.replace("[", "_")
    name = name.replace("]", "_")
    name = regex.sub("_+", "_", name)
    name = regex.sub("_$", "", name)
    name = regex.sub("^_", "", name)
    return name


def get_key(key_name: str, attr: dict, lang: str = None):
    if lang and lang != out_dict['default'] and f'{key_name}.{lang}' in attr:
        return attr[f'{key_name}.{lang}']
    return attr[key_name]


def build_doc(lang: str = None):
    with open("attributes.json") as file:
        attrs = json.load(file)

    lang = lang or out_dict['default']
    not_def_lang = lang != out_dict['default']

    out = out_dict[lang]['head']
    for id_, attr in attrs.items():
        k = functools.partial(get_key, attr=attr, lang=lang)

        out += f"## {id_}. {k('name')}\n\n"

        if not_def_lang:
            out += f"-   {out_dict[lang]['name']}: {k('name', lang=None)}\n\n"

        out += f"-   {k('desc')}\n\n"

        dnln = '\n\n'
        if 0 < len(k('notes')):
            out += f"-   {f'{dnln}    '.join(k('notes'))}\n\n"

        if 0 < len(k('flags')):
            out += f"    | {out_dict[lang]['property']} | {out_dict[lang]['flag_value']} |\n"
            out += "    | :- | -: |\n"

            for value, desc in attr["flags"].items():
                out += f"    | {desc} | {value} | \n"
            out += "\n"

    out = out[:-1]
    output_file = "index"
    output_file = f"{output_file}.{lang}.md" if not_def_lang else f"{output_file}.md"
    with open(output_file, "w") as file:
        file.write(out)


build_doc()
build_doc('zh')
