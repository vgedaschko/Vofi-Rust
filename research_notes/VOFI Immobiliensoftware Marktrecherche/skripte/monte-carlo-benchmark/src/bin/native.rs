use mcbench::*;
use rayon::prelude::*;
use std::time::Instant;
fn main() {
    let n: u32 = 100_000;
    for (name, kind) in [("ChaCha8", 0u32), ("Xoshiro256++", 1u32)] {
        for with_irr in [false, true] {
            let t = Instant::now();
            let r = if kind == 0 { run_chacha(42, 0, n, with_irr) } else { run_xoshiro(42, 0, n, with_irr) };
            let dt = t.elapsed().as_secs_f64();
            println!("native 1T {name} irr={with_irr}: n={n} {:.3}s  {:.0} paths/s  result={:.17e}", dt, n as f64 / dt, r);
            let chunks = 64u32;
            let t = Instant::now();
            let s: f64 = (0..chunks).into_par_iter().map(|c| {
                if kind == 0 { run_chacha(42, c as u64, n / chunks * 4, with_irr) } else { run_xoshiro(42, c, n / chunks * 4, with_irr) }
            }).sum::<f64>() / chunks as f64;
            let dt = t.elapsed().as_secs_f64();
            let total = (n / chunks * 4 * chunks) as f64;
            println!("native rayon({}T) {name} irr={with_irr}: n={} {:.3}s  {:.0} paths/s  result={:.17e}", rayon::current_num_threads(), total, dt, total / dt, s);
        }
    }
}
