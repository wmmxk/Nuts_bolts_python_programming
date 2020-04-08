#$1 is the number jobs to run
# $2 is the year, e.g. 2018
mkdir /media/wxk/My\ Passport/Data/intraday/data/raw_from_quantopian/$2
for i in `seq 1 1 $1` ; 
do 
  python test_login_run_all_save.py; 
  mv ~/Downloads/*stock* /media/wxk/My\ Passport/Data/intraday/data/raw_from_quantopian/$2/
  echo $i
done
