# XS 脚本：初学者指南

_作者：Alian713_

---

## 你是程序员吗？

如果您知道如何用任何语言进行编程，那么您在本页上就是浪费时间！请参阅 [对于程序员](../programmer/ "跳转到：XS 脚本 > 对于程序员")，它是一个更短、更精确的文档，因为 XS 只是另一种具有不同的语法的编程语言。

如果您不是程序员，请不要害怕！您来对地方了，这里可以了解有关 XS 的所有知识！

## 1. 使用 XS 脚本

要使用 XS 脚本：

1.  确保您可以看到文件扩展名。这意味着您计算机上的每个文件都应该有一个类似于 `文件名.扩展名` 的名称。如果您可以看到文件扩展名，请继续执行步骤 2。如果看不到，请按照以下步骤操作：

    1. 按 :material-microsoft-windows: + E
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
2. 在 `地图` 选项卡下，于 `脚本文件名` 字段中键入您创建的 XS 脚本的名称，末尾不带 `.xs`。 例如，如果您的文件名为 `filename.xs`，那么您将在此字段中写入 `filename`。
3. 现在，在编辑器的 `触发` 选项卡下，添加新触发，然后添加新效果。（如果您不知道什么是 触发/效果，请参阅本手册的 `自定义场景：触发：触发基础知识`部分）
4. 从 `效果列表` 中选择 `脚本调用`。
5. 现在，您可以通过在消息框中键入 "function_name_here();" 使用 XS 脚本中的函数。
6. 我们上面创建的 `main()` 函数会在场景被游玩时自动执行。
7. 如果代码没有错误，点击 `E#0：脚本调用` 效果会变成绿色。如果脚本中有错误，将会显示错误消息。
8. 现在测试场景将在上面定义的触发中运行 `脚本调用` 效果，该效果又将运行 XS 脚本中的 `main()` 函数，并且 `30` 将显示在聊天中。

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

    3.  逻辑型 (`bool`)

        `bool` 又称布尔，是一种只能存储真（`#!cpp true`）或假（`#!cpp false`）两个布尔值之一的数据类型。任何是或否问题在某种意义上都是布尔问题，因为只有两个答案，是或否。布尔变量对于条件非常重要，我们稍后会讨论。

        用法： `#!cpp bool a = true;` 这声明了一个名为 `a` 的 `bool` 类型变量，其值为 `#!cpp true`

        !!! note "注意"

            `true` 的值也由 `#!cpp 1` 表示，而 `false` 的值也由 `#!cpp 0` 表示。

    4.  字符串 (`string`)

        `string` 是一个词语、一个句子或一个段落。字符串始终用（半角）双引号括起来。

        用法： `#!cpp string a = "这是一串文本！哈哈";` 这声明了一个名为 `a` 的 `string` 类型变量，其值为 `#!cpp "这是一串文本！哈哈"`

        !!! bug

            上文中的中文字符串实际上无法如此实现，目前版本中不能直接在 `string` 中使用非 ASCII 字符，如果必须要使用，请参阅本手册的 `技巧 > 使用非 ASCII 字符` 部分，它是通过读写文件的方式实现的。

    5.  向量型 (`#!cpp vector`)

        A `#!cpp vector` is a variable that can store the coordinates of a point `#!cpp (x, y, z)`. If you don't know what that means, just take it as a variable that stores three different `#!cpp float` values. The first value is called the "X component", the second value is called the "Y component" and the last value is called the "Z component".

        Usage `#!cpp vector v = vector(1.2, 2.3., 3.2);` This declares a variable of type `#!cpp vector` called `v` that represents a point with coordinates `#!cpp (1.2, 2.3, 3.2)`.

    Remember that your variable names can be almost anything! However, this does not mean that you should just use single letters or alphabets for variable names. Variable names should be chosen such that they represent, or hint to what the purpose of the variable is. Naming your variables such that they make intuitive sense is a good programming practise.

4.  How do I actually change a variable?

    ```cpp
    void main() {
        int my_var = 20;

        // you only need to specify the data type of a variable once
        // when it is created. This "first time" creation is known
        // as "variable declaration" or "initialisation".

        // This way, when you change the value of the variable
        // you don't need to say that it is an integer again
        my_var = 30;

        // you can set variables equal to each other as well.
        int my_var2 = my_var;

        // note that a variable can only be changed to another value
        // of a similar data type. This means that this following line
        // is WRONG:
        my_var = "this is a string";

        // trying to initialise a variable without a data type is also
        // WRONG:

        my_var3 = "this string cannot be initalised since the data type is missing!";

        float my_var4 = my_var;
    }
    ```

    This process of changing the value that a variable stores is called "assignment". So in the above example,

    1. We first initalise `my_var` to `#!cpp 20`.
    2. Then we assign a value of `#!cpp 30` to `my var`.
    3. Then we initialise another variable called `my_var2` whose value is equal to the value of `my_var`.
    4. Then we try to assign the string `#!cpp "this is a string"` to `my_var` but remember that `my_var` is an integer, and it is not capable of storing a string, so this will actually give you an error. Think about it this way, you cannot put water in a paper bag, paper bags are not meant to store water!
       There is an exception to this rule:

    ```cpp
    void main() {
        int a = 10;
        float b = 20.5;

        // the only cases where you can assign one type of data to another
        // is when going from integers to floats
        float c = a;

        // this will show 10.0 in game chat
        xsChatData(""+c);

        // or when going from floats to integers.
        // However, since integers cannot store the fractional part,
        // it is discarded!
        int d = b;

        // this will show 20 in game chat
        xsChatData(""+d);
    }
    ```

    5. Lastly, we try to initialise a new variable called `my_var3` but we have not specified a data type! This will also give you an error. Think about it this way, if you want to store water, you need to specify if you want to use a paper bag or a water bottle.

