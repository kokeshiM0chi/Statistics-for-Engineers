# kokeshi-question #04: 作者 Heinrich Hartmann の小ネタ

このリポジトリ「Statistics for Engineers」の作者についての、ちょっとした話のまとめ。
（2026-11 時点で Web 上の公開プロフィールを確認した内容。出典は末尾）

## 経歴: 弦理論の数学者 → 監視 SaaS のデータサイエンティスト → SRE

| 時期 | 内容 |
|---|---|
| 〜2012年ごろ | ドイツ・**ボン大学で博士号**。テーマは**弦理論の幾何学的な側面**。その後 **オックスフォード大学**で研究者 |
| 2012年 | 数学からコンピュータサイエンスへ転向 |
| 2015〜2019年ごろ | 監視 SaaS の **Circonus** で Analytics Lead → **Chief Data Scientist**。レイテンシ監視のための**ヒストグラム手法**を開発 |
| 2020年代 | EC 大手の **Zalando**（ドイツ）で **Senior Principal SRE**。全社の信頼性エンジニアリングをリード（2024年の SRECon プロフィールより） |

「数学者がたまたま運用をやっている」というより、**純粋数学の研究者が現場の SRE になった**人。
講演で数式が自然に出てくるのはこのため。

## リポジトリの中に残っている「Circonus 時代」の痕跡

- README 冒頭の「This work was made possibly by **Circonus**」
- 2022年ノートブックの `prelude.py` にあった `from circllhist import Circllhist`
  - **circllhist** は Circonus が作ったヒストグラム形式（"circonus log-linear histogram"）
  - 作者の手元の Circonus 設定ファイルを読みにいくので、そのままでは動かなかった（kokeshi ブランチで修正済み）
- `2019-10-02-SRECon-Dublin/2.4 Mergeable Percentile Aggregation Comparison.ipynb` で、circllhist を HDR Histogram や t-digest と比べている
- その後、ヒストグラムのライブラリは **OpenHistogram** としてオープンソースになっている

## 「パーセンタイルは集約できない」発言

`2019-10-02-SRECon-Dublin/2.2 Aggregating Percentiles.ipynb` の見出しは
**「So I said "Percentiles can't be aggregated" ...」**（「パーセンタイルは集約できない」と言ったら…）。

Twitter（当時）や Reddit で反論が来たらしく、ノートブックでその反論に**実データで答える**構成になっている。
結論は「やっぱり平均すると 50% 以上ずれる。件数（count-below）かマージできるヒストグラムを使え」。
2022年ノートブックで p90 を平均すると 68% ずれた話も同じ主張の続き。

## ワークショップの歴史

- 2015年の SRECon Dublin から、ほぼ毎年ヨーロッパの SRECon で開催されている**定番ワークショップ**
- Monitorama 2016（ポートランド）でも講演。動画は Vimeo にある（README にリンク）
- 2016年に内容をまとめた記事が **ACM Queue** と **Communications of the ACM**（CACM）に掲載
- 2019年に Hacker News でも話題に（README にスレッドへのリンク）

## 日付の小ネタ

- `2023-10-11-SRECon-Dublin/` のフォルダ名は講演日（SRECon EMEA 2023 は 10月10〜12日、ダブリン）
- 中のノートブックは `2023-10-08 SLOs at SRECon.ipynb` で、**講演の3日前**の日付
- Git に追加されたのは講演後の 10月15日（コミット `cf824bb`）
- 本人のサイトではこの回の講演が「**Mathematics of SLOs**」として載っている（USENIX の公式ページ上の題は「Workshop: Statistics for Engineers」）

## その他

- 2022年ノートブックの冒頭: **「Warning: This is write-only code for illustration purposes. Use at your own risk.」**
  （「書くだけで読み返すことは想定していないコード。自己責任で」）
  → 解説がなくセルが重複しているのは、講演用のデモだから
- `Dockerfile` を見ると、元々は Docker で配る想定だったが、`docker.sh` は実際には **podman** を呼んでいる
- 本人のサイト（heinrichhartmann.com）には、サンプル数と誤差を計算する **Sampling Calculator** がある。
  2022年ノートブックの「サンプリングの誤差」の話をそのまま道具にしたもの
- 統計以外にも「Writing for Engineers」（2022）や「Reflections on Leadership」（2025）など、エンジニアの書き方やリーダーシップについても書いている

## 出典

- [heinrichhartmann.com](https://www.heinrichhartmann.com/) — 講演・記事・ツールの一覧
- [SRECon24 EMEA 講演者プロフィール（Zalando SE）](https://usenix.org/conference/srecon24emea/speaker-or-organizer/heinrich-hartmann-zalando-se)
- [SRECon23 EMEA: Workshop: Statistics for Engineers](https://usenix.org/conference/srecon23emea/presentation/hartmann)
- [SRECon19 EMEA: Heinrich Hartmann, Circonus](https://usenix.org/conference/srecon19emea/presentation/hartmann-statistics)
- [GOTO 講演者ページ](https://gotopia.tech/experts/1755/heinrich-hartmann)
- [ACM Queue: Statistics for Engineers (2016)](https://queue.acm.org/detail.cfm?id=2903468)
