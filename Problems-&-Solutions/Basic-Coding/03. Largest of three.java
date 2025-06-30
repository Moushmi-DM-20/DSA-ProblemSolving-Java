//Write a program to find the largest of three numbers.

//solution
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter first number : ");
        int a = scan.nextInt();
        System.out.println("Enter second number : ");
        int b = scan.nextInt();
        System.out.println("Enter third number : ");
        int c = scan.nextInt();
        if(a>b && a>c){
            System.out.println("The number a = "+ a +" is greatest.");
        }
        else if(b>a && b>c){
            System.out.println("The number b = "+ b +" is greatest.");
        }
        else{
            System.out.println("The number c = "+ c +" is greatest.");
        }
    }
}
