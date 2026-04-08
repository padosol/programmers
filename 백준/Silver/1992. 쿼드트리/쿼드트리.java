import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int N;
    static int[][] arr;

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        arr = new int[N][N];

        for (int i = 0; i < N; i++) {
            String str = br.readLine();
            for (int j = 0; j < N; j++) {
                arr[i][j] = str.charAt(j) - '0';
            }
        }

        divide(0, 0, N);
    }

    public static void divide(int x, int y, int size) {

        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (arr[i][j] != arr[x][y]) {

                    // 나누기 4분할로
                    System.out.print("(");
                    divide(x, y, size / 2);
                    divide(x, y + size / 2, size / 2);
                    divide(x + size / 2, y, size / 2);
                    divide(x + size / 2, y + size / 2, size / 2);
                    System.out.print(")");
                    return;
                }
            }
        }

        System.out.print(arr[x][y]);
    }

}
