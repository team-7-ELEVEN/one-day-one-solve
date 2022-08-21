package com.seven;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BJ1389 {
    static int[][] user;
    static int[][] graph;
    static int N;
    static boolean[] visited;

    public static class queue{
        int node,cnt;

        public queue(int node,int cnt){
            this.node=node;
            this.cnt=cnt;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());
        graph=new int[N][N];
        user=new int[N][N];

        for(int i=0;i<M;i++){
            st=new StringTokenizer(br.readLine());
            int a=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());
            graph[a-1][b-1]=1;
            graph[b-1][a-1]=1;
        }

        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(i==j) continue;
                bfs(i,j);
            }
        }

        int min=Integer.MAX_VALUE;
        int idx=0;
        for(int i=0;i<N;i++){
            int sum=0;
            for(int j=0;j<N;j++){
                sum+=user[i][j];
            }
            if(min>sum){
                min=sum;
                idx=i;
            }
        }

        System.out.println(idx+1);
    }

    public static void bfs(int start,int target){
        Queue<queue> queue=new LinkedList<>();
        visited=new boolean[N];
        queue.add(new queue(start,0));

        while(!queue.isEmpty()){
            queue tmp=queue.poll();
            if(tmp.node==target) user[start][target]=tmp.cnt;
            for(int i=0;i<N;i++){
                if(visited[i]) continue;

                if(graph[tmp.node][i]==1){
                    visited[i]=true;
                    queue.offer(new queue(i,tmp.cnt+1));
                }
            }
        }
    }
}
