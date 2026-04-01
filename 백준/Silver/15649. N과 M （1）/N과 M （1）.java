import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Main {

    static int N, M;
    static boolean[] visited;
    static Stack<Integer> stack;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        visited = new boolean[N + 1];
        stack = new Stack<>();

        permutations(0);
    }

    public static void permutations(int depth) {
        if (depth == M) {
            String result = stack.stream().map(String::valueOf).collect(Collectors.joining(" "));
            System.out.println(result);
            return;
        }

        for (int i = 1; i < N + 1; i++) {
            if (!visited[i]) {
                visited[i] = true;
                stack.push(i);
                permutations(depth + 1);
                stack.pop();
                visited[i] = false;
            }

        }
    }

}
