package com.three;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BJ1966 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int T=Integer.parseInt(st.nextToken());
        for(int tc=0;tc<T;tc++){
            st=new StringTokenizer(br.readLine());
            int N=Integer.parseInt(st.nextToken());
            int M=Integer.parseInt(st.nextToken());
            int ans=0;

            ArrayList<int[]> queue=new ArrayList<>();

            st=new StringTokenizer(br.readLine());
            for(int i=0;i<N;i++){
                int[] tmp=new int[2];
                tmp[0]=Integer.parseInt(st.nextToken());
                tmp[1]=i;
                queue.add(tmp);
            }

            while(true){
                int[] num=queue.get(0);
                boolean flag=false;

                //가장 큰 수 인지 확인
                for(int i=1;i<queue.size();i++){
                    if(queue.get(i)[0]>num[0]){
                        flag=true;
                        queue.add(num);
                        queue.remove(0);
                        break;
                    }
                }

                //0번째 index가 가장 큰 수
                if(!flag){
                    if(num[1]==M){
                        System.out.println(++ans);
                        break;
                    }else{
                        ans++;
                        queue.remove(0);
                    }
                }
            }
        }
    }
}
