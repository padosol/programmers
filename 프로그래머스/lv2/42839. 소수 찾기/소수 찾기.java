import java.util.*;

class Solution {
    
    static Set<Integer> numbersSet = new HashSet<>();
    
    public int solution(String numbers) {
        int answer = 0;

        bfs("", numbers);

        for(Integer item : numbersSet){
            if(isPrime(item))answer++;
        }

        return answer;
    }
    
        public static boolean isPrime(int num){
        if(num == 0 || num == 1)return false;
        int max = (int)Math.sqrt(num);
            
        for(int i=2;i<max+1;i++){
            if(num%i == 0)return false;
        }

        return true;
    }
    
        public static void bfs(String first, String second){

        if(!first.equals("")){
            numbersSet.add(Integer.valueOf(first));
        }

        for(int i=0;i<second.length();i++){
            bfs(first + second.charAt(i), second.substring(0, i) + second.substring(i+1));
        }
    }
    
    
    
}