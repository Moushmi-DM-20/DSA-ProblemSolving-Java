//Take in two numbers and an operator (+, -, *, /) and calculate the value. (Use if conditions)

//Solution
import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter first number : ");
        int num1 = scan.nextInt();
        System.out.println("Enter second number : ");
        int num2 = scan.nextInt();
        System.out.println("Enter an operator (+,-,*,/) : ");
        char operator = scan.next().charAt(0);
        int result=0;
        
        if(operator == '+'){
            result = num1+num2;
        }
        else if(operator == '-'){
            result = num1-num2;
        }
        else if(operator == '*'){
            result = num1-num2;
        }
        else if(operator == '/'){
            result = num1-num2;
        }
        else{
            System.out.println("Invalid Operator");
        }
        System.out.println("Result = "+result);
    }
}