5.  Can I make a variable whoes value cannot be changed?

    Yes! initialising a variable with the word `#!cpp const` will make it a constant, and you won't be able to change its values.

    Usage: `#!cpp const int a = 10;`

    If you now try to change the value of `a`, you will get an error.

### 2.3. Variable Naming Rules and Conventions:

There are some rules that must be followed when naming a variable. They are:

1. You can only use letters, numbers and underscores to name your variables.

2. A variable name cannot start with a number.

3. Variable names are `CaSe SeNsItIvE`. This means that `a` and `A` are two different variable names!

4. Variable names must not be keywords. A keyword is a reserved word in any programming language that has a special meaning! For example, `#!cpp int` is a keyword in XS because it is used to declare a variable of the `#!cpp int` data type.

While these are the only _laws_ that you absolutely must follow, there are some conventions or _unwritten rules_ that all programmers agree to follow to make their code more readable, and more clear.

1. When you are writing a variable name that is just one word, it is conventional to write it in all small letters. For example `#!cpp int radius = 10;` or `#!cpp string name = "Alian713";`.

2. When you are writing a variable name that consists of more than one word, then it is conventional to write it in a special case known as "camel case". Camel case is where the first letter of every word is capitalised except the first word. For Example: `#!cpp float gearRatio = 2.2;` or `#!cpp string firstName = "Bruce";` or `#!cpp string lastName = "Wayne";`.

3. When you are writing a variable that is supposed to just store the value of a constant, one which you never intend to change, it is conventional to use capital letters and words are separated by underscores. For example: `#!cpp float PI = 3.14159;` or `#!cpp float GOLDEN_RATIO = 1.61803;`.

4. Variable names should be precise and mnemonic. That is, they should indicate to a casual programmer their purpose. Usage of single letter variable names is discouraged unless it is a throwaway or temporary variable.

### 2.4. Operations

Now that we know how to store and change the values of a variable, what can we actually do with them?

#### 2.4.1. Arithmetic Operations

The most obvious thing that we can do with numbers, is do arithmetic with them. XS Scripts support the following five arithmetic operations:

1. Addition: `a+b` this gives you the sum of two variables, `a` and `b`. for example,
2. Subtraction: `a-b` this gives you the difference of two variables, `a` from `b`.
3. Multiplication: `a*b` this gives you the product of two variables, `a` and `b`.

    For example:

    ```cpp
    void main() {
        int a = 69;
        int b = 420;

        // this will chat 489 in game (69+420 = 489)
        xsChatData("result of 420+69 = "+(a+b));

        // this will chat 351 in game (420-69 = 351)
        xsChatData("result of 420-69 = "+(b-a));

        // this will chat 28980 in game (420*69 = 28980)
        xsChatData("result of 420*69 = "+(a*b));
    }
    ```

4. Division: `a/b` this gives you the division of `a` by `b`.

    Note that in programming, division is weird with how it works for integers and floats:

    For `#!cpp int`, it performs what we call "integer division":

    `#!cpp 5/2 = 2`

    `#!cpp 17/6 = 2`

    Basically, you round down any fractional part to your answer when you do normal division for integers.

    For `#!cpp float`, it performs regular division as you would expect:

    `#!cpp 5.0/2.0 = 2.5`

    `#!cpp 17.0/6.0 = 2.83333`

    This gives you the exact result of division.

    What if you mix a `#!cpp float` and an `#!cpp int`? In that case, regular division is used.

5. Modulo: `a%b` this gives you the remainder when dividing `a` by `b`.

    !!! bug "DataType of Result of Operation"
    Due to a bug at the moment, the data type of the answer of any operation is decided by the first number used in the operation. This means that `#!cpp 9*5.5` evaluates to `#!cpp 49` instead of `#!cpp 49.5`. However, `#!cpp 5.5*9` will correctly evaluate to `#!cpp 49.5`. Note that this is a bug in XS itself and will probably be fixed in a future update

    For Example:

    ```cpp
    void main() {
        // this will chat 2 in game (5/2 = 2.5 but remember, this is integer division! so round down to 2)
        xsChatData("result of 5/2 = "+(5/2));

        // this will chat 2 in game (17/6 = 2.833 but remember, this is integer division! so round down to 2)
        xsChatData("result of 17/6 = "+(17/6));

        // this will chat 2.5 in game (since the numerator is a float, float division will give the exact value)
        xsChatData("result of 5.0/2 = "+(5.0/2));

        // this will chat 2 in game (since the numerator is an int, integer division will give the exact value)
        xsChatData("result of 5/2.0 = "+(5/2.0));

        // this will chat 5 in game (17%6 = 5)
        xsChatData("result of 17%6 = "+(17%6));

        // this should chat 0.5 in game (2.5%1 = 0.5)
        xsChatData("result of 17%6 = "+(2.5%1));
        // Due to a bug at the moment, this will actually show 0.0
        // Modulo on fractions does not work properly at this time.
    }
    ```

    Also Additionally, when testing stuff using `xsChatData`, be wary of some quirks that this has:

    ```cpp
    void main() {
        // Note that chat data does not send the same thing multiple consecutively
        // which means if two calculations have the same result, only the first
        // one is shown
        xsChatData("this is shown only once");
        xsChatData("this is shown only once");
        xsChatData("this is shown only once");
        xsChatData("this is shown only once");

        xsChatData("this is shown twice");
        xsChatData("this will make them non consecutive");
        xsChatData("this is shown twice");
    }
    ```

    The way around this is to use a unique number or letter at the start of every message so that even if the content of the message is the same, the number is different so that it gets shown the right amount of times

#### 2.4.2. The Assignment Operation

Remember that when we use the `=` sign in programming, it is not a mathematical equality statement. It actually tells us that we are assigning a value to a variable. So when you see something like `a = a+1;`, this means that you are simply adding `#!cpp 1` to the value of `a`. you are assigning the value `a+1` to `a`. Once again, it is not a mathematical equality statement, it is an assignment.

