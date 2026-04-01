import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N, K;
    static int[] kits;
    static boolean[] visited;
    static int count = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        kits = new int[N];
        visited = new boolean[N];

        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
            kits[i] = Integer.parseInt(st.nextToken());
        }

        backtracking(500, 0);

        System.out.println(count);
    }

    public static void backtracking(int weight, int depth) {

        if (depth == N) {
            count++;
            return;
        }

        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                int nextWeight = weight + kits[i] - K;

                if (nextWeight >= 500) {
                    visited[i] = true;
                    backtracking(nextWeight, depth + 1);
                    visited[i] = false;
                }
            }
        }

    }

}
