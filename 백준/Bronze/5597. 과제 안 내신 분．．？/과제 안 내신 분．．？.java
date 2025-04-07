import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[28];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);
        int[] arr2 = new int[30];
        for (int i=0;i<30;i++){
            arr2[i] = i+1;
        }

        Set<Integer> set1 = new HashSet<>();
        for (int num : arr){
            set1.add(num);
        }

        Set<Integer> set2 = new HashSet<>();
        for (int num : arr2){
            set2.add(num);
        }

        Set<Integer> diff = new HashSet<>(set2);
        diff.removeAll(set1);

        for (int num : diff){
            System.out.println(num);
        }
    }
}