#### 2.4.3. Postfix Operations

If you want to increase or decrease the value of a variable by one, then writing `a = a + 1;` or `a = a - 1;` is one way to do it. Writing `a++;` or `a--;` is another way to do it.

```cpp
void main() {
    int a = 10;

    // increase the value of a to 11
    a++;

    // decrease the value of a back to 10
    a--;
}
```

#### 2.4.4. Relational Operations

Relational operations allow us to compare one number with another. With these, you can find out if one variable is greater than another or not, if two variables are equal or not, and much more.

If you have two numbers
$\color{yellow} \text{A}$ and $\color{yellow}\text{B}$,
and are asked
"$\text{if} \; \color{yellow}\text{A} \; \color{red} \text{is greater than} \; \color{yellow}\text{B} \color{white}$?"
then you can have only two possible answers, it will either be yes or no. Similarly, if you are asked
"$\text{if} \; \color{yellow}\text{A} \; \color{red} \text{is equal to} \; \color{yellow}\text{B} \color{white}$?"
then this question also has only two answers, yes or no.

Whenever you use a relational operator, it is like asking one of these questions above. Then how does a computer answer a question like this? Remember, a `boolean` data type can either be `true` or `false`, it does exactly this! Thus, the answers to all relational operations give you boolean values.

1. `a < b` This checks if the number `a` is lesser than `b`. If it is, then the expression evaluates to `true`, else it evaluates to `false`.
   For example:

```cpp
// this will print "5 < 10 : 1"
xsChatData("5 < 10 : "+(5 <> 10));
// remember, in programming, 1 is the same as true
```

2. `a > b` This checks if the number `a` is greater than `b`. If it is, then the expression evaluates to `true`, else it evaluates to `false`.
   For example:

```cpp
// this will print "5 > 10 : 0"
xsChatData("5 > 10 : "+(5 > 10));
// remember, in programming, 0 is the same as false
```

3. `a <= b` This checks if the number `a` is lesser than or equal to `b`. If it is, then the expression evaluates to `true`, else it evaluates to `false`.
   For example:

```cpp
// this will print "5 <= 10 : 1"
xsChatData("5 <= 10 : "+(5 <= 10));

// this will print "10 <= 10 : 1"
xsChatData("10 <= 10 : "+(10 <= 10));
```

4. `a >= b` This checks if the number `a` is greater than or equal to `b`. If it is, then the expression evaluates to `true`, else it evaluates to `false`.
   For example:

```cpp
// this will print "5 >= 10 : 0"
xsChatData("5 >= 10 : "+(5 >= 10));

// this will print "10 >= 10 : 1"
xsChatData("10 >= 10 : "+(10 >= 10));
```

5. `a == b` This checks if the number `a` is equal to `b`. If it is, then the expression evaluates to `true`, else it evaluates to `false`.
   For example:

```cpp
// this will print "5 == 10 : 0"
xsChatData("5 == 10 : "+(5 == 10));

// this will print "10 == 10 : 1"
xsChatData("10 == 10 : "+(10 == 10));
```

6. `a != b` This checks if the number `a` is not equal to `b`. If it is, then the expression evaluates to `true`, else it evaluates to `false`.
   For example:

```cpp
// this will print "5 != 10 : 1"
xsChatData("5 != 10 : "+(5 != 10));

// this will print "10 != 10 : 0"
xsChatData("10 != 10 : "+(10 != 10));
```

!!! Note "Relational Operators on Strings"
These relational operators also work on `string` values, for example `a < b` checks if `a` would alphabetically preceed `b`.

For Example:

```cpp
void main() {

    // With numbers:
    int a = 10;
    float b = 20.0;
    int c = 30;

    // this would chat 1
    xsChatData("a < b is "+a < b);

    // this would chat 0
    xsChatData("b > c is "+(b > c));

    // this would chat 0
    xsChatData("(a+b) == b is"+((a+b) == b));

    // this would chat 1
    xsChatData("(a+b) >= c is"+((a+b) >= c));

    // this would chat 1
    xsChatData("b <= c is "+(b <= c));


    // With strings:
    string str1 = "ball";
    string str2 = "apple";
    string str3 = "cat";
    string str4 = "cat";

    // this would chat 0 in game
    // this is because alphabetically, str1 does not come before str2
    xsChatData("str1 < str2 is "+(str1 < str2));

    // this would chat 1 in game
    // this is because alphabetically, str2 comes before str3
    xsChatData("str3 > str2 is "+(str3 > str2));

    // this would cha ttrue
    xsChatData("str3 == str4 is "+(str3 == str4));

    // this would cha ttrue
    xsChatData("str1 != str2 is "+(str1 != str2));
}
```

#### 2.4.5. Boolean Operations

If two or more things are required to do a task, we can say that "this AND that are required to do the task". For example:

To write an email to someone, you must
"$\color{yellow} \text{have a computer} \; \color{red} \text{and} \; \color{yellow} \text{have active internet}$"
To paint something, you must
"$\color{yellow} \text{have a paper} \; \color{red} \text{and} \; \color{yellow} \text{have paint} \; \color{red} \text{and} \; \color{yellow} \text{have a paint brush}$"

Similarly, if only one, or more things are required to do a task we say that "this OR that is needed to do the task". For example:

To play a video game, you need to
"$\color{yellow} \text{own a computer} \; \color{red} \text{or} \; \color{yellow} \text{own a gaming console}$"
Note that you can still play video games if you own both!

To draw something you must
"$\color{yellow} \text{have a pencil} \; \color{red} \text{or} \; \color{yellow} \text{have a pen} \; \color{red} \text{and} \; \color{yellow} \text{have a paper}$"

