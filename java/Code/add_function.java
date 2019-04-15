public class add_function{
    private int val1,val2;
    public void add_func(int x,int y)
    {
        val1 = x;
        val2 = y;
        System.out.println("the sum is:" + (val1 + val2));
    }
    public static void main(String arg[])
    {
        add_function Myobj = new add_function();
        Myobj.add_func(1,2);
    }
}