from flask import Flask, render_template, request, session, redirect, url_for
from datetime import datetime, timezone

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b''

hints = {1: 'I always forget this, so I made a note nearby',
         2: 'My favourite football team were founded this year',
         3: 'Look for the red letters!'}

passwords = {1: '9752', 2: '1878', 3: 'python', 5: 'true'}


@app.route('/', methods=['GET', 'POST'])
def home():
    if 'level' in session:
        return redirect(url_for('play'))

    if request.method == 'POST':
        session['team'] = request.form['team_name']
        session['level'] = 1
        session['start_time'] = datetime.now(timezone.utc)
        return redirect(url_for('play'))
        
    return render_template('start.html')


@app.route('/play', methods=['GET', 'POST'])
def play():
    if 'level' not in session:
        return redirect(url_for('home'))

    error = False
    if request.method == 'POST':
        if session['level'] == 4:
            session['level'] = 5
        else:
            input = request.form['password'].lower()
            if input == passwords[session['level']]:
                session['level'] += 1
            else:
                error = True
    
    if session['level'] > 5:
        session['time'] = (datetime.now(timezone.utc) - session['start_time']).total_seconds()
        return redirect(url_for('finish'))  

    if session['level'] == 4:
        return render_template('level-4.html')

    if session['level'] == 5:
        return render_template('code-level.html', error=error)
    
    return render_template('password-level.html',
                           password_num=session['level'],
                           hint=hints[session['level']],
                           error=error)


@app.route('/finish')
def finish():
    if 'time' not in session:
        return redirect(url_for('home'))
    
    minutes, seconds = divmod(session['time'], 60)
    return render_template('finish.html', team_name=session['team'], minutes=minutes, seconds=seconds)


@app.route('/restart')
def restart():
    session.clear()
    return redirect(url_for('home'))


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=80)