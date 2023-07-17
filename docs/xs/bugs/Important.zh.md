# 重要

## 1. XS 文件传输 { #1 }

描述: 

1. 在大厅中，对其他玩家：
    1. 在 RMS 中：
        1. [ ] 来自游戏目录
        2. [x] 来自配置文件目录
        3. [x] 来自模组（本地/订阅）目录
    2. 在场景中：
        1. [ ] 来自游戏目录
        2. [x] 来自配置文件目录
        3. [x] 来自模组（本地/订阅）目录
2. 对观战者：
    1. 在 RMS 中：
        1. [ ] 来自游戏目录
        2. [ ] 来自配置目录
        3. [ ] 将直接包含的 XS（使用 #includeXS）文件从 mods（本地/订阅）目录传输到其他目录，但位于错误的临时文件夹位置
    2. 在场景中：
        1. [ ] 来自游戏目录
        2. [ ] 来自配置目录
        3. [ ] 将直接包含的 XS（使用脚本文件名框）文件从 mods（本地/订阅）目录传输到其他目录，但位于错误的临时文件夹位置

预期行为: --

复现步骤:

1. --

## 2. 科技相关的 XS 功能在 RMS 中不起作用 { #2 }

描述: `xsResearchTechnology` 和 `xsGetPlayerNumberOfTechs` 不能在 RMS 中使用

预期行为: 这些功能应该像在场景中一样在 RMS 中工作

复现步骤:

1. 创建新的 RMS
2. 使用以下代码创建新的 XS 脚本：

    ```cpp
    void main() {
      // these functionds do not work in an RMS
      xsResearchTechnology(22, true, false, 2);
      xsGetPlayerNumberOfTechs(1);
    }

    ```

3. 使用包含 XS 脚本的 RMS 玩游戏时，会显示解析错误

## 3. 对象计数相关的 XS 功能在 RMS 中不起作用 { #3 }

描述: `xsGetObjectCount` 和 `xsGetObjectCountTotal` 不能在 RMS 中使用

预期行为: 这些功能应该像在场景中一样在 RMS 中工作

复现步骤:

1. 创建新的 RMS
2. 使用以下代码创建新的 XS 脚本：

    ```cpp
    void main() {
      // these functionds do not work in an RMS
      xsGetObjectCount(1, 83);
      xsGetObjectCountTotal(1, 83);
    }

    ```

3. 使用包含 XS 脚本的 RMS 玩游戏时，会显示解析错误
