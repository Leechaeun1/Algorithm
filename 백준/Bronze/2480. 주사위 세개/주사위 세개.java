import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int max;
        if (a == b && b == c) {
            System.out.println(10000 + a * 1000);
        } else if (a == b || b == c || a == c) {
            int same;
            if (a == b) {
                System.out.println(1000 + a * 100);
            } else if (b == c) {
                System.out.println(1000 + b * 100);

            } else {
                System.out.println(1000 + a * 100);
            }
        } else {
            max = Math.max(a, Math.max(b, c));
            System.out.println(max * 100);
        }
    }
}
