>datos.txt
for i in {1..10000}
do
python p1.py $i >> datos.txt
done
python p2.py datos.txt

