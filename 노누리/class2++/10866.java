package com.five;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class BJ10866 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        StringBuilder sb=new StringBuilder();

        int N=Integer.parseInt(st.nextToken());
        Deque<Integer> deque=new ArrayDeque<>();
        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine());
            String str=st.nextToken();

            if(st.hasMoreTokens()){
                if(str.equals("push_front")){
                    deque.addFirst(Integer.parseInt(st.nextToken()));
                }else if(str.equals("push_back")){
                    deque.addLast(Integer.parseInt(st.nextToken()));
                }
            }else{
                if(str.equals("pop_front")){
                    if(deque.isEmpty()){
                        sb.append("-1\n");
                    }else{
                        sb.append(deque.pollFirst()+"\n");
                    }
                }else if(str.equals("pop_back")){
                    if(deque.isEmpty()){
                        sb.append("-1\n");
                    }else{
                        sb.append(deque.pollLast()+"\n");
                    }
                }else if(str.equals("size")){
                    sb.append(deque.size()+"\n");
                }else if(str.equals("empty")){
                    if(deque.isEmpty()){
                        sb.append("1\n");
                    }else{
                        sb.append("0\n");
                    }
                }else if(str.equals("front")){
                    if(deque.isEmpty()){
                        sb.append("-1\n");
                    }else{
                        sb.append(deque.peekFirst()+"\n");
                    }
                }else if(str.equals("back")){
                    if(deque.isEmpty()){
                        sb.append("-1\n");
                    }else{
                        sb.append(deque.peekLast()+"\n");
                    }
                }
            }
        }
        System.out.println(sb);
    }
}
