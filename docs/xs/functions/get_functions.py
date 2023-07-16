import winreg

import regex

path = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Microsoft Games\Age of Empires II DE')
path = winreg.QueryValueEx(path, 'Install Location')[0]
path += "/AoE2DE_s.exe"

fun_set = {}

fix_name = {"xsGetMapType": "xsGetMapID", "xsGetFuntionID": "xsGetFunctionID"}

with open(path, "rb") as file:
    fun_addr = [0x02ED2E70, 0x02ED3F18]
    for addr in fun_addr:
        file.seek(addr)
        txt = ""
        i_c = 0
        while c := file.read(1):
            if b'\x00' == c:
                i_c += 1
                continue

            if i_c:
                # print(f"{len(txt)}\t+\t{i_c}\t=\t{len(txt) + i_c}\t{txt}")
                if regex.match(r"^\w+$", txt):
                    fun_set[txt] = ''
                elif t := regex.match(r"^(\w+ )*(\w+)\((?!%)", txt):
                    name = t[2]

                    if name in fix_name:
                        name = fix_name[name]

                        if 'xsGetMapType' == name:
                            txt = txt.replace('xsGetMapType', 'xsGetMapID')

                    if name in fun_set:
                        if fun_set[name]:
                            if 'xsArrayGetInt' == name:
                                name = 'xsArrayGetBool'
                            else:
                                raise Exception()
                        fun_set[name] = txt
                    else:
                        raise Exception

                txt = ''
                i_c = 0

            if b'\x02' == c:
                break

            txt += c.decode()

fun_set = {k: v for k, v in fun_set.items() if v}
# fun_set = {k: fun_set[k] for k in sorted(fun_set)}

for i, (f, pt) in enumerate(fun_set.items(), 1):
    print(f"{i:<4}{f:<24}{pt}")
