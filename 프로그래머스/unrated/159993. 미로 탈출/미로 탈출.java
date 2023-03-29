import java.util.*;

class Solution {
    static int x, y, sx, sy, ex, ey, lx, ly;
    static boolean[][] visited;
    static char[][] map;
    static int[] dx = {1,-1,0,0};
    static int[] dy = {0,0,1,-1};
    static char target;
    
    
    public static int bfs(int sx, int sy, int ex, int ey){
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{sx, sy, 0});
        visited[sx][sy] = true;

        while(!q.isEmpty()){
            int[] point = q.poll();

            int xx = point[0];
            int yy = point[1];
            int dist = point[2];

            if(xx == ex && yy == ey)return dist;

            // 방향
            for(int i = 0;i<4;i++){
                int tmpX = xx+dy[i];
                int tmpY = yy+dx[i];
                boolean flag = true;

                if( tmpX >= 0 && tmpX < x && tmpY >=0 && tmpY < y && map[tmpX][tmpY] != 'X'){
                    if(visited[tmpX][tmpY])continue;

                    visited[tmpX][tmpY] = true;
                    q.add(new int[]{tmpX, tmpY, dist+1});
                }
            }
        }

        return -1;
    }
    
    
    
    public int solution(String[] board) {
        
        x = board.length;
        y = board[0].length();
        target = 'L';

        map = new char[x][y];
        visited = new boolean[x][y];

        for(int i=0; i< board.length;i++){
            map[i] = board[i].toCharArray();
            for(int j=0;j<y;j++){
                if(map[i][j] == 'S'){
                    sx = i;
                    sy = j;
                }else if(map[i][j] == 'L'){
                    lx = i;
                    ly = j;
                }else if(map[i][j] == 'E'){
                    ex = i;
                    ey = j;
                }
            }
        }
        int result1 = bfs(sx, sy, lx, ly);
        visited = new boolean[x][y];
        target = 'E';
        int result2 = bfs(lx, ly, ex, ey);
        return result1 != -1 && result2 != -1?result1 + result2:-1;
        
    }
}