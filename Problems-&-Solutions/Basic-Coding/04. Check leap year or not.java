//Write a program to check if a year is a leap year or not.

//Solution
import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the year : ");
        int a = scan.nextInt();
        if((a%4==0 && a%100 != 0) || (a%400 == 0)){
            System.out.println(a +" is a leap year.");
        }
        else{
            System.out.println(a +" is not a leap year.");
        }
    }
}
