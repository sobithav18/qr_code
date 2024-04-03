import qrcode

features =qrcode.QRCode(version=1,box_size=40,border=3)

features.add_data('https://www.youtube.com/watch?v=RsN0aXfPR1E&ab_channel=GeeksforGeeks')
features.make(fit=True)


#generate_image=qrcode.make("GeeksforGeeks")
generate_image=features.make_image(fill_color="black",back_color="white")
generate_image.save('gfg.png')


