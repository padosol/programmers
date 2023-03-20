class Solution {
    public int solution(int[] array) {
       String num = "";
        for(int i = 0; i< array.length; i++) {
        	num += array[i];
        }
        
        char[] strChar = num.toCharArray();
		int answer = 0;
		
		System.out.println();
		
		for(int i = 0; i<strChar.length; i++) {
			System.out.print(strChar[i]);
			if( strChar[i] == '7') {
				answer++;
			}
		}
        return answer;
    }
}