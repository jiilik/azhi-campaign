"""Step 1 of 4: procedural heightmap for Azhi on a periodic (theta, phi) grid -> build/H.npy, build/grid.npy.
See worldgen/README.md."""
import os
HERE = os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
os.makedirs('build', exist_ok=True); os.makedirs('output', exist_ok=True)
import numpy as np
R, r = 3.0, 1.0
NP = 768            # tubewise samples (phi)
NT = NP * 3         # ringwise samples (theta)  ~isotropic at mid-ring
rng = np.random.default_rng(7)

th = np.linspace(0, 2*np.pi, NT, endpoint=False)
ph = np.linspace(-np.pi, np.pi, NP, endpoint=False)
TH, PH = np.meshgrid(th, ph)          # shape (NP, NT)

def fbm(beta, seed, lo=2):
    g = np.random.default_rng(seed)
    w = g.normal(size=(NP, NT))
    F = np.fft.fft2(w)
    ky = np.fft.fftfreq(NP)*NP; kx = np.fft.fftfreq(NT)*NT/3
    KX, KY = np.meshgrid(kx, ky)
    k = np.sqrt(KX**2+KY**2); k[0,0]=1
    filt = k**(-beta/2); filt[k<lo]=0
    n = np.real(np.fft.ifft2(F*filt)); n/=n.std(); return n

def wrap(a): return (a+np.pi)%(2*np.pi)-np.pi
def gauss(dt, dp, st, sp): return np.exp(-(wrap(dt)/st)**2-(wrap(dp)/sp)**2)

n1 = fbm(3.2, 1); n2 = fbm(2.4, 2, lo=8); n3 = fbm(3.6, 3)
ridged = 1-np.abs(fbm(2.6, 4, lo=6)); ridged = ridged/ridged.max()

H = 0.45*np.cos(PH)                         # outer high, inner low
H += -0.55*np.exp(-((np.abs(PH)-np.pi)/0.75)**2)   # belly basin
H += 0.42*n1 + 0.10*n2

# --- spine: vertebrae, with gap at the Bite and thinning toward the tail
dt0 = wrap(TH)                              # theta relative to the Bite
tail = np.clip((TH-(2*np.pi-1.6))/1.6, 0, 1)  # 0..1 over the last stretch
spw = 0.20*(1-0.45*tail)
vert = 1+0.30*np.cos(70*TH)
spine = (1.05-0.35*tail)*vert*np.exp(-(PH/spw)**2)*(0.6+0.5*ridged)
spine *= 1-0.85*np.exp(-(dt0/0.035)**2)     # the Bite: jaws close over the tail
H += spine

# --- head: skull dome, horns, eye-socket lakes
H += 0.75*gauss(TH-0.17, PH, 0.11, 0.55)
for s in (1,-1):
    for k in range(25):
        t=k/24; H += 0.35*(1-0.5*t)*gauss(TH-(0.22+0.38*t), PH-s*(0.28+0.12*t), 0.035, 0.07)
    H -= 0.75*gauss(TH-0.12, PH-s*0.55, 0.04, 0.12)   # eye sockets -> crater lakes

# --- lower jaw: a U-shaped mandible across the belly; chin at the Bite, opening toward the hinge
dpi = wrap(PH-np.pi)
J = np.zeros_like(H)
for s in (1,-1):
    for k in range(80):
        t=k/79; tc = -0.02+0.50*t; pc = s*(0.05+0.32*t**0.75)
        J += gauss(TH-tc, dpi-pc, 0.030, 0.055)*(1-0.25*t)
    for k in range(16):                                      # teeth along the inner rim
        t=(k+0.5)/16*0.8; tc=-0.02+0.50*t; pc=s*(0.05+0.32*t**0.75-0.045)
        J += 1.4*gauss(TH-tc, dpi-pc, 0.010, 0.018)
    for k in range(40):                                      # rami curving up to the skull hinge
        t=k/39; H += 0.32*(1-0.5*t)*gauss(TH-(0.48-0.16*t**2), dpi-s*(0.38+1.45*t), 0.035, 0.08)*np.clip(0.5+0.6*n3,0,1.2)
J = J/np.percentile(J[J>0.05],95)
H += 2.15*np.clip(J,0,1.6)*(0.9+0.15*n2)
H -= 0.35*gauss(TH-0.25, dpi, 0.16, 0.12)                    # the Maw: lagoon cradled by the jaw
# --- vestigial limbs (subtle, eroded)
erode = np.clip(0.8+0.35*n3, 0.25, 1.1)*(0.45+0.75*ridged)
def limb(t0, sweep, reach, amp, toes, s, width=0.05, bend=0.0):
    out = np.zeros_like(H)
    for k in range(60):
        t=k/59
        tc = t0+sweep*t+bend*np.sin(np.pi*t); pc = s*(0.3+reach*t)
        out += amp*(1-0.3*t)*gauss(TH-tc, PH-pc, width, width*1.2)
    for j in range(toes):                   # claw peninsulas at the end
        a = (j-(toes-1)/2)*0.06
        for k in range(12):
            t=k/11; out += 0.9*amp*gauss(TH-(t0+sweep+a*(1+t)), PH-s*(0.3+reach+0.25*t), 0.02, 0.028)
    return out*erode
L = np.zeros_like(H)
for s in (1,-1):
    L += limb(0.80, 0.05, 1.55, 0.12, 4, s, width=0.055, bend=0.18)        # forelimbs
    L += limb(3.30, -0.05, 1.65, 0.13, 4, s, width=0.06, bend=0.22)        # hindlimbs
    for (sw,re) in [(0.95,0.30),(0.85,0.62),(0.62,0.95),(0.35,1.2)]:         # wing spars
        L += limb(1.25, sw, re, 0.035, 0, s, width=0.03, bend=-0.04)
H += L*2.4

np.save('build/H.npy', H); np.save('build/grid.npy', np.stack([TH,PH]))
print('terrain ok', H.shape)
