import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    static int endX;
    static int endY;
    static int count = 0;
    
    public int solution(int[][] maps) {
        endX = maps[0].length - 1;
        endY = maps.length - 1;

        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[]{0,0,0});

        int[][] directions = {{0, -1}, {0 ,1}, {1, 0}, {-1, 0}};
        boolean[][] visited = new boolean[endY + 1][endX + 1];
        visited[0][0] = true;

        while(!q.isEmpty()) {
          int[] position = q.pop();
          int x = position[0];
          int y = position[1];
          int c = position[2];

          if (x == endX && y == endY) {
            return c + 1;
          }

          for (int[] d : directions) {
            int nx = x + d[0];
            int ny = y + d[1];

            if (0 <= nx && nx <= endX && 0 <= ny && ny <= endY && maps[ny][nx] == 1) {
              if (visited[ny][nx]) {
                continue;
              }

              visited[ny][nx] = true;
              q.add(new int[]{nx, ny, c + 1});
            }
          }
        }
        
        return -1;
    }
}