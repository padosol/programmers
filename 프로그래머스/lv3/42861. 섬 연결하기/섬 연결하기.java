import java.util.*;
class Solution {
    static int[] parent;
    public int solution(int n, int[][] costs) {
        int answer = 0;
        Arrays.sort(costs, (a, b) -> a[2] == b[2]?b[2]-a[2]: -(b[2]-a[2]));

        parent = new int[n];
        for(int i=0;i<n;i++){
            parent[i] = i; 
        }
        for(int i=0; i<costs.length;i++){
            if(union(costs[i][0], costs[i][1])) continue;
            answer+=costs[i][2];
        }
        return answer;
    }
    
        private static int find(int x){
        if(x == parent[x]) return x;
        return find(parent[x]);
    }

    private static boolean union(int a, int b) {

        int pa = find(a);  
        int pb = find(b); 

        if(pa == pb)return true;

        if(pa < pb){
            parent[pb] = pa;
        }else{
            parent[pa] = pb;
        }
        return false;
    }
}