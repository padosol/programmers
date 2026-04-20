import java.util.*;

class Solution {
    int n;
    int infection;
    int[][] edges;
    int k;
    int answer = 0;
    List<Node>[] nodes;
    
    public int solution(int n, int infection, int[][] edges, int k) {
        this.n = n;
        this.infection = infection;
        this.edges = edges;
        this.k = k;
        
        this.nodes = new ArrayList[n + 1];

        for (int i = 1; i <= n; i++) {
            this.nodes[i] = new ArrayList<>();
        }

        for (int[] edge : edges) {
            this.nodes[edge[0]].add(new Node(edge[1], edge[2]));
            this.nodes[edge[1]].add(new Node(edge[0], edge[2]));
        }
        
        
        boolean[] visited = new boolean[n + 1];
        visited[infection] = true;

        dfs(0, visited);
        
        return this.answer;
    }
    
    
    public void dfs(int depth, boolean[] visited) {
        int count = 0;
        for (int i = 0; i < visited.length; i++) {
            if (visited[i]) {
                count++;
            }
        }

        this.answer = Math.max(this.answer, count);

        if (depth == k) {
            return;
        }

        for (int i = 1; i <= 3; i++) {
            // 감염
            boolean[] nextVisited = visited.clone();
            bfs(i, nextVisited);

            // 다음 파이프라인
            dfs(depth + 1, nextVisited);
        }
    }

    public void bfs(int type, boolean[] visited) {
        Deque<Integer> q = new LinkedList<>();

        for (int i = 1; i <= n; i++) {
            if (visited[i]) {
                q.add(i);
            }
        }

        while (!q.isEmpty()) {
            int node = q.poll();

            for (Node n : this.nodes[node]) {
                if (n.type == type && !visited[n.node]) {
                    visited[n.node] = true;
                    q.add(n.node);
                }
            }
        }
    }

    public class Node {
        int node;
        int type;

        public Node(int node, int type) {
            this.node = node;
            this.type = type;
        }
    }

    
}