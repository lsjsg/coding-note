import java.util.function.DoubleBinaryOperator;

public class ChangeDatatype {
    public static void main(String[] args) {
        int x;
        double y;
        x = (int) 32.42 + (int) 34.52;
        y = (double) x + (double) 10 + 1;
        System.out.println("the value of x is:" + x);
        System.out.println("the value of y is:" + y);
    }
}