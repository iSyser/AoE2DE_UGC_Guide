import regex
import json


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


def f2math(md: str) -> str:
    md = md.replace(">=", "$≥$")
    md = md.replace("<=", "$≤$")
    md = md.replace(">", "$>$")
    md = md.replace("<", "$<$")
    return md


def load_json_dict(file_name: str, default_language: str, language: str = None) -> dict:
    result = {None: default_language}

    with open(file_name + ".json") as file:
        result[default_language] = json.load(file)

    if language and language != default_language:
        with open(f"{file_name}.{language}.json") as file:
            result[language] = json.load(file)

    return result


def get_key(key_name: str, *, dict_set: dict, parent_key: str, lang: str):
    if lang and lang in dict_set and (parent := dict_set[lang].get(parent_key)):
        if result := parent.get(key_name):
            return result

    parent = dict_set[dict_set[None]].get(parent_key)
    if parent:
        return parent.get(key_name)
    raise Exception(f"Unknown parent: {parent}")
