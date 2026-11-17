import fs from 'node:fs';
const buf = fs.readFileSync(process.argv[2]);
const { instance } = await WebAssembly.instantiate(buf, {});
const n = 100000;
for (const [name, kind] of [["ChaCha8",0],["Xoshiro256++",1]]) {
  for (const irr of [0,1]) {
    instance.exports.wasm_run(kind, 2000, irr); // warm-up
    const t = performance.now();
    const r = instance.exports.wasm_run(kind, n, irr);
    const dt = (performance.now() - t)/1000;
    console.log(`wasm(node ${process.version}) 1T ${name} irr=${!!irr}: n=${n} ${dt.toFixed(3)}s ${(n/dt).toFixed(0)} paths/s result=${r.toExponential(17)}`);
  }
}
