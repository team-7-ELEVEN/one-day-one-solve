package com.five;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class BJ10828 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        StringBuilder sb=new StringBuilder();

        int N=Integer.parseInt(st.nextToken());
        Stack<Integer> stack=new Stack<>();
        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine());
            String[] com=st.nextToken().split(" ");

            if(st.hasMoreTokens()){
                stack.push(Integer.valueOf(st.nextToken()));
            }else{
                if(com[0].equals("pop")){
                    if(stack.isEmpty()){
                        sb.append("-1\n");
                    }else{
                        sb.append(stack.pop()+"\n");
                    }
                }else if(com[0].equals("size")){
                    sb.append(stack.size()+"\n");
                }else if(com[0].equals("empty")){
                    if(stack.isEmpty()){
                        sb.append("1\n");
                    }else{
                        sb.append("0\n");
                    }
                }else if(com[0].equals("top")){
                    if(stack.isEmpty()){
                        sb.append("-1\n");
                    }else{
                        sb.append(stack.peek()+"\n");
                    }
                }
            }
        }
        System.out.println(sb);
    }
}
