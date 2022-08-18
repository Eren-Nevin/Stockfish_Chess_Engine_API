from flask import Flask, request
import chess
import chess.engine

app = Flask(__name__)

# TODO: Should we quit the engine or should we have an instance of it open
# for all requests?
@app.route('/best_move', methods=['POST'])
def get_best_move():
    engine_executable_path = ''
    # initialize engine
    engine = chess.engine.SimpleEngine.popen_uci(engine_executable_path)

    # get the payload
    received_fen_state = request.data.decode('utf-8')
    board = chess.Board(received_fen_state)
    engine_response = engine.play(board, chess.engine.Limit(time=0.100))
    engine.quit()

    return engine_response.move.uci()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7767)
