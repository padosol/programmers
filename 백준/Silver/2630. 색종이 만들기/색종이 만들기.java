import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static int[][] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        graph = new int[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        divide(0, 0, N);

        System.out.println(count[0]);
        System.out.println(count[1]);
    }

    static int[] count = { 0, 0 };

    public static void divide(int x, int y, int size) {
        int color = graph[x][y];
        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (color != graph[i][j]) {

                    int quarter = size / 2;

                    divide(x, y, quarter);
                    divide(x + quarter, y, quarter);
                    divide(x, y + quarter, quarter);
                    divide(x + quarter, y + quarter, quarter);

                    return;
                }

            }
        }

        count[color] += 1;
    }

}

// input
// 8
// 1 1 0 0 0 0 1 1
// 1 1 0 0 0 0 1 1
// 0 0 0 0 1 1 0 0
// 0 0 0 0 1 1 0 0
// 1 0 0 0 1 1 1 1
// 0 1 0 0 1 1 1 1
// 0 0 1 1 1 1 1 1
// 0 0 1 1 1 1 1 1

// output
// 9
// 7