Boolean operations allow us to ask these sorts of questions but with boolean values instead. For example, if you wanted to ask "is A greater than B and C?" then you require boolean operations.

1. Boolean AND: This is used to check if two or more boolean values are simultaneously `true`.

    Usage: `#!cpp a && b` (Here, `a` and `b` are boolean variables)

    This checks if both `a` **AND** `b` are `true`. If they are, the expression evaluates to `true`, otherwise it evaluates to `false`.

    Every combination of inputs and outputs for `a && b` can be written in a table:

    | **a** | **b** | **a && b** |
    | :---: | :---: | :--------: |
    | false | false |   false    |
    | false | true  |   false    |
    | true  | false |   false    |
    | true  | true  |    true    |

    !!! Tip
    The AND operation is not limited to just two variables. Any number of variables may be AND-ed together.
    For Example: `#!cpp a && b && c && d`. For this expression to evaluate to true, ALL of `a`, `b`, `c` and `d` must be true.
    Writing a table that lists every combination of inputs and outputs for this expression is left as an excersise for the reader.

2. Boolean OR: This is used to check if one or more booleans are `true`.

    Usage: `#!cpp a || b` (Here, `a` and `b` are boolean variables)

    This checks if either `a` **or** `b` is `true`. If one of them is, then the expression evaluates to `true`, else it evaluates to `false`.

    Every combination of inputs and outputs for `a || b` can be written in a table:

    | **a** | **b** | **a \|\| b** |
    | :---: | :---: | :----------: |
    | false | false |    false     |
    | false | true  |     true     |
    | true  | false |     true     |
    | true  | true  |     true     |

    !!! Tip
    The OR operation is not limited to just two variables. Any number of variables may be OR-ed together.
    For Example: `#!cpp a || b || c || d`. For this expression to evaluate to true, only one of `a`, `b`, `c` and `d` needs to be true.
    Writing a table that lists every combination of inputs and outputs for this expression is left as an excersise for the reader.

ANDs and ORs can be used together in the same expression. For example:

`(a || b) && c`: for this expression to be `true`, either `a` or `b` and `c` must be `true`.

`a || (b && c)`: for this expression to be `true`, either `a` must be `true`or `b` and `c` must be `true` simultaneously.

!!! Note
If no brackets are used when writing these expressions the expression is evaluated left to right. This means that `a || b && c || d` is the same as `((a || b) && c) || d`. Thus, to make it absolutely clear as to what you mean when writing a boolean expression, you should ALWAYS use brackets appropriately for clarity, even though it is not necessary to do so.

For example:

```cpp
void main() {
    int a = 10;
    int b = 20;
    int c = 30;

    // this would assign true to d
    // because both a < b and c > d are true
    bool d = (a < b) && (c > b);

    // this would assign false to d
    // because c < b is not true
    d = (a < b) && (c < b);

    // this would assign true to d
    // because a < b is true
    d = (a < b) || (c < b);

    // this would assign false to d
    // because neither a > b nor  c < b is true
    d = (a > b) || (c < b);
}
```

#### 2.4.6. Concatenation

When two strings are joined to form a new string, it is known as concatenation. Other data types may also be concatenated with strings.

For Example:

```cpp
void main() {
    string a = "this is ";
    string b = "string concatenation!";
    int c = 11;
    float d = 5.5;
    bool e = true;
    vector v = vector(1, 2, 3);

    // chats "this is string concatenation! 11 5.5 1 (1.0, 2.0, 3.0)"
    xsChatData(a+b+" "+c+" "+d+" "+e+" "+v);
    // remember, true and false are also represented by 1 and 0 respectively!
}
```

#### 2.4.7. Vector Operations

Manipulating vectors in XS is done in a bit of a special way:

1. Initialising a vector:

    We have already seen how this is done: `#!cpp vector v = vector(1, 2, 3);`

    !!! warning "No Vars in Vector Initialisation"
    For some reason, currently we cannot use variables to initialise vectors inside `#!cpp vector()`;
    This is probably a bug and will be fixed in future versions of XS.

    For example:

    ```cpp
    void main() {
        float x = 1.0;
        float y = 2.0;
        float z = 3.0;

        vector myVector = vector(x, y, z); // does not work, thxDE

        // alternatively, this would work:
        vector myVector = cInvalidVector;
        myVector = xsVectorSetX(myVector, x); // sets the X component of the vector
        myVector = xsVectorSetY(myVector, y); // sets the y component of the vector
        myVector = xsVectorSetZ(myVector, z); // sets the z component of the vector

        // alternatively, even shorter way to do this:
        myVector = xsVectorSet(1, 2, 3);

        // here cInvalidVector is a pre-defined constant that XS recognises, it is the vector (-1, -1, -1)
        // Similarly, cOriginVector is a pre-defined constant that XS recognises, it is the vector (0, 0, 0)
    }
    ```

2. Obtaining the X, Y, and Z components of a vector:

    The X, Y and Z components of a vector can be accessed as follows:

    ```cpp
    void main() {
        vector myVector = vector(1, 2, 3);

        float x = xsVectorGetX(myVector); // gives you the X component of the vector
        float y = xsVectorGetY(myVector); // gives you the y component of the vector
        float z = xsVectorGetZ(myVector); // gives you the z component of the vector
    }
    ```

3. Setting the X, Y, and Z components of a vector individually:

    The X, Y and Z components of a vector can be set as follows:

    ```cpp
    void main() {
        vector myVector = vector(1, 2, 3);
        myVector = xsVectorSetX(myVector, 10); // sets the X component of the vector
        myVector = xsVectorSetY(myVector, 20); // sets the y component of the vector
        myVector = xsVectorSetZ(myVector, 30); // sets the z component of the vector
    }
    ```

    Note that it is not necessary to change all 3 components at the same time, you can chose to only change one if you want to.

