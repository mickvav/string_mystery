all: pyresult.txt goresult.txt
	gnuplot plot.plt

pyresult.txt: main.py
	python3 main.py > pyresult.txt

goresult.txt: main.go
	go run main.go > goresult.txt
