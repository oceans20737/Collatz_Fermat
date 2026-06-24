# **Collatz Dynamics: Mersenne-Fermat分解とJacobsthal数列によるCollatz逆木の構造的記述**

Hiroshi Harada - June 24, 2026

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Document: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## **概要 (Overview)**
本プロジェクトは、**Collatz予想**における**逆木（Inverse Tree）**の生成構造を、**Mersenne-Fermat（M-F）分解**と**Jacobsthal（J）数列**の観点から完全に決定論的な代数プロセスとして記述・実証する研究データセットです。

奇数核 $a$ を $a\cdot 2^k - 1$ の形に変換し、Fermat型の二乗差 $(a\cdot 2^k)^2 - 1$ に埋め込むことで生じる「**M型因子**」と「**F型因子**」の分裂、および mod 3 の選別ゲートによる逆木軌跡（**$3J$**）の抽出過程を理論とコードの両面から証明しています。

## **収録ファイル (Files)**
* **研究報告書**:
  * `Report_JP.pdf` / `Report_EN.pdf` (Mersenne-Fermat分解とJacobsthal数列によるCollatz逆木の構造的記述)
* **実証コード**:
  * `collatz_fermat_branches.py`: 任意の奇数核からM-F分裂と選別ゲート（$3J/cJ$）を計算し、結果をCSVとして出力する数値検証スクリプト。
  * `collatz_fermat_cascade.py`: Graphvizを用いて、初期値 7 のCollatz逆軌道における純粋な軌跡（$J$）の抽出と不要因子（$cJ$）の分離を描画する「カスケード崩壊図」の生成スクリプト。

## **実行手順 (Usage)**
Python 3.x 環境で動作します。

### **1. 数値実証スクリプトの実行**
```bash
python collatz_fermat_branches.py

```

※実行後、カレントディレクトリに計算結果のCSVファイル（例: `collatz_branches_a=5.csv`）が生成されます。コード内の変数 `a` を変更することで、任意の奇数核で追試が可能です。

### **2. カスケード崩壊図の生成**

外部ライブラリ `graphviz` が必要です。

```bash
pip install graphviz
python collatz_fermat_cascade.py

```

※実行後、同ディレクトリに `MF_Cascade_Decay.png` が生成されます。

## **ライセンス (License)**

* Research Document: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
* Python Source Code: [MIT License](https://opensource.org/licenses/MIT)

Copyright (c) 2026 Hiroshi Harada
