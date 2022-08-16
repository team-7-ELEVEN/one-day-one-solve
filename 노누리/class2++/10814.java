package com.five;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class BJ10814 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int N=Integer.parseInt(st.nextToken());
        String[][] person=new String[N][2];
        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine());
            person[i][0]=st.nextToken();
            person[i][1]=st.nextToken();
        }

        Arrays.sort(person, (o1, o2) -> Integer.valueOf(o1[0])-Integer.valueOf(o2[0]));

        for(int i=0;i<N;i++){
            System.out.println(person[i][0]+" "+person[i][1]);
        }
    }
}
