import java.util.*;
import java.io.*;

public class Main {
    static int[][] graph;
    static int[] visited_dfs;
    static int[] visited_bfs;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st; // = new StringTokenizer(br.readLine());
        String[] sp = br.readLine().split(" ");
        int N = Integer.parseInt(sp[0]);
        int M = Integer.parseInt(sp[1]);
        int V = Integer.parseInt(sp[2]) - 1;
        graph = new int[N][N];
        visited_dfs = new int[N];
        visited_bfs = new int[N];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            graph[a][b] = 1;
            graph[b][a] = 1;
        }
        dfs(V);
        System.out.print("\n");
        bfs(V);
    }

    static void dfs(int node) {
        System.out.print((1 + node) + " ");
        visited_dfs[node] = 1;
        for (int i = 0; i < graph[node].length; i++) {
            if (visited_dfs[i] == 0 && graph[node][i] == 1) {
                dfs(i);
            }
        }
    }

    static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        visited_bfs[start] = 1;
        q.add(start);
        while (q.size() != 0) {
            int cur = q.poll();
            System.out.print((1+cur)+" ");
            for (int i = 0; i < graph[cur].length; i++) {
                if (visited_bfs[i] == 0 && graph[cur][i] == 1) {
                    visited_bfs[i] = 1;
                    q.add(i);
                }
            }
        }
    }
}