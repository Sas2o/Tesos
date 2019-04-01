>datos.txt
for i in {1..10000}
do
python3 p1.py $i >> datos.txt
done
python3 p2.py datos.txt

