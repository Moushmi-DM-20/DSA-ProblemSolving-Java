// Find the ceiling of a number

//Solution
public class Ceiling {
	public static void main(String[] args) {
        int[] arr = {2,3,5,6,9,14,16,18};
        int target = 15;
        int result = ceilValue(arr, target);       		
        System.out.println(result);
    }
	public static int ceilValue(int[] arr, int target) {
		int start = 0;
    int end = arr.length-1;
    int answer = 0;
    while(start<=end){
        int mid = start+(end-start)/2;
        if(arr[mid]==target){
            answer =  arr[mid];
            break;
        }
        else if(arr[mid]<target) {
          start = mid+1;
          answer = arr[start];
        }
        else {
          end = mid-1;
        }
    }
    return answer;
	}
}
