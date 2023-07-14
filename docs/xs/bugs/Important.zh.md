# 重要

## 1. XS File Transferring { #1 }

描述: 

1. In a lobby, to other players:
    1. In an RMS:
        1. [ ] from the game dir
        2. [X] from the profile dir
        3. [X] from the mods (local/subscribed) dir
    2. In a Scenario:
        1. [ ] from the game dir
        2. [X] from the profile dir
        3. [X] from the mods (local/subscribed) dir
2. To spectators:
    1. In an RMS:
        1. [ ] from the game dir
        2. [ ] from the profile dir
        3. [ ] Transfers the directly included XS (using #includeXS) file from the mods (local/subscribed) dir to others, but in the wrong temp folder location
    2. In a Scenario:
        1. [ ] from the game dir
        2. [ ] from the profile dir
        3. [ ] Transfers the directly included XS (using script file name box) file from the mods (local/subscribed) dir to others, but in the wrong temp folder location

预期行为: --

复现步骤:

1. --

## 2. Technology Related XS function Do Not Work In RMS { #2 }

描述: `xsResearchTechnology` and `xsGetPlayerNumberOfTechs` cannot be used in RMS

预期行为: These functions should work in an RMS as they do in scenarios

复现步骤:

1. Create a new RMS
2. Create a new XS script with the following code:

    ```cpp
    void main() {
      // these functionds do not work in an RMS
      xsResearchTechnology(22, true, false, 2);
      xsGetPlayerNumberOfTechs(1);
    }

    ```

3. When a game is played using the XS script included in an RMS, a parsing error is shown

## 3. Object Count Related XS function Do Not Work In RMS { #3 }

描述: `xsGetObjectCount` and `xsGetObjectCountTotal` cannot be used in RMS

预期行为: These functions should work in an RMS as they do in scenarios

复现步骤:

1. Create a new RMS
2. Create a new XS script with the following code:

    ```cpp
    void main() {
      // these functionds do not work in an RMS
      xsGetObjectCount(1, 83);
      xsGetObjectCountTotal(1, 83);
    }

    ```

3. When a game is played using the XS script included in an RMS, a parsing error is shown
