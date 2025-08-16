//Given a,b,c,d print the output as a/b ÷ c/d

//Solution

import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter a number1 : ");
        int a = scan.nextInt();
        System.out.print("Enter a number2 : ");
        int b = scan.nextInt();
        System.out.print("Enter a number3 : ");
        int c = scan.nextInt();
        System.out.print("Enter a number4 : ");
        int d = scan.nextInt();
        if(a==0||d==0){
            System.out.println("0");
        }
        else if(b==0||c==0){
            System.out.println("Number 2,3 must not be zero");
        }
        else{
            int num = a*d;
            int deno = b*c;
            System.out.println(num+"/"+deno);
        }
    }
}
