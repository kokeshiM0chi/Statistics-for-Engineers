import sys
import pandas as pd

# 入力: Time, total 列を持つ TSV（1分ごとの件数）。datasets/slo_requests.csv と同じ形式
path   = sys.argv[1] if len(sys.argv) > 1 else "datasets/slo_requests.csv"
SLO    = 0.999   # 自分のサービスの SLO
T      = 14.4    # 判定に使うバーンレートの基準
WINDOW = "1h"    # 判定する窓

df = pd.read_csv(path, sep="\t", index_col="Time", parse_dates=True)
N = df["total"].resample(WINDOW).sum()           # 窓ごとのリクエスト数
r = N / N.mean()                                 # トラフィック比 r = N ÷ N̄

baseline = N.groupby([N.index.day_of_week, N.index.hour]).transform("mean")
resid = N - baseline                             # 曜日・時刻の周期パターンを除いた残り

print(f"窓あたり平均 N̄            : {N.mean():.1f}")
print(f"窓あたり最小 N             : {N.min():.1f}")
print(f"1件の失敗で鳴る N の境目   : {1 / (T * (1 - SLO)):.1f}")
print(f"  そうなる窓の割合         : {(N < 1 / (T * (1 - SLO))).mean():.1%}")
print(f"分散指数 D (ポアソン=1)    : {N.var() / N.mean():.1f}")
print(f"周期パターン除去後の D     : {resid.var() / N.mean():.1f}")
print(f"周期パターンで説明できる割合: {1 - resid.var() / N.var():.0%}")
print(f"r の 1% 点 / 99% 点        : {r.quantile(0.01):.2f} / {r.quantile(0.99):.2f}")
print(f"total が全停止を見逃す r   : r < {T * (1 - SLO):.4f}")
print(f"  そうなる窓の割合         : {(r < T * (1 - SLO)).mean():.1%}")
print(f"r ≥ T の窓の割合（健全でも total が鳴りうる）: {(r >= T).mean():.1%}")
