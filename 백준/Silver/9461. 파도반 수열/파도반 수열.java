import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N;
    static long[] arr;

    public static void main(String[] args) throws NumberFormatException, IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        arr = new long[100];
        arr[0] = 1;
        arr[1] = 1;
        arr[2] = 1;
        arr[3] = 2;
        arr[4] = 2;

        for (int i = 5; i < 100; i++) {
            arr[i] = arr[i - 1] + arr[i - 5];
        }

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            System.out.println(arr[num - 1]);
        }
    }
}
