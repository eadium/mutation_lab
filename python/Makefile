all: ray mm mp mt

custom:
	./test.sh

ray: 
	cosmic-ray init config.toml ray.sqlite; \
	cosmic-ray baseline --report ray.sqlite || echo 'ray FAILED'; \
	cosmic-ray exec ray.sqlite; \
	cr-report ray.sqlite; \
	cr-html ray.sqlite > ray.html

mm:
	mutmut run || echo 'mutmut FAILED'; \
	mutmut results

mp:
	mut.py --target ./fsm --unit-test ./test_fsm.py -e --report-html mut_py.html

mt:
	mutatest -s fsm/ -t "python3 -m unittest" -m f -n 100

test:
	python3 -m unittest

clean:
	rm -r .mutmut-cache *.sqlite mut_py.html/