tc qdisc add dev s1-eth2 root handle 1: htb default 12

tc class add dev s1-eth2 parent 1: classid 1:1 htb rate 100kbps ceil 100kbps
tc class add dev s1-eth2 parent 1:1 classid 1:10 htb rate 30kbps ceil 100kbps
tc class add dev s1-eth2 parent 1:1 classid 1:11 htb rate 10kbps ceil 100kbps
tc class add dev s1-eth2 parent 1:1 classid 1:12 htb rate 60kbps ceil 100kbps

tc filter add dev s1-eth2 protocol ip parent 1:0 prio 1 u32 match ip src 10.0.0.2 match ip dport 80 0xffff flowied 1:10
tc filter add dev s1-eth2 protocol ip parent 1:0 prio 1 u32 match ip src 10.0.0.2 match ip dport 25 0xffff flowied 1:11

tc qdisc add dev s1-eth2 parent 1:10 handle 20: pfifo limit 5
tc qdisc add dev s1-eth2 parent 1:11 handle 30: pfifo limit 5
tc qdisc add dev s1-eth2 parent 1:12 handle 40: sfq perturb 10

