print("Nhập các dòng văn bản(nhấn 'done' để kết thúc):")
texts = []
while True:
    text = input()
    if text == "done":
        break
    texts.append(text)
print("Chuyển văn bản đã nhập thành chữ hoa:")
for text in texts:
    print(text.upper())