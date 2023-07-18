# 技巧

_作者：Alian713, 别云_

---

## 1. 设置和取消成本

一座房屋通常需要 25 木材，但如果我们想让它花费 10 块石头怎么办？

有可能会这样尝试：

```cpp
const int HOUSE = 70;

xsEffectAmount(cSetAttribute, HOUSE, cStoneCost, 10, 1);
xsEffectAmount(cSetAttribute, HOUSE, cWoodCost, -2, 1);

```

这是对如何做到这一点的合理猜测，但不幸的是这不起作用。石头成本不会添加到房子中，并且建造房子实际上不会取消木材成本，而是向玩家返还 2 点木材！

然而，有一个技巧可以实现这一目标：

```cpp
const int HOUSE = 70;

xsEffectAmount(cMulAttribute, HOUSE, cStoneCost, -1, 1);
xsEffectAmount(cSetAttribute, HOUSE, cStoneCost, 10, 1);
xsEffectAmount(cMulAttribute, HOUSE, cWoodCost, -2, 1);

```

不过同样的技巧对于改变科技成本来说**不起作用**。

## 2. 使用非 ASCII 字符

也许你已经发现了，目前版本中不能直接在 `#!cpp string` 中使用非 ASCII 字符。这意味着下面的语句是无效的：

```cpp
string tip = "你好";
xsChatData(tip + "，世界！");

```

考虑到 xs 语言实际上是 C++ 一个非常残缺的子集，许多应有的功能都还未有，想让开发者在脚本内部支持非 ASCII 字符更是一种奢望，即使该支持仅限在字符串中。

但是，你可以在游戏中看到人们用不同的语言的文字交谈、战役中的提示文本也是有许多语言，这意味着发送聊天本就是支持多语言的，只是由于 xs 语言自身的限制无法使用这些特性。不过，有一种非常取巧的方式能够实现这样的目的：

以中文为例，我们假定你正在编辑器中测试场景，而不是单人游戏或者发布的战役，请在以下目录中创建 `file4utf.xs` 文件：

```
%USERPROFILE%/Games/Age of Empires 2 DE/你的 ID/resources/_common/xs
```

内容是：

```cpp
const string DATFILE = "default0";

bool InitMyDat() {
  // 有一个 Bug，使得将全局变量写入文件中会出错
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

将该文件作为场景的脚本文件，测试场景后，如果没有错误，应该会在屏幕中打印文本 `#!cpp "The quick brown fox jumps over the lazy dog."`，并生成以下文件：

```
%USERPROFILE%/Games/Age of Empires 2 DE/你的 ID/profile/default0.xsdat
```

不要关闭游戏，用文本编辑器打开该文件，你会发现这个文件内容中包含我们在代码中所输出的 `#!cpp "The quick..."`，如果在该文本最前面插入 `#!cpp "你好，世界！"`，变成 `#!cpp "你好，世界！The quick..."`，重新测试场景，你会发现 `xsChatData();` 正确地打印出了中文！

这是实现该功能所需的主要操作，还有许多细节需要处理。例如，文本 `#!cpp "The quick..."` 前面的无法显示的字符是什么？实际上，该字符是二进制数，如果用 Hex 编辑器打开，会发现它指定了接下来的字符串的实际长度。如果你足够细心，会发现添加中文后，原先的英文句子显示不完整，这是因为插入了中文内容后，英文句子的后面部分已经不在原有的长度下了。

因此，如果想要制作一个有诸多语言的 `.xsdat`，你可能需要借助 Hex 编辑器的帮助来正确填写该字符串的长度，这样做是非常乏味的，可以使用其他你熟悉的编程语言自动化，将精力更多地留在制作内容上。

将该功能投入生产，需要付出许多努力，并且带有语言文本的 `.xsdat` 文件需要跟随你的战役分发，上文我们是使用编辑器的场景测试，这个文件被固定为 `default0.xsdat`。如果你将发布为模组，这个文件名将是你的战役文件名。
