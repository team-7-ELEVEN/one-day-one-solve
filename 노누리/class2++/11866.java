package com.five;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BJ11866 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        StringBuilder sb=new StringBuilder();

        int N=Integer.parseInt(st.nextToken());
        int K=Integer.parseInt(st.nextToken());
        Queue<Integer> queue=new LinkedList<>();

        for(int i=1;i<=N;i++){
            queue.add(i);
        }

        sb.append("<");
        int idx=1;
        while(!queue.isEmpty()){
            if(idx==K){
                idx=1;
                sb.append(queue.poll());
                if(queue.isEmpty()){
                    sb.append(">");
                }else{
                    sb.append(", ");
                }
            }else{
                idx++;
                queue.offer(queue.poll());
            }
        }

        System.out.println(sb);
    }
}
