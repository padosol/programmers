import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = null;

        Map<String, Integer> rankMap = new HashMap<>();

        for(int i=0;i<players.length;i++){
            rankMap.put(players[i], i);
        }

        for(int i=0;i< callings.length;i++){
            int num = rankMap.get(callings[i]);

            String back = players[num-1];
            int num2 = rankMap.get(back);

            rankMap.put(callings[i], num-1);
            rankMap.put(back, num);
            players[num-1] = callings[i];
            players[num] = back;
        }

        return players;
    }
}