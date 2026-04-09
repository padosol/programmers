import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    static int N, M;
    static ArrayList<City>[] cities;
    static int[] dist;
    static int S, E;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        cities = new ArrayList[N + 1];
        dist = new int[N + 1];
        Arrays.fill(dist, -1); // 최소 중량은 0 이상이므로 -1로 초기화

        for (int i = 1; i <= N; i++) {
            cities[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            cities[u].add(new City(v, w));
            cities[v].add(new City(u, w));
        }

        st = new StringTokenizer(br.readLine());
        S = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        solve();
    }

    static void solve() {
        // 내림차순 정렬 (최대 힙)
        PriorityQueue<City> pq = new PriorityQueue<>();
        pq.add(new City(S, Integer.MAX_VALUE));
        dist[S] = Integer.MAX_VALUE;

        while (!pq.isEmpty()) {
            City cur = pq.poll();
            int u = cur.num;
            int curW = cur.weight;

            // 이미 확인한 경로보다 중량이 작으면 스킵 (최적화)
            if (dist[u] > curW)
                continue;

            // 목적지 도착 시 즉시 종료 가능 (최대 힙이므로 처음 도착이 최대값)
            if (u == E) {
                System.out.println(curW);
                return;
            }

            for (City next : cities[u]) {
                // 다음 지점까지의 중량 제한은 (현재까지의 제한, 다리의 제한) 중 최솟값
                int nextWeight = Math.min(curW, next.weight);

                // 만약 다음 지점에 기록된 최대 중량보다 지금 경로가 더 크다면 갱신
                if (dist[next.num] < nextWeight) {
                    dist[next.num] = nextWeight;
                    pq.add(new City(next.num, nextWeight));
                }
            }
        }
    }

    public static class City implements Comparable<City> {
        int num;
        int weight;

        public City(int num, int weight) {
            this.num = num;
            this.weight = weight;
        }

        @Override
        public int compareTo(City o) {
            // 내림차순: 큰 값이 우선순위를 가짐
            return o.weight - this.weight;
        }
    }
}