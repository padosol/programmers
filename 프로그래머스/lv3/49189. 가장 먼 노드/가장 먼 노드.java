import java.util.*;
class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        Arrays.sort(edge, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });
        
        
        ArrayList<ArrayList<Integer>> graphs = new ArrayList<>();
        
        for(int i=0;i<=n;i++){
            graphs.add(new ArrayList<>());
        }

        for(int[] vertex : edge){
            graphs.get(vertex[0]).add(vertex[1]);
            graphs.get(vertex[1]).add(vertex[0]);
        }
        
        
        Queue<Integer> q = new LinkedList<>();
        boolean[] visited = new boolean[n+1];
        
        int start = 1;

        q.add(start);
        visited[start] = true;

        while(!q.isEmpty()){
            int size = q.size();

            for(int i=0;i<size;i++){
                int next = q.poll(); 

                for(int j=0;j<graphs.get(next).size();j++){
                    int now = graphs.get(next).get(j);
                    if(!visited[now]){
                        visited[now] = true;
                        q.add(now);
                    }
                }
            }

            answer = size;
        }
        
        return answer;
    }
}