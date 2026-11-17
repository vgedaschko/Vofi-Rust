use rand::{Rng, SeedableRng};
use rand_chacha::ChaCha8Rng;
use rand_distr::StandardNormal;
use rand_xoshiro::Xoshiro256PlusPlus;

pub const PERIODS: usize = 360; // 30 Jahre monatlich

// Cholesky-Faktor einer festen 3x3-Korrelationsmatrix (Miete, Zins, Leerstand)
const L: [[f64; 3]; 3] = [
    [1.0, 0.0, 0.0],
    [0.3, 0.953_939_201_416_945_6, 0.0],
    [-0.4, 0.020_965_696_734_438_5, 0.916_275_103_152_869_6],
];

#[inline]
fn npv(cf: &[f64], r_m: f64) -> (f64, f64) {
    // liefert NPV und Ableitung nach r
    let mut v = 0.0;
    let mut d = 0.0;
    let mut df = 1.0;
    let q = 1.0 / (1.0 + r_m);
    for (t, c) in cf.iter().enumerate() {
        v += c * df;
        d -= (t as f64) * c * df * q;
        df *= q;
    }
    (v, d)
}

#[inline]
fn irr(cf: &[f64]) -> f64 {
    let mut r = 0.004;
    for _ in 0..50 {
        let (v, d) = npv(cf, r);
        if d.abs() < 1e-14 { break; }
        let step = v / d;
        r -= step;
        if r <= -0.99 { r = -0.99; }
        if step.abs() < 1e-12 { break; }
    }
    r
}

#[inline]
fn one_path<R: Rng>(rng: &mut R, cf: &mut [f64; PERIODS + 1], with_irr: bool) -> f64 {
    let price = 5_000_000.0;
    let equity = 0.3 * price;
    let mut debt = price - equity;
    let mut rent = 22_000.0_f64; // Monatsmiete
    let mut rate = 0.038_f64; // Zins p.a.
    let mut vacancy = 0.03_f64;
    let annuity_rate = 0.058 / 12.0;
    let annuity = (price - equity) * annuity_rate;
    cf[0] = -equity;
    for t in 1..=PERIODS {
        let z0: f64 = rng.sample(StandardNormal);
        let z1: f64 = rng.sample(StandardNormal);
        let z2: f64 = rng.sample(StandardNormal);
        let e0 = L[0][0] * z0;
        let e1 = L[1][0] * z0 + L[1][1] * z1;
        let e2 = L[2][0] * z0 + L[2][1] * z1 + L[2][2] * z2;
        rent *= libm::exp(0.02 / 12.0 + 0.01 * e0);
        if t % 120 == 0 { rate = (rate + 0.01 * e1).max(0.005); }
        vacancy = (vacancy + 0.2 * (0.03 - vacancy) + 0.005 * e2).clamp(0.0, 0.5);
        let interest = debt * rate / 12.0;
        let principal = (annuity - interest).max(0.0).min(debt);
        debt -= principal;
        let noi = rent * (1.0 - vacancy) * 0.82;
        let tax = ((noi - interest - price * 0.8 * 0.02 / 12.0) * 0.3).max(0.0);
        cf[t] = noi - interest - principal - tax;
    }
    cf[PERIODS] += rent * 12.0 * 22.0 - debt; // Exit
    if with_irr { irr(&cf[..]) } else { npv(&cf[..], 0.05 / 12.0).0 }
}

pub fn run_chacha(seed: u64, stream: u64, n: u32, with_irr: bool) -> f64 {
    let mut rng = ChaCha8Rng::seed_from_u64(seed);
    rng.set_stream(stream);
    let mut cf = [0.0; PERIODS + 1];
    let mut acc = 0.0;
    for _ in 0..n { acc += one_path(&mut rng, &mut cf, with_irr); }
    acc / n as f64
}

pub fn run_xoshiro(seed: u64, jumps: u32, n: u32, with_irr: bool) -> f64 {
    let mut rng = Xoshiro256PlusPlus::seed_from_u64(seed);
    for _ in 0..jumps { rng.jump(); }
    let mut cf = [0.0; PERIODS + 1];
    let mut acc = 0.0;
    for _ in 0..n { acc += one_path(&mut rng, &mut cf, with_irr); }
    acc / n as f64
}

#[no_mangle]
pub extern "C" fn wasm_run(kind: u32, n: u32, with_irr: u32) -> f64 {
    if kind == 0 { run_chacha(42, 0, n, with_irr != 0) } else { run_xoshiro(42, 0, n, with_irr != 0) }
}
