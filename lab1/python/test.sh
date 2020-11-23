s=0;
(python3 -m unittest > /dev/null 2>&1 && echo Run tests without mutations OK) || (echo "Run tests without mutations FAILED" && exit 1);
cp ./fsm/fsm.py ./mutants/fsm.py
for i in $(seq 20 $END); 
do 
    cp "./mutants/$i.py" ./fsm/fsm.py;
    python3 -m unittest > /dev/null 2>&1 && echo Mutant $i survived! && ((s+=1));
done
cp ./mutants/fsm.py ./fsm/fsm.py
echo Made $i tests, $s survived