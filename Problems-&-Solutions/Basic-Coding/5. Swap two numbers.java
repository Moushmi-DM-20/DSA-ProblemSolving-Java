//Write a program to swap two numbers.

//Solution
class Main {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;
        System.out.println("Before Swapping");
        System.out.println("A = "+a+" B = "+b);
        System.out.println("After Swapping");
        int temp = a;
        a = b;
        b = temp;
        System.out.println("A = "+a+" B = "+b);
    }
}
