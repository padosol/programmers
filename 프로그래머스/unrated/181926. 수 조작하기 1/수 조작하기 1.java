import java.util.*;
class Solution {
    public int solution(int n, String control) {
        int answer = 0;
        
        for(int i=0;i<control.length();i++){
            if(control.charAt(i) == 'w'){
                n += 1;
            } else if ( control.charAt(i) == 's' ){
                n -= 1;
            } else if (control.charAt(i) == 'd'){
                n += 10;
            } else {
                n -= 10;
            }
            
        }
        
        return n;
    }
}