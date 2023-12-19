import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;
        int xMax = maps.length - 1;
        int yMax = maps[0].length - 1;
        
        boolean success = false;


        boolean[][] visited = new boolean[maps.length][maps[0].length];

        Queue<int[]> position = new LinkedList<>();
        position.add(new int[]{0,0});
        visited[0][0] = true;

        while(!position.isEmpty()) {

            int size = position.size();

            for(int i=0;i<size;i++) {

                int[] map = position.poll();

                int x = map[0];
                int y = map[1];

                if( x == xMax && y == yMax) {
                    success = true;
                    position.clear();
                    break;
                }

                // 상
                if( x - 1 >= 0 && maps[x-1][y] == 1 && !visited[x-1][y]) {
                    visited[x-1][y] = true;
                    position.add(new int[]{x-1, y});
                }

                // 하
                if( x + 1 <= xMax && maps[x+1][y] == 1 && !visited[x+1][y]) {
                    visited[x+1][y] = true;
                    position.add(new int[]{x+1, y});
                }

                // 좌
                if(y-1 >= 0 && maps[x][y-1] == 1 && !visited[x][y-1]) {
                    visited[x][y-1] = true;
                    position.add(new int[]{x, y-1});
                }

                // 우
                if( y + 1 <= yMax && maps[x][y + 1] == 1 && !visited[x][y+1]) {
                    visited[x][y+1] = true;
                    position.add(new int[]{x, y+1});
                }
            }

            answer++;
        }
        
        return success?answer:-1;
    }
}