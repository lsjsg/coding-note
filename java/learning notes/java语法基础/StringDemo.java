import java.util.*;
public class StringDemo{
    public static void main(String[] args) {
        String stuname = "Tom";
        int age = 18;
        float score = 92.5f;

        String info = stuname + " age at " + age + " get score " + score;
        System.out.println(info);
        System.out.println("length of the string is :" + info.length());
        // str.charAt(int) 字符串索引
        System.out.println("char at 6 is: " + info.charAt(6));
        // str.contains(char) 判断字符是否在字符串中
        System.out.println("a is in the info: " + info.contains("a"));
        // str.replace(string,string) 字符串替换
        System.out.println("replacement:" + info.replace("Tom","Jerry"));
        // split() 以指定字符串对当前字符串进行分割
        String test = "test_with_this_string";
        String strArray[] = test.split("_");
        System.out.println(Arrays.toString(strArray));
    }
}