4. Setting the entire vector:

    If you know that you want to change all 3 components of a vector, it can be done in one go instead of in 3 separate lines like above:

    ```cpp
    void main() {
        vector myVector = vector(1, 2, 3);
        myVector = xsVectorSet(10, 20, 30);
    }
    ```

5. Obtaining the length of a vector:

    The length of a vector can be obtained as follows:

    ```cpp
    void main() {
        vector myVector = vector(1, 2, 3);
        float length = xsVectorLength(myVector);
    }
    ```

    !!! Note
    Mathematically, the length of a vector is given by $\sqrt{x^2+y^2+z^2}$

6. Normalizing a vector:

    The unit vector along the direction of the given vector is obtained by normalising it:

    ```cpp
    void main() {
        vector myVector = vector(1, 2, 3);
        vector unitVectorAlongMyVector = xsVectorNormalize(myVector);
    }
    ```

    !!! note
    Mathematically, the normalised vector is given by $\left(\cfrac{x}{\sqrt{x^2+y^2+z^2}}, \cfrac{y}{\sqrt{x^2+y^2+z^2}}, \cfrac{z}{\sqrt{x^2+y^2+z^2}}\right)$

### 2.5. Flow Control Statements

There are two types of flow control statements:

#### 2.5.1. Conditionals

There are times in life when you need to make decisions, and these decisions depend on certain conditions. For example, suppose that you are in a class, then a decision that you might have to make would be:

$\color{red} \text{if} \; \color{yellow} \text{you have a pen,} \; \color{red} \text{then} \; \color{white} \text{you can write on a piece of paper,} \; \color{red} \text{else} \; \color{white} \text{you borrow a pen}$

Similarly, when writing a script, it might be needed to make decisions at some points in your code. Conditionals are decision making statements that can be used to chose which set of instructions to execute depending on given conditions. There are two types of conditionals suported by XS:

1.  The `#!cpp if else if` statement

    An `#!cpp if else` statement is used whenever you need your script to make decisions. It executes one set of instructions `#!cpp if` a conditon is true or `#!cpp else` it executes another set of instructions.

    Usage:

    ```cpp
    void main() {
        int a = 10;
        int b = 20;
        // if(boolean expression / variable / constant)
        if(b > a) {
            // if the above condition is true do:
            xsChatData("does one thing");
            xsChatData("b > a confirmed!");
        }
        else {
            // if the above condition is not true do:
            xsChatData("does another thing");
            xsChatData("b <= a confirmed!");
        }
    }
    ```

    Anything that is written inside curly braces `{}` is known as a "block" of code. A block of code written under an `#!cpp if` is called the "body" of that `#!cpp if`.

    If there is only one instruction that needs to be run inside an `#!cpp if` or `#!cpp else` then the curly braces `{}` can be omitted:

    ```cpp
    void main() {
        int a = 10;
        int b = 20;
        if(b > a)
            xsChatData("does only one thing");
        else
            xsChatData("does only another thing");
    }
    ```

    An `#!cpp if` statement does not need to be followed by an `#!cpp else` statement everytime

    ```cpp
    void main() {
        int a = 10;
        int b = 20;
        if(b > a)
            xsChatData("doesn't do anything if the conditon is false");
    }
    ```

    What if you need to check multiple conditions and do separate things for each case? this is when you use an `#!cpp if else if` statement!

    ```cpp
    void main() {
        int a = 10;
        int b = 20;
        if(b > a)
            xsChatData("b > 20");
        else if (b == 20)
            xsChatData("b == 20");
        else
            xsChatData("no condition is true");
    }
    ```

    !!! Note
    In the above example, both the `#!cpp (b > a)` and `#!cpp (b == 20)` conditions are true. However, in an `#!cpp if else if` statement, only one branch of instructions is ever executed. Which condition takes proiority is decided by what order you write them in. So in this case, `#!cpp "b > 20"` will be chatted to the screen because that is the first condition which is true.

    Technically, whenever a condition becomes true and its branch of instructions are executed, all of the remaining conditions are skipped, and not even evaluated.

    ???+ Question "Practise"
    Now that you are armed with the power of `#!cpp if else if`, can you:

        Write a script that would chat to the screen the maximum of 3 given variables.

        When you're ready, click the "Answer" to view the solution.

        ??? Success "Answer"
            ```cpp
            void main() {
                int a = 10;
                int b = 20;
                int c = 30;
                if (a > b && a > c)
                    xsChatData("the maximum is a: "+a);
                else if (b > c && b > a)
                    xsChatData("the maximum is b: "+b);
                else
                    xsChatData("the maximum is c: "+c)
            }
            ```

2.  The `#!cpp switch-case` statements:

    A `#!cpp switch-case` is a branching structure used when you want to do several differnt things depending on the value of a variable:
    For example:

    ```cpp
    void main() {
        int a = 10;
        switch(a) {
            case 10: {
                xsChatData("if(a == 10)");
                xsChatData("do this");
            }
            case 20: {
                xsChatData("else if(a == 20)");
                xsChatData("do this");
            }
            default : {
                xsChatData("else");
                xsChatData("do this");
            }
        }
    }
    ```

    This is the same as doing:

    ```cpp
    void main() {
        int a = 10;
        if (a == 10) {
            xsChatData("if(a == 10)");
            xsChatData("do this");
        }
        else if (a == 20) {
            xsChatData("else if(a == 20)");
            xsChatData("do this");
        }
        else  {
            xsChatData("else");
            xsChatData("do this");
        }
    }
    ```

    Similar to `#!cpp if else`, if there is only one instruction to execute, the curly braces `{}` can be omitted:

    ```cpp
    void main() {
        int a = 10;
        switch(a) {
            case 10:
                xsChatData("if(a == 10) do this");
            case 20:
                xsChatData("else if(a == 20) do this");
            default :
                xsChatData("else do this");
        }
    }
    ```

