//Print all Armstrong numbers from 1 to 1000.

//Solution
class Main {
    public static void main(String[] args) {
        for(int i=0;i<=1000;i++){
            int sum = 0;
            int original = i;
            int num = original;
            while(num>0){
                int rem = num%10;
                sum = sum+(rem*rem*rem);
                num = num/10;    
            }
            if(original==sum){
                System.out.println(sum);
            }
        }
    } 
}
