#!/usr/bin/awk -f
BEGIN { 
    OFS=",";
    i=0;
    while (getline < dict){
        split($0,ft,",");
        starts[i]=ft[1];
        lens[i]=ft[2];
        labels[i]=ft[3];
        i++;
    }
    N = length(labels);
    for(i=0;i<N;i++) {
        printf labels[i];
        if(i<N-1) { printf OFS }
    }
    printf("\n");
}
{
    for(i=0;i<N;i++) {
        printf substr($0,starts[i],lens[i]);
        if(i<N-1) { printf OFS }
    }
    printf("\n");
}