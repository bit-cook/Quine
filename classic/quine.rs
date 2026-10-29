/*
 * Rust Quine - classic self-reproducing program.
 * Build & verify: rustc -O quine.rs && ./quine | diff - quine.rs
 */

fn main() {
    let s = "/*\n * Rust Quine - classic self-reproducing program.\n * Build & verify: rustc -O quine.rs && ./quine | diff - quine.rs\n */\n\nfn main() {\n    let s = @;\n    print!(\"{}\", s.replacen('@', &format!(\"{:?}\", s), 1))\n}\n";
    print!("{}", s.replacen('@', &format!("{:?}", s), 1))
}
