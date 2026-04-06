import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    // Map 대신 ArrayList 배열을 사용하는 것이 메모리와 속도 면에서 효율적입니다.
    static ArrayList<City>[] adj;
    static int S, E;
    static int[] dist;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine()); // N과 M은 별도의 줄에 있을 수 있습니다.
        M = Integer.parseInt(br.readLine());

        adj = new ArrayList[N + 1];
        for (int i = 0; i <= N; i++) {
            adj[i] = new ArrayList<>();
        }

        dist = new int[N + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);

        for (int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            // 중복된 길이라도 모두 리스트에 넣습니다.
            // 다익스트라 과정에서 거리순으로 먼저 정렬되므로 문제없습니다.
            adj[s].add(new City(e, v));
        }

        StringTokenizer st = new StringTokenizer(br.readLine());
        S = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        dijkstra();

        System.out.println(dist[E]);
    }

    static void dijkstra() {
        PriorityQueue<City> pq = new PriorityQueue<>();
        pq.add(new City(S, 0));
        dist[S] = 0;

        boolean[] visited = new boolean[N + 1];

        while (!pq.isEmpty()) {
            City curr = pq.poll();

            // 방문 체크: 이미 처리된 노드는 건너뜁니다.
            if (visited[curr.node])
                continue;
            visited[curr.node] = true;

            // 현재 노드와 연결된 모든 다음 노드 탐색
            for (City nextCity : adj[curr.node]) {
                if (dist[nextCity.node] > dist[curr.node] + nextCity.dist) {
                    dist[nextCity.node] = dist[curr.node] + nextCity.dist;
                    pq.add(new City(nextCity.node, dist[nextCity.node]));
                }
            }
        }
    }

    public static class City implements Comparable<City> {
        int node;
        int dist;

        public City(int node, int dist) {
            this.node = node;
            this.dist = dist;
        }

        @Override
        public int compareTo(City o) {
            return this.dist - o.dist;
        }
    }
}