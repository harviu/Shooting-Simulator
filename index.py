from flask import Flask, request, url_for, redirect, Response
import json
app = Flask(__name__)

@app.route('/f/writeData', methods=['POST'])
def writeData():
	name=request.args.get('n').encode('utf-8')
	delta=request.form.get('data').encode('utf-8')
	condition=request.form.get('type').encode('utf-8')
	with open("static/data/"+name+condition+".txt",'a') as f:
		f.write(delta+'\n');
	return ''

@app.route('/f/readLB', methods=['GET'])
def sendLeaderBoard():
	with open("static/score/leaderboard.txt",'r') as r:
			people=r.readlines()
#	board=[]
#	for i in range(len(people)):
#		s1=people[i].find('\t')
#		e1=people[i].find('\n')
#		board[i]={'name':people[i][0:s1],'score':int(people[i][s1:e1])}
	return Response(json.dumps(people), mimetype='application/json')

@app.route('/f/writeLB', methods=['POST'])
def writeLeaderBoard():
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

if __name__ == '__main__':
	app.run()
