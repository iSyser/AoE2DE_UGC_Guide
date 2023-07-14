# 崩溃

## 1. Crash On Using `%` Symbols In `xsChatData()` { #1 }

描述: Cannot escape `%` symbols in the message, since they are considered special characters because of the `%d` and `%f` usage.

预期行为: It should be possible to escape the `%` character by using a backslash `\`.

复现步骤:

1. Create a new scenario or RMS
2. Create a new XS script with the following code:

    ```cpp
    void main() {
      // This crashes the game altogether
      // prints `this  will not appear in game`
      xsChatData("this % will not appear in game");
      // prints `neither will this \ appear in game`
      xsChatData("neither will this \% appear in game");
    }

    ```

3. Include the script in the scenario or RMS
4. When a game is played using the scenario or RMS, the game will crash

## 2. Using `goto` With A Non Existent Label Crashes The Game { #2 }

描述: If a goto statement is used as shown below, it crashes the game. How to define a working label in XS is currently unknown

预期行为: The game should warn about wrong usage of `goto` to a non existent label. How is a label defined in the first place in XS?

复现步骤:

1. Create a new scenario or RMS
2. Create a new XS script with the following code:

    ```cpp
    void main() { goto non_existent_label; }

    ```

3. Include the script in the scenario or RMS
4. When a game is played using the scenario or RMS, A crash will occur

## 3. Crash On Using An Integer Larger Than `999_999_999` In Chat Data { #3 }

描述: Trying to chan an `#!cpp int` that is bigger than `999_999_999` with `%d` in `xsChatData` causes a crash

预期行为: The int value should be printed properly as expected

复现步骤:

1. Create a new scenario or RMS
2. Create a new XS script with the following code:

    ```cpp
    void main() {
      int a = 999999999 + 1;
      xsChatData("t %d", a); // crashes the game
      // xsChatData("t "+a); // this works normally
    }

    ```

3. Include the script in the scenario or RMS
4. When a game is played using the scenario or RMS, A crash will occur
