import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# style
# -----------------------------
sns.set_theme(style="whitegrid", context="talk")
plt.rcParams["font.family"] = ["Apple SD Gothic Neo", "Noto Sans KR", "sans-serif"]

# -----------------------------
# 모델 파라미터 (시각화를 위해 정규화)
# -----------------------------
alpha = 1.0      # 전파 진폭 상수
c = 1.0         # 전파 속도(정규화)
lam = 1.0       # 파장 (정규화): f = c/lam
f = c / lam
d = 10.0        # Tx-Wall 거리

# -----------------------------
# 신호 정의
# Path1: Tx -> Rx 직선 경로 (거리 r)
# Path2: Tx -> Wall -> Rx 반사 경로 (거리 2d - r), 반사 위상 반전 포함
# -----------------------------
def path_components(t, r, d=d, c=c, f=f, alpha=alpha):
    L1 = r
    L2 = 2 * d - r
    s1 = (alpha / L1) * np.cos(2 * np.pi * f * (t - L1 / c))
    s2 = -(alpha / L2) * np.cos(2 * np.pi * f * (t - L2 / c))
    srx = s1 + s2
    return s1, s2, srx, L1, L2

def delta_theta(r, d=d, c=c, f=f):
    # Δθ = 2πf(L2-L1)/c + π
    L1 = r
    L2 = 2*d - r
    return 2*np.pi*f*(L2 - L1)/c + np.pi

# -----------------------------
# 마지막 수식의 두 조건을 만족하는 r값(예시)
# d-r를 조절하면 보강/상쇄 지점 생성
# 조건:
#   constructive: 2π((L2-L1)/λ) + π = 2nπ  -> (L2-L1)= (2n-1)λ/2
#   destructive: 2π((L2-L1)/λ) + π = (2n+1)π -> (L2-L1)= nλ
# (L2-L1) = 2(d-r)
# -----------------------------
n = 1
r_construct = d - (2*n - 1)*lam/4   # ΔL = 2(d-r) = λ/2  (보강)
r_destruct  = d - n*lam/2           # ΔL = 2(d-r) = λ    (상쇄)
r_middle = (r_construct + r_destruct) / 2  # 보강/상쇄 사이 중간 지점

# 타임축(파형 확인용: 4주기)
t = np.linspace(0, 4 / f, 2000)

# -----------------------------
# 파형 계산
# -----------------------------
s1_c, s2_c, srx_c, L1_c, L2_c = path_components(t, r_construct)
s1_m, s2_m, srx_m, L1_m, L2_m = path_components(t, r_middle)
s1_d, s2_d, srx_d, L1_d, L2_d = path_components(t, r_destruct)

# -----------------------------
# Δθ 분포(확인용)
# -----------------------------
r_scan = np.linspace(0.2, d-0.2, 1200)
theta = np.mod(delta_theta(r_scan), 2*np.pi)     # 0~2π
theta_norm = theta / np.pi                       # 0~2 범위 (단위 π)
theta_c = np.mod(delta_theta(r_construct), 2*np.pi) / np.pi
theta_m = np.mod(delta_theta(r_middle), 2*np.pi) / np.pi
theta_d = np.mod(delta_theta(r_destruct), 2*np.pi) / np.pi

# -----------------------------
# 시각화
# -----------------------------
fig_wave, axes = plt.subplots(3, 1, figsize=(13, 11), sharex=True)

# (1) 보강 간섭
axes[0].plot(t, s1_c, "--", lw=1.6, label="Path 1 (직진파)")
axes[0].plot(t, s2_c, "--", lw=1.6, label="Path 2 (반사파, 위상반전)")
axes[0].plot(t, srx_c, "k", lw=2.0, label="Rx 합성신호")
axes[0].set_title("보강 간섭 (constructive): $\\Delta\\theta = 2n\\pi$")
axes[0].set_ylabel("Amplitude")
axes[0].legend(loc="upper right")
axes[0].text(0.01, 0.95,
             f"$r = {r_construct:.3f},\\; \\Delta L = 2(d-r) = {L2_c-L1_c:.3f} = \\lambda/2$",
             transform=axes[0].transAxes, va="top")

