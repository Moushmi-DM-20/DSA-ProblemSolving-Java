//Take 2 numbers as inputs and find their HCF and LCM.

//Solution
class Main {
    public static void main(String[] args) {
        int a = 12;
        int b = 18;
        System.out.println("HCF ="+Hcf(a,b));
        System.out.println("LCM ="+Lcm(a,b));
    }
    public static int Hcf(int a,int b) {
        while(b!=0){
            int temp = b;
            b = a%b;
            a = temp;
        }
        return a;
    }
    public static int Lcm(int a,int b) {
        return (a*b)/Hcf(a,b);
    }
}
