/*
 * Java Quine - 经典实现
 * 
 * 编译和验证:
 *     javac Quine.java && java Quine | diff - Quine.java
 */

public class Quine {
    public static void main(String[] args) {
        String s = "public class Quine {\n    public static void main(String[] args) {\n        String s = %c%s%c;\n        System.out.printf(s, 34, s, 34);\n    }\n}\n";
        System.out.printf(s, 34, s, 34);
    }
}
