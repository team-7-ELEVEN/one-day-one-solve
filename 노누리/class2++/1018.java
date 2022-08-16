package com.one;

import java.util.Arrays;
import java.util.Scanner;

public class Chess {
    public static int check(int i,int j,String[][] chess){
        String[][] black={{"B","W","B","W","B","W","B","W"},{"W","B","W","B","W","B","W","B"},{"B","W","B","W","B","W","B","W"},{"W","B","W","B","W","B","W","B"},{"B","W","B","W","B","W","B","W"},{"W","B","W","B","W","B","W","B"},{"B","W","B","W","B","W","B","W"},{"W","B","W","B","W","B","W","B"}};
        String[][] white={{"W","B","W","B","W","B","W","B"},{"B","W","B","W","B","W","B","W"},{"W","B","W","B","W","B","W","B"},{"B","W","B","W","B","W","B","W"},{"W","B","W","B","W","B","W","B"},{"B","W","B","W","B","W","B","W"},{"W","B","W","B","W","B","W","B"},{"B","W","B","W","B","W","B","W"}};

        int cntB=0;
        int cntW=0;

        for(int n=0;n<8;n++){
            for(int m=0;m<8;m++){
                if (!chess[i + n][j + m].equals(black[n][m])) {
                    cntB++;
                }
                if (!chess[i + n][j + m].equals(white[n][m])) {
                    cntW++;
                }
            }
        }
        return Math.min(cntB,cntW);
    }

    public static void main(String[] args) {
        int MIN=Integer.MAX_VALUE;

        Scanner sc=new Scanner(System.in);

        int N=sc.nextInt();
        int M=sc.nextInt();

        String[][] chess=new String[N][M];
        for(int i=0;i<N;i++){
            chess[i]=sc.next().split("");
        }

        //System.out.println(Arrays.deepToString(chess));

        for(int i=0;i<N;i++) {
            int ans=0;
            for (int j = 0; j < M; j++) {
                if(i+8<=N && j+8<=M){
                    ans = check(i, j, chess);
                    if(ans<MIN){
                        MIN=ans;

                    }
                }
            }
        }

        System.out.println(MIN);
    }
}
