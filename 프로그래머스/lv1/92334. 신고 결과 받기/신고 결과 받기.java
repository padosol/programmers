import java.util.*;
class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        Arrays.fill(answer, 0);
        Map<String, Set<String>> map = new LinkedHashMap<>();
        for(String item : id_list){
            map.put(item, new HashSet<>());
        }

        for(String item : report){
            String[] tmp = item.split(" ");
            map.get(tmp[1]).add(tmp[0]);
        }

        for(String item : map.keySet()){
            if(map.get(item).size()>=k){
                int idx = 0;
                for(String count : map.keySet()){
                    if(map.get(item).contains(count)){
                        answer[idx++]++;
                    }else{
                        idx++;
                    }
                }
            }
        }

        return answer;
    }
}