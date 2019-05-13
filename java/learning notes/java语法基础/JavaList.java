import java.util.Scanner;

public class JavaList{
    public static void main(String[] args) {
        int demoArray[] = new int[5];
        long total = 0;
        int len = demoArray.length;
        // int len = demoArray.length;
        System.out.print("enter " + len + " integers ");
        Scanner sc = new Scanner(System.in);
        for (int i=0;i<len;i++){
            demoArray[i] = sc.nextInt();
        }
        for (int i=0;i<len;i++){
            total+=demoArray[i];
        }
        System.out.println("the sum of the list is:"+total);
    }
}