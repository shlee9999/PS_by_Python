import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[][] board = new String[15][15];

        for(String[] row : board){
            Arrays.fill(row, " ");
        }

        for(int i = 0; i < 5; i++){
            String[] sp = br.readLine().split("");
            for(int j = 0; j < sp.length; j++){
                board[i][j] = sp[j];
            }
        }


        for(int col = 0; col < 15; col++){
            for(int row = 0; row < 15; row++){
                if (board[row][col].equals(" ")) continue;
                bw.write(board[row][col]);
            }
        }   
        
        bw.flush();
        bw.close();
    }
}
