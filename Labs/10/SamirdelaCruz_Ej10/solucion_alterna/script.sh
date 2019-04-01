>datos.txt
for j in {0..9}
do
for i in {1..1000}
do
python3 p1.py $j $i >> datos.txt
done
python3 p2.py datos.txt
python3 msj.py $j datos.txt histogram.png
done
