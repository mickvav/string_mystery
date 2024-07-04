all: pyresult.txt goresult.txt

pyresult.txt: main.py
	python3 main.py > pyresult.txt

goresult.txt: main.go
	go run main.go > goresult.txt
