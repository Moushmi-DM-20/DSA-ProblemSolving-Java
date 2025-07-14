//Write a program to input principal, time, and rate (P, T, R) from the user and find Simple Interest.

//Solution
import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the principle amount : ");
        double principle = scan.nextDouble();
        System.out.println("Enter the rate : ");
        int rate = scan.nextInt();
        System.out.println("Enter the time : ");
        double time = scan.nextDouble();
        
        int SI = (int)(principle*rate*time)/100;
        System.out.println("Simple Interest "+SI );
    }
}
