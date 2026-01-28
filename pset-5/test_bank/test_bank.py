from bank import value


def test_value_starts_with_hello():
	assert value("Hello world") == 0
	assert value("hello world") == 0
	assert value("HeLlo world") == 0
	assert value("HELLo world") == 0
	assert value("helloworld") == 0


def test_value_starts_with_h():
	assert value("hhello world") == 20 
	assert value("Hey") == 20
	assert value("Hell0 world") == 20


def test_value_other():
	assert value("yhello world") == 100 
	assert value("yo world") == 100 
	assert value("goodbye world") == 100 


	
