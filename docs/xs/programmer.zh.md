# XS 脚本：程序员参考

_作者：Alian713_

---

这会是您发现的最简短、最精确的 XS 脚本指南，它没有对编程主题进行任何介绍，而是直接切入正题，如果您是一名程序员，那么这对您来说是完美的。如果您不是程序员，不用担心！请参阅本指南的 [对于初学者](../beginner/ "跳转至：XS 脚本语言 > 对于初学者") 部分。

## 1. 使用 XS 脚本

要使用 XS 脚本：

1.  导航至文件夹：

    `文件夹路径/AoE2DE/resources/_common/xs`

2.  该文件夹中应该已经有 2 个文件，名为 `Constants.xs` 和 `xs.txt`。在这里，创建一个新文件，名称以 `.xs` 结尾。例如，该文件可以为 `filename.xs`

    !!! Warning "default0.xs"

        可能还有一个名为 `default0.xs` 的附加文件。切勿在此文件中写入代码，因为这是临时文件，会被游戏覆盖。

    !!! Note "Constants.xs"

        文件 `Constants.xs` 包含可直接在任何 XS 脚本中使用的常量列表，无需使用 include 语句。

    !!! Tip "XS 的 VSC 插件"

        可以在[此处](https://marketplace.visualstudio.com/items?itemName=Divy.vscode-xs)找到用于 AoE XS 脚本的语法高亮显示和代码自动完成的 VSC 扩展

3.  要开始使用 XS，请在文件中写入以下基本代码：

    ```cpp
    // 这是一条注释
    /* 这是
    一条
    多行注释
    */
    void main() {
      int a = 10;
      int b = 20;

      // 与 Java 和 Python 不同，
      // 变量不能通过用逗号分隔来声明。

      // 发送屏幕聊天
      xsChatData("a + b = " + (a + b));
    }

    ```

### 1.1. 在自定义场景中

1. 在编辑器中打开场景
2. 在 `地图` 选项卡下，于 `脚本文件名` 字段中键入您创建的 XS 脚本的名称，末尾不带 `.xs`。例如，如果您的文件名为 `filename.xs`，那么您将在此字段中写入 `filename`。
3. 现在，在编辑器的 `触发` 选项卡下，添加新触发，然后添加新效果。（如果您不知道 触发/效果 是什么，请参阅本手册的 `自定义场景：触发：触发基础知识` 部分）
4. 从 `效果列表` 中选择 `脚本调用`。
5. 您现在可以通过普通函数调用在消息框中使用 XS 脚本中的函数。请记住，只有那些不带任何参数的函数才可以在这里工作！
6. 我们上面创建的 `main()` 函数会在场景被游玩时自动执行。
7. 如果代码没有错误，点击 `E#0：脚本调用` 效果会变成绿色。如果脚本中有错误，将会显示错误消息。
8. 现在测试场景将在上面定义的触发中运行 `脚本调用` 效果，该效果又将运行 XS 脚本中的 `main()` 函数，并且 `30` 将显示在聊天中。

### 1.2. 在 RMS 中

1. 在文本编辑器中打开 RMS 脚本
2. 在最顶部，输入 `#includeXS filename.xs`。此处 `filename.xs` 是您上面创建的文件的名称。
3. 当使用 RMS 生成地图时，会自动调用 `main();` 函数。
4. 要进行测试，请在单人游戏（或多人游戏）大厅中加载 RMS 并启动游戏。要进行测试，请在单人游戏（或多人游戏）大厅中加载 RMS 并开始游戏。
5. 建议您使用自定义场景来测试 XS 脚本，因为在编辑器中调试它们更容易。

现在您已经创建了一个包含 `main()` 函数的 XS 文件，您可以在该函数中键入代码来执行不同的操作！我们将一一探讨所有已知可能发生的不同事情：

## 2. 变量数据类型

XS 总共支持 5 种数据类型，它们是：

|  **数据类型**  |                **句法**                 |
| :------------: | :-------------------------------------: |
|  `#!cpp int`   |           `#!cpp int a = 10;`           |
| `#!cpp float`  |         `#!cpp float a = 3.1;`          |
| `#!cpp string` |      `#!cpp string a = "string";`       |
|  `#!cpp bool`  |         `#!cpp bool a = true;`          |
| `#!cpp vector` | `#!cpp vector v = vector(1.2, 2.3, 3);` |

有关可用于向量的所有不同函数，请参阅本指南的 [向量操作](../functions/#Vectors "跳转至：XS 脚本语言 > 函数参考 > 向量) 部分。

!!! Bug "向量初始化中不能有变量"

    变量不能用于向量初始化。例如：`#!cpp vector v = vector(x, y, z);` 不起作用。这里 `x`、`y`、`z` 是浮点值。请改用 `#!cpp vector v = xsVectorSet(x, y, z);`。

!!! info "常数和作用域"

    1. 常数变量

        句法 `#!cpp const int a = 10;` 或 `#!cpp const float PI = 3.1415;` 将声明一个不可变变量。

    2. 变量的作用域

        局部变量和全局变量的概念适用于 XS。

!!! bug

    目前版本中不能直接在 `#!cpp string` 中使用非 ASCII 字符，如果必须要使用，请参阅本手册的 `技巧 > 使用非 ASCII 字符` 部分，它是通过读写文件的方式实现的。

## 3. 操作

### 3.1. 算术运算

| **运算** | **句法** |
| :------: | :------: |
|   加法   | `a + b`  |
|   减法   | `a - b`  |
|   乘法   | `a * b`  |
|   除法   | `a / b`  |
|   取模   | `a % b`  |

有关有用的数学函数，请参阅本指南的 [数学运算](../functions/#Maths "跳转至：XS 脚本语言 > 函数参考 > 数学") 部分。

!!! warning "一元负号"

    XS 中没有一元负运算符

    ```cpp
    void main() {
      int a = 10;

      // 这样不行：
      int b = -a + 20;

      // 应该用：
      int b = 0 - a + 20;
    }

    ```

### 3.2. 前缀和后缀运算

| **运算** | **句法** |
| :------: | :------: |
|  后自增  |  `a++`   |
|  后自减  |  `a--`   |

XS 不支持前缀操作。

### 3.3. 简写赋值运算

XS 不支持简写赋值运算。

### 3.4. 位运算

XS 不支持按位运算。

### 3.5. 关系运算

|  **运算**  | **句法** |
| :--------: | :------: |
|    小于    | `a < b`  |
|    大于    | `a > b`  |
| 小于或等于 | `a <= b` |
| 大于或等于 | `a >= b` |
|    等于    | `a == b` |
|   不等于   | `a != b` |

!!! info "字符串的关系运算"

    这些关系运算符也适用于字符串，例如 `a < b` 告诉您按字典顺序 `a` 是否在 `b` 之前。

### 3.6. 逻辑运算

<!-- prettier-ignore -->
| **运算** | **句法** |
| :------: | :------: |
|    与    | `a && b` |
|    或    | `a || b` |

XS 不支持“非”。

!!! bug "运算结果的数据类型"

    由于目前的一个 Bug，任何操作的结果的数据类型都由第一个操作数确定。这意味着 `#!cpp 9 * 5.5` 的计算结果为 `#!cpp 49`，而不是 `#!cpp 49.5`。但是，`#!cpp 5.5 * 9` 将正确计算为 `#!cpp 49.5`。

## 4. 流程控制语句

XS 支持以下流控制语句：

1. `#!cpp if else if` 结构：

    句法例程：

    ```cpp
    void main() {
      int a = 10;
      float b = 20;
      int c = 30;
      float max = 0;
      if (a > b && a > c)
        max = a;
      else if (b > c && b > a)
        max = b;
      else
        max = c;
    }

    ```

2. `#!cpp switch-case` 结构：

    句法例程：

    ```cpp
    void main() {
      int a = 10;
      switch (a) {
      case 1: {
        // 做些操作
      }
      case 2: {
        // 做些操作
      }
      case 3: {
        // 做些操作
      }
      default: {
        // 做些操作
      }
      }
    }

    ```

3. `#!cpp while` 循环：

    句法例程：

    ```cpp
    void main() {
      int a = 0;
      while (a < 10) {
        xsChatData("a = " + a);
        a++;
      }
    }

    ```

4. `#!cpp for` 循环：

    句法：

    ```cpp
    void main() {
      // 这将 a 从 0 循环到 10
      for (a = 0; < 10)
        xsChatData("a = " + a);

      // 这将 a 从 10 循环到 0
      for (a = 10; > 0)
        xsChatData("a = " + a);

      // 与 Java 不同，您不需要指定增量或减量，
      // for 循环会处理这一点

      // 遗憾的是，步长无法更改。
    }

    ```

## 5. 函数

句法：

```cpp
returnType functionName(dataType parameter1 = defaultValue1,
                        dataType parameter2 = defaultValue2) {
  return (value);
  // value 必须用括号括起来
}

```

句法例程：

```cpp
int max(int a = 0, int b = 2) {
  if (a > b)
    return (a);
  return (b);

  // 返回值必须始终在括号内。
}

void main() { xsChatData("max " + max(10, 20)); }

```

XS 脚本可以使用以下语法导入其他 XS 脚本：

```cpp
include "绝对/或/相对/路径/到/文件.xs";
```

## 6. 数组

有关如何使用数组的信息，请参阅本指南的[数组操作](../functions/#Arrays "跳转至：XS 脚本语言 > 函数参考 > 数组")部分。

XS 不支持 `#!cpp int a[] = new int[10];` 或 `#!cpp a[2];` 等标准语法。

## 7. 类型转换

`#!cpp int`、`#!cpp float` 和 `#!cpp bool` 数据类型可以相互隐式转换。所有这些都可以通过执行 `#!cpp string a = "this will work " + 5.6;` 隐式转换为字符串。但是，`#!cpp string a = 5.5;` 不起作用，而应使用：`#!cpp string a = "" + 5.5;`。

仍未知 XS 是否支持正确的显式类型转换

## 8. 规则

规则是一段代码，可以设置为在整个游戏过程中以设定的时间间隔重复执行。规则总是在方法之外初始化。它的用法如下：

句法：

```cpp
rule ruleName       // 这是规则的名称。遵循与变量相同的命名规则。

  active/inactive   // 这是规则的初始状态，active 意味着默认运行，
                    // inactive 意味着默认情况下不会运行。
                    // 这与 启用/禁用 触发器时触发器的工作方式类似。

  group groupName   // 该规则所属的组。遵循与变量相同的命名规则。

  minInterval <int> // 再次执行块之前必须经过的最小时间间隔
  maxInterval <int> // 在块必须再次执行之前可能经过的最大时间间隔
  highFrequency     // 每物理秒循环规则 60 次（这与游戏速度无关）
                    // 仅使用 “highFrequency” 或 “minInterval” 和 “maxInterval” 之一。两者不能一起使用

  runImmediately    // 目前尚不清楚此选项的作用
  priority <int>    // 规则按照优先级降序执行
{
  // 要执行的代码
}

```

例程：

```cpp
int a = 0;
// 该规则每 2 秒打印一次 a 的值。
rule chatTheValueOfA
  active
  minInterval 2
  maxInterval 2
  group chatGroup
{
  xsChatData("a = " + a);
  a++;
}

```

有很多内置的 XS 函数可以与规则交互。请参阅本指南的 [规则](../functions/#Rules "跳转至：XS 脚本语言 > 函数参考 > 规则") 部分。

变量 `cActivationTime` 在规则块内使用时，给出规则的激活时间（以秒为单位）。

至此，您现在已经了解了当前已知的与 XS 脚本配合使用的所有内容。祝你好运，并享受创建精彩地图的乐趣！
