# 帝国时代 2 场景解析器

_作者：KSneijders (MrKirby)_

---

## 解析器的用途是什么？

在处理场景时，您可能必须多次执行一些重复性任务。一些常见的例子是：将单位放置在网格中、为所有玩家复制触发器或创建许多类似的效果。使用编程语言可以轻松解决此类问题！

它也是一个能够调整迷你游戏或地图的完美工具。假设您有一个小游戏，每杀死一个单位即可获得 10 黄金。后来你发现，它的威力太大了，所以你想将所有效果更改为每单位 5 金币。如果您使用解析器来设置所有触发器和效果，并且您有一个类似以下的变量：`gold_per_unit = 10`，您只需将其更改为 5，重新运行代码，然后您就可以一次性修复它！

解析器的工作原理是读取场景文件，并将其转换为编程语言 `Python3` 中的对象。然后，您可以使用可用的功能轻松添加或更改场景中的内容。几个示例函数：`add_unit`、`add_trigger`、`copy_trigger_per_player` 等等！

查看 [帝国时代 2 场景解析器官方文档] 以获取最新的安装指南以及如何开始！

[帝国时代 2 场景解析器官方文档]: https://ksneijders.github.io/AoE2ScenarioParser/installation/

## 安装 Python

如需最新的安装指南，您应该查看官方的 `帝国时代 2 场景解析器` 文档。

可以在 [此处] 找到。

[此处]: https://ksneijders.github.io/AoE2ScenarioParser/installation/

---

您可以使用 pip 安装该项目：

    pip install AoE2ScenarioParser

如果您不知道 pip 是什么，您可以在 [他们的文档] 中阅读它

[他们的文档]: https://pip.pypa.io/en/stable/
