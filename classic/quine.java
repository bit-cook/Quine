/* Quine in Java - verify: javac quine.java && java quine | diff - quine.java */
class quine {
    public static void main(String[] args) {
        String s = "/* Quine in Java - verify: javac quine.java && java quine | diff - quine.java */%cclass quine {%c    public static void main(String[] args) {%c        String s = %c%s%c;%c        System.out.printf(s, 10, 10, 10, 34, s, 34, 10, 10, 10, 10);%c    }%c}%c";
        System.out.printf(s, 10, 10, 10, 34, s, 34, 10, 10, 10, 10);
    }
}
