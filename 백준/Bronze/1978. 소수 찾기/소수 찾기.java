import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a = 0;
        int[] arr = new int[n];
        int j;
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
            if (arr[i] == 1) {
                continue;
            }
            for (j = 2; j <= Math.sqrt(arr[i]); j++) {
                if (arr[i] % j == 0) break;
            }
            if (j > Math.sqrt(arr[i])) a++;


        }
        System.out.println(a);
    }
}
