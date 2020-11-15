all: ray mm mp mt

ray: 
	cosmic-ray init config.toml ray.sqlite; \
cosmic-ray baseline --report ray.sqlite || exit 1; \
cosmic-ray exec ray.sqlite; \
cr-report ray.sqlite; \
cr-html ray.sqlite > ray.html

mm:
	mutmut run

mp:
	mut.py --target ./fsm --unit-test ./test_fsm.py -e --report-html mut_py.html

mt:
	mutatest -s fsm/ -t "python3 -m unittest"

test:
	python3 test_fsm.py

clean:
	rm -r .mutmut-cache *.sqlite mut_py.html/