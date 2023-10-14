#/bin/bash

for l in 25 75 125
do
    for m in 60 100 125
    do
        for n in 60 100 150
        do
            python3 plot_results.py -i results/l"$l"_m"$m"_n"$n".txt -o plots/l"$l"_m"$m"_n"$n".png
        done
    done
done
