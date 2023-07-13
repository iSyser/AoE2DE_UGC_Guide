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


class CXsBase:
    def __init__(self, info_def: dict, info_local: dict = None):
        self._name: str = info_def['name']
        self._nickname: str = ""
        self._type: str = info_def.get('type')
        self._desc: str = ""

        if info_local:
            self._nickname = info_local.get('nickname')
            self._desc = info_local.get('desc')

        if not self._desc:
            self._desc = info_def['desc']

    def __str__(self) -> str:
        return self.get_type() + ' ' + self.get_real_name()

    def have_nickname(self) -> bool:
        return bool(self._nickname)

    def get_name(self) -> str:
        return self._nickname or self._name

    def get_real_name(self) -> str:
        return self._name

    def get_type(self):
        return self._type

    def get_desc(self) -> str:
        return self._desc


class CXsConstant(CXsBase):
    def __init__(self, info_def: dict, info_local: dict = None):
        super().__init__(info_def, info_local)

        self._desc_name: str = ""
        desc_name = self.get_name()[1:]
        remove_str = "Attribute"
        if desc_name.startswith(remove_str):
            desc_name = desc_name[len(remove_str):]
        for c in desc_name:
            if c.isupper():
                self._desc_name += ' '
            self._desc_name += c
        self._desc_name = self._desc_name.strip()

        self._value: str = info_def['value']

        self._desc = self._desc.replace("GET_NAME", self._desc_name).replace("GET_ID", str(self._value))

        self._usage = info_def['usage']
        if info_local and (usage_local := info_local.get('usage')):
            for k in self._usage:
                # if "example" == k:
                #     continue
                self._usage[k] = usage_local.get(k) or self._usage[k]

    def get_value(self) -> str:
        return self._value

    def get_usage(self) -> dict:
        return self._usage


class CXsParam(CXsBase):
    def __init__(self, info_def: dict, info_local: dict = None):
        super().__init__(info_def, info_local)

        self._required = info_def['required']

    def is_required(self) -> bool:
        return self._required


class CXsFunction(CXsBase):

    def __init__(self, fun_name: str, fun_dict: dict, lang: str = None):

        def_lang = fun_dict[None]
        lang = lang or def_lang

        info_def = fun_dict[def_lang][fun_name]

        if lang != def_lang and lang in fun_dict and (info_local := fun_dict[lang].get(fun_name)):
            l = info_local.get('params')
        else:
            info_local = None
            l = []

        super().__init__(info_def, info_local)
        if not self._type:
            self._type = info_def['return_type']
        if params := info_def.get('params'):
            self._params = [CXsParam(p, l[i] if l else None) for i, p in enumerate(params)]
        else:
            self._params: list[CXsParam] = []

    def __str__(self) -> str:
        prototype = self.get_type() + ' ' + self.get_real_name() + "("
        if params := self._params:
            prototype += ', '.join([str(p) for p in params])
        prototype += ");"
        return prototype

    def have_param(self) -> bool:
        return bool(self._params)

    def get_params(self) -> list[CXsParam]:
        return self._params
