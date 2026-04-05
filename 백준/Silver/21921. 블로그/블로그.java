import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int X, N;
    static int[] arr;
    static int result = 0;
    static int max = 0;
    static int count = 1;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        X = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        arr = new int[X];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < X; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < N; i++) {
            result += arr[i];
        }

        max = result;

        for (int i = N; i < X; i++) {
            result = result + arr[i] - arr[i - N];

            if (max == result) {
                count++;
            } else if (max < result) {
                max = result;
                count = 1;
            }
        }

        if (max == 0) {
            System.out.println("SAD");
        } else {
            System.out.println(max);
            System.out.println(count);
        }
    }
}
