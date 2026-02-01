/*
 * Rust Quine - 经典实现
 * 
 * 编译和验证:
 *     rustc quine.rs && ./quine | diff - quine.rs
 */

fn main() {
    let s = "fn main() {\n    let s = %c%s%c;\n    println!(s, 34, s, 34);\n}\n";
    println!(s, 34, s, 34);
}