#### 2.5.2. Loops

There are times in life when you need to repeatedly keep doing something under certain conditions. For example, suppose that you are playing a game and you are stuck on a boss fight where you keep dying, something that you are doing might be:

$\color{red} \text{while} \; \color{yellow} \text{you have not defeated the boss,} \; \color{white} \text{try again}$

If you wanted to write out the times two table, you might do:

$\color{red} \text{for} \; \color{yellow} \text{every} \; \color{green} \text{number} \; \color{red} \text{between 1 and 10} \; \color{white} \text{write }2\times \color{green} \text{number}$

Similarly, when writing a script, it might be needed to repeat certain parts of your code multiple times. Loops are statements that can be used to repeatedly execute a block of code given a condition is true.

Sometimes the need arises to repeatedly execute the same statement or a statement where only a few things are changing.
Loops are statements that allow us to do exactly that! There are two types of loops suported by XS:

1.  The `#!cpp while` loop:

    A `#!cpp while` statement repeatedly executes a block of code as long as (while) something is `true`. This process of repeatedly executing the same block of code is known as iteration!
    For example:

    ```cpp
    void main() {
        int a = 0;
        while(a < 10) {
            xsChatData("a = "+a);
            a++;
            // remember that a++ increases the value of a by one.

            // what would happen if you forgot to write a++?
            // your script would get stuck in an "infinite" loop
            // and the game would crash
        }
    }
    ```

    ???+ Question "Practise"
    Now that you are armed with the power of `#!cpp while`, can you:

        Write a script that would chat to the screen the following pattern:

        `1, 2, 4, 7, 11, 16... up to 15 terms?`

        If you need help, but don't want to see the full solution immediately, click "Hint"

        When you're ready, click "Answer" to view the solution.

        ??? Info "Hint"
            Hint: Notice that the pattern here is that each time, the increase of the terms is also going up by one. The 2nd term is the first term + 1, the 3rd term is the 2nd term + 2, and so on.

        ??? Success "Answer"
            ```cpp
            void main() {
                int number = 1;
                int increase = 1;
                while(increase <= 15) {
                    xsChatData("number = "+number);
                    number = number + increase;
                    increase++;
                }
            }
            ```

2.  The `#!cpp for` loop:

    A `#!cpp for` statement is specifically used to loop over a range of values, say `#!cpp 5` to `#!cpp 23`

    For example:

    ```cpp
    void main() {
        for(a = 5; < 23) {
            xsChatData("a = "+a);
            // the for loop takes care of increasing the value
            // of a by one every time

            // you cannot modify 'a' inside the for loop
        }

        // what if i wanted to go down from 10 to 0?
        // that is also possible:
        for(a = 10; > 0) {
            xsChatData("a = "+a);
            // here the for loop figures out automatically
            // that you need to decrease a instead of increasing it.
        }
    }
    ```

How do we pick which loop to use? Firstly, a `#!cpp while` loop can do all that a `#!cpp for` loop can. However, a `#!cpp while` loop is much slower than a `#!cpp for` loop in performance! If it is possible, you should **always** stick to using for loops! A `#!cpp for` loop also takes care of increasing or decreasing the variables of iteration, which means that you cannot accidently cause an "infinite" loop unlike a while loop.

### 2.6. Modular Programming

#### 2.6.1. Functions

Lets say that you are watching TV. Every time you want to change the channel, you will use the same remote. It would be quite inconvenient if you had to make a new remote each time you wanted to change the channel. Similarly, when writing a script, you might want to write a piece of code that you need to re-use multiple times in different parts of your script. Functions allow us to do exactly this!

A function is a piece of code that can input some values and use them to perform a given task. You have already seen a function before! `xsChatData(string str);` is actually a function which inputs a `string` and chats it in game.

Another useful function is `sqrt(float number);` which calculates the square root of a value.

Usage: `#!cpp float a = sqrt(4);`

This assigns the value `#!cpp 2.0` to `a`.

An interesting thing to note here is that some functions "give you back" a value, like `#!cpp sqrt(5);` will "give you back" $\approx$ `#!cpp 2.24`.

This property that a function "gives you back" a value is formally known as the fact that the function "returns" a value. Not all functions do this, for example `#!cpp xsChatData("my message");` simply displays that message on screen and does not return any value. A function can return a value of any data type.

Each function also takes a set of inputs. `xsChatData` takes in a string, `sqrt` takes in a float. The set of inputs that a function can take are formally known as its "parameters".

While these are inbuilt functions in XS that are provided to us to use to use directly, we can also define our own functions. This is how a function is defined in XS:

Usage:

```cpp
returnType functionName(dataType parameter1 = defaultValue, dataType parameter2 = defaultValue) {
    return (value);
    // value must be a data type that is the same as returnType
}
```

If it is not clear what this means, bare with this usage for a minute and see this example below:

```cpp
// this is a custom function that returns the maximum of two integers.

int max(int a = 0, int b = 0) {
    // the 'int' at the start tells us that this function
    // is going to return an integer value,

    // max is the name of the function

    // this function takes in two integer values, 'a' and 'b'
    // 'a' and 'b' are initialised to 0 by default, meaning if
    // the person using this function doesn't specify what values
    // to use for 'a' and 'b', 0 will be used.

    // a return statement tells the function to "give you back" whatever
    // value is specified.
    if(a > b)
        return (a);
    return (b);

    // wait, why have we not writte an else statement here?
    // a function ALWAYS terminates as soon as it encounters a 'return'
    // statement. this tells the function to stop doing whatever it is
    // doing and "give you back" the value specified.
    // this is why writing an else here is unecessary, because if
    // a > b then the 2nd return statement will never run in the first place
}

void main() {
    // this is how the function is then used:
    xsChatData("max "+max(10, 20));
    // the values for the variables in the function are
}
// wait, isn't this 'main' also a function that we've been using so far?
// yes it is! The 'void' signifies that it doesn't return any value

// since there is nothing writting inside the brackets after 'main',
// it does not take in any parameters either
```

