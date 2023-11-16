import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

class Solution {
    public int solution(String numbers) {
        int answer = 0;

        boolean[] visited = new boolean[numbers.length()];
        String[] number = numbers.split("");

        Set<Integer> numberSet = new HashSet<>();

        dfs(number, "",  visited,  numberSet);

        Iterator<Integer> iter = numberSet.iterator();
        while(iter.hasNext()) {
            int num = iter.next();

            if(isPrime(num)) {
                answer++;
            }
        }

        return answer;
    }
    
    
    
    public static boolean isPrime(int num){

        if(num == 0 || num == 1) {
            return false;
        }

        for(int i=2; i*i<=num; i++){
            if(num % i == 0) return false;
        }

        return true;
    }
    
    public static void dfs(String[] number, String pn, boolean[] visited, Set<Integer> numberSet) {

        for(int i=0;i< number.length;i++) {
            if(!visited[i]) {
                visited[i] = true;
                String nexNn = pn + number[i];
                numberSet.add(Integer.parseInt(nexNn));
                dfs(number, nexNn, visited, numberSet);
                visited[i] = false;
            }
        }

    }
    
    
}