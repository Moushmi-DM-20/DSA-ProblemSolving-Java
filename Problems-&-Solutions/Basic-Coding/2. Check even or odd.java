//Write a program to check if a number is even or odd.

//solution

import java.util.Scanner;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the number : ");
        int a = scan.nextInt();
        if(a%2==0){
            System.out.println("The number "+ a +" is even.");
        }
        else{
            System.out.println("The number "+ a +" is odd.");
        }
    }
}