Function names follow the same laws and conventions that variable names do.

A list of all inbuilt XS functions and their descriptions are provided in the [Fucntion Reference](../functions/ "Jump to: XS Scripting > Function Reference") section of this guide.

#### 2.6.2. File Structure

When you write an XS Script, it is a good idea to group your functions and put them into an appropriately named file.

For example, if you have an XS Script that does calculations with vectors, like adding, subtracting, dot product or cross product, or other vector operations, you might want to use it in more than on XS Script.

Copying all the functions in every XS Script that you want to use them in is tedious and is considered a bad programming practise. What we can do instead is write another XS Script named "VectorOperations.xs" and then "call" this script in every other script where vector operations are required.

For Example:

If I have two files, `test.xs` and `VectorOperations.xs` in the same folder, then:

```cpp
// test.xs

include "./VectorOperations.xs";
// "./VectorOperations.xs" is the relative path of the
// VectorOperations.xs file from the text.xs file.
// This can also be the absolute path of a file.
// If you do not know what absolute/relative paths are,
// a quick google search will tell you more about them.

void main() {
    vector a = vector(1, 2, 3);
    vector b = vector(3, 2, 1);
    xsChatData("dot: "+dotProduct(a, b));
    xsChatData("cross: "+crossProduct(a, b));
    xsChatData("add: "+add(a, b));
}

```

```cpp
// VectorOperations.xs

int dotProduct(vector a = cInvalidVector, vector b = cInvalidVector) {
    return (xsVectorGetX(a)*xsVectorGetX(b)+
            xsVectorGetY(a)*xsVectorGetY(b)+
            xsVectorGetZ(a)*xsVectorGetZ(b));
}

vector crossProduct(vector a = cInvalidVector, vector b = cInvalidVector) {
    vector product = cInvalidVector;
    product = xsVectorSetX(product, xsVectorGetY(a)*xsVectorGetZ(b) - xsVectorGetZ(a)*xsVectorGetY(b));
    product = xsVectorSetY(product, 0 - xsVectorGetX(a)*xsVectorGetZ(b) + xsVectorGetZ(a)*xsVectorGetX(b));
    product = xsVectorSetZ(product, xsVectorGetX(a)*xsVectorGetY(b) - xsVectorGetY(a)*xsVectorGetX(b));
    return (product);
}

vector add(vector a = cInvalidVector, vector b = cInvalidVector) {
    vector addition = cInvalidVector;
    addition = xsVectorSetX(addition, xsVectorGetX(a)+xsVectorGetX(b));
    addition = xsVectorSetY(addition, xsVectorGetY(a)+xsVectorGetY(b));
    addition = xsVectorSetZ(addition, xsVectorGetZ(a)+xsVectorGetZ(b));
    return (addition);
}
```

This way, for every file that you need to use "VectorOperations.xs" in, you just need to write `#!cpp include "/relative/or/absolute/path/to/file";` and you can use all the functions that you wrote in it in that file as well!

Code that is written like this, where:

1. Every separate operation is in its own function
2. Every group of similar functions is in their own file,

Is known as modular code! Writing code like this is considered a very very good programming practise. This way, others reading your code can easily read, and understand your code and get the idea of the big picture!

However... Currently there is a bug (thxDE 11) due to which XS Scripts are not properly transfered to other players in the lobby. For now, a workaround is to manually give everyone the XS Scripts needed.

### 2.7. Scope of a Variable

Every variable has a scope, i.e. an "area" of the code where it can be used. For example, you cannot use a variable before it has been initialised, that doesn't make sense!

```cpp
void main() {
    a++; // wait, a doesn't exist yet! you cannot do this.
    int a = 10;
}
```

Similarly, Variables initialised inside one function can only be used in that particular function, and do not exist outside of them. These kinds of variables are known as local variables. For example:

```cpp
void main() {
    int a = 10;
}
void anotherFunction() {
    a++; // wait, a doesn't exist inside another! you cannot do this.
    // you can actually declare another variable named a inside of another:
    int a = 44;
    // this a is completely different and independent from the a in main();
}
```

What if you want a variable that is shared between functions? A variable like this must be declared outside of all functions. Such a variable is known as a global variable. For example:

```cpp
int a = 10;
void main() {
    a++;
}
void anotherFunction() {
    a++;
}
```

### 2.8. Arrays

An array is a data structure that allows you to make ordered, numbered lists of one kind of data type. In every numbered list, each element is identified using its number. This number is known as an index. If `a` is an array of integers, then it might looks something like this:

| Index | Value |
| :---: | :---: |
|   0   |  23   |
|   1   |   4   |
|   2   |  42   |
|   3   |  32   |
|   4   |  92   |

The index is what identifies elements in an array and indices for each array always starts from 0. For example: `#!cpp a[2]` is `#!cpp 42`.
While in most programming languages `#!cpp a[2]` is the way to access elements in an array, that is not how it is done in XS. Lets look at how arrays are used in XS:

For creating arrays, the following functions are used for the relevant data type:

```cpp
// creates a sized and named integer array, with every value
// initialised to defaultValue. returns an integer arrayID.
int xsArrayCreateInt(int size, int defaultValue, string name)

// creates a sized and named float array, with every value
// initialised to defaultValue. returns an integer arrayID.
int xsArrayCreateFloat(int size, float defaultValue, string name)

// creates a sized and named boolean array, with every value
// initialised to defaultValue. returns an integer arrayID.
int xsArrayCreateBool(int size, bool defaultValue, string name)

// creates a sized and named string array, with every value
// initialised to defaultValue. returns an integer arrayID.
int xsArrayCreateString(int size, string defaultValue, string name)

// creates a sized and named vector array, with every value
// initialised to defaultValue. returns an integer arrayID.
int xsArrayCreateVector(int size, vector defaultValue, string name)
```

