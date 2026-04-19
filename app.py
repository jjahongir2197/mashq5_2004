@app.route('/result1', methods=['GET', 'POST'])
def result1():
    res = None
    
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()

        if len(name) > 2 and '@' in email:
            res = [name, email]
        else:
            res = ["Ma'lumotlar noto'g'ri kiritildi"]

    return render_template('result1.html', res=res)
