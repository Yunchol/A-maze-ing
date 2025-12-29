1. cell.py
2. generator.py（枠だけ）
3. generator.py（道を掘る）
4. renderer.py
5. solver.py
6. generator.py（PERFECT）
7. exporter.py
8. a_maze_ing.py

おすすめ動画
https://youtube.com/shorts/H1nQV9V27cs?si=ZffTC22O2CPK8q7B




**「最小だけど評価で安全」な構成**で説明するね。
まず全体、そのあと **1ファイルずつ役割**を話す。

---

# 📁 全体のファイル構成（おすすめ）

```text
.
├── a_maze_ing.py          # 実行用メイン（入口）
├── config_default.txt    # デフォルト設定ファイル
├── maze/
│   ├── __init__.py
│   ├── generator.py      # 迷路を作る本体（最重要）
│   ├── cell.py           # 1マスの定義（壁の情報）
│   ├── solver.py         # 最短経路を探す
│   ├── exporter.py       # 16進数形式でファイル出力
│   └── renderer.py       # 画面表示（ASCII）
├── mazegen-1.0.0.py      # 再利用用（単一ファイル版）
├── README.md
├── Makefile
├── .gitignore
```

👉 **評価で一番大事なのは `maze/generator.py`**

---

# 🧠 ファイルごとの役割（超やさしく）

---

## 🟦 a_maze_ing.py

### 「司令塔」

**役割**

* コマンド引数を読む
* config.txt を読む
* 迷路を作る人（generator）に頼む
* 表示する
* 保存する
* エラーをまとめて処理する

**ここではやらないこと**

* 迷路の作り方
* 壁のロジック
* 経路探索

👉
**「流れだけを書く」ファイル**

---

## 🟦 config_default.txt

### 「注文書」

* 迷路のサイズ
* スタート
* ゴール
* PERFECTかどうか

評価時に
「config用意して」って言われたらこれを見せる

---

## 🟦 maze/cell.py

### 「1マスの定義」

**中身のイメージ**

```python
class Cell:
    north: bool
    east: bool
    south: bool
    west: bool
```

**役割**

* 壁があるかないかを持つ
* 壁を開ける・閉める

👉
「マスって何？」を1箇所にまとめる

---

## 🟦 maze/generator.py

### ⭐ 迷路を作る人（最重要）

**役割**

* WIDTH / HEIGHT を受け取る
* マスを並べる
* ランダムに壁を壊して道を作る
* PERFECT迷路を保証する
* 42パターンを入れる

**ここが評価の8割**

---

## 🟦 maze/solver.py

### 「道を探す人」

**役割**

* ENTRY → EXIT の最短ルートを探す
* 結果を `N E S W` の文字列で返す

**使うのは**

* BFS（幅優先探索）

👉
「生成」と「解く」を分けるのが設計的に◎

---

## 🟦 maze/exporter.py

### 「ファイルに書く人」

**役割**

* Cell の壁情報を
* 16進数1文字に変換
* 行ごとに書き出す
* 最後に ENTRY / EXIT / PATH を追加

👉
**出力形式が変わっても generator を触らなくていい**

---

## 🟦 maze/renderer.py

### 「画面に描く人」

**役割**

* 迷路を文字で表示
* 壁を `#` や `|` で描く
* ENTRY / EXIT を表示
* パスのON/OFF切り替え

---

## 🟦 mazegen-1.0.0.py

### 「再利用用の完成品」

**役割**

* `MazeGenerator` を1ファイルにまとめたもの
* 将来こう使える👇

```python
from mazegen import MazeGenerator

maze = MazeGenerator(width=20, height=15)
maze.generate()
```

👉
課題で言ってる
**「pipで使える形」** の正体

---

## 🟦 README.md

### 「説明書」

書くこと：

* この課題は何？
* どうやって実行？
* configの説明
* 使った迷路アルゴリズム
* なぜそれを選んだか
* 再利用できる部分はどこ？

---

## 🟦 Makefile

### 「楽するボタン」

* `make run`
* `make lint`
* `make clean`

評価で
「lintして」って言われたら即OK

---

# 🧩 役割分担の考え方（超大事）

| 役割    | ファイル          |
| ----- | ------------- |
| 全体の流れ | a_maze_ing.py |
| 迷路を作る | generator.py  |
| マスの定義 | cell.py       |
| 道を探す  | solver.py     |
| 保存    | exporter.py   |
| 表示    | renderer.py   |

👉
**1ファイル = 1仕事**

---

## 最後に（安心して）

最初から全部作らなくていい。

まずは👇
1️⃣ `Cell`
2️⃣ `MazeGenerator`
3️⃣ ASCII表示

ここまでできたら
**もう半分合格ライン**。

---

次はどれ行く？

* 🟩 generator.py の中身を図で説明
* 🟩 PERFECT迷路の作り方を1ステップずつ
* 🟩 最初の最低限コードを書いてみる

「ここから手を動かしたい」って言ってくれてOK 👍
