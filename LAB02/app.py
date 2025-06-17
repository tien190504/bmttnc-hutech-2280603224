from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailfenceCipher

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# —— CAESAR —— #
@app.route('/caesar', methods=['GET', 'POST'])
def caesar_handler():
    if request.method == 'POST':
        text = request.form.get('text')
        shift_str = request.form.get('shift')
        action = request.form.get('action')
        result_text = ""

        if not text or not shift_str:
            result_text = "Lỗi: Vui lòng nhập cả văn bản và khóa dịch chuyển."
            return render_template('ceasar.html', result=result_text)

        try:
            shift = int(shift_str)
            if not (0 <= shift <= 25):
                result_text = "Lỗi: Độ dịch phải là một số nguyên từ 0 đến 25."
                return render_template('ceasar.html', result=result_text)
        except ValueError:
            result_text = "Lỗi: Độ dịch phải là một số nguyên."
            return render_template('ceasar.html', result=result_text)

        cipher = CaesarCipher()  # The constructor shift is not used by encrypt_text/decrypt_text if shift is an argument

        if action == 'encrypt':
            encrypted = cipher.encrypt_text(text, shift)
            result_text = encrypted
        elif action == 'decrypt':
            decrypted = cipher.decrypt_text(text, shift)
            result_text = decrypted
        else:
            result_text = "Lỗi: Hành động không hợp lệ."

        return render_template('ceasar.html', result=result_text)

    return render_template('ceasar.html')


# —— PLAYFAIR —— #
@app.route('/playfair', methods=['GET', 'POST'])
def playfair_handler():
    if request.method == 'POST':
        text = request.form.get('text')
        key = request.form.get('key')
        action = request.form.get('action')
        result_text = ""
        matrix_display = None

        if not text or not key:
            result_text = "Lỗi: Vui lòng nhập cả văn bản và khóa."
            return render_template('playfair.html', result=result_text)

        pf = PlayFairCipher()
        try:
            matrix = pf.create_playfair_matrix(key)
            matrix_display = "\n".join([" ".join(row) for row in matrix])

            if action == 'encrypt':
                ciphertext = pf.playfair_encrypt(text, matrix)
                result_text = ciphertext
            elif action == 'decrypt':
                plaintext = pf.playfair_decrypt(text, matrix)
                result_text = plaintext
            else:
                result_text = "Lỗi: Hành động không hợp lệ."
        except Exception as e:
            result_text = f"Đã xảy ra lỗi: {str(e)}"

        return render_template('playfair.html', result=result_text, matrix=matrix_display)

    return render_template('playfair.html')


# —— VIGENÈRE —— #
@app.route('/vigenere', methods=['GET', 'POST'])
def vigenere_handler():
    if request.method == 'POST':
        text = request.form.get('text')
        keyword = request.form.get('keyword')  # Name from vigenere.html
        action = request.form.get('action')
        result_text = ""

        if not text or not keyword:
            result_text = "Lỗi: Vui lòng nhập cả văn bản và từ khóa."
            return render_template('vigenere.html', result=result_text)

        if not keyword.isalpha():
            result_text = "Lỗi: Khóa phải hoàn toàn là chữ cái."
            return render_template('vigenere.html', result=result_text)

        vg = VigenereCipher()
        if action == 'encrypt':
            ciphertext = vg.vigenere_encrypt(text, keyword)
            result_text = ciphertext
        elif action == 'decrypt':
            plaintext = vg.vigenere_decrypt(text, keyword)
            result_text = plaintext
        else:
            result_text = "Lỗi: Hành động không hợp lệ."

        return render_template('vigenere.html', result=result_text)

    return render_template('vigenere.html')


# —— RAILFENCE —— #
@app.route('/railfence', methods=['GET', 'POST'])
def railfence_handler():
    if request.method == 'POST':
        text = request.form.get('text')
        rails_str = request.form.get('rails')  # Name from railfence.html
        action = request.form.get('action')
        result_text = ""

        if not text or not rails_str:
            result_text = "Lỗi: Vui lòng nhập cả văn bản và số hàng."
            return render_template('railfence.html', result=result_text)

        try:
            rails = int(rails_str)
            if rails < 2:
                result_text = "Lỗi: Số hàng phải là một số nguyên lớn hơn hoặc bằng 2."
                return render_template('railfence.html', result=result_text)
        except ValueError:
            result_text = "Lỗi: Số hàng phải là một số nguyên."
            return render_template('railfence.html', result=result_text)

        rf = RailfenceCipher()
        if action == 'encrypt':
            ciphertext = rf.railfence_encrypt(text, rails)
            result_text = ciphertext
        elif action == 'decrypt':
            plaintext = rf.railfence_decrypt(text, rails)
            result_text = plaintext
        else:
            result_text = "Lỗi: Hành động không hợp lệ."

        return render_template('railfence.html', result=result_text)

    return render_template('railfence.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)