# (2) 보강/상쇄 사이 중간 간섭
axes[1].plot(t, s1_m, "--", lw=1.6, label="Path 1 (직진파)")
axes[1].plot(t, s2_m, "--", lw=1.6, label="Path 2 (반사파, 위상반전)")
axes[1].plot(t, srx_m, "k", lw=2.0, label="Rx 합성신호")
axes[1].set_title("중간 수준의 간섭")
axes[1].set_ylabel("Amplitude")
axes[1].legend(loc="upper right")
axes[1].text(0.01, 0.95,
             f"$r = {r_middle:.3f},\\; \\Delta L = 2(d-r) = {L2_m-L1_m:.3f}$",
             transform=axes[1].transAxes, va="top")

# (3) 상쇄 간섭
axes[2].plot(t, s1_d, "--", lw=1.6, label="Path 1 (직진파)")
axes[2].plot(t, s2_d, "--", lw=1.6, label="Path 2 (반사파, 위상반전)")
axes[2].plot(t, srx_d, "k", lw=2.0, label="Rx 합성신호")
axes[2].set_title("상쇄 간섭 (destructive): $\\Delta\\theta = (2n+1)\\pi$")
axes[2].set_xlabel("Time (normalized)")
axes[2].set_ylabel("Amplitude")
axes[2].legend(loc="upper right")
axes[2].text(0.01, 0.95,
             f"$r = {r_destruct:.3f},\\; \\Delta L = 2(d-r) = {L2_d-L1_d:.3f} = \\lambda$",
             transform=axes[2].transAxes, va="top")

fig_wave.tight_layout()
fig_wave.savefig("interference_waveforms_constructive_middle_destructive.png", dpi=200, bbox_inches="tight")

# 별도 Figure: r에 대한 Δθ 분포 + 보강/중간/상쇄 점
fig_phase, ax_phase = plt.subplots(1, 1, figsize=(13, 4.2))
ax_phase.plot(r_scan, theta_norm, color="tab:blue", label=r"$\Delta\theta / \pi$ (mod)")
ax_phase.axhline(0, color="k", ls="--", alpha=0.5)
ax_phase.axhline(1, color="k", ls="--", alpha=0.5)
ax_phase.axhline(2, color="k", ls="--", alpha=0.5)
ax_phase.scatter([r_construct], [theta_c], s=100, zorder=3,
                 label="Constructive point", color="tab:green")
ax_phase.scatter([r_middle], [theta_m], s=100, zorder=3,
                 label="Middle point", color="tab:orange")
ax_phase.scatter([r_destruct], [theta_d], s=100, zorder=3,
                 label="Destructive point", color="tab:red")
ax_phase.set_xlim(0, d)
ax_phase.set_ylim(-0.1, 2.1)
ax_phase.set_yticks([0, 0.5, 1, 1.5, 2])
ax_phase.set_xlabel(r"Receiver distance $r$ (from Tx, with fixed wall distance $d$)")
ax_phase.set_ylabel(r"$\Delta\theta/\pi$  (mod 2)")
ax_phase.set_title(r"Phase difference $\Delta\theta = 2\pi\frac{(2d-r-r)}{c}f+\pi$")
ax_phase.legend(loc="upper right")

fig_phase.tight_layout()
fig_phase.savefig("phase_difference_distribution.png", dpi=200, bbox_inches="tight")

plt.show()

# 수치 확인
print(f"Constructive: Δθ = {delta_theta(r_construct):.6f} rad (mod 2π)")
print(f"Middle: Δθ = {delta_theta(r_middle):.6f} rad (mod 2π)")
print(f"Destructive: Δθ = {delta_theta(r_destruct):.6f} rad (mod 2π)")
