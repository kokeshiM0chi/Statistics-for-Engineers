# kokeshi-question #02: Jupyter Notebook の開き方

## 質問

> `2023-10-11-SRECon-Dublin/2023-10-08 SLOs at SRECon.ipynb` の Jupyter Notebook の開き方を教えてほしい。

## おすすめ: uv で一発起動（Mac, 動作確認済み）

`uv` が入っていれば、仮想環境やパッケージを自分で用意せずに起動できる。

```bash
cd ~/kokeshi/Statistics-for-Engineers
uv run --python 3.12 \
  --with jupyterlab --with pandas --with numpy --with matplotlib --with imageio \
  jupyter lab
```

1. ブラウザが自動で開く（開かなければ、ターミナルに出る `http://localhost:8888/lab?token=...` の URL を開く）
2. 左のファイル一覧から `2023-10-11-SRECon-Dublin` → `2023-10-08 SLOs at SRECon.ipynb` をダブルクリック
3. 上から順にセルを実行する
   - `Shift + Enter`: 今のセルを実行して次へ
   - メニュー **Run → Run All Cells**: 全部まとめて実行
4. 終了するときはターミナルで `Ctrl + C`（確認が出たら `y`）

> **ポイント**: リポジトリのルートで起動すると、左のファイル一覧にリポジトリ全体が表示されて探しやすい。
> なお、ノートブックの `../datasets/slo_requests.csv` という相対パスは、ノートブックのあるフォルダが基準になる（Jupyter はノートブックのあるフォルダで実行する）ので、起動場所によってデータが読めなくなることはない。

### このノートブックで必要なパッケージ

| パッケージ | 用途 |
|---|---|
| pandas | 時系列データ（good / bad / total）の集計、rolling window |
| numpy | 数値計算 |
| matplotlib | SLI / Error Budget / Burn Rate のグラフ |
| imageio | 最後のセルでアニメーション GIF（`animated_plot.gif`）を作る |

`--python 3.12` を付けているのは、最新の Python (3.14) だと一部パッケージが未対応のことがあるため。

## 見るだけなら: GitHub 上で開く

実行せずに中身とグラフを見るだけなら、GitHub で `.ipynb` ファイルを開けばそのまま表示される（保存済みの出力が表示される）。

## 注意点

- **最後のセル（アニメーション）を実行すると `animated_plot.gif` が上書きされる。**
  変更をコミットしたくなければ、終わった後に以下で元に戻す:
  ```bash
  git restore 2023-10-11-SRECon-Dublin/animated_plot.gif
  ```
- ノートブック自体も実行結果が保存されると差分が出る。元に戻すなら同様に `git restore` する。

## 参考: README の Docker 方式について

README には `./docker.sh` で環境を立ち上げる方法が書かれているが、現状そのままでは動かない可能性が高い。

- `docker.sh` は実際には `podman` コマンドを呼んでいる（Docker ではない）
- `Dockerfile` が参照する `cmd.sh` がリポジトリに存在しない
- ベースイメージ `heinrichhartmann/jupyter` が古い

そのため、上記の uv 方式がおすすめ。
