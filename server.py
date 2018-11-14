import http.server
import socketserver
import gym
import gym_sample
from QLearning import QLearning
import json

PORT = 8080

env = gym.make('sample-v0')
qLearning = QLearning(env, 99)


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        if(self.path == '/train'):
            self.wfile.write(json.dumps(qLearning.train(5000, 0.7, 0.618, 1, 1, 0.01, 0.01).tolist()).encode('utf8'))
        elif(self.path == '/ai_step'):
            self.wfile.write(json.dumps(qLearning.ai_step()).encode('utf8'))
        elif(self.path == '/reset'):
            qLearning.reset()
            self.wfile.write('{"reseted": true}'.encode('utf8'))
        else:
            self.wfile.write('{"rodando": "ta"}'.encode('utf8'))
        return

httpd = socketserver.TCPServer(('', PORT), Handler)

print("Listening port ", PORT)
httpd.serve_forever()