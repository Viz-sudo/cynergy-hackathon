package javaapplication1;
import java.util.*;

class VK_problem1 {
    public int numOfIslands(int[][] grid){
        int row = grid.length;
        int col = grid[0].length;
        ArrayList<Integer> visit;
        visit = new ArrayList<>();
             
        boolean[][] dfs = null;
        int islands = 1;
        for(int i=0; i<row; i++){
            for(int j=0; j<col; j++){
                if(dfs[i][j]){
                    islands += 1;
                }
            }
        }
        return islands;
    }
    public boolean dfs(int grid[][], int r, int c, ArrayList<Integer> visit){ 
        int row = grid.length;
        int col = grid[0].length;

        if(r<0 || r>= row || c<0 || c>= col || grid[r][c] == "0" or visit.contains((r,c))){
            return false;
        }
        visit.add((r,c));
        if(dfs(r + 1, c)){
            return True;
        }
        if(dfs(r - 1, c)){
            return True;
        }
        if(dfs(r, c + 1)){
            return True;
        }
        if(dfs(r, c - 1)){
            return True;
        }
        visit.remove((r,c));
        
    }
    public static void main(String[] args) {
        JavaApplication1 obj1 = new JavaApplication1();
        obj1.Start();
    }
}

