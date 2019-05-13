public class StringBufferDemo{
    public static void main(String[] args) {
        StringBuffer str = new StringBuffer("test string buffer");
        str.append(true);
        System.out.println(str);
        str.deleteCharAt(4);
        System.out.println(str);
        str.delete(0,4);
        System.out.println(str);
        str.insert(3, "3");
        System.out.println(str);
        // '' is for char while "" is for strings
        str.setCharAt(4, 'z');
        System.out.println(str);
        int times = 1000;
        for (int i=0;i<1000;i++){
            str.append(' ');
        }
        long time1 = System.currentTimeMillis();
        System.out.println("Change of string buffer need"+(time1 - times)+"ms");
    }
}