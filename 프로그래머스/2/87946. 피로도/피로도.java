import java.util.Arrays;
class Solution {
    public int solution(int k, int[][] dungeons) {
        int answer = 0;
        boolean[] visited = new boolean[dungeons.length];
        Arrays.fill(visited, false);

        answer = dfs(k, dungeons, visited, 0,0);

        return answer;
    }
    
    
    public static int dfs(int k, int[][] dungeons, boolean[] visited, int max, int count) {

        int maxCount = max;

        for(int i=0;i<dungeons.length;i++) {
            if(!visited[i] && k >= dungeons[i][0]) {
                visited[i] = true;
                maxCount = dfs(k - dungeons[i][1], dungeons, visited, maxCount,count+1);
                visited[i] = false;
            }
        }

        return Math.max(maxCount, count);
    }
    
    
}