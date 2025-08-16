//Subtract the Product and Sum

//Solution

class Solution {
    public int subtractProductAndSum(int n) {
        return product(n)-sum(n);
    }
    public static int product(int n){
        int product = 1;
        while(n>0){
            int rem = n%10;
            product *= rem;
            n = n/10;
        }
        return product;
    }
    public static int sum(int n){
        int sum = 0;
        while(n>0){
            int rem = n%10;
            sum += rem;
            n = n/10; 
        }
        return sum;
    }
}
