//Write a program to input principal, time, and rate (P, T, R) from the user and find Simple Interest.

//Solution
import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double principle = scan.nextDouble();
        int rate = scan.nextInt();
        double time = scan.nextDouble();
        
        int SI = (int)(principle*rate*time)/100;
        System.out.println("Simple Interest "+SI );
    }
}
