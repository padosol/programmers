import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;
import java.util.StringTokenizer;

public class Main {

    static int N, M;
    static ArrayList<Integer>[] graph;
    static int result = Integer.MAX_VALUE;
    static int count;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        graph = new ArrayList[N + 1];
        for (int i = 0; i < N + 1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            graph[start].add(end);
            graph[end].add(start);
        }

        for (int i = 1; i <= N; i++) {
            bfs(i);
        }

        System.out.println(count);
    }

    public static void bfs(int start) {
        Deque<Integer> q = new ArrayDeque<>();
        int[] visited = new int[N + 1];
        Arrays.fill(visited, -1);

        q.add(start);
        visited[start] = 0;

        while (!q.isEmpty()) {
            Integer num = q.poll();

            for (Integer nextNum : graph[num]) {
                if (visited[nextNum] == -1) {
                    visited[nextNum] = visited[num] + 1;

                    q.add(nextNum);
                }

            }
        }

        int total = 0;
        for (int i = 1; i <= N; i++) {
            total += visited[i];
        }

        if (total < result) {
            result = total;
            count = start;
        }
    }

}