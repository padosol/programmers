import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int n, k, answer;
    static int[] arr;
    static boolean[] visit;
    //static int[] ansArr;
    // public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        arr = new int[n];
        // ansArr = new int[n];
        for(int i=0; i<n; i++){
            arr[i]=Integer.parseInt(st.nextToken());
        }
        visit=new boolean[n];
        answer=0;
        dfs(500, 0);
        System.out.println(answer);
        // System.out.println(sb);
    }

    public static void dfs(int sum, int cnt){
        if(cnt == n){
            answer++;
            // for(int val:ansArr) sb.append(val).append(" ");
            // sb.append("\n");
            return;
        }
        for(int i=0; i<n; i++){
            if(!visit[i] && sum+arr[i]-k >= 500) {
                visit[i]=true;
                // ansArr[cnt]=i+1;
                dfs(sum+arr[i]-k, cnt+1);
                visit[i]=false;
            }
        }
    }
}