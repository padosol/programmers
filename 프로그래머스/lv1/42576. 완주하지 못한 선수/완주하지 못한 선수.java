import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
		Arrays.sort(participant);
		Arrays.sort(completion);

		String answer = participant[participant.length-1];

		for(int i=0;i< completion.length;i++){
			if(!completion[i].equals(participant[i])){
				return participant[i];
			}
		}
		return answer;
    }
}