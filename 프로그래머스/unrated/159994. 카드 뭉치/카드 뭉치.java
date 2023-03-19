import java.util.*;

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "";
        List<String> l_cards1 = new ArrayList<>(Arrays.asList(cards1));
        List<String> l_cards2 = new ArrayList<>(Arrays.asList(cards2));
        
        Boolean flag = false;
        for(String item : goal){
            
            if(l_cards1.size() > 0 && item.equals(l_cards1.get(0))){
                l_cards1.remove(0);
                continue;
            }

            if(l_cards2.size() > 0 && item.equals(l_cards2.get(0))){
                l_cards2.remove(0);
                continue;
            }

            flag = true;
        }
        if(flag){
            answer = "No";
        }else{
            answer = "Yes";
        }

        return answer;
    }
}
