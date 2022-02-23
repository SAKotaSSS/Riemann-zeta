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
for k in range(0, 5001, 100):
    # 空リスト作成
    u = []
    t = []
    # s = 1/2 + it で、tを0.01ずつ動かし、ζ(s)の値を求める。それを、実部、虚部に分け、リストに出力。
    for n in range(0, k + 1):
        s = 1/2 + 0.01 * n * 1j
        i = mpmath.zeta(s)
        u.append(i.real)
        t.append(i.imag)
    print(u)
    # グラフを描画
    plt.xlim([-4, 4]); plt.ylim([-4, 4])
    plt.title("ζ(s)")
    plt.xlabel("Real part"); plt.ylabel("Imaginary part")
    plt.grid(True)
    grh = plt.plot(u, t, color="g")
    text = plt.text(-3.5, -3.5, f"1/2 + {k/100}i", color="blue", fontsize="xx-large")
    # グラフをリストに追加
    img.append(grh + [text])

# アニメーションを作成
print(img)
ani = animation.ArtistAnimation(fig, img, interval=200)
ani.save("rzPlot.gif", writer="imagemagick")
plt.show()