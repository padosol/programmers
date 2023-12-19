class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;

        boolean[] visited = new boolean[n];

        for(int i=0;i<n;i++) {

            if(!visited[i]) {
                dfs(n, computers, i, visited);
                answer++;
            }

        }

        return answer;
    }
    
    
    public static void dfs(int n, int[][] computers, int i, boolean[] visited) {
        visited[i] = true;

        for(int j=0;j<n;j++) {

            if(i != j && computers[i][j] == 1 && !visited[j]) {
                dfs(n, computers, j, visited);
            }
        }
    }
    
}