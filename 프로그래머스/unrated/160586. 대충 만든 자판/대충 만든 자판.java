
import java.util.HashMap;
import java.util.Map;

class Solution {
    final int NOT_VALID = 1000;
    final int IMPOSSIBLE = -1;
    
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];

        Map<Character, Integer> dict = new HashMap<>();
        for (String key : keymap) {
            for (int i = 0; i < key.length(); i++) {
                char curChar = key.charAt(i);
                int curPushNum = i + 1;
                int findPushNum = dict.getOrDefault(curChar, NOT_VALID);

                if (curPushNum < findPushNum) {
                    dict.put(curChar, curPushNum);
                }
            }
        }

        for (int idx = 0; idx < targets.length; idx++) {
            int tempVal = 0;
            boolean fail = false;

            String curStr = targets[idx];
            for (int i = 0; i < curStr.length(); i++) {
                char curChar = curStr.charAt(i);
                int findPushNum = dict.getOrDefault(curChar, NOT_VALID);

                if (findPushNum == NOT_VALID) {
                    fail = true;
                    break;
                }

                tempVal += findPushNum;
            }

            if (fail) {
                answer[idx] = IMPOSSIBLE;
            } else {
                answer[idx] = tempVal;
            }

        }
        
        return answer;
    }
}