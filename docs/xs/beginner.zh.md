# XS 脚本：初学者指南

_作者：Alian713_

---

## 你是程序员吗？

如果您知道如何用任何语言进行编程，那么您在本页上就是浪费时间！请参阅 [对于程序员](../programmer/ "跳转至：XS 脚本语言 > 对于程序员")，它是一个更短、更精确的文档，因为 XS 只是另一种具有不同的语法的编程语言。

如果您不是程序员，请不要害怕！您来对地方了，这里可以了解有关 XS 的所有知识！

## 1. 使用 XS 脚本

要使用 XS 脚本：

1.  确保您可以看到文件扩展名。这意味着您计算机上的每个文件都应该有一个类似于 `文件名.扩展名` 的名称。如果您可以看到文件扩展名，请继续执行步骤 2。如果看不到，请按照以下步骤操作：

    1. 按 ++windows+e++
    2. 单击顶部的 `查看`。
    3. 在出现的面板右侧，将有一个名为 `文件扩展名` 的选项。
    4. 如果尚未选中此选项，请选中该选项。

2.  导航至文件夹：

    `文件夹路径/AoE2DE/resources/_common/xs`

    该文件夹中应该已经有 2 个文件，名为 `Constants.xs` 和 `xs.txt`。在这里，创建一个新文件，名称以 `.xs` 结尾。例如，该文件可以为 `filename.xs`

    !!! Warning "default0.xs"

        可能还有一个名为 `default0.xs` 的附加文件。切勿在此文件中写入代码，因为这是临时文件，会被游戏覆盖。

    文件 `Constants.xs` 包含可在任何 XS 脚本中使用的常量列表（使用其名称）。它们本质上是 XS 语言为您预先定义的常量。

