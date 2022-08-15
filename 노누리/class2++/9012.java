package com.five;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class BJ9012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        StringBuilder sb=new StringBuilder();

        int T=Integer.parseInt(st.nextToken());
        for(int t=0;t<T;t++){
            st=new StringTokenizer(br.readLine());
            String[] str=st.nextToken().split("");
            Stack<String> stack=new Stack<>();
            String ans="";

            for(int i=0;i<str.length;i++){
                if(str[i].equals(")")){
                    if(stack.isEmpty()){
                        ans="NO";
                        break;
                    }
                    stack.pop();
                }else{
                    stack.push(str[i]);
                }
            }

            if(ans.equals("NO")){
                sb.append("NO\n");
            }else{
                if(stack.isEmpty()){
                    sb.append("YES\n");
                }else{
                    sb.append("NO\n");
                }
            }
        }
        System.out.println(sb);
    }
}