For the name of the array, any string may be used but all names must be unique

All of these functions return an integer which is the ID of the array that you just created. This ID is used to perform other operations on the array. You want to store this integer in a variable that is named apty so that you can use the array later.

To get a value at a specific index from an array, we use the following functions for the relevant data types:

```cpp
// returns an integer from the specified index of the specified array
int xsArrayGetInt(int arrayID, int index)

// returns a float from the specified index of the specified array
float xsArrayGetFloat(int arrayID, int index)

// returns a boolean from the specified index of the specified array
bool xsArrayGetBool(int arrayID, int index)

// returns a string from the specified index of the specified array
string xsArrayGetString(int arrayID, int index)

// returns a vector from the specified index of the specified array
vector xsArrayGetVector(int arrayID, int index)
```

If you ever try to access values in arrays that dont exist (invalid arrayID) or values at indices that dont exist (negative indices or indices more than the length of the array) then the default values for the data types are returned. These are:

```cpp
int defaultValue = -1
float defaultValue = -1.0
bool defaultValue = false
string defaultValue = ""
vector defaultValue = vector(0, 0, 0)
```

To set a value at a specific index in an array, we use the following functions for the relevant data types:

```cpp
// Sets the value at the specified index in the specified array.
int xsArraySetInt(int arrayID, int index, int value)

// Sets the value at the specified index in the specified array.
int xsArraySetFloat(int arrayID, int index, float value)

// Sets the value at the specified index in the specified array.
int xsArraySetBool(int arrayID, int index, bool value)

// Sets the value at the specified index in the specified array.
int xsArraySetString(int arrayID, int index, string value)

// Sets the value at the specified index in the specified array.
int xsArraySetVector(int arrayID, int index, vector value)
```

Note that these Set functions return a value of `#!cpp 1` every time, however this does not need to be stored in a variable.

To change the size of an array

```cpp
// Resize the specified array.
int xsArrayResizeInt(int arrayID, int newSize)
// Resize the specified array.
int xsArrayResizeFloat(int arrayID, int newSize)
// Resize the specified array.
int xsArrayResizeBool(int arrayID, int newSize)
// Resize the specified array.
int xsArrayResizeString(int arrayID, int newSize)
// Resize the specified array.
int xsArrayResizeVector(int arrayID, int newSize)
```

Note that these Resize functions return a value of `#!cpp 1` every time, however this does not need to be stored in a variable.

`#!cpp int xsArrayGetSize(int arrayID)` is also a useful array function that returns the size of the specified array.

### 2.9. Type Casting

Type casting is when a value of one data type is "transformed" into a value of another, similar data type. This is like taking an object stored in one type of container and putting it into another.

For example, When you try to store an `#!cpp int` in a `#!cpp float`, it would work without any issues. It is similar to storing water in a bottle and then putting the water from that bottle into a flask. When you try to store a `#!cpp float` in an `#!cpp int` however, the fractional part of the `#!cpp float` is lost! This is like trying to put water from a water bottle into a paper bag. Some of the water will leak out!

There are two kinds of type casting:

1. Implicit Type Casting

    Implicit type casting is done automatically by the script (hence implicit) when you assign one type of value to another, similar data type. For example:

    ```cpp
    void main() {
        int a = 5;
        float b = 3.9;
        bool c = true;

        // implicit type casting:
        int d = c; // remember, true is 1 and false is 0
        float e = c;
        string f = ""+c; // just string f = c; will not work

        // when type casting a float to an int, the fractional part of the number is lost!
        // note that it is not rounded off, 3.9 would become 3 after type casting
        int = b;
        // anything other than a 0 gives true for a bool
        bool = b;
        string = ""+b;

        float g = a;
        // anything other than a 0 gives true for bool
        bool h = a;
        string i = ""+a;
    }
    ```

2. Explicit Type Casting

    Explicit type casting is done manually by the programmer (hence explicit). For example:

    ```cpp
    void main() {
        float a = 5.5;

        float b = (int)a; // assigns 5.0 to b
        float c = (int)22.5; // assigns 22.0 to c
    }
    ```

## 3. Rules

A rule is a block of code that can be set to repeatedly execute at set intervals throughout the duration of the game. A rule is always initialised outside of a function. Its usage looks like:

```cpp
rule ruleName // This is the name of the rule. Follows same naming laws as variables.

    active/inactive // this is the initial state of the rule, active means that runs by default
                    // and inactive means that it wont run by default.
                    // this is similar to how triggers work when you enable/disable them.

    group groupName // the group that this rule belongs to. Follows same naming laws as variables.

    minInterval <int> // the minimum time interval that must pass before the block is executed again
    maxInterval <int> // the maximum time interval that may pass before the block has to be executed again
    highFrequency   // Loop the rule 60 times every physical second (this is independant of inagme speed)
                    // Only one of "highFrequency" or "minInterval" and "maxInterval" are used. Both cannot be used together

    runImmediately  // It is currently unknown as to what this option does
    priority <int>    // rules are executed in order of their descending priority
{
    // code to execute
}
```

Example Usages:

```cpp
int a = 0;
// This rule prints the value of a every 2 seconds.
rule chatTheValueOfA
    active
    minInterval 2
    maxInterval 2
    group chatGroup
{
    xsChatData("a = "+a);
    a++;
}
```

There are a lot of built in XS functions that can interact with rules. Check the [Rules](../functions/#1-rules "Jump to: XS Scripting > Function Reference > Rules") Section of this guide.

The variable `cActivationTime`, when used inside the block of a rule, gives the time of activation of the rule in seconds.

With that, you now know everything that is currently known to work with XS Scripts. Good luck and have fun creating awesome maps!
