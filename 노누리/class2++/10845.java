package com.five;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BJ10845 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        StringBuilder sb=new StringBuilder();

        int N=Integer.parseInt(st.nextToken());
        Deque<Integer> queue=new LinkedList<>();
        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine());
            String str=st.nextToken();

            if(st.hasMoreTokens()){
                queue.add(Integer.parseInt(st.nextToken()));
            }else{
                if(str.equals("pop")){
                    if(queue.isEmpty()){
                        sb.append("-1\n");
                    }else{
                        sb.append(queue.poll()+"\n");
                    }
                }else if(str.equals("size")){
                    sb.append(queue.size()+"\n");
                }else if(str.equals("empty")){
                    if(queue.isEmpty()){
                        sb.append("1\n");
                    }else{
                        sb.append("0\n");
                    }
                }else if(str.equals("front")){
                    if(queue.isEmpty()){
                        sb.append("-1\n");
                    }else{
                        sb.append(queue.peek()+"\n");
                    }
                }else if(str.equals("back")){
                    if(queue.isEmpty()){
                        sb.append("-1\n");
                    }else{
                        sb.append(queue.peekLast()+"\n");
                    }
                }
            }
        }

        System.out.println(sb);
    }
}
