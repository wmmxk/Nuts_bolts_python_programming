n=100
source activate py3
for i in {1..4}
do
  echo -e version $i "\n"
  time python ./version${i}/test* ${n}
done
