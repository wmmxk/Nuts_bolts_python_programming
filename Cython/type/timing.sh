for i in {1..3}
do
  echo -e version ${i} "\n"
  time python ./version${i}/test*

done
