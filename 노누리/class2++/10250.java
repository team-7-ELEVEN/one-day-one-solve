package com.five;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BJ10250 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int T=Integer.parseInt(st.nextToken());
        for(int t=0;t<T;t++){
            String floor="";
            String num="";
            st=new StringTokenizer(br.readLine());
            double H=Integer.parseInt(st.nextToken());
            int W=Integer.parseInt(st.nextToken());
            double N=Integer.parseInt(st.nextToken());

            floor=String.valueOf((int)(N%H));
            if(floor.equals("0")){
                floor=String.valueOf((int)H);
            }
            num=String.valueOf((int)Math.ceil(N/H));
            if(num.length()==1){
                System.out.println(floor+"0"+num);
            }else{
                System.out.println(floor+num);
            }

        }
    }
}