3.  现在用你最喜欢的 文本/代码 编辑器打开您刚刚创建的文件！如果您还没有，建议使用 [Visual Studio Code (VSC)](https://code.visualstudio.com/download)。

    用于 AoE XS 脚本的语法高亮显示和代码自动完成的 VSC 扩展可以在[此处](https://marketplace.visualstudio.com/items?itemName=Divy.vscode-xs)找到

4.  要开始使用 XS，请在文件中写入以下基本代码：

```cpp
// 双斜杠后面写的任何内容都是注释。
// 注释是运行脚本时被忽略的行。
// 注释对于向他人解释你的代码很有用，
// 更重要的是，向未来的你解释自己的代码。

// 写注释是一个好习惯，
// 因为它可以帮助你更好地理解自己的代码。
// 您将看到本手册中广泛使用的注释，
// 用于解释您看到的几乎所有代码

// 但请注意，尽管注释是一种很好的做法，
// 但过度注释代码是一件更糟糕的事情。
// 只注释真正需要注释的内容！

/* 由正斜杠和星号
对括起来的所有内容
都是多行注释 */

// 在这里，您将创建一个名为 'main' 的函数。
void main() {

  // 这行表示有一个名为 'a' 的整数，其值为 10。
  // 请注意，XS 中的几乎每个语句都以分号结尾，
  // 就像中文一样，我们使用句号来表示句子的结尾。
  int a = 10;
  int b = 20;

  // 这行表示您创建了一个名为 'c' 的新整数，
  // 它是 'a' 和 'b' 的和。
  int c = a + b;

  // 此行将在游戏聊天中显示 'c' 的值。
  // 此处在聊天中显示 '30'。
  xsChatData("" + c);
}

```

### 1.1. 在自定义场景中

1. 在编辑器中打开场景
2. 在 `地图` 选项卡下，于 `脚本文件名` 字段中键入您创建的 XS 脚本的名称，末尾不带 `.xs`。例如，如果您的文件名为 `filename.xs`，那么您将在此字段中写入 `filename`。
3. 现在，在编辑器的 `触发器` 选项卡下，添加新触发器，然后添加新效果。（如果您不知道 触发器/效果 是什么，请参阅本手册的 `自定义场景：触发器：触发器基础知识` 部分）
4. 从 `效果列表` 中选择 `脚本调用`。
5. 现在，您可以通过在消息框中键入 "function_name_here();" 使用 XS 脚本中的函数。
6. 我们上面创建的 `main()` 函数会在场景被游玩时自动执行。
7. 如果代码没有错误，点击 `E#0：脚本调用` 效果会变成绿色。如果脚本中有错误，将会显示错误消息。
8. 现在测试场景将在上面定义的触发器中运行 `脚本调用` 效果，该效果又将运行 XS 脚本中的 `main()` 函数，并且 `30` 将显示在聊天中。

### 1.2. 在 RMS 中

1. 在文本编辑器中打开 RMS 文件
2. 在最顶部，输入 `#includeXS filename.xs`。此处 `filename.xs` 是您上面创建的文件的名称。
3. 当使用 RMS 生成地图时，我们上面创建的 `main()` 函数会自动运行。
4. 要进行测试，请在单人游戏（或多人游戏）大厅中加载 RMS 并开始游戏。生成地图后，XS 脚本中的 `main()` 函数将被执行，并且聊天中将显示 `30`。
5. 建议您使用自定义场景来测试 XS 脚本，因为在编辑器中调试它们更容易。

现在您已经创建了一个包含 `main()` 函数的 XS 文件，您可以在该函数中键入代码来执行不同的操作！我们将一一探讨所有已知可能发生的不同事情，事情会变得更加清晰。

## 2. 编程概念:

### 2.1. 常量

要在 XS 脚本中执行任何操作，我们需要常量。在脚本执行过程中保持不变的任何值都称为常量。确切地说，它在脚本的整个执行过程中保持不变。 例如，`#!cpp 10` 是一个常量。 每个数字都是一个常数。

### 2.2. 变量

变量就像用于存储常量的盒子。变量是在脚本执行期间可以更改的值！这样想吧，如果变量是一个存储常量的盒子，则可以取出该常量，然后放入另一个常量。确切地说，它是一个变量（它可能会改变！）。 例如，我们之前看到的脚本使用 3 个变量，称为 `a`、`b` 和 `c`。

```cpp
void main() {
  int a = 10;
  int b = 20;
  int c = a + b;
  xsChatData("" + c);
}

```

您现在可能有的一些问题是：

1.  变量名称前面的 `#!cpp int` 是什么？ 这是变量的“数据类型”！

2.  您问数据类型是什么？脚本中的每个变量都有一个数据类型，也就是说，它告诉您变量中存储的值类型。这样想，如果你想储存水，你需要指定它必须存储在瓶子里。你可能会说，这不是很明显吗？虽然对于人类来说，这可能是显而易见的，但计算机是一台愚蠢的机器。除非你告诉它，否则它不知道该怎么做，它就像一个婴儿，必须用勺子喂每一个微小的细节和指令才能正常工作。

3.  还有哪些其他类型的数据类型？

    XS 总共支持 5 种数据类型，它们是：

    1.  整数型 (`#!cpp int`)

        你之前见过 `#!cpp int`，整数型是一种存储整数（Integer）数量的数据类型。整数可以是负数、正数或零。它永远不会有任何分数或小数部分（例如，整数型永远不会有 `#!cpp 0.5`）。

        用法：`#!cpp int a = 10;` 这声明了一个名为 `a` 的 `#!cpp int` 类型变量，其值为 `#!cpp 10`

    2.  浮点型(`#!cpp float`)

        `#!cpp float` 是一种可以存储带有分数或小数部分的值的数据类型。例如 `#!cpp 1.5` 是一个浮点（Floating Point）值。

        用法：`#!cpp float a = 3.14159;` 这声明了一个名为 `a` 的 `#!cpp float` 类型变量，其值为 `#!cpp 3.14159`

        那么为什么要使用 `#!cpp int` 呢？原因是计算机需要更长的时间来执行浮点数计算！如果您知道您的计算不会涉及分数和小数，则应始终使用整数型而不是浮点值

    3.  逻辑型 (`#!cpp bool`)

        `#!cpp bool` 又称布尔，是一种只能存储真（`#!cpp true`）或假（`#!cpp false`）两个布尔值之一的数据类型。任何是或否问题在某种意义上都是布尔问题，因为只有两个答案，是或否。布尔变量对于条件非常重要，我们稍后会讨论。

        用法：`#!cpp bool a = true;` 这声明了一个名为 `a` 的 `#!cpp bool` 类型变量，其值为 `#!cpp true`

        !!! note "注意"

            `#!cpp true` 的值也由 `#!cpp 1` 表示，而 `#!cpp false` 的值也由 `#!cpp 0` 表示。

    4.  字符串 (`#!cpp string`)

        `#!cpp string` 是一个词语、一个句子或一个段落。字符串始终用（半角）双引号括起来。

        用法：`#!cpp string a = "这是一串文本！哈哈";` 这声明了一个名为 `a` 的 `#!cpp string` 类型变量，其值为 `#!cpp "这是一串文本！哈哈"`

        !!! bug

            上文中的中文字符串实际上无法如此实现，目前版本中不能直接在 `#!cpp string` 中使用非 ASCII 字符，如果必须要使用，请参阅本手册的 `技巧 > 使用非 ASCII 字符` 部分，它是通过读写文件的方式实现的。

    5.  向量型 (`#!cpp vector`)

        `#!cpp vector` 是一个可以存储点 `#!cpp (x, y, z)` 的坐标的变量。如果您不知道这意味着什么，只需将其视为存储三个不同的 `#!cpp float` 值的变量即可。第一个值称为 “X 分量”，第二个值称为 “Y 分量”，最后一个值称为 “Z 分量”。

        用法：`#!cpp vector v = vector(1.2, 2.3., 3.2);` 这声明了一个名为 `v` 的 `#!cpp vector` 类型变量，它表示坐标为 `#!cpp (1.2, 2.3, 3.2)` 的点。

    请记住，您的变量名称几乎可以是任何英文内容！但是，这并不意味着您应该只使用一个或几个字母作为变量名称。变量名称的选择应能够代表或暗示变量的用途。对变量进行命名，使其具有直观意义是一种很好的编程实践。

4.  我如何更改变量的实际值？

    ```cpp
    void main() {


      // 创建变量时只需指定一次变量的数据类型。
      // 这种“第一次”创建称为“变量声明”或“初始化”。
      int my_var = 20;

      // 这样，当你改变变量的值时，
      // 你不需要再次声明它是一个整数
      my_var = 30;

      // 您也可以将变量设置为彼此相等。
      int my_var2 = my_var;

      // 请注意，变量只能更改为类似数据类型的另一个值。
      // 而以下行将声明为 “int” 的变量赋予了 "string" 的值
      // 这意味着它是错误的：
      my_var = "this is a string";

      // 尝试初始化没有数据类型的变量也是
      // 错误的：
      my_var3 = "this string cannot be initalised since the data type is missing!";

      float my_var4 = my_var;
    }

    ```

    更改变量存储的值的过程称为“赋值”。所以在上面的例子中，

    1. 我们首先将 `my_var` 初始化为 `#!cpp 20`。
    2. 然后我们将值 `#!cpp 30` 赋给 `my var`。
    3. 然后我们初始化另一个名为 `my_var2` 的变量，其值等于 `my_var` 的值。
    4. 然后我们尝试将字符串 `#!cpp "this is a string"` 分配给 `my_var`，但由于 `my_var` 是一个整数，它不能存储字符串，所以这实际上会抛出一个错误。想想看，你不能把水放在纸袋里，纸袋不是用来储存水的！

        此规则有一个例外：

        ```cpp
        void main() {
          int a = 10;
          float b = 20.5;

          // 唯一可以将一种数据类型分配给另一种类型的情况
          // 是从整数转换为浮点数时
          float c = a;

          // 这将在游戏聊天中显示 10.0
          xsChatData("" + c);

          // 或者从浮点数转换为整数时。
          // 但是，由于整数无法存储小数部分，
          // 因此这部分将被丢弃！
          int d = b;

          // 这将在游戏聊天中显示 20
          xsChatData("" + d);
        }

        ```

    5. 最后，我们尝试初始化一个名为 `my_var3` 的新变量，但我们尚未指定数据类型！这也会抛出一个错误。想想看，如果你想储存水，你需要指定你想用纸袋还是水瓶。

5.  我可以创建一个值无法更改的变量吗？

    是的！ 使用单词 `#!cpp const` 初始化变量将使其成为常量，并且您将无法更改其值。

    用法：`#!cpp const int a = 10;`

    如果您现在尝试更改 `a` 的值，您将收到错误。

### 2.3. 变量命名规则和约定：

命名变量时必须遵循一些规则。 他们是：

1. 变量命名只能使用字母、数字和下划线。

2. 变量名不能以数字开头。

3. 变量名称 `区分大小写`。这意味着 `a` 和 `A` 是两个不同的变量名！

4. 变量名不能是关键字。关键字是任何编程语言中具有特殊含义的保留字！例如，`#!cpp int` 是 XS 中的关键字，因为它用于声明 `#!cpp int` 数据类型的变量。

以上这些是唯一您必须遵守的“法律”，但所有程序员都同意遵循一些约定或*不成文的规则*，以使他们的代码更具可读性和更清晰。

1.  当您的变量名只有一个单词时，通常采用全小写字母。例如 `#!cpp int radius = 10;` 或 `#!cpp string name = "Syser";`。

2.  当您的变量名由多个单词组成时，通常采用一种称为“驼峰式命名法”的特殊大小写形式。驼峰式大小写是指除第一个单词外的每个单词的第一个字母都大写。例如：`#!cpp float gearRatio = 2.2;` 或 `#!cpp string firstName = "Bruce";` 或 `#!cpp string lastName = "Wayne";`。

3.  当您的变量实际上仅存储永不变更的常量值时，通常使用大写字母，并且单词之间用下划线分隔。 例如： `#!cpp float PI = 3.14159;` 或 `#!cpp float GOLDEN_RATIO = 1.61803;`。

    !!! info "信息"

         文件 `Constants.xs` 中的常量是另一种命名规则，这种规则是以小写的“c”开头的驼峰式命名法，

         例如：`#!cpp const int cAttributeGold = 3;`

4、变量名应准确、易记。也就是说，他们应该能向临时接触该代码的程序员表明他们的目的。不鼓励使用单字母变量名，除非它是一次性变量或临时变量。

### 2.4. 操作

现在我们知道如何存储和更改变量的值，那么我们可以用它们做什么呢？

#### 2.4.1. 算术运算

我们可以用数字做的最明显的事情就是用它们做算术。XS 脚本支持以下五种算术运算：

1.  加法：`#!cpp a + b` 给出两个变量 `a` 和 `b` 的和。
2.  减法：`#!cpp a - b`给出两个变量 `a` 和 `b` 的差值。
3.  乘法：`#!cpp a * b` 给出两个变量 `a` 和 `b` 的乘积。

    例程:

    ```cpp
    void main() {
      int a = 69;
      int b = 420;

      // 这将在游戏中显示 489 聊天 (69 + 420 = 489)
      xsChatData("result of 420 + 69 = " + (a + b));

      // 这将在游戏中显示 351 聊天 (420 - 69 = 351)
      xsChatData("result of 420 - 69 = " + (b - a));

      // 这将在游戏中显示 28980 聊天 (420 * 69 = 28980)
      xsChatData("result of 420 * 69 = " + (a * b));
    }

    ```

4.  除法：`#!cpp a / b` 给出 `a` 除以 `b` 的商。

    请注意，在编程中，除法对于整数和浮点数的工作方式很奇怪：

    对于 `#!cpp int`，它执行我们所说的“整数除法”：

    `#!cpp 5 / 2 = 2`

    `#!cpp 17 / 6 = 2`

    基本上，当您对整数进行正常除法时，答案会将任何小数部分（向下）舍去。

    对于 `#!cpp float`，它会按照您的预期执行常规除法：

    `#!cpp 5.0 / 2.0 = 2.5`

    `#!cpp 17.0 / 6.0 = 2.83333`

    这将得到精确的除法结果。

    如果混合使用 `#!cpp float` 和 `#!cpp int` 会怎样？在这种情况下，使用常规除法。

5.  取模：`#!cpp a % b` 给出 `a` 除以 `b` 时的余数。

    !!! bug "运算结果的数据类型"

        由于目前的一个 Bug，任何操作的结果的数据类型都由操作中使用的第一个数字决定。这意味着 `#!cpp 9 * 5.5` 的计算结果为 `#!cpp 49`，而不是 `#!cpp 49.5`。但是，`#!cpp 5.5 * 9` 将正确计算为 `#!cpp 49.5`。请注意，这是 XS 本身的错误，可能会在未来的更新中修复

    例程：

    ```cpp
    void main() {

      // 这将在游戏中显示 2 聊天（5 / 2 = 2.5，但，这是整数除法！
      // 所以向下舍入为 2）
      xsChatData("result of 5 / 2 = " + (5 / 2));

      // 这将在游戏中显示 2 聊天（17 / 6 = 2.833，但，这是整数除法！
      // 所以向下舍入为 2）
      xsChatData("result of 17 / 6 = " + (17 / 6));

      // 这将在游戏中显示 2.5 聊天（由于被除数是浮点数，
      // 因此浮点除法将给出精确值）
      xsChatData("result of 5.0 / 2 = " + (5.0 / 2));

      // 这将在游戏中显示 2 聊天（由于被除数是整数，
      // 因上文所述 Bug，整数除法被执行）
      xsChatData("result of 5 / 2.0 = " + (5 / 2.0));

      // 这将在游戏中显示 5 聊天（17 % 6 = 5）
      xsChatData("result of 17 % 6 = " + (17 % 6));

      // 这本应该在游戏中显示 0.5 聊天（2.5 % 1 = 0.5）
      xsChatData("result of 2.5 % 1 = " + (2.5 % 1));
      // 由于目前存在 Bug，实际上会显示 0.0
      // 小数求模目前无法正常工作。
    }

    ```

    此外，当使用 `xsChatData` 测试内容时，请注意以下一些怪异杂项：

    ```cpp
    void main() {
      // 请注意，聊天数据不会连续多次发送相同的内容，
      // 这意味着如果两次计算具有相同的结果，
      // 则仅显示第一个
      xsChatData("this is shown only once");
      xsChatData("this is shown only once");
      xsChatData("this is shown only once");
      xsChatData("this is shown only once");

      xsChatData("this is shown twice");
      xsChatData("this will make them non consecutive");
      xsChatData("this is shown twice");
    }

    ```

    解决这个问题的方法是在每条消息的开头使用唯一的数字或字母，这样即使消息的内容相同，数字也不同，以便显示正确的次数

#### 2.4.2. 赋值运算

请记住，当我们在编程中使用 `#!cpp =` 符号时，它不是数学相等语句。它实际上告诉我们正在为变量赋值。因此，当您看到类似 `#!cpp a = a + 1;` 的内容时，它仅表示给变量 `a` 的值加 `#!cpp 1`。您正在将值 `#!cpp a + 1` 赋给 `a`。再次强调，这不是一个数学等式陈述，而是一个赋值操作。

#### 2.4.3. 后缀运算

如果您想将变量的值增加或减少 1，一种方法是编写 `#!cpp a = a + 1;` 或 `#!cpp a = a - 1;`，不过还有另一种方法是编写 `#!cpp a++;` 或 `#!cpp a--;`。

```cpp
void main() {
  int a = 10;

  // 将 a 的值增加到 11
  a++;

  // 将 a 的值减少回 10
  a--;
}

```

#### 2.4.4. 关系运算

关系运算使我们能够将一个数字与另一个数字进行比较。通过这些，您可以了解一个变量是否大于另一个变量、两个变量是否相等等等。

如果有两个数字
$\textcolor{var(--set-color)}{\text{A}}$ 和 $\textcolor{var(--set-color)}{\text{B}}$
，并且问你
“$\text{是否} \; \textcolor{var(--set-color)}{\text{A}} \; \textcolor{var(--function-color)}{\text{大于}} \; \textcolor{var(--set-color)}{\text{B}}$？”
那么你只有两个可能的答案，是或否。同样，如果问你
“$\text{是否} \; \textcolor{var(--set-color)}{\text{A}} \; \textcolor{var(--function-color)}{\text{等于}} \; \textcolor{var(--set-color)}{\text{B}}$？”
那么这个问题也只有两个答案，是或否。

每当您使用关系运算符时，就像问上述问题一样。那么计算机如何回答这样的问题呢？回想上文，布尔（`#!cpp bool`）数据类型可以是真（`#!cpp true`）或假（`#!cpp false`），计算机正是通过这个来回答的！因此，所有关系运算的答案都是布尔值。

1. `#!cpp a < b` 这会检查数字 `a` 是否小于 `b`。如果是，则表达式的计算结果为 `#!cpp true`，否则计算结果为 `#!cpp false`。例如:

    ```cpp
    // 这将打印“5 < 10 : 1”
    xsChatData("5 < 10 : " + (5 < 10));
    // 请记住，在编程中，1 与 true 相同

    ```

2. `#!cpp a > b` 这会检查数字 `a` 是否大于 `b`。如果是，则表达式的计算结果为 `#!cpp true`，否则计算结果为 `#!cpp false`。例如：

    ```cpp
    // 这将打印“5 > 10 : 0”
    xsChatData("5 > 10 : " + (5 > 10));
    // 请记住，在编程中，0 与 false相同

    ```

3. `#!cpp a <= b` 这会检查数字 `a` 是否小于或等于 `b`。如果是，则表达式的计算结果为 `#!cpp true`，否则计算结果为 `#!cpp false`。例如：

    ```cpp
    // 这将打印“5 <= 10 : 1”
    xsChatData("5 <= 10 : " + (5 <= 10));

    // 这将打印“10 <= 10 : 1”
    xsChatData("10 <= 10 : " + (10 <= 10));

    ```

4. `a >= b` 这会检查数字 `a` 是否大于或等于 `b`。如果是，则表达式的计算结果为 `#!cpp true`，否则计算结果为 `#!cpp false`。例如：

    ```cpp
    // 这将打印“5 >= 10 : 0”
    xsChatData("5 >= 10 : " + (5 >= 10));

    // 这将打印“10 >= 10 : 1”
    xsChatData("10 >= 10 : " + (10 >= 10));

    ```

5. `#!cpp a == b` 这会检查数字 `a` 是否等于 `b`。如果是，则表达式的计算结果为 `#!cpp true`，否则计算结果为 `#!cpp false`。例如：

    ```cpp
    // 这将打印“5 == 10 : 0”
    xsChatData("5 == 10 : " + (5 == 10));

    // 这将打印“10 == 10 : 1”
    xsChatData("10 == 10 : " + (10 == 10));

    ```

6. `#!cpp a != b` 这会检查数字 `a` 是否不等于 `b`。如果是，则表达式的计算结果为 `#!cpp true`，否则计算结果为 `#!cpp false`。例如：

    ```cpp
    // 这将打印“5 != 10 : 1”
    xsChatData("5 != 10 : " + (5 != 10));

    // 这将打印“10 != 10 : 0”
    xsChatData("10 != 10 : " + (10 != 10));

    ```

!!! Note "字符串的关系运算符"

    这些关系运算符也适用于 `#!cpp string` 值，例如 `#!cpp a < b` 检查 `a` 是否按字母顺序位于 `b`之前。

例程：

```cpp
void main() {

  // 对于数字:
  int a = 10;
  float b = 20.0;
  int c = 30;

  // 这将显示聊天 1
  xsChatData("a < b is " + a < b);

  // 这将显示聊天 0
  xsChatData("b > c is " + (b > c));

  // 这将显示聊天 0
  xsChatData("(a + b) == b is" + ((a + b) == b));

  // 这将显示聊天 1
  xsChatData("(a + b) >= c is" + ((a + b) >= c));

  // 这将显示聊天 1
  xsChatData("b <= c is " + (b <= c));

  // 对于字符串:
  string str1 = "ball";
  string str2 = "apple";
  string str3 = "cat";
  string str4 = "cat";

  // 这将在游戏中显示 0 聊天
  // 这是因为按字母顺序，str1 不位于 str2 之前
  xsChatData("str1 < str2 is " + (str1 < str2));

  // 这将在游戏中显示 1 聊天
  // 这是因为按字母顺序，str2 位于 str3 之前
  xsChatData("str3 > str2 is " + (str3 > str2));

  // 这将显示聊天 true
  xsChatData("str3 == str4 is " + (str3 == str4));

  // 这将显示聊天 ttrue
  xsChatData("str1 != str2 is " + (str1 != str2));
}

```

#### 2.4.5. 逻辑运算

如果完成一项任务需要两个或更多的东西，我们可以说“需要这个**与**那个才能完成该任务”。例如：

要给某人写电子邮件，您必须有
“$\textcolor{var(--set-color)}{\text{一台计算机}} \; \textcolor{var(--function-color)}{\text{与}} \; \textcolor{var(--set-color)}{\text{可用的互联网}}$”

要画东西，你必须有
“$\textcolor{var(--set-color)}{\text{纸}} \; \textcolor{var(--function-color)}{\text{与}} \; \textcolor{var(--set-color)}{\text{颜料}} \; \textcolor{var(--function-color)}{\text{与}} \; \textcolor{var(--set-color)}{\text{画笔}}$”

类似地，如果完成一项任务需要一件或多件事情，我们会说“需要这个**或**那个才能完成该任务”。例如：

要玩电子游戏，您需要有
“$\textcolor{var(--set-color)}{\text{一台计算机}} \; \textcolor{var(--function-color)}{\text{或}} \; \textcolor{var(--set-color)}{\text{一个游戏机}}$”
请注意，如果您同时拥有两者，您仍然可以玩电子游戏！

要画东西，你必须有
“$\textcolor{var(--set-color)}{\text{一支铅笔}} \; \textcolor{var(--function-color)}{\text{或}} \; \textcolor{var(--set-color)}{\text{一支钢笔}} \; \textcolor{var(--function-color)}{\text{与}} \; \textcolor{var(--set-color)}{\text{一张纸}}$”

逻辑（布尔）运算允许我们提出这些类型的问题，但使用的是布尔值。例如，如果您想问“是否 A 大于 B 和 C？”，需要布尔逻辑。

1.  逻辑**与**：用于检查两个或多个布尔值是否同时为真（`#!cpp true`）。

    用法：`#!cpp a && b`（此处，`a` 和 `b` 是逻辑变量）

    这会检查 `a` **与** `b` 是否都为真（`#!cpp true`）。如果是，则表达式的计算结果为真（`#!cpp true`），否则计算结果为假（`#!cpp false`）。

    `#!cpp a && b` 的每个输入和输出组合都可以写在一个表中：

    | **a** | **b** | **a && b** |
    | :---: | :---: | :--------: |
    | false | false |   false    |
    | false | true  |   false    |
    | true  | false |   false    |
    | true  | true  |    true    |

    !!! Tip "提示"

        运算符 **与** 不仅限于两个变量。任意数量的变量都可以通过 **与** 连接在一起。
        例如：`#!cpp a && b && c && d`。要使该表达式计算结果为真，`a`, `b`, `c` 和 `d` 都必须为真。
        作为读者的练习，请编写一个列出该表达式的输入和输出的每种组合的表格。

2.  逻辑**或**：用于检查一个或多个布尔值是否为真（`#!cpp true`）。

    用法：`#!cpp a || b` （此处，`a` 和 `b` 是逻辑变量）

    这会检查 `a` **或** `b` 是否为真（`#!cpp true`）。如果其中之一是，则表达式的计算结果为真（`#!cpp true`），否则计算结果为假（`#!cpp false`）。

    `#!cpp a || b` 的每个输入和输出组合都可以写在一个表中：

    | **a** | **b** | **a \|\| b** |
    | :---: | :---: | :----------: |
    | false | false |    false     |
    | false | true  |     true     |
    | true  | false |     true     |
    | true  | true  |     true     |

    !!! Tip "提示"

        运算符 **或** 不仅限于两个变量。任意数量的变量都可以通过 **或** 连接在一起。
        例如：`#!cpp a && b && c && d`。要使该表达式计算结果为真，只需 `a`, `b`, `c` 和 `d` 其中之一为真。
        作为读者的练习，请编写一个列出该表达式的输入和输出的每种组合的表格。

运算符 **与** 和运算符 **或** 可以在同一表达式中一起使用。例如：

`#!cpp (a || b) && c`：要使该表达式为真（`#!cpp true`），`a` 或 `b` 和 `c` 必须为真（`#!cpp true`）。

`a || (b && c)`：要使该表达式为真（`#!cpp true`），`a` 必须为真（`#!cpp true`），或者 `b` 和 `c` 必须同时为真（`#!cpp true`）。

!!! Note "注意"

    如果在编写这些表达式时没有使用括号，则表达式将从左到右进行计算。这意味着 `#!cpp a || b && c || d` 与 `#!cpp ((a || b) && c) || d` 含义相同。因此，为了在编写逻辑表达式时非常清楚地表达您的意思，您应该始终适当地使用括号以保持清晰，即使没有必要这样做。

例程：

```cpp
void main() {
  int a = 10;
  int b = 20;
  int c = 30;

  // 这将使 d 为真
  // 因为 a < b 与 c > d 都为真
  bool d = (a < b) && (c > b);

  // 这将使 d 为假
  // 因为 c < b 不为真
  d = (a < b) && (c < b);

  // 这将使 d 为真
  // 因为 a < b 为真
  d = (a < b) || (c < b);

  // 这将使 d 为假
  // 因为 a > b 和 c < b 都不为真
  d = (a > b) || (c < b);
}

```

#### 2.4.6. 串联

当两个字符串连接形成一个新字符串时，称为串联。其他数据类型也可以与字符串连接。

例程：

```cpp
void main() {
  string a = "this is ";
  string b = "string concatenation!";
  int c = 11;
  float d = 5.5;
  bool e = true;
  vector v = vector(1, 2, 3);

  // 发送聊天 "this is string concatenation! 11 5.5 1 (1.0, 2.0, 3.0)"
  xsChatData(a + b + " " + c + " " + d + " " + e + " " + v);
  // 注意，true 和 false 也分别用 1 和 0 表示！
}

```

#### 2.4.7. 向量运算

在 XS 中操作向量是通过一种特殊的方式完成的：

1.  初始化向量：

    我们已经看到过这是如何完成的：`#!cpp vector v = vector(1, 2, 3);`

    !!! warning "向量初始化中不能有变量"

        由于某些原因，目前我们无法在 `#!cpp vector()` 中使用变量来初始化向量；
        这可能是一个 bug，将在 XS 的未来版本中修复。

    例程：

    ```cpp
    void main() {
      float x = 1.0;
      float y = 2.0;
      float z = 3.0;

      vector myVector = vector(x, y, z); // 不起作用，谢谢决定版

      // 或者，可以这样：
      vector myVector = cInvalidVector;
      myVector = xsVectorSetX(myVector, x); // 设置向量的 x 分量
      myVector = xsVectorSetY(myVector, y); // 设置向量的 y 分量
      myVector = xsVectorSetZ(myVector, z); // 设置向量的 z 分量

      // 或者，甚至更短的方法来做到这一点：
      myVector = xsVectorSet(1, 2, 3);

      // 这里 cInvalidVector 是 XS 识别的预定义常量，
      // 它是向量 (-1, -1, -1)
      // 类似地，cOriginVector 是 XS 识别的预定义常量，
      // 它是向量 (0, 0, 0）
    }

    ```

2.  获取向量的 X、Y 和 Z 分量：

    向量的 X、Y 和 Z 分量可以按如下方式访问：

    ```cpp
    void main() {
      vector myVector = vector(1, 2, 3);

      float x = xsVectorGetX(myVector); // 给出向量的 x 分量
      float y = xsVectorGetY(myVector); // 给出向量的 y 分量
      float z = xsVectorGetZ(myVector); // 给出向量的 z 分量
    }

    ```

3.  单独设置向量的 X、Y 和 Z 分量：

    向量的 X、Y 和 Z 分量可以如下设置：

    ```cpp
    void main() {
      vector myVector = vector(1, 2, 3);
      myVector = xsVectorSetX(myVector, 10); // 设置向量的 x 分量
      myVector = xsVectorSetY(myVector, 20); // 设置向量的 y 分量
      myVector = xsVectorSetZ(myVector, 30); // 设置向量的 z 分量
    }

    ```

    请注意，不必同时更改所有 3 个分量，您可以根据需要选择仅更改其中一个。

4.  设置整个向量：

    如果您想要更改向量的所有 3 个分量，则可以一次性完成，而不是像上面那样分 3 行来完成：

    ```cpp
    void main() {
      vector myVector = vector(1, 2, 3);
      myVector = xsVectorSet(10, 20, 30);
    }

    ```

5.  获取向量的模长：

    向量的模长可以通过以下方式获得：

    ```cpp
    void main() {
      vector myVector = vector(1, 2, 3);
      float length = xsVectorLength(myVector);
    }

    ```

    !!! note "注意"

        数学上，向量的模长由下式给出：$\sqrt{x^2+y^2+z^2}$

6.  归一化向量：

    通过对给定向量进行归一化，得到沿给定向量方向的单位向量：

    ```cpp
    void main() {
      vector myVector = vector(1, 2, 3);
      vector unitVectorAlongMyVector = xsVectorNormalize(myVector);
    }

    ```

    !!! note "注意"

        在数学上，归一化向量由下式给出：$\left(\cfrac{x}{\sqrt{x^2+y^2+z^2}}, \cfrac{y}{\sqrt{x^2+y^2+z^2}}, \cfrac{z}{\sqrt{x^2+y^2+z^2}}\right)$

### 2.5. 流程控制语句

流程控制语句有两种类型：

#### 2.5.1. 条件语句

生活中有时您需要做出决定，而这些决定取决于某些条件。例如，假设您在课堂上，那么您可能需要做出的决定是：

$\textcolor{var(--function-color)}{\text{如果}} \; \textcolor{var(--set-color)}{\text{你有笔，}} \; \textcolor{var(--function-color)}{\text{则}} \; \text{可以在纸上写字，} \; \textcolor{var(--function-color)}{\text{否则}} \; \text{借一支笔}$

同样，在编写脚本时，可能需要在代码中的某些点做出决定。条件语句是决策语句，可用于根据给定条件选择要执行的指令集。XS 支持两种类型的条件语句：

1.  `#!cpp if else if` 语句

    每当您需要脚本做出决定时，都会使用 `#!cpp if else` 语句。如果（`#!cpp if`）条件为真，它就执行某一组指令，否则（`#!cpp else`）它就执行另一组指令。

    用法：

    ```cpp
    void main() {
      int a = 10;
      int b = 20;

      // if (逻辑表达式 / 变量 / 常量)
      if (b > a) {

        // 如果上述条件为真则执行：
        xsChatData("does one thing");
        xsChatData("b > a confirmed!");
      } else {

        // 如果上述条件不为真则执行：
        xsChatData("does another thing");
        xsChatData("b <= a confirmed!");
      }
    }

    ```

    任何写在大括号 `{}` 内的内容都被称为代码“块”。在 `#!cpp if` 下编写的代码块称为该 `#!cpp if` 的“主体”。

    如果只有一条指令需要在 `#!cpp if` 或 `#!cpp else` 内运行，则可以省略大括号 `{}`：

    ```cpp
    void main() {
      int a = 10;
      int b = 20;
      if (b > a)
        xsChatData("does only one thing");
      else
        xsChatData("does only another thing");
    }

    ```

    `#!cpp if` 语句不需要每次都跟有 `#!cpp else` 语句：

    ```cpp
    void main() {
      int a = 10;
      int b = 20;
      if (b > a)
        xsChatData("doesn't do anything if the conditon is false");
    }

    ```

    如果您需要检查多个条件并针对每种情况执行单独的操作怎么办？这时你应该使用`#!cpp if else if` 语句！

    ```cpp
    void main() {
      int a = 10;
      int b = 20;
      if (b > a)
        xsChatData("b > 20");
      else if (b == 20)
        xsChatData("b == 20");
      else
        xsChatData("no condition is true");
    }

    ```

    !!! Note "注意"

        在上面的示例中，`#!cpp (b > a)` 和 `#!cpp (b == 20)` 条件均为真。然而，在`#!cpp if else if` 语句中，仅执行一个指令分支。哪个条件优先取决于您编写它们的顺序。因此，在这种情况下，`#!cpp "b > 20"` 将在屏幕上显示，因为这是第一个为真的条件。

    从技术上讲，每当一个条件变为真并且执行其指令分支时，所有剩余的条件都会被跳过，也不会进行计算。

    ???+ Question "实践"

        现在您已经掌握了 `#!cpp if else if` 的强大功能，您可否：

        编写一个脚本，在屏幕上显示给定的 3 个变量的最大值。

        准备好后，单击“答案”即可查看解决方案。

        ??? Success "答案"

            ```cpp
            void main() {
              int a = 10;
              int b = 20;
              int c = 30;
              if (a > b && a > c)
                xsChatData("the maximum is a: " + a);
              else if (b > c && b > a)
                xsChatData("the maximum is b: " + b);
              else
                xsChatData("the maximum is c: " + c)
            }

            ```

2.  `#!cpp switch-case` 语句

    `#!cpp switch-case` 是一种分支结构，当您想要根据变量的值执行几项不同的操作时使用。

    例程：

    ```cpp
    void main() {
      int a = 10;
      switch (a) {
      case 10: {
        xsChatData("if(a == 10)");
        xsChatData("do this");
      }
      case 20: {
        xsChatData("else if(a == 20)");
        xsChatData("do this");
      }
      default: {
        xsChatData("else");
        xsChatData("do this");
      }
      }
    }

    ```

    这与以下操作等价：

    ```cpp
    void main() {
      int a = 10;
      if (a == 10) {
        xsChatData("if(a == 10)");
        xsChatData("do this");
      } else if (a == 20) {
        xsChatData("else if(a == 20)");
        xsChatData("do this");
      } else {
        xsChatData("else");
        xsChatData("do this");
      }
    }

    ```

    与 `#!cpp if else` 类似，如果只有一条指令要执行，大括号 `{}` 可以省略：

    ```cpp
    void main() {
      int a = 10;
      switch (a) {
      case 10:
        xsChatData("if(a == 10) do this");
      case 20:
        xsChatData("else if(a == 20) do this");
      default:
        xsChatData("else do this");
      }
    }

    ```

#### 2.5.2. 循环语句

生活中有时你需要在某些条件下反复坚持做某件事。例如，假设您正在玩游戏，并且陷入了一场不断死亡的 Boss 战中，您正在做的事情可能是：

$\textcolor{var(--function-color)}{\text{当}} \; \textcolor{var(--set-color)}{\text{你还没有打败 Boss，}} \; \text{再试一次}$

如果你想将一些数乘二的结果全部写出来，你可以这样做：

$\textcolor{var(--function-color)}{\text{对}} \; \textcolor{var(--set-color)}{\text{每个}} \; \textcolor{var(--function-color)}{\text{从 1 到 10 之间的}} \; \textcolor{var(--armour-color)}{\text{数}} \; \text{写出 }2 \times \textcolor{var(--armour-color)}{\text{数}}$

同样，在编写脚本时，可能需要多次重复代码的某些部分。循环语句可用于在条件为真时重复执行代码块。

有时需要重复执行相同的语句或只有少数内容发生变化的语句。
循环语句允许我们做到这一点！ XS 支持两种类型的循环：

1.  `#!cpp while` 循环

    只要（当，`#!cpp while`）某些东西为真（`#!cpp true`），就重复执行代码块的语句。这种重复执行同一代码块的过程称为迭代！

    例程：

    ```cpp
    void main() {
      int a = 0;
      while (a < 10) {
        xsChatData("a = " + a);
        a++;
        // 注意 a++ 是将 a 的值加一。

        // 如果你忘记写 a++ 会发生什么？
        // 你的脚本会陷入“无限”循环
        // 并且游戏会崩溃
      }
    }

    ```

    ???+ Question "实践"

        现在您已经掌握了 `#!cpp while` 的强大功能，您可否：

        编写一个脚本，发送以下格式的文本到聊天：

        `1, 2, 4, 7, 11, 16...` 共有 15 项？

        如果您需要帮助，但不想立即看到完整的解决方案，请单击“提示”

        准备好后，单击“答案”即可查看解决方案。

        ??? Info "提示"

            提示：注意这里的格式是，每增加一次，项数也增加 1。第二项是第一项 + 1，第三项是第二项 + 2，以此类推。

        ??? Success "答案"

            ```cpp
            void main() {
              int number = 1;
              int increase = 1;
              while (increase <= 15) {
                xsChatData("number = " + number);
                number = number + increase;
                increase++;
              }
            }

            ```

2.  `#!cpp for` 循环

    `#!cpp for` 语句专门用于遍历一系列值，例如从 `#!cpp 5` 到 `#!cpp 23`

    例程：

    ```cpp
    void main() {
      for (a = 5; < 23) {
        xsChatData("a = " + a);
        // for 循环负责每次将 a 的值加一


        // 你不应该在 for 循环中修改 'a'
      }

      // 如果我想从 10 降到 0 该怎么办？
      // 可以这样：
      for (a = 10; > 0) {
        xsChatData("a = " + a);
        // 这里 for 循环自动计算出
        // 您需要减少 a 而不是增加它。
      }
    }

    ```

我们如何选择使用哪个循环？ 首先，`#!cpp while` 循环可以完成 `#!cpp for` 循环可以做的所有事情。然而，`#!cpp while` 循环在性能上比 `#!cpp for` 循环慢得多！如果可能的话，您应该坚持**始终**使用 `#!cpp for` 循环！`#!cpp for` 循环还负责增加或减少迭代变量，这意味着您不会像`#!cpp while` 循环一样意外地导致“无限”循环。

### 2.6. 模块化编程

#### 2.6.1. 函数

假设您正在看电视。 每次你想改变频道时，你都会使用同一个遥控器。如果每次想换频道都得重新制作一个遥控器，那就很不方便了。同样，在编写脚本时，您可能想要编写一段需要在脚本的不同部分中多次重复使用的代码。函数使我们能够做到这一点！

函数是一段代码，通过输入一些值并使用它们来执行给定的任务。您之前已经见过一个函数了！`#!cpp xsChatData(string str);` 实际上是一个输入 `#!cpp string` 并在游戏中显示聊天的函数。

另一个有用的函数是 `#!cpp sqrt(float number);`，它计算一个值的平方根。

用法：`#!cpp float a = sqrt(4);`

这会将值 `#!cpp 2.0` 赋给 `a`。

这里需要注意的一个有趣的事情是，某些函数“返回给你”一个值，例如 `#!cpp sqrt(5);` 会“返回给你” $\approx$ `#!cpp 2.24`。

函数“返回给你”值的这种属性事实上被正式称为函数“返回”值。并非所有函数都会这样做，例如 `#!cpp xsChatData("my message");` 只是在屏幕上显示该消息并且不返回任何值。函数可以返回任何数据类型的值。

每个函数还接受一组输入。`xsChatData` 接受一个字符串，`sqrt` 接受一个浮点数。函数可以采用的输入集被正式称为“参数”。

这些是 XS 中提供给我们直接使用的内置函数，但我们也可以定义自己的函数。这是 XS 中定义函数的方式：

用法：

```cpp
returnType functionName(dataType parameter1 = defaultValue,
                        dataType parameter2 = defaultValue) {
  return (value);
  // value 必须与 returnType 的数据类型相同
}

```

如果不清楚这意味着什么，请先了解一下这个用法，然后看下面的示例：

```cpp

// 这是一个自定义函数，返回两个整数中的最大值。
int max(int a = 0, int b = 0) {

  // 开头的 “int” 告诉我们这个函数将返回一个整数值，


  // max 是函数的名称

  // 该函数接受两个整数值 “a” 和 “b”
  // 默认情况下，“a” 和 “b” 初始化为 0，
  // 这意味着如果使用此函数的人未指定 “a” 和 “b” 使用什么值，
  // 则将使用 0。


  // return 语句告诉函数“返回”指定的任何值。
  if (a > b)
    return (a);
  return (b);


  // 等等，为什么我们不在这里写一个 else 语句呢？
  // 函数总是在遇到 “return” 语句时立即终止。
  // 这条语句告诉函数停止做它正在做的事情并“返回”指定的值。
  // 这就是为什么不必在这里编写 else，
  // 因为如果 a > b 那么第二个 return 语句将不会被执行
}

void main() {
  // 这就是该函数的使用方式：
  xsChatData("max " + max(10, 20));
  // 函数中变量的值为 10 和 20。
}

// 等等，这个 “main” 不也是到目前为止我们一直在使用的函数吗？
// 是的！“void” 表示它不返回任何值

// 由于 “main” 后面的括号内没有任何内容，
// 因此它也不接受任何参数

```

函数名称遵循与变量名称相同的规则和约定。

本指南的[函数参考](../functions/ "跳转至：XS 脚本语言 > 函数参考")部分列出了所有内置 XS 函数及其描述。

#### 2.6.2. 文件结构

当您编写 XS 脚本时，最好将函数分组并将它们放入适当命名的文件中。

例如，如果您有一个进行向量计算的 XS 脚本，像加法、减法、点积或叉积，或其他向量运算，那么您可能希望在 XS 脚本之外的更多用途中使用它。

复制每个您想要使用的 XS 脚本中的所有函数过于乏味，并且是一种糟糕的编程实践。我们可以做的是编写另一个名为 `VectorOperations.xs` 的 XS 脚本，然后在需要矢量操作的每个其他脚本中“调用”该脚本。

例如：

如果我在同一文件夹中有两个文件 `test.xs` 和 `VectorOperations.xs`，则：

```cpp
// test.xs

include "./VectorOperations.xs";
// “./VectorOperations.xs” 是 VectorOperations.xs 文件
// 对于 text.xs 文件的相对路径。
// 这也可以是文件的绝对路径。
// 如果您不知道 绝对/相对 路径是什么，
// 使用搜索引擎简单搜索可以了解有关它们的更多信息。

void main() {
  vector a = vector(1, 2, 3);
  vector b = vector(3, 2, 1);
  xsChatData("dot: " + dotProduct(a, b));
  xsChatData("cross: " + crossProduct(a, b));
  xsChatData("add: " + add(a, b));
}

```

```cpp
// VectorOperations.xs

int dotProduct(vector a = cInvalidVector, vector b = cInvalidVector) {
  return (xsVectorGetX(a) * xsVectorGetX(b) +
          xsVectorGetY(a) * xsVectorGetY(b) +
          xsVectorGetZ(a) * xsVectorGetZ(b));
}

vector crossProduct(vector a = cInvalidVector, vector b = cInvalidVector) {
  vector product = cInvalidVector;
  product = xsVectorSetX(product, xsVectorGetY(a) * xsVectorGetZ(b) -
                                      xsVectorGetZ(a) * xsVectorGetY(b));
  product = xsVectorSetY(product, 0 - xsVectorGetX(a) * xsVectorGetZ(b) +
                                      xsVectorGetZ(a) * xsVectorGetX(b));
  product = xsVectorSetZ(product, xsVectorGetX(a) * xsVectorGetY(b) -
                                      xsVectorGetY(a) * xsVectorGetX(b));
  return (product);
}

vector add(vector a = cInvalidVector, vector b = cInvalidVector) {
  vector addition = cInvalidVector;
  addition = xsVectorSetX(addition, xsVectorGetX(a) + xsVectorGetX(b));
  addition = xsVectorSetY(addition, xsVectorGetY(a) + xsVectorGetY(b));
  addition = xsVectorSetZ(addition, xsVectorGetZ(a) + xsVectorGetZ(b));
  return (addition);
}

```

这样，对于每个需要使用 `VectorOperations.xs` 的文件，您只需编写 `#!cpp include "相对/或/绝对/路径/到/文件.xs";` 就可以在该文件中使用您在其中编写的所有函数!

像这样写的代码：

1. 每个单独的操作都有其自己的功能
2. 每组类似的函数都在自己的文件中，

被称为模块化代码！像这样编写代码被认为是一种非常非常好的编程实践。这样，其他阅读您代码的人就可以轻松阅读和理解您的代码并了解全局！

然而...目前存在一个 Bug（谢谢决定版 11），导致 XS 脚本无法正确传输给大厅中的其他玩家。目前，一种解决方法是手动为每个人提供所需的 XS 脚本。

### 2.7. 变量的作用域

每个变量都有一个范围，即可以使用它的代码“区域”。例如，在变量初始化之前你不能使用它，这是没有意义的！

```cpp
void main() {
  a++; // 等等，a 还不存在！你不可以这么做。
  int a = 10;
}

```

同样，在一个函数内部初始化的变量只能在该特定函数中使用，并且不能存在于该函数之外。这些类型的变量称为局部变量。例如：

```cpp
void main() { int a = 10; }
void anotherFunction() {
  a++; // 等等，a 不存在于本函数之中！你不可以这样做。
  // 实际上您可以在另一个函数内部声明另一个名为 a 的变量：
  int a = 44;
  // 这个 a 与 main(); 中的 a 完全不同并且独立
}

```

如果您想要一个能在函数之间共享的变量怎么办？像这样的变量必须在所有函数之外声明。这样的变量称为全局变量。例如：

```cpp
int a = 10;
void main() { a++; }
void anotherFunction() { a++; }

```

### 2.8. 数组

数组是一种数据结构，允许您创建一种数据类型的有序编号列表。在每个编号列表中，每个元素都使用其编号进行标识。这个数字称为索引。如果 `a` 是一个整数数组，那么它可能看起来像这样：

| 索引 | 值  |
| :--: | :-: |
|  0   | 23  |
|  1   |  4  |
|  2   | 42  |
|  3   | 32  |
|  4   | 92  |

索引用于标识数组中的元素，每个数组的索引始终从 0 开始。例如：`#!cpp a[2]` 是 `#!cpp 42`。

虽然在大多数编程语言中 `#!cpp a[2]` 是访问数组中元素的方法，但在 XS 中却不是这样。让我们看看 XS 中数组是如何使用的：

为了创建数组，以下函数用于相关数据类型：

```cpp
// 创建一个特定大小的的命名整数数组，每个值都初始化为 defaultValue。
// 返回一个整数数组ID。
int xsArrayCreateInt(int size, int defaultValue, string name);

// 创建一个特定大小的的命名浮点数数组，每个值都初始化为 defaultValue。
// 返回一个浮点数数组ID。
int xsArrayCreateFloat(int size, float defaultValue, string name);

// 创建一个特定大小的的命名布尔数组，每个值都初始化为 defaultValue。
// 返回一个布尔数组ID。
int xsArrayCreateBool(int size, bool defaultValue, string name);

// 创建一个特定大小的的命名字符串数组，每个值都初始化为 defaultValue。
// 返回一个字符串数组ID。
int xsArrayCreateString(int size, string defaultValue, string name);

// 创建一个特定大小的的命名向量数组，每个值都初始化为 defaultValue。
// 返回一个向量数组ID。
int xsArrayCreateVector(int size, vector defaultValue, string name);

```

对于数组的名称，可以使用任何字符串，但所有名称必须是唯一的

所有这些函数都返回一个整数，它是您刚刚创建的数组的 ID。该 ID 用于对数组执行其他操作。您应该将此整数存储在名为 apty 的变量中，以便稍后可以使用该数组。

要从数组中获取特定索引处的值，我们对相关数据类型使用以下函数：

```cpp
// 返回指定数组的指定索引处的整数
int xsArrayGetInt(int arrayID, int index);

// 返回指定数组的指定索引处的浮点数
float xsArrayGetFloat(int arrayID, int index);

// 返回指定数组的指定索引处的布尔值
bool xsArrayGetBool(int arrayID, int index);

// 返回指定数组的指定索引处的字符串
string xsArrayGetString(int arrayID, int index);

// 返回指定数组的指定索引处的向量
vector xsArrayGetVector(int arrayID, int index);

```

如果您尝试访问不存在的数组（无效的 arrayID）或不存在的索引（负索引或大于等于数组长度的索引），则返回数据类型的默认值。这些是：

```cpp
int defaultValue = -1;
float defaultValue = -1.0;
bool defaultValue = false;
string defaultValue = "";
vector defaultValue = vector(0, 0, 0);

```

要设置在数组中的特定索引处的值，我们对相关数据类型使用以下函数：

```cpp
// 设置指定数组中指定索引处的值。
int xsArraySetInt(int arrayID, int index, int value);

// 设置指定数组中指定索引处的值。
int xsArraySetFloat(int arrayID, int index, float value);

// 设置指定数组中指定索引处的值。
int xsArraySetBool(int arrayID, int index, bool value);

// 设置指定数组中指定索引处的值。
int xsArraySetString(int arrayID, int index, string value);

// 设置指定数组中指定索引处的值。
int xsArraySetVector(int arrayID, int index, vector value);

```

请注意，这些 Set 函数每次都会返回 `#!cpp 1`，但这不需要存储在变量中。

为了更改数组的大小：

```cpp
// 调整指定数组的大小。
int xsArrayResizeInt(int arrayID, int newSize);
// 调整指定数组的大小。
int xsArrayResizeFloat(int arrayID, int newSize);
// 调整指定数组的大小。
int xsArrayResizeBool(int arrayID, int newSize);
// 调整指定数组的大小。
int xsArrayResizeString(int arrayID, int newSize);
// 调整指定数组的大小。
int xsArrayResizeVector(int arrayID, int newSize);

```

请注意，这些 Resize 函数每次都会返回 `#!cpp 1`，但这不需要存储在变量中。

`#!cpp int xsArrayGetSize(int arrayID);` 也是一个实用数组函数，它返回指定数组的大小。

### 2.9. 类型转换

类型转换是指将一种数据类型的值“转换”为另一种类似数据类型的值。这就像将存储在一种容器中的物体放入另一种容器中。

例如，当您尝试将 `#!cpp int` 存储在 `#!cpp float` 中时，它会正常工作。这类似于将水储存在瓶子中，然后将瓶子中的水放入烧瓶中。然而，当您尝试将 `#!cpp float` 存储在 `#!cpp int` 中时，`#!cpp float` 的小数部分会丢失！这就像试图将水瓶中的水放入纸袋中一样。有些水会漏出来！

类型转换有两种：

1. 隐式类型转换

    当您将一种类型的值分配给另一种类似的数据类型时，隐式类型转换由脚本自动完成（因此是隐式的）。例如：

    ```cpp
    void main() {
      int a = 5;
      float b = 3.9;
      bool c = true;

      // 隐式类型转换：
      int d = c; // 记住，true 为 1，false 为 0
      float e = c;
      string f = "" + c; // 只有 string f = c 不行

      // 当将 float 类型转换为 int 时，
      // 数字的小数部分会丢失！
      // 请注意，它没有四舍五入，类型转换后 3.9 将变为 3
      int g = b;

      // 除 0 之外的任何值转成布尔值都是 true
      bool h = b;

      string i = "" + b;

      float j = a;

      // 除 0 之外的任何值转成布尔值都是 true
      bool k = a;

      string l = "" + a;
    }

    ```

2. 显式类型转换

    显式类型转换由程序员手动完成（因此是显式的）。例如：

    ```cpp
    void main() {
      float a = 5.5;

      float b = (int)a;    // 将 5.0 赋给 b
      float c = (int)22.5; // 将 22.0 赋给 c
    }

    ```

## 3. 规则

规则是一段代码，可以设置为在整个游戏过程中以设定的时间间隔重复执行。规则始终在函数外部初始化。它的用法如下：

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
