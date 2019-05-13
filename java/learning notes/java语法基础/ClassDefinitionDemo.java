public class ClassDefinitionDemo {
    public static void main(String[] args) {
        // define class named Student
        class Student {
            // define the variables
            String name;
            int age;
            float score;

            // create function inside a class
            void say() {
                System.out.println(name + " age is " + age + ", score is " + score);
            }
        }
        // create instance, must use new
        Student stu1 = new Student();
        stu1.name = "test";
        stu1.age = 18;
        stu1.score = 98.5f;
        stu1.say();
    }
}