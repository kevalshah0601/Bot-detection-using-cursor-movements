cursor_movement:
	python3 run_options.py

run-human:
	gcc cursor_human.c -o cursor_human -lX11
	./cursor_human

	gcc -o cursor_move cursor_move.c -lX11 -lXtst
	./cursor_move

	python3 test.py

run-robot:
	python3 cursor_robot.py

	gcc -o cursor_move cursor_move.c -lX11 -lXtst
	./cursor_move

	python3 test.py