from flask import Flask, request, url_for, redirect, Response
import json
app = Flask(__name__)

@app.route('/dl', methods=['POST'])
def dl():
	name=request.args.get('n').encode('utf-8')
	delta=request.form.get('data').encode('utf-8')
	condition=request.form.get('type').encode('utf-8')
	with open("static/data/"+name+condition+".txt",'a') as f:
		f.write(delta+'\n');
	return ''

@app.route('/ld', methods=['GET'])
def ld():
	with open("static/score/leaderboard.txt",'r') as r:
			people=r.readlines()
#	board=[]
#	for i in range(len(people)):
#		s1=people[i].find('\t')
#		e1=people[i].find('\n')
#		board[i]={'name':people[i][0:s1],'score':int(people[i][s1:e1])}
	return Response(json.dumps(people), mimetype='application/json')

@app.route('/ss', methods=['POST', 'GET'])
def ss():
	if request.method == 'GET':
		return app.send_static_file('shooting_simulator.html')
	if request.method == 'POST':
		name=request.args.get('n').encode('utf-8')
		score=request.form.get('score').encode('utf-8')
		with open("static/score/leaderboard.txt",'a') as f:
			f.write(name+"\t"+score+"\n")
		with open("static/score/leaderboard.txt",'r') as r:
			people=r.readlines()
		for index in range(len(people)-1,0,-1):
			for i in range(index):
				s1=people[i].find('\t')
				e1=people[i].find('\n')
				s2=people[i+1].find('\t')
				e2=people[i+1].find('\n')
				if int(people[i][s1:e1])<int(people[i+1][s2:e2]):
					temp=people[i]
					people[i]=people[i+1]
					people[i+1]=temp
		with open("static/score/leaderboard.txt",'w') as w:
			for item in people:
				w.write(item)
		return ''

@app.route('/jquery.js')
def jquery():
	return app.send_static_file('jquery.js')	
	
@app.route('/')
def index():
	return app.send_static_file('index.html')
	
@app.route('/modernizr-custom.js')
def modernizr():
	return app.send_static_file('modernizr-custom.js')

@app.route('/demoTarget.jpg')
def demoTarget():
	return app.send_static_file('demoTarget.jpg')
	
@app.route('/pic0.jpg')
def pic0():
	return app.send_static_file('pic0.jpg')
	
@app.route('/pic1.jpg')
def pic1():
	return app.send_static_file('pic1.jpg')
	
@app.route('/pic2.jpg')
def pic2():
	return app.send_static_file('pic2.jpg')
	
@app.route('/pic3.jpg')
def pic3():
	return app.send_static_file('pic3.jpg')
	
@app.route('/pic4.jpg')
def pic4():
	return app.send_static_file('pic4.jpg')
	
@app.route('/pic5.jpg')
def pic5():
	return app.send_static_file('pic5.jpg')
	
@app.route('/pic6.jpg')
def pic6():
	return app.send_static_file('pic6.jpg')
	
@app.route('/pic7.jpg')
def pic7():
	return app.send_static_file('pic7.jpg')
	
@app.route('/pic8.jpg')
def pic8():
	return app.send_static_file('pic8.jpg')

@app.route('/pic9.jpg')
def pic9():
	return app.send_static_file('pic9.jpg')
	
@app.route('/pic10.jpg')
def pic10():
	return app.send_static_file('pic10.jpg')
	
@app.route('/sherman-front-switch.png')
def shermanfront():
	return app.send_static_file('sherman-front-switch.png')
	
@app.route('/sherman-side-switch.png')
def shermanside():
	return app.send_static_file('sherman-side-switch.png')
	
@app.route('/t-34-76-m1943-3.png')
def t34s():
	return app.send_static_file('t-34-76-m1943-3.png')
	
@app.route('/t-34-76-m1943-3_2.png')
def t34f():
	return app.send_static_file('t-34-76-m1943-3_2.png')
	
@app.route('/t-34-front-switch.png')
def t34front():
	return app.send_static_file('t-34-front-switch.png')
	
@app.route('/t-34-side-switch.png')
def t34side():
	return app.send_static_file('t-34-side-switch.png')
	
if __name__ == '__main__':
	app.run()