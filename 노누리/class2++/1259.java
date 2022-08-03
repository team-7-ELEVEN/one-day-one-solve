package com.two;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class BJ1259 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();

        while(true){
            StringTokenizer st=new StringTokenizer(br.readLine());
            String num=st.nextToken();
            if(num.equals("0")) break;
            char[] tmp=num.toCharArray();
            String flag="yes";

            Stack<Character> stack=new Stack<>();
            for(int i=0;i<tmp.length;i++){
                if(tmp.length%2==1 && i==tmp.length/2)
                    continue;
                if(i<tmp.length/2){
                    stack.push(tmp[i]);
                }else{
                    char top=stack.pop();
                    if(top!=tmp[i]){
                        flag="no";
                    }
                }
            }
            sb.append(flag+"\n");
        }

        System.out.println(sb);
    }
}
