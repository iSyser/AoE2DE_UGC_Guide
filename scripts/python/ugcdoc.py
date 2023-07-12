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


def json_list_2_dict(src: list) -> dict:
    result = {}
    if not src:
        return result

    for i in src:
        result[i['name']] = i
    return result


def load_json_dict(file_name: str, default_language: str, language: str = None, fix_2_dict: bool = False) -> dict:
    result = {None: default_language}

    with open(file_name + ".json", "rb") as file:
        result[default_language] = json.load(file)

    if language and language != default_language:
        with open(f"{file_name}.{language}.json", "rb") as file:
            result[language] = json.load(file)

    if fix_2_dict:
        for i in result:
            if i:
                result[i] = json_list_2_dict(result[i])
    return result


def get_key(key_name: str, *, dict_set: dict, parent_key: str, default_language: str = None, language: str = None):
    if language and language in dict_set and (parent := dict_set[language].get(parent_key)):
        if result := parent.get(key_name):
            return result
    default_language = default_language or dict_set[None]
    parent = dict_set[default_language].get(parent_key)
    if parent:
        return parent.get(key_name)

    # raise Exception(f"Unknown parent: {parent}")


def export_md_file(file_name: str, content: str, default_language: str, language: str = None):
    if language and language != default_language:
        file_name = '.'.join([file_name, language, "md"])
    else:
        file_name += ".md"

    with open(file_name, "w", encoding="UTF-8") as file:
        file.write(content)


class CXsParam:
    def __init__(self, param_def: dict, param_local: dict = None):
        self.name: str = ""
        self.nickname: str = ""
        self.type: str = ""
        self.desc: str = ""
        self.required: bool = False

        if param_local:
            self.nickname = param_local.get('nickname')
            self.desc = param_local.get('desc')

        self.name = param_def['name']
        self.type = param_def['type']
        if not self.desc:
            self.desc = param_def['desc']
        self.required = param_def['required']

    def is_required(self) -> bool:
        return self.required

    def have_nickname(self) -> bool:
        return bool(self.nickname)

    def get_name(self) -> str:
        return self.nickname or self.name

    def get_real_name(self) -> str:
        return self.name

    def get_type(self):
        return self.type

    def get_desc(self) -> str:
        return self.desc


class CXsFunction:

    def __init__(self, fun_name: str, fun_dict: dict, lang: str = None):
        self.name: str = ""
        self.nickname: str = ""
        self.type: str = ""
        self.desc: str = ""
        self.params: list[CXsParam] = []

        def_lang = fun_dict[None]
        lang = lang or def_lang

        info_def = fun_dict[def_lang][fun_name]

        l: list = []
        if lang != def_lang and lang in fun_dict and (info_local := fun_dict[lang].get(fun_name)):
            self.nickname = info_local.get('nickname')
            self.desc = info_local.get('desc')
            l = info_local.get('params')

        if params := info_def.get('params'):
            self.params = [CXsParam(p, l[i] if l else None) for i, p in enumerate(params)]

        self.name = info_def['name']
        self.type = info_def['return_type']
        if not self.desc:
            self.desc = info_def['desc']

    def have_nickname(self) -> bool:
        return bool(self.nickname)

    def have_param(self) -> bool:
        return bool(self.params)

    def get_name(self) -> str:
        return self.nickname or self.name

    def get_real_name(self) -> str:
        return self.name

    def get_type(self):
        return self.type

    def get_desc(self) -> str:
        return self.desc

    def get_params(self) -> list[CXsParam]:
        return self.params

    def get_prototype(self) -> str:
        prototype = self.get_type() + ' ' + self.get_real_name() + "("
        if params := self.params:
            prototype += ', '.join([p.get_type() + ' ' + p.get_real_name() for p in params])
        prototype += ");"
        return prototype
