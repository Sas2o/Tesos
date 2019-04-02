>datos.txt
for n in {1..10000}
do
python3 p1.py $n >> datos.txt
done
python3 p2.py datos.txt hist.png

