# モジュールをインポート
import matplotlib.pyplot as plt
from matplotlib import animation
import mpmath


# 精度：十進数表示で30桁。
mpmath.mp.dps = 30

# plt.figureインスタンスを作成
fig = plt.figure()

# 空リストを作成
img = []

# グラフのリストを作成
for k in range(1, 5001, 150):
    # 空リスト作成
    u = []
    t = []
    # s = 1/2 + it で、tを0.01ずつ動かし、ζ(s)の値を求める。それを、実部、虚部に分け、リストに出力。
    for n in range(0, k):
        s = 1/2 + 0.01 * n * 1j
        i = mpmath.zeta(s)
        u.append(i.real)
        t.append(i.imag)
    print(u)
    # グラフを描画
    plt.xlim([-4, 4]); plt.ylim([-4, 4])
    plt.xlabel("Real part"); plt.ylabel("Imaginary part")
    plt.grid(True)
    grh = plt.plot(u, t, color="g")
    # グラフをリストに追加
    img.append(grh)

# アニメーションを作成
ani = animation.ArtistAnimation(fig, img, interval=200)
ani.save("rzPlot.gif", writer="imagemagick")
plt.show()