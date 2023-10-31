import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static Queue<Point> q = new LinkedList<Point>();
    static int n, m;
    static boolean[][] road;
    static int[][] time;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] split = br.readLine().split(" ");
        n = Integer.parseInt(split[0]);
        m = Integer.parseInt(split[1]);
        road = new boolean[n][m];
        time = new int[n][m];
        for (int i = 0; i < n; i++) {
            String[] split1 = br.readLine().split("");
            for (int j = 0; j < m; j++) {
                if (split1[j].equals("1"))
                    road[i][j] = true;
            }
        }
        BFS(0, 0);
    }

    static void BFS(int x, int y) { //시작 항상 (0,0)임
        q.add(new Point(x,y));
        time[x][y] = 1;
        while (!q.isEmpty()) {
            Point p = q.poll();
            x = p.x;
            y = p.y;
            int sec = time[x][y];
//            System.out.print("(" + x + "," + y + ")  ");
//            System.out.print(sec + "초\n");
            for (int i = 0; i < 4; i++) {
                int a = -1, b = -1;
                if (i == 0 && x > 0) {
                    a = x - 1;
                    b = y;
                }
                if (i == 1 && y < m - 1) {
                    a = x;
                    b = y + 1;
                }
                if (i == 2 && x < n - 1) {
                    a = x + 1;
                    b = y;
                }
                if (i == 3 && y > 0) {
                    a = x;
                    b = y - 1;
                }
                if (a == -1 || b == -1) continue;
                if (x == n - 1 && y == m - 1) {
                    System.out.println(sec);
                    return;
                }
                if (time[a][b]==0 && road[a][b]) {
                    q.add(new Point(a,b));
                    time[a][b] = sec+1;
                }
            }

        }
    }
}



