_Written by: Alian713, Syser_

---

## 1. Setting and Unsetting Costs

A house normally costs 25 wood, but what if we want to make it cost, lets say, 10 stone instead?

One might attempt something like this:

```cpp
const int HOUSE = 70;

xsEffectAmount(cSetAttribute, HOUSE, cStoneCost, 10, 1);
xsEffectAmount(cSetAttribute, HOUSE, cWoodCost, -2, 1);

```

This is a reasonable guess for how to do it, but unfortunately this does not work. The stone cost does not get added to the house, and instead of unsetting the wood cost, making a house actually gives back 2 wood to the player!

There is however a trick that can achieve this:

```cpp
const int HOUSE = 70;

xsEffectAmount(cMulAttribute, HOUSE, cStoneCost, -1, 1);
xsEffectAmount(cSetAttribute, HOUSE, cStoneCost, 10, 1);
xsEffectAmount(cMulAttribute, HOUSE, cWoodCost, -2, 1);

```

This same trick does **not** work for changing technology costs.

## 2. Using non-ASCII characters

Maybe you have discovered that non-ASCII characters cannot be used directly in `#!cpp string` in the current version. This means the following statement is invalid:

```cpp
string tip = "你好";
xsChatData(tip + "，世界！");

```

Considering that the xs language is actually a very incomplete subset of C++, and many functions that should be there are not yet available, it is a luxury for developers to support non-ASCII characters inside the script, even if the support is limited to strings middle.

However, you can see people talking in different languages in the game, and the prompt text in the campaign also has many languages, which means that sending chat supports multiple languages, but these cannot be used due to the limitations of the xs language itself characteristic. However, there is a very tricky way to achieve this:

Taking Chinese as an example, we assume that you are testing the scene in the editor, not a single player game or a published campaign, please create a `file4utf.xs` file in the following directory:

```
%USERPROFILE%/Games/Age of Empires 2 DE/Your ID/resources/_common/xs/
```

The content is:

```cpp
const string DATFILE = "default0";

bool InitMyDat() {
  // There is a bug where writing global variables to a file will fail
  const string VERSION = "File4Utf.0.1.0";

  if (xsOpenFile(DATFILE)) {
    if (VERSION == xsReadString())
      return (true);

    xsCloseFile();
  }

  if (false == xsCreateFile(false))
    return (false);

  xsWriteString(VERSION);
  xsWriteString("The quick brown fox jumps over the lazy dog.");
  xsCloseFile();

  xsOpenFile(DATFILE);

  return (xsOffsetFilePosition(cOffsetString));
}

void main() {
  InitMyDat();
  xsChatData(xsReadString());
  xsCloseFile();
}
```

Use this file as the script file for the scene. After testing the scene, if there are no errors, the text `#!cpp "The quick brown fox jumps over the lazy dog."` should be printed to the screen, and the following files should be generated:

```
%USERPROFILE%/Games/Age of Empires 2 DE/Your ID/profile/default0.xsdat
```

Do not close the game, open the file with a text editor, you will find that the content of this file contains `#!cpp "The quick..."` that we output in the code, if you insert `#!cpp "你好，世界！"`, becomes `#!cpp "你好，世界！The quick..."`, re-test the scene, you will find that `xsChatData();` prints Chinese correctly!

This is the main operation required to implement the functionality, there are many details that need to be dealt with. For example, what is the unprintable character preceding the text `#!cpp "The quick..."`? In fact, this character is a binary number, and if you open it with a Hex editor, you will find that it specifies the actual length of the string that follows. If you are careful enough, you will find that after adding Chinese, the original English sentence is incomplete. This is because after inserting Chinese content, the latter part of the English sentence is no longer under the original length.

Therefore, if you want to make a `.xsdat` with many languages, you may need to use the help of a Hex editor to correctly fill in the length of the string, which is very tedious and can be automated using other programming languages ​​you are familiar with, and focus more on producing content.

It takes a lot of effort to put this feature into production, and the `.xsdat` file with the language text needs to be distributed with your campaign, above we are using the editor scenario test, this file is fixed to `default0.xsdat`. If you will be publishing as a Mod, this filename will be your campaign filename.
