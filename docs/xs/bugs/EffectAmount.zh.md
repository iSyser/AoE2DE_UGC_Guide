# 函数 Effect Amount

## 1. `xsEffectAmount` effect `cMulAttribute` and `cAddAttribute` with attribute `cAttack/cArmor` { #1 }

描述: When using `xsEffectAmount` and `cMulAttribute` or `cAddAttribute` to modify `cAttack/cArmor`, the effect does not change the attack/armour at all

预期行为: Expected behaviour is demonstrated using the following example:

复现步骤:

1. Create a new scenario or RMS
2. Create a new XS script with the following code:

    ```cpp
    void main() {
      const int cGenghisKhan = 731;
      const int cPierce = 3;
      // Both of these work correctly as expected
      xsEffectAmount(cSetAttribute, cGenghisKhan, cAttack, cPierce * 65536 + 5);
      xsEffectAmount(cSetAttribute, cGenghisKhan, cArmor, cPierce * 65536 + 5);
      // These however do not do anything.
      xsEffectAmount(cAddAttribute, cGenghisKhan, cAttack, cPierce * 65536 + 5);
      xsEffectAmount(cMulAttribute, cGenghisKhan, cArmor, cPierce * 65536 + 5);
      // To make cAddAttribute and cMulAttribute work, we need to currently use the
      // old format: xsEffectAmount(cAddAttribute, cGenghisKhan, cAttack,
      // cPierce*256 + 5); xsEffectAmount(cMulAttribute, cGenghisKhan, cArmor,
      // cPierce*256 + 5);
    }

    ```

3. Include the script in the scenario or RMS
4. When a game is played using the scenario or RMS, The attack and armour of the Genghis Khan unit is unchanged
