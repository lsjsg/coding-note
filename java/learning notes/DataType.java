import javax.swing.plaf.synth.SynthMenuBarUI;

public class DataType {
    public static void main(String[] args) {
        char name1 = 'a';
        char name2 = 'b';
        char name3 = 'c';
        System.out.println("name is:" + name1 + name2 + name3);

        short a = 22;
        int b = 022;
        long c = 0x22L;
        System.out.println("Convert into octa is:a=" + a + ",b=" + b + ",c=" + c);

        float x = 0.12341f;
        double y = 0.234;
        System.out.println("The product of " + x + " and " + y + " is:" + x * y);

        boolean e = 10 > 100;
        boolean f = 3 < 4;
        if (f) {
            System.out.println(f);
        } else {
            System.out.println("Error");
        }
    }
}