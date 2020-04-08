#$1 is the number jobs to run
# $2 is the year, e.g. 2018
conda activate tf
mkdir /media/wxk/My\ Passport/Data/intraday/$2
for i in `seq 1 1 $1` ; 
do 
  python no_login_run_all.py; 
  mv ~/Downloads/*stock* /media/wxk/My\ Passport/Data/intraday/$2/
  echo $i
done
